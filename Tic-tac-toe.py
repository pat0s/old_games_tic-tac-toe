# Tic-tac-toe Game
# Author: Patrik Sehnoutek (pat0s)
# Date: August 2018


#=================================Splash Window===========================================
import tkinter
from tkinter import ttk
master = tkinter.Tk()
master.resizable(False,False)


image_file = "cord_.gif"
image = tkinter.PhotoImage(file = image_file)

window_height = 500
window_width = 500

screen_width  = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

master.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

s = tkinter.Canvas(master, width = 500, height = 500)

master.overrideredirect(1)

s.create_image(x_cordinate-120, y_cordinate+210,    
                   image = image,anchor="center")
s.create_text( 330, 470, text = "The app is powered by Cord",
		  fill = "gray", font = "Velvetica 10", anchor="sw")
s.create_text( 140, 470, text = "Made by Patos © 2018",
		  fill = "gray", font = "Velvetica 10", anchor="se")
style = ttk.Style()
style.theme_use('clam')
style.configure("red.Horizontal.TProgressbar", foreground ='red', background='red')
pb = ttk.Progressbar(master,  style="red.Horizontal.TProgressbar",orient="horizontal", length=500, mode="determinate")
pb.pack()
pb.start()
s.pack()

master.after(5000, lambda: master.destroy())
master.mainloop()

#===================================The Game===========================================

def qQuit():
        qExit = messagebox.askyesno("Exit program", " Do u want to exit a program?")
        if qExit >0:
            app.destroy()
            return

from tkinter import*
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter import messagebox
import random



class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="ttt.ico")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)           
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}

        for F in (MainMenu, SinglePlayer, MultiPlayer, Online, HowToPlay):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column = 0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

#=========================================-Main Menu====================================================


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):  #parent is class above SeaofBTCapp
        tk.Frame.__init__(self,parent)    
        label = tk.Label(self, text="GAME MENU", font=('Velvetica 15 bold'), anchor="center")
        label.grid(row=0, column = 1)

        lbl = tk.Label(self, text = " ", width= 17)
        lbl.grid(row = 0, column = 0)
        
        lbl1 = tk.Label(self, text = " ", width= 17)
        lbl1.grid(row = 1, column = 1)
        lbl2 = tk.Label(self, text = " ", width= 30)
        lbl2.grid(row = 3, column = 1)
        lbl3 = tk.Label(self, text = " ", width= 30)
        lbl3.grid(row = 5, column = 1)
        lbl4 = tk.Label(self, text = " ", width= 30)
        lbl4.grid(row = 7, column = 1)
        lbl5 = tk.Label(self, text = " ", width= 30)
        lbl5.grid(row = 9, column = 1)
        
        button1 = tk.Button(self, text="Single Player",font=('Velvetica 12 bold'), width = 25,height=1, fg="white", bg="black",
                            activeforeground = "white",activebackground = "black",
                            command=lambda: controller.show_frame(SinglePlayer),cursor="circle")
        button1.grid(row = 2, column = 1)

        button2 = tk.Button(self, text="Multi Player",font=('Velvetica 12 bold'), height=1,width = 25,fg="white", bg="black",
                            activeforeground = "white",activebackground = "black",
                            command=lambda: controller.show_frame(MultiPlayer),cursor="circle")
        button2.grid(row= 4, column = 1)

        button3 = tk.Button(self, text="Online",font=('Velvetica 12 bold'), height=1,width = 25,fg="white", bg="black",
                            activeforeground = "white",activebackground = "black",
                            command=lambda: controller.show_frame(Online),cursor="circle")
        button3.grid(row = 6, column = 1)

        button4 = tk.Button(self, text="How to play?",font=('Velvetica 12 bold'), height=1,width = 25,fg="white", bg="black",
                            activeforeground = "white",activebackground = "black",
                            command=lambda: controller.show_frame(HowToPlay))
        button4.grid(row = 8, column = 1)

        button5 = tk.Button(self, text="Quit",font=('Velvetica 12 bold'), height=1,width = 25,fg="white", bg="red",
                            activeforeground = "white",activebackground = "red",
                            command=qQuit)
        button5.grid(row = 10, column = 1)


#====================================SinglePlayer=====================================
        
