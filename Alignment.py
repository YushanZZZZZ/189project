import tkinter as tk
import numpy as np

def global_alignment(seq1, seq2, match=2, mismatch=-1, gap=-2):
    print("Processing Global Alignment...")
    print(f"Sequence1: {seq1}")
    print(f"Sequence2: {seq2}")
    print("Score Matrix:")
    length1 = len(seq1)
    length2 = len(seq2)
    # Initialize the score_matrix
    score_matrix = np.zeros((length1+1,length2+1))
    for i in range(1, length1+1):
        score_matrix[0][i] = score_matrix[0][i-1] + gap
    for j in range(1, length2+1):
        score_matrix[j][0] = score_matrix[j-1][0] + gap
    # Spread through the score_matrix
    for i in range(1, length1+1):
        for j in range(1, length2+1):
            if seq1[i-1] == seq2[j-1]:
                diagonal_change_score = match
            else:
                diagonal_change_score = mismatch
            diagonal_score = score_matrix[i-1][j-1] + diagonal_change_score
            vertical_score = score_matrix[i-1][j] + gap
            horizontal_score = score_matrix[i][j-1] + gap
            score_matrix[i][j] = max(diagonal_score, vertical_score, horizontal_score)
    print(score_matrix)

    # Start the trace back


def local_alignment(seq1, seq2, match=2, mismatch=-1, gap=-2):
    print("Processing Local Alignment...")
    print(f"Sequence1: {seq1}")
    print(f"Sequence2: {seq2}")
    print("Score Matrix:")

# def calculate_both():
#     seq1 = sequence1.get()
#     seq2 = sequence2.get()
#     if seq1 == "":
#         print("Sequence 1 is empty!") # better to have a pop window
#         return
#     if seq2 == "":
#         print("Sequence 2 is empty!") # better to have a pop window
#         return
    # here should add an error check for "A","C","G","T" if other character appears, should report error.


if __name__ == "__main__":
    # window = tk.Tk()
    # window.title("Sequence Alignment")
    # window.geometry("600x400")
    # tk.Label(window, text="Sequence 1:", font=("NORMAL", 25)).grid(row=0, column=0)
    # tk.Label(window, text="Sequence 2:", font=("NORMAL", 25)).grid(row =1, column=0)
    # sequence1 = tk.Entry(window)
    # sequence2 = tk.Entry(window)
    # sequence1.grid(row=0, column=1)
    # sequence2.grid(row=1, column=1)
    #
    # submit_button = tk.Button(window,text="submit",font=("NORMAL", 25),command=calculate_both)
    # submit_button.grid(row=2, column=0)
    # window.mainloop()
    global_alignment("ATTCC", "ATTCC")
