# UI Packages
import customtkinter
import tkinter as tk
from tkinter import messagebox

# Variables to store total, grade, percentage details.
total = None
percentage = None
grade = None


# This function is used to find the total, percentage and grade.
def find_grade(a, b, c, d, e, f, g):
    global total, percentage, grade
    total = a + b + c + d + e + f + g
    percentage = (total / 700) * 100
    percentage = round(percentage, 2)

    if percentage >= 85 and percentage <= 100:
        grade = "O"
    elif percentage >= 70 and percentage <= 84:
        grade = "A"
    elif percentage >= 55 and percentage <= 69:
        grade = "B"
    elif percentage >= 40 and percentage <= 54:
        grade = "C"

    messagebox.showinfo(title="Result", message=f"Total Marks:{total}\n Percentage:{percentage}\n Grade:{grade}\n")


# This function is used to validate the data.
def validate():
    try:
        # Used to read values of entry fields after submit.
        a = int(e1.get())
        b = int(e2.get())
        c = int(e3.get())
        d = int(e4.get())
        e = int(e5.get())
        f = int(e6.get())
        g = int(e7.get())
    except ValueError:
        # Used to display a message when user leaves any field empty while submitting the data.
        messagebox.showerror(title="Invalid Input", message="Empty values are not allowed")
        a, b, c, d, e, f, g = [0] * 7

    # Prevents user from entering values other than 0-100.
    con = [a not in range(0, 101), b not in range(0, 101),
           c not in range(0, 101), d not in range(0, 101),
           e not in range(0, 101), f not in range(0, 101),
           g not in range(0, 101)]

    # Checks if any of the field having values other than 0-100.
    if any(con):
        messagebox.showwarning(title="Invalid Input", message="Enter values correctly")
        del([a, b, c, d, e, f, g])
    # Finds total,grade and percentage when a user got pass marks in all subjects.
    else:
        if all([a >= 40, b >= 40, c >= 40, d >= 40, e >= 40, f >= 40, g >= 40]):
            find_grade(a, b, c, d, e, f, g)
        # Display only total if a user fails in any of the subjects.
        else:
            global total
            total = a + b + c + d + e + f + g
            messagebox.showinfo(title="Result", message=f"Total Marks:{total}\n Percentage:'NA'\n"
                                                        f" Grade:'Fail'\n")


# Used to set window size and title.
ct = customtkinter.CTk()
ct.geometry("530x480")
ct.title("Grading System")
# Used for storing field values after clicking submit.
e1 = tk.StringVar()
e2 = tk.StringVar()
e3 = tk.StringVar()
e4 = tk.StringVar()
e5 = tk.StringVar()
e6 = tk.StringVar()
e7 = tk.StringVar()
e8 = tk.StringVar(value=total)
e9 = tk.StringVar(value=percentage)
e10 = tk.StringVar(value=grade)

# Used to get labels.
for i in range(1, 8):
    sub = customtkinter.CTkLabel(master=ct, text=f"Enter marks of subject-{i}:",
                                     font=customtkinter.CTkFont(family="Times New Roman", size=20))
    sub.grid(row=i-1, column=0, pady=10, padx=20)

# Used to create entry fields.
entry1 = customtkinter.CTkEntry(master=ct, width=250, height=40, fg_color="white", text_color="black",
                                    placeholder_text="Enter value", corner_radius=10, textvariable=e1,
                                font=customtkinter.CTkFont(family="Times New Roman", size=20))
entry1.grid(row=0, column=1, pady=10, padx=20)

entry2 = customtkinter.CTkEntry(master=ct, width=250, height=40, fg_color="white", text_color="black",
                                    placeholder_text="Enter value", corner_radius=10, textvariable=e2,
                                font=customtkinter.CTkFont(family="Times New Roman", size=20))
entry2.grid(row=1, column=1, pady=10, padx=20)

entry3 = customtkinter.CTkEntry(master=ct, width=250, height=40, fg_color="white", text_color="black",
                                    placeholder_text="Enter value", corner_radius=10, textvariable=e3,
                                font=customtkinter.CTkFont(family="Times New Roman", size=20))
entry3.grid(row=2, column=1, pady=10, padx=20)

entry4 = customtkinter.CTkEntry(master=ct, width=250, height=40, fg_color="white", text_color="black",
                                    placeholder_text="Enter value", corner_radius=10, textvariable=e4,
                                font=customtkinter.CTkFont(family="Times New Roman", size=20))
entry4.grid(row=3, column=1, pady=10, padx=20)

entry5 = customtkinter.CTkEntry(master=ct, width=250, height=40, fg_color="white", text_color="black",
                                    placeholder_text="Enter value", corner_radius=10, textvariable=e5,
                                font=customtkinter.CTkFont(family="Times New Roman", size=20))
entry5.grid(row=4, column=1, pady=10, padx=20)

entry6 = customtkinter.CTkEntry(master=ct, width=250, height=40, fg_color="white", text_color="black",
                                    placeholder_text="Enter value", corner_radius=10, textvariable=e6,
                                font=customtkinter.CTkFont(family="Times New Roman", size=20))
entry6.grid(row=5, column=1, pady=10, padx=20)

entry7 = customtkinter.CTkEntry(master=ct, width=250, height=40, fg_color="white", text_color="black",
                                    placeholder_text="Enter value", corner_radius=10, textvariable=e7,
                                font=customtkinter.CTkFont(family="Times New Roman", size=20))
entry7.grid(row=6, column=1, pady=10, padx=20)

# Used for creating submit button.
button = customtkinter.CTkButton(master=ct, text="Submit", anchor="CENTER", width=250, height=40,
                                 corner_radius=10, command=validate)
button.grid(row=7, column=1, pady=10)

ct.mainloop()
