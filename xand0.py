from Tkinter import *
root = Tk()
one = None
two = None
three = None
four = None
five = None
six = None
seven = None
eight = None
nine = None
score_X = 0
score_O = 0
result = Label(root, text = "")
score = Label(root, text = " ")

def process_O_1(event):
	global one
	one = "O"
	number_1["text"] = "O"
def process_O_2(event):
	global two
	two = "O"
	number_2["text"] = "O"
def process_O_3(event):
	global three
	three = "O"
	number_3["text"] = "O"
def process_O_4(event):
	global four
	four = "O"
	number_4["text"] = "O"
def process_O_5(event):
	global five
	five = "O"
	number_5["text"] = "O"
def process_O_6(event):
	global six
	six = "O"
	number_6["text"] = "O"
def process_O_7(event):
	global seven
	seven = "O"
	number_7["text"] = "O"
def process_O_8(event):
	global eight
	eight = "O"
	number_8["text"] = "O"
def process_O_9(event):
	global nine
	nine = "O"
	number_9["text"] = "O"

def process_X_1(event):
	global one
	one = "X"
	number_1["text"] = "X"
def process_X_2(event):
	global two
	two = "X"
	number_2["text"] = "X"
def process_X_3(event):
	global three
	three = "X"
	number_3["text"] = "X"
def process_X_4(event):
	global four
	four = "X"
	number_4["text"] = "X"
def process_X_5(event):
	global five
	five = "X"
	number_5["text"] = "X"
def process_X_6(event):
	global six
	six = "X"
	number_6["text"] = "X"
def process_X_7(event):
	global seven
	seven = "X"
	number_7["text"] = "X"
def process_X_8(event):
	global eight
	eight = "X"
	number_8["text"] = "X"
def process_X_9(event):
	global nine
	nine = "X"
	number_9["text"] = "X"

def check(event):
	global one, two, three, four, five, six, seven, eight, nine, score_X, score_O
	if one == "X" and two == "X" and three == "X":
		result["text"] = "X win"
		score_X += 1
		result.grid(row = 3, column = 2)
	elif four == "X" and five == "X" and six == "X":
		result["text"] = "X win"
		result.grid(row = 3, column = 2)
		score_X += 1
	elif seven == "X" and eight == "X" and nine == "X":
		result["text"] = "X win"
		result.grid(row = 3, column = 2)
		score_X += 1
	elif one == "X" and four == "X" and seven == "X":
		result["text"] = "X win"
		result.grid(row = 3, column = 2)
		score_X += 1
	elif two == "X" and five == "X" and eight == "X":
		result["text"] = "X win"
		result.grid(row = 3, column = 2)
		score_X += 1
	elif three == "X" and six == "X" and nine == "X":
		result["text"] = "X win"
		result.grid(row = 3, column = 2)
		score_X += 1
	elif one == "X" and five == "X" and nine == "X":
		result["text"] = "X win"
		result.grid(row = 3, column = 2)
		score_X += 1
	elif three == "X" and five == "X" and seven == "X":
		result["text"] = "X win"
		result.grid(row = 3, column = 2)
		score_X += 1
	elif one == "O" and two == "O" and three == "O":
		result["text"] = "O win"
		result.grid(row = 3, column = 2)
		score_O += 1
	elif four == "O" and five == "O" and six == "O":
		result["text"] = "O win"
		result.grid(row = 3, column = 2)
		score_O += 1
	elif seven == "O" and eight == "O" and nine == "O":
		result["text"] = "O win"
		result.grid(row = 3, column = 2)
		score_O += 1
	elif one == "O" and four == "O" and seven == "O":
		result["text"] = "O win"
		result.grid(row = 3, column = 2)
		score_O += 1
	elif two == "O" and five == "O" and eight == "O":
		result["text"] = "O win"
		result.grid(row = 3, column = 2)
		score_O += 1
	elif three == "O" and six == "O" and nine == "O":
		result["text"] = "O win"
		result.grid(row = 3, column = 2)
		score_O += 1
	elif one == "O" and five == "O" and nine == "O":
		result["text"] = "O win"
		result.grid(row = 3, column = 2)
		score_O += 1
	elif three == "O" and five == "O" and seven == "O":
		result["text"] = "O win"
		result.grid(row = 3, column = 2)
		score_O += 1
	score["text"] = score_X, " : ", score_O
	score.grid(row = 4, column = 2)


def clear(event):
	global number_1, number_2, number_3, number_4, number_5, number_6, number_7, number_8, number_9, one, two, three, four, five, six, seven, eight, nine, result 
	
	one = " "
	two = " "
	three = " "
	four = " "
	five = " "
	six = " "
	seven = " "
	eight = " "
	nine = " "
	
	number_1['text'] = " "
	number_2['text'] = " "
	number_3['text'] = " "
	number_4['text'] = " "
	number_5['text'] = " "
	number_6['text'] = " "
	number_7['text'] = " "
	number_8['text'] = " "
	number_9['text'] = " "
	result["text"] = " "
	
number_1 = Button(root, text = " ")
number_2 = Button(root, text = " ")
number_3 = Button(root, text = " ")
number_4 = Button(root, text = " ")
number_5 = Button(root, text = " ")
number_6 = Button(root, text = " ")
number_7 = Button(root, text = " ")
number_8 = Button(root, text = " ")
number_9 = Button(root, text = " ")
check_button = Button(root, text ="Check")
clear_button = Button(root, text = "Clear")
restart_button = Button(root, text = "restart")

number_1.grid(row = 0, column = 0) 
number_2.grid(row = 0, column = 1)
number_3.grid(row = 0, column = 2)
number_4.grid(row = 1, column = 0)
number_5.grid(row = 1, column = 1)
number_6.grid(row = 1, column = 2)
number_7.grid(row = 2, column = 0)
number_8.grid(row = 2, column = 1)
number_9.grid(row = 2, column = 2)
check_button.grid(row = 0, column = 3)
clear_button.grid(row = 1, column = 3)
restart_button.grid(row = 2, column = 3) 

number_1.bind("<Button-3>", process_O_1)
number_2.bind("<Button-3>", process_O_2)
number_3.bind("<Button-3>", process_O_3)
number_4.bind("<Button-3>", process_O_4)
number_5.bind("<Button-3>", process_O_5)
number_6.bind("<Button-3>", process_O_6)
number_7.bind("<Button-3>", process_O_7)
number_8.bind("<Button-3>", process_O_8)
number_9.bind("<Button-3>", process_O_9)

number_1.bind("<Button-1>", process_X_1)
number_2.bind("<Button-1>", process_X_2)
number_3.bind("<Button-1>", process_X_3)
number_4.bind("<Button-1>", process_X_4)
number_5.bind("<Button-1>", process_X_5)
number_6.bind("<Button-1>", process_X_6)
number_7.bind("<Button-1>", process_X_7)
number_8.bind("<Button-1>", process_X_8)
number_9.bind("<Button-1>", process_X_9)

check_button.bind("<Button-1>", check)
clear_button.bind("<Button-1>", clear)

root.mainloop()