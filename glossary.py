import tkinter as tk
from tkinter import messagebox

# 1. THE DATA (The Dictionary)
# This is like a mini-database of your IRS studies
irs_terms = {
    "Diplomacy": "The established method of influencing the decisions and behavior of foreign governments and people through dialogue and negotiation.",
    "Sovereignty": "The full right and power of a governing body over itself, without any interference from outside sources.",
    "Treaty": "A formally concluded and ratified agreement between states.",
    "Sanctions": "Commercial and financial penalties applied by one or more countries against a self-governing state, group, or individual.",
    "Bilateralism": "The conduct of political, economic, or cultural relations between two sovereign states."
}

# 2. THE SEARCH FUNCTION
def search_term():
    query = entry.get().title() # This makes sure 'diplomacy' matches 'Diplomacy'
    
    if query in irs_terms:
        definition = irs_terms[query]
        result_label.config(text=f"{query}:\n\n{definition}", fg="#006633")
    else:
        result_label.config(text="Term not found.", fg="red")
        messagebox.showwarning("Not Found", f"Sorry, '{query}' is not in the IRS database yet.")

# 3. THE INTERFACE
root = tk.Tk()
root.title("Hamxus IRS Glossary")
root.geometry("400x350")

tk.Label(root, text="IRS Terminology Search", font=("Arial", 14, "bold")).pack(pady=15)

tk.Label(root, text="Enter a term (e.g., Treaty, Sovereignty):").pack()
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

tk.Button(root, text="Search Definition", command=search_term, bg="#006633", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 10), wraplength=350, justify="center")
result_label.pack(pady=20)

root.mainloop()