class SinglePlayer(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)

                
#--------------------------------------variables + functions-----------------------------------------------
        def Reset():
            global game
            global theBoard
            global playerletter, computerletter
            global turn
            game = True
            theBoard = [" "]*10
            _btn7 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_btn7, 7))
            _btn7.grid(row=3, column = 0, sticky="nsew")

            _btn8 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_btn8, 8))
            _btn8.grid(row=3, column = 1, sticky="nsew")

            _btn9 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_btn9, 9))
            _btn9.grid(row=3, column = 2, sticky="nsew")

            _btn4 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_btn4, 4))
            _btn4.grid(row=4, column = 0, sticky="nsew")

            _btn5 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_btn5, 5))
            _btn5.grid(row=4, column = 1, sticky="nsew")

            _btn6 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_btn6, 6))
            _btn6.grid(row=4, column = 2, sticky="nsew")

            _btn1 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_btn1, 1))
            _btn1.grid(row=5, column = 0, sticky = "nsew")

            _btn2 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                          bg="white",command=lambda:checker(_btn2, 2))
            _btn2.grid(row=5, column = 1, sticky="nsew")

            _btn3 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_btn3, 3))
            _btn3.grid(row=5, column = 2, sticky="nsew")

            playerletter, computerletter = character()
            if playerletter == "O":
                colorP1 = "blue"
                colorP2 = "red"
            else:
                colorP1 = "red"
                colorP2 = "blue"

            lblInfo1 = tk.Label(self,font=('Times', 15, 'bold'),text="Player",fg=colorP1,
                             height=1, width = 7, anchor = "center")
            lblInfo1.grid(row = 2, column = 0)

            lblInfo2 = tk.Label(self,font=('Times', 15, 'bold'),text="Computer",fg=colorP2,
                             height=1, width = 7, anchor = "center")
            lblInfo2.grid(row = 2, column = 2)

            turn = whoGoesFirst()

            if turn == "computer":
                if game == True:                
                                move = getComputerMove(theBoard, computerletter)
                                makeMove(theBoard, computerletter, move)
                                drawComputerMove(move)
                                #draw the computer move to board !!!

                                if isWinner(theBoard, computerletter):
                                    tkinter.messagebox.showinfo("Winner" + computerletter, "You have just won a game!!!")
                                    game = False
                                else:
                                    if fullBoard(theBoard):
                                        tkinter.messagebox.showinfo("Draw", "It's a tie!!!")
                                        game = False
                turn = "player"

            
        def character():
            if random.randint(0,1) == 1:
                return ["X","O"]
            else:
                return ["O","X"]
        
        def whoGoesFirst():
            if random.randint(0,1) == 1:
                return "computer"
            else:
                return "player"

        def makeMove(board, letter, move):
            board[move] = letter


        def isWinner(bo, le):
            return((bo[7] == le and bo[8] == le and bo[9] == le) or
                   (bo[4] == le and bo[5] == le and bo[6] == le) or
                   (bo[1] == le and bo[2] == le and bo[3] == le) or
                   (bo[7] == le and bo[4] == le and bo[1] == le) or
                   (bo[8] == le and bo[5] == le and bo[2] == le) or
                   (bo[9] == le and bo[6] == le and bo[3] == le) or
                   (bo[7] == le and bo[5] == le and bo[3] == le) or
                   (bo[9] == le and bo[5] == le and bo[1] == le))

        def isSpaceFree(board, move):
            return board[move] == " "

        def getBoardCopy(board):
            dupBoard = []
            for i in board:
                dupBoard.append(i)
                
            return dupBoard
                     
        def randomMoveFromList(board, movesList):
            possibleMoves = []

            for i in movesList:
                if isSpaceFree(board, i):
                    possibleMoves.append(i)

            if len(possibleMoves) != 0:
                return random.choice(possibleMoves)
            else:
                return None

        def getComputerMove(board, computerletter):

            if computerletter == "X":
                playerletter = "O"
            else:
                playerletter = "X"

            for i in range(1,10):
                copy = getBoardCopy(board)
                if isSpaceFree(board, i):
                    makeMove(copy, computerletter, i)
                    if isWinner(copy, computerletter):
                        return i

            for i in range(1, 10):
                copy = getBoardCopy(board)
                if isSpaceFree(board, i):
                    makeMove(copy, playerletter, i)
                    if isWinner(copy, playerletter):
                        return i

            move = randomMoveFromList(board, [1,3,7,9])

            if move != None:
                return move

            if isSpaceFree(board, 5):
                return 5

            return randomMoveFromList(board, [2,4,6,8])


        def drawComputerMove(move):
            buttons = StringVar()
            if computerletter == "O":
                color = "blue"
            else:
                color = "red"
            if move == 1:
                _btn1 = tk.Button(self, text=computerletter, font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",fg = color,command=lambda:checker(_btn1, 1))
                _btn1.grid(row=5, column = 0, sticky="nsew")
            elif move == 2:
                _btn2 = tk.Button(self, text=computerletter, font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",fg = color,command=lambda:checker(_btn2, 2))
                _btn2.grid(row=5, column = 1, sticky="nsew")
            elif move == 3:
                _btn3 = tk.Button(self, text=computerletter, font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",fg = color,command=lambda:checker(_btn3, 3))
                _btn3.grid(row=5, column = 2, sticky="nsew")
            elif move == 4:
                _btn4 = tk.Button(self, text=computerletter, font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",fg = color,command=lambda:checker(_btn4, 4))
                _btn4.grid(row=4, column = 0, sticky="nsew")
            elif move == 5:
                _btn5 = tk.Button(self, text=computerletter, font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",fg = color,command=lambda:checker(_btn5, 5))
                _btn5.grid(row=4, column = 1, sticky="nsew")
            elif move == 6:
                _btn6 = tk.Button(self, text=computerletter, font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",fg = color,command=lambda:checker(_btn6, 6))
                _btn6.grid(row=4, column = 2, sticky="nsew")
            elif move == 7:
                _btn7 = tk.Button(self, text=computerletter, font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",fg = color,command=lambda:checker(_btn7, 7))
                _btn7.grid(row=3, column = 0, sticky="nsew")
            elif move == 8:
                _btn8 = tk.Button(self, text=computerletter, font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",fg = color,command=lambda:checker(_btn8, 8))
                _btn8.grid(row=3, column = 1, sticky="nsew")
            elif move == 9:
                _btn9 = tk.Button(self, text=computerletter, font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",fg = color,command=lambda:checker(_btn9, 9))
                _btn9.grid(row=3, column = 2, sticky="nsew")
                
        def fullBoard(board):
            x = ""
            for i in range(1, 10):
                if board[i] == "X" or board[i] == "O":
                    x = True
                else:
                    x = False
                    break
            return x
         
            

#----------------------------------play--------------------------------------------

        
        global theBoard, game
        global playerletter, computerletter
        global colorP1, colorP2
        global turn
        theBoard = [" "]*10
        turn = whoGoesFirst()
        playerletter, computerletter = character()
        if playerletter == "O":
                colorP1 = "blue"
                colorP2 = "red"
        else:
                colorP1 = "red"
                colorP2 = "blue"
        game = True



        
                
        def checker(buttons, moving):
                    
            global theBoard,game
            global playerletter,computerletter

            if game == True:
                        if buttons["text"] == " ":
                            makeMove(theBoard, playerletter, moving)
                            buttons["text"] = playerletter
                            if playerletter == "O":
                                buttons["fg"] = "blue"
                            else:
                                buttons["fg"] = "red"

                            if isWinner(theBoard, playerletter):
                                tkinter.messagebox.showinfo("Winner" + playerletter,"You have just won a game!!!"+turn)
                                game = False
                            else:
                                if fullBoard(theBoard):
                                    tkinter.messagebox.showinfo("Draw", "It's a tie!!!")
                                    game = False

                                                  
                            if game == True:                
                                move = getComputerMove(theBoard, computerletter)
                                makeMove(theBoard, computerletter, move)
                                drawComputerMove(move)
                                #draw the computer move to board !!!

                                if isWinner(theBoard, computerletter):
                                    tkinter.messagebox.showinfo("Winner" + computerletter, "You have just won a game!!!")
                                    game = False
                                else:
                                    if fullBoard(theBoard):
                                        tkinter.messagebox.showinfo("Draw", "It's a tie!!!")
                                        game = False

    
                                            
#----------------------------------label + buttons------------------------------------


        button1 = tk.Button(self, font=('Velvetica 12 bold'), text="Reset",height=2, width = 14,
                            fg="black", bg="white",command=Reset)
        button1.grid(row=1, column=0)

        button2 = tk.Button(self, font=('Velvetica 12 bold'),text="Main Menu",height=2, width = 14,
                            fg="black", bg="white",command=lambda: controller.show_frame(MainMenu))
        button2.grid(row=1, column=1)

        button3 = tk.Button(self, font=('Velvetica 12 bold'),text="Quit",height=2, width = 14,
                            fg="red", bg="white",command=qQuit)
        button3.grid(row=1, column=2)
                    
        label = tk.Label(self, text="Single Player", font=('Velvetica 15 bold'))
        label.grid(row=0, columnspan = 3)

      



        buttons = StringVar()
    
        lblInfo1 = tk.Label(self,font=('Times', 15, 'bold'),text="Player",fg=colorP1,
                             height=1, width = 7, anchor = "center")
        lblInfo1.grid(row = 2, column = 0)

        lblInfo2 = tk.Label(self,font=('Times', 15, 'bold'),text="Computer",fg=colorP2,
                             height=1, width = 7, anchor = "center")
        lblInfo2.grid(row = 2, column = 2)

        _btn7 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_btn7, 7))
        _btn7.grid(row=3, column = 0, sticky="nsew")

        _btn8 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_btn8, 8))
        _btn8.grid(row=3, column = 1, sticky="nsew")

        _btn9 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_btn9, 9))
        _btn9.grid(row=3, column = 2, sticky="nsew")

        _btn4 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_btn4, 4))
        _btn4.grid(row=4, column = 0, sticky="nsew")

        _btn5 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_btn5, 5))
        _btn5.grid(row=4, column = 1, sticky="nsew")

        _btn6 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_btn6, 6))
        _btn6.grid(row=4, column = 2, sticky="nsew")

        _btn1 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_btn1, 1))
        _btn1.grid(row=5, column = 0, sticky = "nsew")

        _btn2 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                          bg="white",command=lambda:checker(_btn2, 2))
        _btn2.grid(row=5, column = 1, sticky="nsew")

        _btn3 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_btn3, 3))
        _btn3.grid(row=5, column = 2, sticky="nsew")

        
        if turn == "computer":
            if game == True:                
                                move = getComputerMove(theBoard, computerletter)
                                makeMove(theBoard, computerletter, move)
                                drawComputerMove(move)
                                #draw the computer move to board !!!

                                if isWinner(theBoard, computerletter):
                                    tkinter.messagebox.showinfo("Winner" + computerletter, "You have just won a game!!!")
                                    game = False
                                else:
                                    if fullBoard(theBoard):
                                        tkinter.messagebox.showinfo("Draw", "It's a tie!!!")
                                        game = False
            turn = "player"


      

