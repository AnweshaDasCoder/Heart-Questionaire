from tkinter import *

root=Tk()
root.title("Heart_Diagnoses_Report")
root.geometry("600x600")
root.configure(background="light pink")

question1_radioButton = StringVar(value="0")

Question1=Label(root,text="Do you experience a shortness of breath during regular activities?")
Question1.pack()
question1_r1=Radiobutton(root,text="yes",variable=question1_radioButton,value="yes")
question1_r1.pack()
question1_r2=Radiobutton(root,text="no",variable=question1_radioButton, value="no")
question1_r2.pack()

question2_radioButton=StringVar(value="0")

Question2=Label(root,text="Do you having swelling at the bottom of your feet/leg/ankle (shoes feel tighter) or abdomen?")
Question2.pack()
question2_r1=Radiobutton(root,text="yes",variable=question2_radioButton,value="yes")
question2_r1.pack()
question2_r2=Radiobutton(root,text="no",variable=question2_radioButton, value="no")
question2_r2.pack()

question3_radioButton = StringVar(value="0")

Question3=Label(root,text="Do you feel any of these syptoms - confusion, disoration, or loss of memory?")
Question3.pack()
question3_r1=Radiobutton(root,text="yes",variable=question3_radioButton, value="yes")
question3_r1.pack()
question3_r2=Radiobutton(root,text="no",variable=question3_radioButton, value="no")
question3_r2.pack()

question4_radioButton = StringVar(value="0")

Question4=Label(root,text="Do you experience shortness of breath while resting/sitting down")
Question4.pack()
question4_r1=Radiobutton(root,text="yes",variable=question4_radioButton, value="yes")
question4_r1.pack()
question4_r2=Radiobutton(root,text="no",variable=question4_radioButton, value="no")
question4_r2.pack()

question5_radioButton = StringVar(value="0")

Question5=Label(root,text="Do you experience costant coughing with white or a pink blood tinged mucus?")
Question5.pack()
question5_r1=Radiobutton(root,text="yes",variable=question5_radioButton, value="yes")
question5_r1.pack()
question5_r2=Radiobutton(root,text="no",variable=question5_radioButton, value="no")
question5_r2.pack()

def heart():
    score=0
    if question1_radioButton.get() == "yes":
        score = score+20
        
    if question2_radioButton.get() == "yes":
        score = score+20
        
    if question3_radioButton.get() == "yes":
        score = score+20
        
    if question4_radioButton.get() == "yes":
        score = score+20
        
    if question5_radioButton.get() == "yes":
        score = score+20
        
    if score <= 20:
        messagebox.showinfo("Report", "You don't need to vist a doctor.")
    elif score > 20 and score <= 30:
        messagebox.showinfo("Report", "You might perhaps have to vist a doctor.")
    elif score > 30 and score <= 40:
            messagebox.showinfo("Report", "I would reccomend you vist a doctor.")
    else :
        messagebox.showinfo("Report","You 100% need to vist the.")
        
btn = Button(root, text="Click Me After Answering All Questions", command = heart)
btn.pack()
root.mainloop()
