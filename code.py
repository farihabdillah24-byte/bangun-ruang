import tkinter as tk
from tkinter import ttk
import math

# Fungsi hitung volume
def hitung():
    bangun = combo.get()
    
    try:
        if bangun == "Kubus":
            s = float(entry1.get())
            volume = s ** 3
            hasil.config(text=f"Volume Kubus = {volume:.2f}")
            
        elif bangun == "Tabung":
            r = float(entry1.get())
            t = float(entry2.get())
            volume = math.pi * r**2 * t
            hasil.config(text=f"Volume Tabung = {volume:.2f}")
            
        elif bangun == "Bola":
            r = float(entry1.get())
            volume = (4/3) * math.pi * r**3
            hasil.config(text=f"Volume Bola = {volume:.2f}")
            
    except:
        hasil.config(text="Input tidak valid!")

# Membuat window
root = tk.Tk()
root.title("Aplikasi Hitung Volume")
root.geometry("400x350")

# Judul
tk.Label(root, text="Aplikasi Hitung Volume Bangun Ruang", 
         font=("Arial", 12, "bold")).pack(pady=10)

# Pilih bangun
tk.Label(root, text="Pilih Bangun:").pack()
combo = ttk.Combobox(root, values=["Kubus", "Tabung", "Bola"])
combo.pack()

# Input 1
tk.Label(root, text="Input 1 (s atau r):").pack()
entry1 = tk.Entry(root)
entry1.pack()

# Input 2 (khusus tabung)
tk.Label(root, text="Input 2 (t untuk Tabung):").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Tombol hitung
tk.Button(root, text="Hitung", command=hitung).pack(pady=10)

# Hasil
hasil = tk.Label(root, text="Hasil akan muncul di sini")
hasil.pack(pady=10)

root.mainloop()