#=================================================PvP===============================================


class MultiPlayer(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="PLAYER vs PLAYER", font=('Velvetica 15 bold'))
        label.grid(row=0, columnspan=3)

        
        def Reset():
            global p1, colorP1
            global p2, colorP2
            global click
            _button1["text"] = " "
            _button2["text"] = " "
            _button3["text"] = " "
            _button4["text"] = " "
            _button5["text"] = " "
            _button5["text"] = " "
            _button6["text"] = " "
            _button7["text"] = " "
            _button8["text"] = " "
            _button9["text"] = " "
            p1 = 0
            p2 = 0

            click = True
            colorP1 = "red"
            colorP2 = "blue"
            result_ = str(p1) + "  :  " + str(p2)
            
            result = tk.Label(self,font=('Times', 15, 'bold'),text=result_, height=1, width = 7, anchor = "center")
            result.grid(row = 2, column = 1)
            lblInfo1 = tk.Label(self,font=('Times', 15, 'bold'),text="P1",fg=colorP1, height=1, width = 7, anchor = "e")
            lblInfo1.grid(row = 2, column = 0)
            lblInfo2 = tk.Label(self,font=('Times', 15, 'bold'),text="P2",fg=colorP2, height=1, width = 7, anchor = "w")
            lblInfo2.grid(row = 2, column = 2)


