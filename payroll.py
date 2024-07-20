from tkinter import *
from tkinter import ttk, messagebox

Payroll_Form = Tk()

Payroll_Form.title("Payroll")

Font_Hel = ("Helvetica", "12", "bold")

Payroll_Form.geometry("600x400")
Payroll_Form.configure(background="grey")

FN = Label(Payroll_Form, text="Name", font=Font_Hel, anchor="w")
FN.place(x=10, y=10)

Date = Label(Payroll_Form, text="Date", font=Font_Hel, anchor="w")
Date.place(x=10, y=60)

Hours = Label(Payroll_Form, text="Hours", font=Font_Hel, anchor="w")
Hours.place(x=10, y=110)

Rate = Label(Payroll_Form, text="Rate", font=Font_Hel, anchor="w")
Rate.place(x=10, y=160)

FN_txt = Entry(Payroll_Form)
FN_txt.place(x=100, y=10)

Date_txt = Entry(Payroll_Form)
Date_txt.place(x=100, y=60)

Hours_txt = Entry(Payroll_Form)
Hours_txt.place(x=100, y=110)

Rate_txt = Entry(Payroll_Form)
Rate_txt.place(x=100, y=160)

def Show_Msg():
    messagebox.showinfo("Instructions",
                        "Please enter your name, the current date, hours worked for the 2 weeks, and your Rate then "
                        "press save")


def Save_details_button():
    FN = FN_txt.get()
    Date = Date_txt.get()
    Hours = Hours_txt.get()
    Rate = Rate_txt.get()
    Hours = float(Hours)
    Rate = float(Rate)
    Paid_Amount = Hours * Rate
    Paid_Amount = str(Paid_Amount)

    File = open("Paid.txt", "a")
    File.write(FN_txt.get())
    File.write(",")
    File.write(Date_txt.get())
    File.write(",")
    File.write(Hours_txt.get())
    File.write(",")
    File.write(Rate_txt.get())
    File.write(",")
    File.write(Paid_Amount)
    File.write("\n")
    File.close()

    messagebox.showinfo("File Saved", "The file has been updated")
    messagebox.showinfo("Pay", "The amount should be" + Paid_Amount)


ttk.Button(Payroll_Form, text="Save details", command=Save_details_button).place(x=100, y=200)

Payroll_Form.mainloop()