import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def global_alignment(seq1, seq2, match=1, mismatch=-1, gap=-2):
    print("Processing Global Alignment...")
    print(f"Sequence1: {seq1}")
    print(f"Sequence2: {seq2}")
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

    # Start the trace back
    inverse_str1 = ""
    inverse_str2 = ""
    trace_i = length1
    trace_j = length2
    while trace_i > 0 and trace_j > 0:
        if trace_matrix[trace_i][trace_j] == "Diagonal":
            inverse_str1 += seq1[trace_i - 1]
            inverse_str2 += seq2[trace_j - 1]
            trace_i -= 1
            trace_j -= 1
        elif trace_matrix[trace_i][trace_j] == "Up":
            inverse_str1 += seq1[trace_i - 1]
            inverse_str2 += '-'
            trace_i -= 1
        elif trace_matrix[trace_i][trace_j] == "Left":
            inverse_str1 += '-'
            inverse_str2 += seq1[trace_j - 1]
            trace_j -= 1
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
    return str1, str2, score_matrix, trace_matrix

def local_alignment(seq1, seq2, match=1, mismatch=-1, gap=-2):
    print("Processing Local Alignment...")
    print(f"Sequence1: {seq1}")
    print(f"Sequence2: {seq2}")
    length1 = len(seq1)
    length2 = len(seq2)
    # Initialize the score_matrix and trace matrix
    score_matrix = np.zeros((length1+1,length2+1))
    trace_matrix = [[''] * (length2 + 1) for _ in range(length1 + 1)]
    # Add the max score value and location
    for i in range(1, length1+1):
        score_matrix[i][0] = score_matrix[i-1][0] + gap
        trace_matrix[i][0] = "Up"
    for j in range(1, length2+1):
        score_matrix[0][j] = score_matrix[0][j-1] + gap
        trace_matrix[0][j] = "Left"
    # Spread through the score_matrix
    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            diagonal_score = score_matrix[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
            vertical_score = score_matrix[i - 1][j] + gap
            horizontal_score = score_matrix[i][j - 1] + gap
            max_score = max(diagonal_score, vertical_score,horizontal_score)  # Local alignment scores can't be negative
            score_matrix[i][j] = max_score
            if max_score == diagonal_score:
                trace_matrix[i][j] = "Diagonal"
            elif max_score == vertical_score:
                trace_matrix[i][j] = "Up"
            elif max_score == horizontal_score:
                trace_matrix[i][j] = "Left"
    # Loop through the score matrix to find the biggest value
    max_score = 0
    max_position = (0, 0)
    for i in range(1, length1+1):
        for j in range(1, length2+1):
            if score_matrix[i][j] >= max_score:
                max_score = score_matrix[i][j]
                max_position = (i, j)

    # Start the trace back
    inverse_str1 = ""
    inverse_str2 = ""
    trace_i, trace_j = max_position
    while score_matrix[trace_i][trace_j] != 0 :
        if trace_matrix[trace_i][trace_j] == "Diagonal":
            inverse_str1 += seq1[trace_i - 1]
            inverse_str2 += seq2[trace_j - 1]
            trace_i -= 1
            trace_j -= 1
        elif trace_matrix[trace_i][trace_j] == "Up":
            inverse_str1 += seq1[trace_i - 1]
            inverse_str2 += '-'
            trace_i -= 1
        elif trace_matrix[trace_i][trace_j] == "Left":
            inverse_str1 += '-'
            inverse_str2 += seq2[trace_j - 1]
            trace_j -= 1

    str1 = inverse_str1[::-1]
    str2 = inverse_str2[::-1]
    return str1, str2, score_matrix, trace_matrix, max_score ,max_position

def get_match_value(str1, str2, match=1, mismatch=-1, gap=-2):
    score = 0
    length = len(str1)
    for i in range(length):
        if str1[i] == str2[i]:
            score += match
        elif str1[i] == '-' or str2[i] == '-':
            score += gap
        else:
            score += mismatch
    return score

def calculate_both():
    seq1 = sequence1.get()
    seq2 = sequence2.get()
    match_value = int(match.get())
    mismatch_value = int(mismatch.get())
    gap_value = int(gap.get())
    if seq1 == "":
        print("Sequence 1 is empty!") # better to have a pop window
        return
    if seq2 == "":
        print("Sequence 2 is empty!") # better to have a pop window
        return
    # here should add an error check for "A","C","G","T" if other character appears, should report error.
    str1, str2, score_matrix, trace_matrix = global_alignment(seq1, seq2, match=match_value,mismatch=mismatch_value, gap=gap_value)
    str3, str4, score_matrix2, trace_matrix2, max_score ,max_position = local_alignment(seq1, seq2, match=match_value, mismatch=mismatch_value, gap=gap_value)
    global_match_value = get_match_value(str1, str2, match=match_value, mismatch=mismatch_value, gap=gap_value)
    local_match_value = get_match_value(str3, str4, match=match_value, mismatch=mismatch_value, gap=gap_value)
    display_results(seq1, seq2, str1, str2, str3, str4, match_value, mismatch_value, gap_value, max_score ,max_position, global_match_value, local_match_value, score_matrix)
def display_results(seq1, seq2, str1, str2, str3, str4, match_value, mismatch_value, gap_value, max_score ,max_position, global_match_value, local_match_value, score_matrix):
    result_window = tk.Toplevel()
    result_window.title("Alignment Results")
    result_window.geometry("800x600")

    text = tk.Text(result_window, wrap = 'word', font = ("Helvetica", 10))
    text.pack(expand = 1, fill = 'both')

    text.insert(tk.END, f"Two Sequences: \n{seq1}\n{seq2}\n\n")
    text.insert(tk.END, f"Parameters:\nMatch Value: {match_value}\nMismatch Value: {mismatch_value}\nGap Value: {gap_value}\n\n")
    text.insert(tk.END, "Score Matrix:\n")
    text.insert(tk.END, np.array2string(score_matrix, separator = ', ') + "\n\n")
    text.insert(tk.END, "Global Alignment Result:\n")
    text.insert(tk.END, f"{str1}\n{str2}\n\n")
    text.insert(tk.END, f"Final Match Value: {global_match_value}\n\n")
    text.insert(tk.END, "Local Alignment:\n")
    text.insert(tk.END, f"{str3}\n{str4}\n")
    text.insert(tk.END, f"Max Score: {max_score}\nMax Position: {max_position}\n\n")
    text.insert(tk.END, f"Final Match Value: {local_match_value}\n\n")

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Sequence Alignment")
    window.geometry("300x250")
    tk.Label(window, text="Sequence 1:", font=("NORMAL", 25)).grid(row=0, column=0)
    tk.Label(window, text="Sequence 2:", font=("NORMAL", 25)).grid(row=1, column=0)
    tk.Label(window, text="Match Value:", font =("NORMAL", 15)).grid(row=2, column=0)
    tk.Label(window, text="Mismatch Value:", font =("NORMAL", 15)).grid(row=3, column=0)
    tk.Label(window, text="Gap Value:", font =("NORMAL", 15)).grid(row=4, column=0)
    sequence1 = tk.Entry(window)
    sequence2 = tk.Entry(window)
    match = tk.Entry(window)
    mismatch = tk.Entry(window)
    gap = tk.Entry(window)
    sequence1.grid(row=0, column=1)
    sequence2.grid(row=1, column=1)
    match.grid(row = 2, column = 1)
    mismatch.grid(row = 3, column = 1)
    gap.grid(row = 4, column = 1)
    match.insert(0,"1")
    mismatch.insert(0, "-1")
    gap.insert(0, "0")

    submit_button = tk.Button(window,text="submit",font=("NORMAL", 25),command=calculate_both)
    submit_button.grid(row=5, column=0)
    window.mainloop()