#--------------------------------------------buttons--------------------------------------------------------         

        button1 = tk.Button(self, font=('Velvetica 12 bold'), text="Reset",height=2, width = 14,
                            fg="black", bg="white",command=Reset)
        button1.grid(row=1, column=0)

        button2 = tk.Button(self, font=('Velvetica 12 bold'),text="Main Menu",height=2, width = 14,
                            fg="black", bg="white",command=lambda: controller.show_frame(MainMenu))
        button2.grid(row=1, column=1)

        button3 = tk.Button(self, font=('Velvetica 12 bold'),text="Quit",height=2, width = 14,
                            fg="red", bg="white",command=qQuit)
        button3.grid(row=1, column=2)

        result_ = "0  :  0"
        result = tk.Label(self,font=('Times', 14, 'bold'),text=result_, height=1, width = 7, anchor = "center")
        result.grid(row = 2, column = 1)

#------------------------------------------variables----------------------------------------------------
        global p1
        global p2
        global check
        global res
        global click
        global colorP1, colorP2

        result_ = ""
        p1 = 0
        p2 = 0
        check = 0
        res = ""
        click = True
        colorP1 = "red"
        colorP2 = "blue"


#---------------------------------------------checker------------------------------------------------

        def checker(buttons):
            global click
            global p1
            global p2
            global res
            global result_
            global colorP1, colorP2
                 
            
            if buttons["text"] == " " and click == True:
                buttons["text"] = "X"
                buttons["fg"] = "red"
                click = False
                if (_button1["text"] == "X" and _button2["text"] == "X" and _button3["text"] == "X" or
                _button4["text"] == "X" and _button5["text"] == "X" and _button6["text"] == "X" or
                _button7["text"] == "X" and _button8["text"] == "X" and _button9["text"] == "X" or
                _button1["text"] == "X" and _button5["text"] == "X" and _button9["text"] == "X" or
                _button3["text"] == "X" and _button5["text"] == "X" and _button7["text"] == "X" or
                _button1["text"] == "X" and _button4["text"] == "X" and _button7["text"] == "X" or
                _button2["text"] == "X" and _button5["text"] == "X" and _button8["text"] == "X" or
                _button3["text"] == "X" and _button6["text"] == "X" and _button9["text"] == "X"):
                    res = "X"
                    if res == "X":
                        tkinter.messagebox.showinfo("Winner X", "You have just won a game!!!")
                        _button1["text"] = " "
                        _button2["text"] = " "
                        _button3["text"] = " "
                        _button4["text"] = " "
                        _button5["text"] = " "
                        _button5["text"] = " "
                        _button6["text"] = " "
                        _button7["text"] = " "
                        _button8["text"] = " "
                        _button9["text"] = " "
                        if colorP1 == "red":
                            p1 += 1
                        else:
                            p2 += 1
                        colorP1 = "blue"
                        colorP2 = "red"
                    
                elif (_button1["text"] == "O" and _button2["text"] == "O" and _button3["text"] == "O" or
                _button4["text"] == "O" and _button5["text"] == "O" and _button6["text"] == "O" or
                _button7["text"] == "O" and _button8["text"] == "O" and _button9["text"] == "O" or
                _button1["text"] == "O" and _button5["text"] == "O" and _button9["text"] == "O" or
                _button3["text"] == "O" and _button5["text"] == "O" and _button7["text"] == "O" or
                _button1["text"] == "O" and _button4["text"] == "O" and _button7["text"] == "O" or
                _button2["text"] == "O" and _button5["text"] == "O" and _button8["text"] == "O" or
                _button3["text"] == "O" and _button6["text"] == "O" and _button9["text"] == "O"):
                    res = "O"
                    if res == "O":
                        tkinter.messagebox.showinfo("Winner O", "You have just won a game!!!")
                        _button1["text"] = " "
                        _button2["text"] = " "
                        _button3["text"] = " "
                        _button4["text"] = " "
                        _button5["text"] = " "
                        _button5["text"] = " "
                        _button6["text"] = " "
                        _button7["text"] = " "
                        _button8["text"] = " "
                        _button9["text"] = " "
                        if colorP1 == "red":
                            p2 += 1
                        else:
                            p1 += 1
                        colorP2 = "blue"
                        colorP1 = "red"
                elif (not(_button1["text"] == "O" and _button2["text"] == "O" and _button3["text"] == "O" or
                        _button4["text"] == "O" and _button5["text"] == "O" and _button6["text"] == "O" or
                        _button7["text"] == "O" and _button8["text"] == "O" and _button9["text"] == "O" or
                        _button1["text"] == "O" and _button5["text"] == "O" and _button9["text"] == "O" or
                        _button3["text"] == "O" and _button5["text"] == "O" and _button7["text"] == "O" or
                        _button1["text"] == "O" and _button4["text"] == "O" and _button7["text"] == "O" or
                        _button2["text"] == "O" and _button5["text"] == "O" and _button8["text"] == "O" or
                        _button3["text"] == "O" and _button6["text"] == "O" and _button9["text"] == "O")and not
                        (_button1["text"] == "X" and _button2["text"] == "X" and _button3["text"] == "X" or
                        _button4["text"] == "X" and _button5["text"] == "X" and _button6["text"] == "X" or
                        _button7["text"] == "X" and _button8["text"] == "X" and _button9["text"] == "X" or
                        _button1["text"] == "X" and _button5["text"] == "X" and _button9["text"] == "X" or
                        _button3["text"] == "X" and _button5["text"] == "X" and _button7["text"] == "X" or
                        _button1["text"] == "X" and _button4["text"] == "X" and _button7["text"] == "X" or
                        _button2["text"] == "X" and _button5["text"] == "X" and _button8["text"] == "X" or
                        _button3["text"] == "X" and _button6["text"] == "X" and _button9["text"] == "X")and
                        ((_button1["text"] == "X" or _button1["text"] == "O") and
                        (_button2["text"] == "X" or _button2["text"] == "O") and
                        (_button3["text"] == "X" or _button3["text"] == "O") and
                        (_button4["text"] == "X" or _button4["text"] == "O") and
                        (_button5["text"] == "X" or _button5["text"] == "O") and
                        (_button6["text"] == "X" or _button6["text"] == "O") and
                        (_button7["text"] == "X" or _button7["text"] == "O") and
                        (_button8["text"] == "X" or _button8["text"] == "O") and
                        (_button9["text"] == "X" or _button9["text"] == "O"))):
                            tkinter.messagebox.showinfo("Draw", "It's a tie!!!")
                            _button1["text"] = " "
                            _button2["text"] = " "
                            _button3["text"] = " "
                            _button4["text"] = " "
                            _button5["text"] = " "
                            _button5["text"] = " "
                            _button6["text"] = " "
                            _button7["text"] = " "
                            _button8["text"] = " "
                            _button9["text"] = " "
                            if colorP1 == "red":
                                colorP2 = "red"
                                colorP1 = "blue"
                            else:
                                colorP2 = "blue"
                                colorP1 = "red"

                    
            elif buttons["text"] == " " and click == False:
                buttons["text"] = "O"
                buttons["fg"] = "blue"
                click = True
                if (_button1["text"] == "X" and _button2["text"] == "X" and _button3["text"] == "X" or
                _button4["text"] == "X" and _button5["text"] == "X" and _button6["text"] == "X" or
                _button7["text"] == "X" and _button8["text"] == "X" and _button9["text"] == "X" or
                _button1["text"] == "X" and _button5["text"] == "X" and _button9["text"] == "X" or
                _button3["text"] == "X" and _button5["text"] == "X" and _button7["text"] == "X" or
                _button1["text"] == "X" and _button4["text"] == "X" and _button7["text"] == "X" or
                _button2["text"] == "X" and _button5["text"] == "X" and _button8["text"] == "X" or
                _button3["text"] == "X" and _button6["text"] == "X" and _button9["text"] == "X"):
                    res = "X"
                    if res == "X":
                        tkinter.messagebox.showinfo("Winner X", "You have just won a game!!!")
                        _button1["text"] = " "
                        _button2["text"] = " "
                        _button3["text"] = " "
                        _button4["text"] = " "
                        _button5["text"] = " "
                        _button5["text"] = " "
                        _button6["text"] = " "
                        _button7["text"] = " "
                        _button8["text"] = " "
                        _button9["text"] = " "
                        if colorP1 == "red":
                            p1 += 1
                        else:
                            p2 += 1
                        colorP1 = "blue"
                        colorP2 = "red"
                    
                elif (_button1["text"] == "O" and _button2["text"] == "O" and _button3["text"] == "O" or
                _button4["text"] == "O" and _button5["text"] == "O" and _button6["text"] == "O" or
                _button7["text"] == "O" and _button8["text"] == "O" and _button9["text"] == "O" or
                _button1["text"] == "O" and _button5["text"] == "O" and _button9["text"] == "O" or
                _button3["text"] == "O" and _button5["text"] == "O" and _button7["text"] == "O" or
                _button1["text"] == "O" and _button4["text"] == "O" and _button7["text"] == "O" or
                _button2["text"] == "O" and _button5["text"] == "O" and _button8["text"] == "O" or
                _button3["text"] == "O" and _button6["text"] == "O" and _button9["text"] == "O"):
                    res = "O"
                    if res == "O":
                        tkinter.messagebox.showinfo("Winner O", "You have just won a game!!!")
                        _button1["text"] = " "
                        _button2["text"] = " "
                        _button3["text"] = " "
                        _button4["text"] = " "
                        _button5["text"] = " "
                        _button5["text"] = " "
                        _button6["text"] = " "
                        _button7["text"] = " "
                        _button8["text"] = " "
                        _button9["text"] = " "
                        if colorP1 == "red":
                            p2 += 1
                        else:
                            p1 += 1
                        colorP2 = "blue"
                        colorP1 = "red"
                elif (not(_button1["text"] == "O" and _button2["text"] == "O" and _button3["text"] == "O" or
                        _button4["text"] == "O" and _button5["text"] == "O" and _button6["text"] == "O" or
                        _button7["text"] == "O" and _button8["text"] == "O" and _button9["text"] == "O" or
                        _button1["text"] == "O" and _button5["text"] == "O" and _button9["text"] == "O" or
                        _button3["text"] == "O" and _button5["text"] == "O" and _button7["text"] == "O" or
                        _button1["text"] == "O" and _button4["text"] == "O" and _button7["text"] == "O" or
                        _button2["text"] == "O" and _button5["text"] == "O" and _button8["text"] == "O" or
                        _button3["text"] == "O" and _button6["text"] == "O" and _button9["text"] == "O")and not
                        (_button1["text"] == "X" and _button2["text"] == "X" and _button3["text"] == "X" or
                        _button4["text"] == "X" and _button5["text"] == "X" and _button6["text"] == "X" or
                        _button7["text"] == "X" and _button8["text"] == "X" and _button9["text"] == "X" or
                        _button1["text"] == "X" and _button5["text"] == "X" and _button9["text"] == "X" or
                        _button3["text"] == "X" and _button5["text"] == "X" and _button7["text"] == "X" or
                        _button1["text"] == "X" and _button4["text"] == "X" and _button7["text"] == "X" or
                        _button2["text"] == "X" and _button5["text"] == "X" and _button8["text"] == "X" or
                        _button3["text"] == "X" and _button6["text"] == "X" and _button9["text"] == "X")and
                        ((_button1["text"] == "X" or _button1["text"] == "O") and
                        (_button2["text"] == "X" or _button2["text"] == "O") and
                        (_button3["text"] == "X" or _button3["text"] == "O") and
                        (_button4["text"] == "X" or _button4["text"] == "O") and
                        (_button5["text"] == "X" or _button5["text"] == "O") and
                        (_button6["text"] == "X" or _button6["text"] == "O") and
                        (_button7["text"] == "X" or _button7["text"] == "O") and
                        (_button8["text"] == "X" or _button8["text"] == "O") and
                        (_button9["text"] == "X" or _button9["text"] == "O"))):
                            tkinter.messagebox.showinfo("Draw", "It's a tie!!!")
                            _button1["text"] = " "
                            _button2["text"] = " "
                            _button3["text"] = " "
                            _button4["text"] = " "
                            _button5["text"] = " "
                            _button5["text"] = " "
                            _button6["text"] = " "
                            _button7["text"] = " "
                            _button8["text"] = " "
                            _button9["text"] = " "
                            if colorP1 == "red":
                                colorP2 = "red"
                                colorP1 = "blue"
                            else:
                                colorP2 = "blue"
                                colorP1 = "red"

                                
            result_ = str(p1) + "  :  " + str(p2)
            result = tk.Label(self,font=('Times', 15, 'bold'),text=result_, height=1, width = 7, anchor = "center")
            result.grid(row = 2, column = 1)

            lblInfo1 = tk.Label(self,font=('Times', 15, 'bold'),text="P1",fg=colorP1, height=1, width = 7, anchor = "e")
            lblInfo1.grid(row = 2, column = 0)
            lblInfo2 = tk.Label(self,font=('Times', 15, 'bold'),text="P2",fg=colorP2, height=1, width = 7, anchor = "w")
            lblInfo2.grid(row = 2, column = 2)


