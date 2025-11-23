import cv2
import mediapipe as mp
import pickle
import numpy as np
import time
import os
from gtts import gTTS
import pygame 

# --- CONFIGURATION ---
LANG_CODE = 'hi'  # 'hi' for Hindi, 'bn' for Bengali, 'en' for English
CONFIDENCE_THRESHOLD = 0.7
# Dictionary: gesture_name -> translated_word
TRANSLATIONS = {
    'Hello': 'नमस्ते', 
    'yes': 'हाँ',     
    'No': 'नहीं',      
    'Thanks': 'धन्यवाद',
    'I Love You': 'मैं तुमसे प्यार करता हूँ'
}
# ---------------------

# Initialize Audio
try:
    pygame.mixer.init()
except Exception as e:
    print("Audio init failed:", e)

def text_to_speech(text, lang):
    """Convert text to speech and play it."""
    try:
        filename = "temp_audio.mp3"
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)
        
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
        pygame.mixer.music.unload()
        os.remove(filename) # Clean up
    except Exception as e:
        print(f"TTS Error: {e}")

# Load Model
print("Loading model...")
try:
    model_dict = pickle.load(open('model.p', 'rb'))
    model = model_dict['model']
except FileNotFoundError:
    print("Error: 'model.p' not found. Please put the downloaded 'model.p' in this folder.")
    exit()

# Setup MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

cap = cv2.VideoCapture(0)

last_prediction = ""
frames_consistent = 0
CONSECUTIVE_FRAMES_REQUIRED = 15  # Wait ~0.5s before speaking

print("--- ISL RECOGNITION APP STARTED ---")
print(f"Target Language: {LANG_CODE}")
print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    H, W, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    prediction_text = "Waiting..."

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

            data_aux = []
            x_list = []
            y_list = []

            for landmark in hand_landmarks.landmark:
                x_list.append(landmark.x)
                y_list.append(landmark.y)

            base_x, base_y = x_list[0], y_list[0]
            for i in range(len(x_list)):
                data_aux.append(x_list[i] - base_x)
                data_aux.append(y_list[i] - base_y)

            try:
                prediction = model.predict([np.asarray(data_aux)])
                predicted_label = prediction[0]
                
                # Check confidence
                probs = model.predict_proba([np.asarray(data_aux)])
                confidence = np.max(probs)

                if confidence > CONFIDENCE_THRESHOLD:
                    prediction_text = predicted_label
                    
                    if predicted_label == last_prediction:
                        frames_consistent += 1
                    else:
                        frames_consistent = 0
                        last_prediction = predicted_label
                    
                    if frames_consistent == CONSECUTIVE_FRAMES_REQUIRED:
                        # Get translation, default to English label if not found
                        text_to_say = TRANSLATIONS.get(predicted_label, predicted_label)
                        print(f"Speaking: {text_to_say}")
                        text_to_speech(text_to_say, LANG_CODE) 
                        frames_consistent = 0
            except Exception as e:
                pass

            # UI
            cv2.rectangle(frame, (0, 0), (W, 80), (245, 117, 16), -1)
            cv2.putText(frame, f"Gesture: {prediction_text}", (20, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (255, 255, 255), 3, cv2.LINE_AA)

    cv2.imshow('ISL to Text & Speech', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()