import tkinter as tk
from tkinter import messagebox
import subprocess

# --- FUNCTIONS TO OPEN THE OTHER APPS ---
def open_analyzer():
    try:
        # Runs analyzer.py in a separate process
        subprocess.Popen(['python', 'analyzer.py'])
    except Exception as e:
        messagebox.showerror("Error", f"Could not open Analyzer.\nDetails: {e}")

def open_glossary():
    try:
        # Runs glossary.py in a separate process
        subprocess.Popen(['python', 'glossary.py'])
    except Exception as e:
        messagebox.showerror("Error", f"Could not open Glossary.\nDetails: {e}")

# --- INTERFACE SETUP ---
root = tk.Tk()
root.title("Hamxus IRS Software Suite")
root.geometry("500x400")
root.configure(bg="#f4f4f4")

# Main Title Header (Fixed padding format)
header_frame = tk.Frame(root, bg="#002244")
header_frame.pack(fill="x", ipady=15)

title_label = tk.Label(
    header_frame, 
    text="HAMXUS DIGITAL DIPLOMACY LAB", 
    font=("Arial", 16, "bold"), 
    fg="white", 
    bg="#002244"
)
title_label.pack(pady=5)

subtitle_label = tk.Label(
    header_frame, 
    text="Decision Support & Academic Tools", 
    font=("Arial", 10, "italic"), 
    fg="#dcdcdc", 
    bg="#002244"
)
subtitle_label.pack()

# Selection Frame
menu_frame = tk.Frame(root, bg="#f4f4f4")
menu_frame.pack(pady=40)

# Button 1: Conflict Analyzer
btn_analyzer = tk.Button(
    menu_frame, 
    text="Launch Conflict Analyzer", 
    command=open_analyzer, 
    bg="#006633", # NEU Green
    fg="white", 
    font=("Arial", 11, "bold"), 
    width=25, 
    height=2
)
btn_analyzer.grid(row=0, column=0, pady=15, padx=10)

# Button 2: Glossary Search
btn_glossary = tk.Button(
    menu_frame, 
    text="Launch IRS Glossary", 
    command=open_glossary, 
    bg="#006633", 
    fg="white", 
    font=("Arial", 11, "bold"), 
    width=25, 
    height=2
)
btn_glossary.grid(row=1, column=0, pady=15, padx=10)

# Footer
footer = tk.Label(
    root, 
    text="Developed by Hamza Umar | North-Eastern University", 
    font=("Arial", 9, "italic"), 
    bg="#f4f4f4", 
    fg="gray"
)
footer.pack(side="bottom", pady=15)

root.mainloop()