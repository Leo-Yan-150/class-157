from tkinter import *
from PIL import ImageTk, Image
import random
root=Tk()
root.title("The crazzzzzy image thiny")
root.geometry("600x400")

root.configure(background="yellow2")

imgg=ImageTk.PhotoImage(Image.open ("thatfriggindice.jpg"))

player1 = Label(root, text="Player 1", bg = "royal blue", fg = "white")
player1.place(relx = 0.1, rely=0.3, anchor = CENTER)

player2 = Label(root, text="Player 2", bg = "royal blue", fg = "white")
player2.place(relx = 0.9, rely=0.3, anchor = CENTER)

player1_score = Label(root, bg = "royal blue", fg = "white")
player1_score.place(relx = 0.1, rely=0.4, anchor = CENTER)

player2_score = Label(root, bg = "royal blue", fg = "white")
player2_score.place(relx = 0.9, rely=0.4, anchor = CENTER)

rdl = Label(root,bg="chocolate1", fg = "white")
rdl.place(relx=0.5,rely=0.5,anchor=CENTER)

player1_scorey = 0
def p1():
   global player1_scorey
   randomn=random.randint(1,6)
   player1_scorey = player1_scorey + randomn
   rdl['text']= "Player 1 dice number: " + str(randomn)
   player1_score['text'] = str(player1_scorey)
   
p1btn = Button(root, image = imgg, command=p1)
p1btn.place(relx=0.1, rely=0.6, anchor=CENTER)

player2_scorey = 0
def p2():
   global player2_scorey
   randomn2=random.randint(1,6)
   player2_scorey = player2_scorey + randomn2
   rdl["text"]= "Player 2 dice number: " + str(randomn2)
   player2_score["text"] = str(player2_scorey)
   
p2btn = Button(root, image = imgg, command=p2)
p2btn.place(relx=0.9, rely=0.6, anchor=CENTER)

root.mainloop()

#this code is totoally not scuffed and totally not copied off of byju's future school