#--------------------------------------------gamefield-------------------------------------------------

        buttons = StringVar()
    
        lblInfo1 = tk.Label(self,font=('Times', 15, 'bold'),text="P1",fg=colorP1, height=1, width = 7, anchor = "e")
        lblInfo1.grid(row = 2, column = 0)

        lblInfo2 = tk.Label(self,font=('Times', 15, 'bold'),text="P2",fg=colorP2, height=1, width = 7, anchor = "w")
        lblInfo2.grid(row = 2, column = 2)

        _button1 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_button1))
        _button1.grid(row=3, column = 0, sticky="nsew")

        _button2 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_button2))
        _button2.grid(row=3, column = 1, sticky="nsew")

        _button3 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_button3))
        _button3.grid(row=3, column = 2, sticky="nsew")

        _button4 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_button4))
        _button4.grid(row=4, column = 0, sticky="nsew")

        _button5 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_button5))
        _button5.grid(row=4, column = 1, sticky="nsew")

        _button6 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_button6))
        _button6.grid(row=4, column = 2, sticky="nsew")

        _button7 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_button7))
        _button7.grid(row=5, column = 0, sticky = "nsew")

        _button8 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                          bg="white",command=lambda:checker(_button8))
        _button8.grid(row=5, column = 1, sticky="nsew")

        _button9 = tk.Button(self, text=" ", font=('Times 25 bold'), height = 3, width = 8,
                         bg="white",command=lambda:checker(_button9))
        _button9.grid(row=5, column = 2, sticky="nsew")

