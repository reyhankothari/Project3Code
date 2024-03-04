
#Importing libraries needed for the project
from tkinter import * #GUI library
from PIL import Image,ImageTk #ImageLibraries
import sqlite3 as lite #Database Library
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

#Creating parent window
root = Tk()

#Connected to the database containing the questions and answer sets
connectedDatabase = lite.connect("QuestionAndAnswers.db")
current = connectedDatabase.cursor()



UsedQuestions = []

#Configuring how many rows and columns to display on the parent window


#Restricting the sizes the user can minimisize down to
root.minsize(width="825", height=547)

root.attributes('-fullscreen', True) #Maybe create a full screen button

root.title("GCSE Computer Science Revision")

#Database Things
# connectedDatabase = lite.connect("QuestionAndAnswers.db")
# current = connectedDatabase.cursor()


#Configuring the rows and columns for my grid system





Font_tuple = ("OstrichSans-Black", 55) 


	




i = 0




def AnyTopic(topic = "Any"):
		global UsedQuestions
		global i

		
		for widget in root.winfo_children():
			# if str(widget) == ".!label" or str(widget) == ".!label2":
			# 	continue
			widget.destroy()

		
		while True:

			with connectedDatabase:
				if topic == "Any":
					current.execute("SELECT count(*) FROM Questions")
					match = current.fetchall()
					Count = match[0][0]
					current.execute(f"SELECT QuestionPath, AnswerPath, Topic FROM Questions ORDER BY RANDOM() LIMIT 1")
				else:
					current.execute(f"SELECT COUNT(CASE WHEN Topic = '{str(topic)}' THEN Topic END) FROM Questions")
					match = current.fetchall()

					Count = match[0][0]
					current.execute(f"SELECT QuestionPath, AnswerPath, Topic FROM Questions WHERE Topic = '{str(topic)}' ORDER BY RANDOM() LIMIT 1")
				match = current.fetchall()
			Question = match[0][0]	
			AnswerPath = match[0][1]
			TopicName = match [0][2]

			if ((Question) not in UsedQuestions):

				break
			else:
				if i > Count:
					UsedQuestions.clear()
					i = 0
					break


			i += 1


		UsedQuestions.append(Question)
		Question = Question.replace("?","/")
		AnswerPath = AnswerPath.replace("?","/")
		my_img = Image.open(str(Question))


		my_img = ImageTk.PhotoImage(my_img)

		# Displaying the topic name of the questio
		label1 = Label(root,text = "Topic:\n" + TopicName,font=("OstrichSans-Black", 20))
		label1.place(relx = 0.1, rely = 0.1,anchor = "center")



		#Displaying image on tkinter windows
		label2 = Label(root,image = my_img,bg = "#1A4121")
		label2.place(relx = 0.5, rely = 0.3,anchor = "center")
		label2.image = my_img	

		#Displaying an entry box with an dark green outline using the frame element
		frame = Frame(root,width = (my_img.width()) + 10, height = 210, bg = "#1A4121")
		frame.place(relx = 0.5, rely = 0.5795,anchor = "n")

		entry = Text(frame, font = ("OstrichSans-Black", 15))
		entry.place(relx = 0.5, rely = 0.5,anchor = "center",width = my_img.width(), height = 200,)

		#Displayi
		Back = Button(root,text = "Back",	font = ("OstrichSans-Black", 20),command = Start, relief= "groove")
		Back.place(relx = 0.3, rely = 0.98,anchor = "s",)

		MarkScheme1 = Button(root,text = "Mark Scheme", command=lambda:[MarkScheme(AnswerPath)]	,font = ("OstrichSans-Black", 20), relief= "groove")
		MarkScheme1.place(relx = 0.7, rely = 0.98,anchor = "s",)

		Repeat = Button(root,text = "Generate New Question", command= lambda:[AnyTopic(topic)] ,font = ("OstrichSans-Black", 20), relief= "groove")
		Repeat.place(relx = 0.5, rely = 0.98,anchor = "s",)

