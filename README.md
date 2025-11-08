# Python-Piano-hand-recognition
A gesture-based piano prototype using a webcam. The system detects finger positions with MediaPipe: each raised finger triggers a different note played through beeps. Not a realistic instrument, but a simple and fun demo of computer vision and natural user input.

What is this?

A playful demo that detects your fingers in real time and plays a beep per raised finger — like a minimalist piano using your hands and a webcam.

Features

Real-time hand/landmark detection (MediaPipe Hands)

Counts raised fingers (thumb logic with handedness)

Optional two-hand mode

Simple beeps for notes (prototype)

Requirements

Windows 10/11 (tested)

Python 3.11 (recommended) → MediaPipe doesn’t provide wheels for 3.13 on Windows at the time of writing

Webcam

Packages: opencv-python, mediapipe (and optionally winsound via stdlib on Windows)

Setup (with venv)

PowerShell / VS Code Terminal

# 1) Ensure you have Python 3.11 installed
py -3.11 --version

# 2) Create and activate the venv in the project folder
py -3.11 -m venv .venv

# If activation is blocked, allow scripts for current user (once):
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# Activate
.\.venv\Scripts\Activate

# 3) Upgrade pip and install deps
python -m pip install --upgrade pip setuptools wheel
pip install opencv-python mediapipe


If you can’t (or don’t want to) activate the venv, you can still run with its interpreter directly:

"path\to\project\.venv\Scripts\python.exe" main.py

Run
# From project folder with venv active
python main.py


Controls:

ESC or q to quit

Troubleshooting

MediaPipe not found / no matching distribution → Use Python 3.11 (not 3.13). Recreate venv with py -3.11 -m venv .venv.

PowerShell blocks activation → Run
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

Camera window opens then closes → Ensure you call cv2.waitKey(1) in loop; check another app isn’t using the camera.

Black screen / slow FPS → Reduce resolution to 640×480; good front lighting; consider disabling debug drawings.

🇮🇹 Italiano
Cos’è?

Una demo divertente che rileva in tempo reale le dita e riproduce un beep per ogni dito alzato — un “pianoforte” minimale con le mani e la webcam.

Funzionalità

Rilevamento mano/landmark in tempo reale (MediaPipe Hands)

Conteggio dita alzate (pollice gestito con right/left)

Modalità opzionale a due mani

Beep semplici come note (prototipo)

Requisiti

Windows 10/11 (testato)

Python 3.11 (consigliato) → MediaPipe non fornisce wheel per 3.13 su Windows al momento

Webcam

Pacchetti: opencv-python, mediapipe (opzionale winsound è nella stdlib su Windows)

Setup (con venv)

PowerShell / Terminale di VS Code

# 1) Verifica Python 3.11
py -3.11 --version

# 2) Crea e attiva l'ambiente
py -3.11 -m venv .venv

# Se l’attivazione è bloccata:
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# Attiva
.\.venv\Scripts\Activate

# 3) Aggiorna pip e installa dipendenze
python -m pip install --upgrade pip setuptools wheel
pip install opencv-python mediapipe


Se non vuoi attivare il venv, puoi eseguire usando direttamente l’interprete del venv:

"percorso\progetto\.venv\Scripts\python.exe" main.py

Esecuzione
# Dalla cartella del progetto con venv attivo
python main.py


Controlli:

ESC o q per uscire

Problemi comuni

MediaPipe non installabile → Usa Python 3.11, ricrea il venv py -3.11 -m venv .venv.

Blocco script PowerShell →
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

Finestra si chiude subito → Assicurati di avere cv2.waitKey(1) nel loop; verifica che nessuna app stia usando la webcam.

Schermo nero / FPS bassi → Imposta 640×480; luce frontale diffusa; disabilita disegni di debug se serve.

Project Structure (suggested)
hand-piano/
├─ main.py
├─ requirements.txt  # optional: opencv-python==4.*, mediapipe==0.10.*
└─ README.md

Notes

This is a prototype: audio uses simple beeps (Windows). Swap in any cross-platform audio lib if you prefer (e.g., simpleaudio).

Two-hand mode increases CPU load; keep lighting stable for better detection.
