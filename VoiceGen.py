
import tkinter as tk
from tkinter import ttk
import pyttsx3
import threading

engine = pyttsx3.init()

def speakagain(text):
    engine.setProperty('rate', speed_var.get())
    engine.setProperty('volume', volume_var.get())

    selected_voice = voice_combo.get()
    voices = engine.getProperty('voices')

    if selected_voice == 'Male Voice':
        engine.setProperty('voice', voices[0].id)
    elif selected_voice == 'Female Voice':
        engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()

def TextToSpeech():
    sentence = text_box.get("1.0", "end-1c").strip()
    if sentence:
        t = threading.Thread(target=speakagain, args=(sentence,))
        t.start()

def clear_text():
    text_box.delete("1.0", "end")

# ================== MAIN WINDOW ==================
root = tk.Tk()
root.title("VoiceGen – Text To Speech Converter")
root.geometry("700x450")
root.minsize(650, 400)
root.configure(bg="#eaf2fb")

# Make window resizable
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)



# ================== MAIN FRAME ==================
main_frame = tk.Frame(root, bg="#eaf2fb")
main_frame.grid(row=0, column=0, sticky="nsew")

for i in range(6):
    main_frame.rowconfigure(i, weight=1)

main_frame.columnconfigure(0, weight=1)

# ================== TITLE ==================
title = tk.Label(
    main_frame,
    text="Text To Speech Converter",
    font=("Segoe UI", 20, "bold"),
    bg="#eaf2fb",
    fg="#1f3c88"
)
title.grid(row=0, column=0, pady=(10,0))

subtitle = tk.Label(
    main_frame,
    text="By Sanjana",
    font=("Segoe UI", 10),
    bg="#eaf2fb"
)
subtitle.grid(row=1, column=0)

# ================== TEXT AREA ==================
label_text = tk.Label(
    main_frame,
    text="Enter Text:",
    font=("Calibri", 15),
    bg="#eaf2fb"
)
label_text.grid(row=2, column=0, pady=(10,5))

text_box = tk.Text(
    main_frame,
    height=6,
    font=("Segoe UI", 11),
    wrap="word"
)
text_box.grid(row=3, column=0, padx=100, sticky="ew")

# ================== CONTROLS FRAME ==================
controls_frame = tk.Frame(main_frame, bg="#eaf2fb")
controls_frame.grid(row=4, column=0, pady=15)

# Voice
voice_label = tk.Label(
    controls_frame,
    text="Select Voice",
    font=("Calibri", 13),
    bg="#eaf2fb"
)
voice_label.grid(row=0, column=0, padx=20)

voice_combo = ttk.Combobox(
    controls_frame,
    values=["Male Voice", "Female Voice"],
    state="readonly"
)
voice_combo.set("Male Voice")
voice_combo.grid(row=1, column=0, padx=20)

# Volume
volume_label = tk.Label(
    controls_frame,
    text="Volume Level",
    font=("Calibri", 13),
    bg="#eaf2fb"
)
volume_label.grid(row=0, column=1, padx=20)

volume_var = tk.DoubleVar(value=1.0)
volume_scale = tk.Scale(
    controls_frame,
    from_=0,
    to=1,
    resolution=0.1,
    orient="horizontal",
    variable=volume_var
)
volume_scale.grid(row=1, column=1, padx=20)

# Speed
speed_label = tk.Label(
    controls_frame,
    text="Speech Speed",
    font=("Calibri", 13),
    bg="#eaf2fb"
)
speed_label.grid(row=0, column=2, padx=20)

speed_var = tk.IntVar(value=150)
speed_scale = tk.Scale(
    controls_frame,
    from_=50,
    to=300,
    orient="horizontal",
    variable=speed_var
)
speed_scale.grid(row=1, column=2, padx=20)

# ================== BUTTONS ==================
button_frame = tk.Frame(main_frame, bg="#eaf2fb")
button_frame.grid(row=5, column=0)

convert_btn = ttk.Button(
    button_frame,
    text="🔊 Convert to Speech",
    command=TextToSpeech
)
convert_btn.grid(row=0, column=0, padx=10, pady=10)

clear_btn = ttk.Button(
    button_frame,
    text="🧹 Clear",
    command=clear_text
)
clear_btn.grid(row=0, column=1, padx=10, pady=10)

root.bind('<Return>', lambda event: TextToSpeech())

root.mainloop()