def SpecificTopic():
		for widget in root.winfo_children():
			widget.destroy()	

		Grid.rowconfigure(root, 3,weight = 1)
		Grid.columnconfigure(root, 0,weight = 4	)
		frame1 = Label(root,font = Font_tuple,text = "SELECT TOPIC" ,fg = "white",bg = "#1A4121",padx = 50,)
		frame1.grid(column = 0, row = 0,rowspan = 4,sticky = "nsew")
		label = Label(frame1,image = my_img,bg = "#1A4121")
		label.image = my_img
		label.place(relx = 0.55, rely = 0.25,anchor = "s")

		Topic1 = Button(root,font = ("OstrichSans-Black", 30),text = "Algorithms", command = lambda: [AnyTopic("Algorithm")]  )
		Topic1.grid(column = 1, row = 0,sticky="nsew")
		
		Topic2 = Button(root,font = ("OstrichSans-Black", 30),text = "Programming", command = lambda: [AnyTopic("Programming")])
		Topic2.grid(column = 2, row = 0,sticky = "nsew")
		
		Topic3 = Button(root,font = ("OstrichSans-Black", 30),text = "Computer Hardware",command = lambda: [AnyTopic("Hardware")])
		Topic3.grid(column = 1, row = 1,sticky="nsew")
		
		Topic4 = Button(root,font = ("OstrichSans-Black", 30),text = "Data\nRepresentation",command = lambda: [AnyTopic("Data Representation")])
		Topic4.grid(column = 2, row = 1,sticky = "nsew")
		
		Topic5 = Button(root,font = ("OstrichSans-Black", 30),text = "Network",command = lambda: [AnyTopic("Network")])
		#Topic6 = Button(root,font = Font_tuple,text = "Algorithms")
		Topic5.grid(column = 1, row = 2,sticky="nsew")
		
		Topic6 = Button(root,font = ("OstrichSans-Black", 30),text = "Ethics",command = lambda: [AnyTopic("Ethics")])
		Topic6.grid(column = 2, row = 2,sticky = "nsew")
		
		Topic7 = Button(root,font = ("OstrichSans-Black", 30),text = "Cyber Security",command = lambda: [AnyTopic("Cyber Security")])
		Topic7.grid(column = 1, row = 3,sticky = "nsew")

		Topic8 = Button(root,font = ("OstrichSans-Black", 30),text = "Back",command = Start)
		Topic8.grid(column = 2, row = 3,sticky="nsew")
		

def MarkScheme(AnswerPath):
		Popup = Toplevel(root) 
		my_img = Image.open(str(AnswerPath))
		my_img = ImageTk.PhotoImage(my_img)
		Label1 = Label(Popup,image=my_img)
		Label1.image = my_img
		Label1.pack(fill="both",expand=True)




def Start():
	for widget in root.winfo_children():
		widget.destroy()

	def Quit():
		for widget in root.winfo_children():
			widget.destroy()

		var = IntVar()
		


		Label1 = Label(root, text = "Exiting program\n Hope you had a productive time", font = Font_tuple).place(relx = 0.5, rely = 0.5, anchor = "center")

		root.after(2500, var.set, 1)
		root.wait_variable(var)

		quit()
	
	global my_img

	Grid.rowconfigure(root, 0 , weight = 1)
	Grid.rowconfigure(root, 1 , weight = 1)
	Grid.rowconfigure(root, 2, weight = 1)
	Grid.rowconfigure(root, 3 , weight = 0)

	Grid.columnconfigure(root, 0 , weight = 1)
	Grid.columnconfigure(root, 1 , weight = 1)
	Grid.columnconfigure(root, 2 , weight = 1) 



	frame = Label(root,font = Font_tuple,text = "GCSE Computer\n Science Revision" ,fg = "white",bg = "#1A4121",padx = 50,)
	frame.grid(column = 0, row = 0,rowspan = 4,sticky = "nsew")	
	my_img = Image.open(str("logo.png"))
	width_new = int(362*1.3)
	height_new = int(86*1.3)

	my_img = my_img.resize((width_new,height_new), Image.LANCZOS)
	my_img = ImageTk.PhotoImage(my_img)
	#my_img = ImageTk.PhotoImage((Image.open(str("logo.png"))).resize((539*1.5,137*1.5), Image.ANTIALIAS))

	label = Label(frame,image = my_img,bg = "#1A4121")
	label.image = my_img
	label.place(relx = 0.55, rely = 0.25,anchor = "s")

	Font_tuple1 = ("OstrichSans-Black", 25) 

	Option1 = Button(root, font = Font_tuple1,text = "Random Question From Any Topic", relief=RAISED,command = AnyTopic)
	Option1.grid(row = 0, columnspan = 3, column = 1,sticky = "nsew")

	Option2 = Button(root, font = Font_tuple1,text = "Random Question From One Topic of Your Choice",command = SpecificTopic)
	Option2.grid(row = 1, columnspan = 3, column = 1,sticky = "nsew")

	Option3 = Button(root, font=Font_tuple1, text = "Admin Panel", command=AdminPanel)
	Option3.grid(row = 2, columnspan= 3, column = 1 ,sticky = "nsew")

	Option4 = Button(root, font=Font_tuple1, text = "Quit", command = Quit)
	Option4.grid(row = 3, columnspan= 3, column = 1 ,sticky = "nsew")

