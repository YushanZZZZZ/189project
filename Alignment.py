import tkinter as tk
import numpy as np

def global_alignment(seq1, seq2, match=1, mismatch=-1, gap=-2):
    print("Processing Global Alignment...")
    print(f"Sequence1: {seq1}")
    print(f"Sequence2: {seq2}")
    print("Score Matrix:")
    length1 = len(seq1)
    length2 = len(seq2)
    # Initialize the score_matrix and trace matrix
    score_matrix = np.zeros((length1+1,length2+1))
    trace_matrix = [[''] * (length2 + 1) for _ in range(length1 + 1)]
    for i in range(1, length1+1):
        score_matrix[i][0] = score_matrix[i-1][0] + gap
        trace_matrix[i][0] = "Up"
    for j in range(1, length2+1):
        score_matrix[0][j] = score_matrix[0][j-1] + gap
        trace_matrix[0][j] = "Left"
    # Spread through the score_matrix
    for i in range(1, length1+1):
        for j in range(1, length2+1):
            diagonal_score = score_matrix[i-1][j-1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
            vertical_score = score_matrix[i-1][j] + gap
            horizontal_score = score_matrix[i][j-1] + gap
            max_score = max(diagonal_score, vertical_score, horizontal_score)
            score_matrix[i][j] = max_score
            if max_score == diagonal_score:
                trace_matrix[i][j] = "Diagonal"
            elif max_score == vertical_score:
                trace_matrix[i][j] = "Up"
            elif max_score == horizontal_score:
                trace_matrix[i][j] = "Left"
            # print(diagonal_change_score)
            # print(diagonal_score, vertical_score,horizontal_score)
            # print(score_matrix)

    print(score_matrix)
    print(trace_matrix)

    # Start the trace back
    inverse_str1 = ""
    inverse_str2 = ""
    trace_i = length1
    trace_j = length2
    while trace_i > 0 and trace_j > 0:
        current_score = score_matrix[trace_i][trace_j]
        diagonal_score = score_matrix[trace_i-1][trace_j-1]
        vertical_score = score_matrix[trace_i-1][trace_j]
        horizontal_score = score_matrix[trace_i][trace_j-1]
        if (diagonal_score == current_score - mismatch) or (diagonal_score == current_score - match): # if the current value is coming from the diagonal value
            inverse_str1 += seq1[trace_i-1]
            inverse_str2 += seq2[trace_j-1]
            trace_i -= 1
            trace_j -= 1
        elif vertical_score == current_score - gap: # if the current value is coming from vertical value
            inverse_str1 += "-"
            inverse_str2 += seq2[trace_j-1]
            trace_j -= 1
        elif horizontal_score == current_score - gap: # if the current value is coming from vertical value
            inverse_str1 += seq1[trace_i-1]
            inverse_str2 += "-"
            trace_i -= 1
    while trace_i > 0:  # handling the situations when one of the trace value is 0 while other is not.
        inverse_str1 += seq1[trace_i-1]
        inverse_str2 += "-"
        trace_i -= 1
    while trace_j > 0:
        inverse_str1 += "-"
        inverse_str2 += seq2[trace_j-1]
        trace_j -= 1

    str1 = inverse_str1[::-1]
    str2 = inverse_str2[::-1]
    print(str1)
    print(str2)



def local_alignment(seq1, seq2, match=2, mismatch=-1, gap=-2):
    print("Processing Local Alignment...")
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
            if seq1[i-1].equals(seq2[j-1]):
                diagonal_change_score = match
            else:
                diagonal_change_score = mismatch
            diagonal_score = score_matrix[i-1][j-1] + diagonal_change_score
            vertical_score = score_matrix[i-1][j] + gap
            horizontal_score = score_matrix[i][j-1] + gap
            score_matrix[i][j] = max(diagonal_score, vertical_score, horizontal_score)
    print(score_matrix)

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
    global_alignment( "ATCGT","TGGTG")
