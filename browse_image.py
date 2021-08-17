def myBrowse():
	frame = Frame(root, bd=2, relief=SUNKEN)
	frame.grid_rowconfigure(0, weight=1)
	frame.grid_columnconfigure(0, weight=1)
	
	canvas = Canvas(frame, bd=0, height=500, width=400)
	canvas.grid(row=0, column=0, sticky=N+S+E+W)
	
	frame.grid(row=1, column=0)
	filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =(("jpeg files","*.jpg"),("all files","*.*")))
	print(filename)
	label = Label(root, text = "")

	# label.configure(text = filename)

	img = Image.open(filename)
	img_not_resize = img
	img = img.resize((500, 400), Image.ANTIALIAS)
	im_show = img
	photo = ImageTk.PhotoImage(img)
	
	label2 = Label(image=photo)
	label2.image = photo 
	#label2.grid(column=0, row=2)
	canvas.create_image(0,0,image=photo,anchor="nw")
	canvas.config(scrollregion=canvas.bbox(ALL))
	def printcoords(event):
		global x,y,label6
		#outputting x and y coords to console
		x = event.x
		y = event.y
		# tt = canvas.create_text(30, 480, anchor=E, font="Purisa",
			# text=str(x)+","+str(y))
		label6 = Label(root,text = "           ")
		label6.image = "       "
		label6.grid(column=0, row=10)
		label6.destroy()
		label6 = Label(root,text = str(x)+","+str(y))
		label6.image = str(x)+str(y)
		label6.grid(column=0, row=10)
	#mouseclick event
	canvas.bind("<Button>",printcoords)
	
