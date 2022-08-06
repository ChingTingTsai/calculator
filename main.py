import tkinter as tk
import tkinter.font as tkFont


class Calculator():
    def __init__(self):
        self.current = 0

    def add(self, num):
        self.current += num

    def subtract(self, num):
        self.current -= num

    def multiply(self, num):
        self.current *= num

    def division(self, num):
        self.current /= num

    def restart(self):
        self.current = 0

    def getVal(self):
        return self.current

    def setVal(self, val):
        self.current += val


class calculatorGUI():
    def __init__(self):
        self.calc = Calculator()
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("400x520")
        self.mainFrame = tk.Frame(padx = 5, background="#E4E4E4", highlightbackground="black", highlightthickness=2)
        self.mainFrame.pack()
        self.val = tk.StringVar()
        self.restart()
        self.showVal()
        self.drawCalcButton()
        self.root.mainloop()

    def restart(self):
        self.valstr = ""
        self.curFunc = None
        self.calc.restart()
        self.val.set(0)

    def incNum(self, num):
        self.valstr += num
        self.val.set(self.valstr)
    
    def setFunc(self, symb):
        if self.curFunc == None:
            self.calc.setVal(float(self.valstr))
        elif self.curFunc != "AC" and self.valstr != "":
            self.curFunc(float(self.valstr))

        if symb == "+":
            self.curFunc = self.calc.add
        elif symb == "-":
            self.curFunc = self.calc.subtract
        elif symb == "*":
            self.curFunc = self.calc.multiply
        elif symb == "/":
            self.curFunc = self.calc.division
        elif symb == "=":
            self.curFunc = "AC"
        self.val.set(str(self.calc.getVal()))
        self.valstr = ""

    def deleteVal(self):
        self.valstr = ""
        self.val.set(0)

    def showVal(self):
        myFont = tkFont.Font(size=25)
        label = tk.Label(self.mainFrame, width=14, height=2, bd=3, relief= "solid", textvariable=self.val, justify= tk.RIGHT)
        self.val.set(self.calc.getVal())
        label['font'] = myFont
        label.pack(pady = 10)

    def drawCalcButton(self):
        buttonFrame = tk.Frame(self.mainFrame, background="#E4E4E4")
        buttonFrame.pack(pady = 20)

        myFont = tkFont.Font(size=20)

        bc = tk.Button(buttonFrame, text="C", height=2, width=4, bg="#E55151", command = lambda:self.deleteVal())
        bc.grid(column=3, row=1, padx=1, pady = 1)
        bc['font'] = myFont
        bac = tk.Button(buttonFrame, text="AC", bg="#E55151", height=2, width=4, command = lambda:self.restart())
        bac.grid(column=2, row=1, padx=1, pady = 1)
        bac['font'] = myFont

        b7 = tk.Button(buttonFrame, text="7", bg="#0066CC", height=2, width=4, command = lambda:self.incNum("7"))
        b7.grid(column=0, row=2, padx=1, pady = 1)
        b7['font'] = myFont
        b8 = tk.Button(buttonFrame, text="8", bg="#0066CC", height=2, width=4, command = lambda:self.incNum("8"))
        b8.grid(column=1, row=2, padx=1, pady = 1)
        b8['font'] = myFont
        b9 = tk.Button(buttonFrame, text="9", bg="#0066CC", height=2, width=4, command = lambda:self.incNum("9"))
        b9.grid(column=2, row=2, padx=1, pady = 1)
        b9['font'] = myFont
        bdiv = tk.Button(buttonFrame, text="/", bg="#0066CC", height=2, width=4, command = lambda:self.setFunc("/"))
        bdiv.grid(column=3, row=2, padx=1, pady = 1)
        bdiv['font'] = myFont

        b4 = tk.Button(buttonFrame, text="4", bg="#0066CC", height=2, width=4, command = lambda:self.incNum("4"))
        b4.grid(column=0, row=3, padx=1, pady = 1)
        b4['font'] = myFont
        b5 = tk.Button(buttonFrame, text="5", bg="#0066CC", height=2, width=4, command = lambda:self.incNum("5"))
        b5.grid(column=1, row=3, padx=1, pady = 1)
        b5['font'] = myFont
        b6 = tk.Button(buttonFrame, text="6", bg="#0066CC", height=2, width=4, command = lambda:self.incNum("6"))
        b6.grid(column=2, row=3, padx=1, pady = 1)
        b6['font'] = myFont
        bmul = tk.Button(buttonFrame, text="X", bg="#0066CC", height=2, width=4, command = lambda:self.setFunc("*"))
        bmul.grid(column=3, row=3, padx=1, pady = 1)
        bmul['font'] = myFont

        b1 = tk.Button(buttonFrame, text="1", bg="#0066CC", height=2, width=4, command = lambda:self.incNum("1"))
        b1.grid(column=0, row=4, padx=1, pady = 1)
        b1['font'] = myFont
        b2 = tk.Button(buttonFrame, text="2", bg="#0066CC", height=2, width=4, command = lambda:self.incNum("2"))
        b2.grid(column=1, row=4, padx=1, pady = 1)
        b2['font'] = myFont
        b3 = tk.Button(buttonFrame, text="3", bg="#0066CC",height=2, width=4, command = lambda:self.incNum("3"))
        b3.grid(column=2, row=4, padx=1, pady = 1)
        b3['font'] = myFont
        bsub = tk.Button(buttonFrame, text="-", bg="#0066CC", height=2, width=4, command = lambda:self.setFunc("-"))
        bsub.grid(column=3, row=4, padx=1, pady = 1)
        bsub['font'] = myFont

        b0 = tk.Button(buttonFrame, text="0", bg="#0066CC", height=2, width=4, command = lambda:self.incNum("0"))
        b0.grid(column=0, row=5, padx=1, pady = 1)
        b0['font'] = myFont
        bdot = tk.Button(buttonFrame, text=".", bg="#0066CC", height=2, width=4, command = lambda:self.incNum("."))
        bdot.grid(column=1, row=5, padx=1, pady = 1)
        bdot['font'] = myFont
        beql = tk.Button(buttonFrame, text="=", bg="#0066CC", height=2, width=4, command = lambda:self.setFunc("="))
        beql.grid(column=2, row=5, padx=1, pady = 1)
        beql['font'] = myFont
        badd = tk.Button(buttonFrame, text="+", bg="#0066CC", height=2, width=4, command = lambda:self.setFunc("+"))
        badd.grid(column=3, row=5, padx=1, pady = 1)
        badd['font'] = myFont


if __name__ == "__main__":
    print("Start")
    calculatorGUI()