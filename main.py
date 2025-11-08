
import cv2
import mediapipe as mp
import time
import threading
import sys


IS_WIN = sys.platform.startswith("win")
if IS_WIN:
    import winsound

def play_beep(freq_hz=440, ms=200):
    if not IS_WIN:
        return
    threading.Thread(target=winsound.Beep, args=(freq_hz, ms), daemon=True).start()


mp_hands = mp.solutions.hands
mp_draw  = mp.solutions.drawing_utils


FREQS = [261, 294, 329, 392, 440]  
NAMES = ["Do", "Re", "Mi", "Fa", "Sol"]


COOLDOWN = 0.30

def fingers_up(landmarks, handedness_label):
    """
    Ritorna lista di 5 int (0/1) [pollice, indice, medio, anulare, mignolo]
    Regola:
      - Pollice: Right => tip.x < ip.x ; Left => tip.x > ip.x
      - Altre dita: tip.y < pip.y (asse Y verso il basso)
    """
    
    TIPS = [4, 8, 12, 16, 20]
    PIPS = [3, 6, 10, 14, 18]  

    up = [0, 0, 0, 0, 0]

    
    thumb_tip = landmarks[TIPS[0]]
    thumb_ip  = landmarks[PIPS[0]]
    if handedness_label == "Right":
        up[0] = 1 if thumb_tip.x < thumb_ip.x else 0
    else:  
        up[0] = 1 if thumb_tip.x > thumb_ip.x else 0

  
    for i in range(1, 5):
        tip = landmarks[TIPS[i]]
        pip = landmarks[PIPS[i]]
        up[i] = 1 if tip.y < pip.y else 0

    return up

def main():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print("ERRORE: webcam non disponibile")
        return

    
    prev = [0, 0, 0, 0, 0]
    last_time = [0.0, 0.0, 0.0, 0.0, 0.0]

    pTime = 0.0

    with mp_hands.Hands(
        model_complexity=0,
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as hands:

        while True:
            ok, img = cap.read()
            if not ok:
                break
            img = cv2.flip(img, 1)
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            res = hands.process(rgb)

            txt = "Mano: NO"
            if res.multi_hand_landmarks:
                handLms = res.multi_hand_landmarks[0]
                
                label = "Right"
                if res.multi_handedness:
                    label = res.multi_handedness[0].classification[0].label

                up = fingers_up(handLms.landmark, label)
                count = sum(up)

               
                now = time.time()
                for i, state in enumerate(up):
                    if state == 1 and prev[i] == 0 and (now - last_time[i] >= COOLDOWN):
                        play_beep(FREQS[i], ms=220)
                        last_time[i] = now
                prev = up[:]  

                
                mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

                
                active_notes = "+".join([NAMES[i] for i, s in enumerate(up) if s])
                if active_notes == "":
                    active_notes = "—"
                txt = f"{label} | Dita su: {up}  ({count})  Note: {active_notes}"

         
            cTime = time.time()
            fps = 1.0 / (cTime - pTime) if cTime > pTime else 0.0
            pTime = cTime

            cv2.putText(img, f"FPS: {int(fps)}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(img, txt, (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (50, 240, 50), 2)

            cv2.imshow("Hand Piano (ESC per uscire)", img)
            if cv2.waitKey(1) & 0xFF == 27:  
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()