#=====================================MultiPlayer=========================================

class Online(tk.Frame):

    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="ONLINE-multiplayer", font=('Velvetica 15 bold'), width = 20)
        label.grid(row = 1, column = 1)


        label2 = tk.Label(self, text = "\nComing soon...",font=('Velvetica 12 italic'), width = 15)
        label2.grid(row = 2, column = 0)

        label3 = tk.Label(self, text = "\n\n\n",font=('Velvetica 12 italic'), width = 15)
        label3.grid(row = 3, columnspan = 3)

        button = tk.Button(self, text="Main Menu",font=('Times 12 bold'), fg="white", bg="black",activeforeground = "white",
                           activebackground = "black", command=lambda: controller.show_frame(MainMenu))
        button.grid(row=5, column = 2)
        
   



      
#==================================How to play=============================================

class HowToPlay(tk.Frame):

    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)


        #label = tk.Label(self, text = "", width = 1)
        #label.grid(row = 0, column = 0)
        label1 = tk.Label(self, text="\nWhat is Tic-tac-toe?", font=('Velvetica 15 bold'))
        label1.grid(row=0, column = 1)
        label2 = tk.Label(self, text=" How to play?", font=('Velvetica 15 bold'))
        label2.grid(row=2, column = 1)
        
        about1 = ("""Tic-tac-toe (also known as noughts and crosses or Xs and Os) is
 a paper-and-pencil game for two players, who take turns marking the spaces in a 3×3
grid. One player is X and the other player is O.\n""" )
        about2 =  ("""If a player gets three of their marks on the board in a row, column or one of the two
diagonals, they win. When the board fills up with neither player winning,
the game ends in a draw.\n\n\n\n""")
        
        button = tk.Button(self, text="Main Menu",font=('Times 12 bold'), fg="white", bg="black",activeforeground = "white",
                           activebackground = "black", command=lambda: controller.show_frame(MainMenu))
        button.grid(row=5, column = 1)

        lbl1 = tk.Label(self,text=about1, font=('Velvetica 10 italic'), anchor = "center")
        lbl1.grid(row = 1, column = 1)
        lbl2 = tk.Label(self,text=about2, font=('Velvetica 10 italic'),anchor = "center")
        lbl2.grid(row = 3, column = 1)
       
            
app = SeaofBTCapp()

app.resizable(False, False)

window_width=510   #534  
window_height=538    #575 690

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

x_coordinate = ((screen_width/2)-(window_width/2))
y_coordinate = ((screen_height/2)-(window_height/2))

app.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
app.title("Tic-tac-toe")
app.iconbitmap("ttt.ico")

app.mainloop()
        


