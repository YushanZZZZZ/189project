import tkinter as tk

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Sequence Alignment")
    window.geometry("800x600")
    tk.Label(window, text="Sequence 1:", font=("NORMAL", 25)).grid(row=0, column=0)
    tk.Label(window, text="Sequence 2:", font=("NORMAL", 25)).grid(row =1, column=0)
    sequence1 = tk.Entry(window).grid(row=0, column=1)
    sequence2 = tk.Entry(window).grid(row=1, column=1)
    window.mainloop()