def AdminPanel():
	for widget in root.winfo_children():
		widget.destroy()
	def Submit():
		Question = QuestionPath.get()
		Answer = AnswerPath.get()
		Topic = clicked.get()
		Option = []

		FieldsMissing = "These follwing fields are missing:"
		Missing = False

		if clicked.get() == "Select Topic":
			Option.append(0)
		else:
			Option.append(1)
		
		if QuestionPath.get() == "None":
			Option.append(0)
		else:
			Option.append(1)

		if AnswerPath.get() == "None":
			Option.append(0)
		else:
			Option.append(1)



		for index, option in enumerate(Option):
			if index == 0 and option == 0:
				FieldsMissing = FieldsMissing + "\nTopic"
			elif index == 1 and option == 0:
				FieldsMissing = FieldsMissing + "\nQuestion Image"
			elif index == 2 and option == 0:
				FieldsMissing = FieldsMissing + "\nMark Scheme Image"

			if option == 0:
				Missing = True

		if Missing == True:
			messagebox.showerror("Missing fields", FieldsMissing)
			return

		with connectedDatabase:
			current.execute(f"INSERT INTO Questions VALUES('{str(Topic)}','{Question}','{Answer}')")
		connectedDatabase.commit()
		Start()
        
	def test1(Path):
		img = askopenfilename(title="Open Image File", filetypes=[(".png .jpg .jpeg .gif .bmp .ico", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
		if img == "":
			return
		my_img = Image.open(str(img))
		width,height = my_img.size

		print(width,height)

		width_new = int(400)
		height_new = int(150)

		my_img = my_img.resize((width_new,height_new), Image.LANCZOS)
		my_img = ImageTk.PhotoImage(my_img)
		
		if Path == "Question":
			if width > 800 or height > 430:
				messagebox.showerror("Error uploading image", "The picture is too big.\nMax size of question image is 800x430 pixels")
				return
			QuestionPath.set(img)
			print("Question",QuestionPath.get())
			imghlder1.config(image=my_img)
			imghlder1.image = my_img
		else:
			if width > 900 or height > 700:
				messagebox.showerror("Error uploading image", "The picture is too big.\nMax size of mark scheme image is 900x700 pixels")
				return
			AnswerPath.set(img)
			print("Answer:",AnswerPath.get())
			imghlder2.config(image=my_img)
			imghlder2.image = my_img
	
	

	TopicList = ["Algorithm","Cyber Security", "Data Representation", "Ethics", "Hardware", "Networks", "Programming"]
	clicked = StringVar() 
	QuestionPath = StringVar(value = "None")
	AnswerPath = StringVar(value="None")
	Hi = QuestionPath.get()
	print(Hi)
# initial menu text 
	clicked.set( "Select Topic" ) 


	frame = Label(root,font = Font_tuple,text = "Admin\nPanel" ,fg = "white",bg = "#1A4121",padx = 50,)
	frame.grid(column = 0, row = 0,rowspan = 4,sticky = "nsew")	
	my_img = Image.open(str("logo.png"))
	width_new = int(362*1.3)
	height_new = int(86*1.3)

	my_img = my_img.resize((width_new,height_new), Image.LANCZOS)
	my_img = ImageTk.PhotoImage(my_img)


	label = Label(frame,image = my_img,bg = "#1A4121")
	label.image = my_img
	label.place(relx = 0.55, rely = 0.25,anchor = "s")

	Font_tuple1 = ("OstrichSans-Black", 25) 

	Option1 = Frame(root)

	Label(Option1, text="TOPIC", font=("OstrichSans-Black", 27) ).place(relx = 0.27,rely=0.5, anchor = "e")
	drop = OptionMenu(Option1 , clicked , *TopicList )
	drop.config(font=("OstrichSans-Black", 27))
	menu = root.nametowidget(drop.menuname)
	menu.config(font = ("OstrichSans-Black", 23))
	drop.place(relx = 0.5, rely= 0.5,anchor="w")

	Option1.grid(row = 0, columnspan = 3, column = 1,sticky = "nsew")

	Option2 = Frame(root)
	Button(Option2, text="Click Here To\nUpload Question\nImage", font=("OstrichSans-Black", 27),command=lambda:test1("Question") ).place(relx = 0.37,rely=0.5, anchor = "e")
	imghlder1 = Label(Option2, text = " ")
	imghlder1.place(relx = 0.4, rely= 0.5,anchor="w")
	Option2.grid(row = 1, columnspan = 3, column = 1,sticky = "nsew")
	
	Option3 = Frame(root)
	Button(Option3, text="Click Here To\nUpload Mark Scheme\nImage", font=("OstrichSans-Black", 27),command=lambda:test1("Answer") ).place(relx = 0.4,rely=0.5, anchor = "e")
	imghlder2 = Label(Option3, text = " ")
	imghlder2.place(relx = 0.4	, rely= 0.5,anchor="w")
	Option3.grid(row = 2, columnspan = 3, column = 1,sticky = "nsew")

	Option4 = Button(root, font=Font_tuple1, text = "Submit", command = Submit)

	Topic8 = Button(frame,font = ("OstrichSans-Black", 30),text = "Back",bg= "#1A4121",command = Start ,relief="raised")
	Topic8.place(relx = 0.5, rely = 0.9, anchor="center")
	

Start()
root.mainloop()
