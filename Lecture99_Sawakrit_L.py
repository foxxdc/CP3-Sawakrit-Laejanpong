from tkinter import *


def leftclickbotton(event):
    print(float(textBoxWeight.get()) / ((float(textBoxHeight.get()) / 100) ** 2))
    labelResult.configure(text=float(textBoxWeight.get()) / ((float(textBoxHeight.get()) / 100) ** 2))
    result = float(textBoxWeight.get()) / ((float(textBoxHeight.get()) / 100) ** 2)
    if result > 29.9:
        labelBMI.configure(text="YOU SO FAT GO SEE DOCTOR MY FRIEND", fg="red")
    elif result > 24.9:
        labelBMI.configure(text="You pretty fat.. better start workout", fg="orange")
    elif result > 22.9:
        labelBMI.configure(text="pretty good weight but still kida chub", fg="yellow")
    elif result > 18.5:
        labelBMI.configure(text="Normal weight (You mid asf)", fg="green")
    else:
        labelBMI.configure(text="Too skinny mister skeleton", fg="red")


def rightclickbotton(event):
    print("Right Click")


def Doubleclickbotton(event):
    print("CLICK CLICKx2")


MainWindow = Tk()
labelHeight = Label(MainWindow, text="Height (cm)").grid(row=0, column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0, column=1)
labelHeight = Label(MainWindow, text="Weight (kg)").grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)
calcalateButton = Button(MainWindow, text="Calculate")
calcalateButton.bind("<Button-1>", leftclickbotton)
calcalateButton.grid(row=2, column=0)
labelResult = Label(MainWindow, text="Final result")
labelResult.grid(row=2, column=1)
labelBMI = Label(MainWindow, text="Your freaking rank :")
labelBMI.grid(row=2, column=2)
MainWindow.mainloop()
