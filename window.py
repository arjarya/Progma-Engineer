import tkinter as tk
window = tk.Tk()
window.title("My First GUI")
label = tk.Label(window, font=("Arial Bold", 20), bg="yellow", fg="blue")
label.pack(padx=20, pady=20)

window.mainloop()