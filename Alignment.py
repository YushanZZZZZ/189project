import tkinter as tk

def global_alignment(seq1, seq2):
    print("Processing Global Alignment...")

def local_alignment(seq1, seq2):
    print("Processing Local Alignment...")

def calculate_both():
    seq1 = sequence1.get()
    seq2 = sequence2.get()
    if seq1 == "":
        print("Sequence 1 is empty!") # better to have a pop window
        return
    if seq2 == "":
        print("Sequence 2 is empty!") # better to have a pop window
        return
    # here should add an error check for "A","C","G","T" if other character appears, should report error.


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Sequence Alignment")
    window.geometry("600x400")
    tk.Label(window, text="Sequence 1:", font=("NORMAL", 25)).grid(row=0, column=0)
    tk.Label(window, text="Sequence 2:", font=("NORMAL", 25)).grid(row =1, column=0)
    sequence1 = tk.Entry(window)
    sequence2 = tk.Entry(window)
    sequence1.grid(row=0, column=1)
    sequence2.grid(row=1, column=1)

    submit_button = tk.Button(window,text="submit",font=("NORMAL", 25),command=calculate_both)
    submit_button.grid(row=2, column=0)
    window.mainloop()