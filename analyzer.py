import tkinter as tk
from tkinter import messagebox

# --- PHASE 1: THE LOGIC (THE BRAIN) ---
def analyze_risk():
    # 1. Get data from the checkboxes
    border = border_var.get()
    trade = trade_var.get()
    talks = talks_var.get()
    
    # 2. Diplomatic Logic Engine
    if border == 1 and talks == 0:
        result = "CRITICAL: High risk of conflict. Immediate mediation required."
        color = "red"
    elif border == 1 and talks == 1:
        result = "TENSE: Border activity detected, but diplomacy is active."
        color = "orange"
    elif border == 0 and trade == 0:
        result = "WARNING: Trade has stopped. Economic instability ahead."
        color = "gold" # Gold shows up better than yellow on white
    else:
        result = "STABLE: Situation is under control."
        color = "green"
    
    # 3. SAVE TO FILE (The Report Generator)
    with open("diplomatic_report.txt", "a") as file:
        file.write(f"--- NEW REPORT ---\n")
        file.write(f"Result: {result}\n")
        file.write(f"Factors: Border={border}, Trade={trade}, Talks={talks}\n")
        file.write("----------------------------\n")
    
    # 4. Update the screen
    status_label.config(text=result, fg=color)
    messagebox.showinfo("Analysis Saved", "The report has been saved to diplomatic_report.txt")

# --- PHASE 2: THE INTERFACE (THE WINDOW) ---
root = tk.Tk()
root.title("Hamxus Diplomatic Analyzer")
root.geometry("450x450")

# Title
tk.Label(root, text="Regional Conflict Risk Assessment", font=("Arial", 14, "bold")).pack(pady=20)

# Checkboxes
border_var = tk.IntVar()
tk.Checkbutton(root, text="Military movement at border?", variable=border_var, font=("Arial", 10)).pack(anchor="w", padx=60)

trade_var = tk.IntVar()
tk.Checkbutton(root, text="Is trade currently active?", variable=trade_var, font=("Arial", 10)).pack(anchor="w", padx=60)

talks_var = tk.IntVar()
tk.Checkbutton(root, text="Are diplomatic talks ongoing?", variable=talks_var, font=("Arial", 10)).pack(anchor="w", padx=60)

# The Analyze Button
tk.Button(root, text="Run Intelligence Analysis", command=analyze_risk, bg="#006633", fg="white", font=("Arial", 11, "bold"), padx=10, pady=5).pack(pady=30)

# The Status Label
status_label = tk.Label(root, text="Waiting for input...", font=("Arial", 10, "italic"))
status_label.pack()

# --- PHASE 3: THE ENGINE START ---
root.mainloop()