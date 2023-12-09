from tkinter import*
class HomePage:

	def create_window(self):

		# Create a gui window
		window = Tk()

		#Set the background color
		window.configure(background = 'light blue')

		#Set the window size
		window.geometry("500x500")

		#Give the application a title
		window.title("Grade Book")

		#Creates a text label
		label1 = Label(window, text="Welcome to Gradebook", background='light blue', fg='black', font=("Ariel", 30))

		label2 = Label(window, text="Select what you are looking for", background='light blue', fg='black', font=("Ariel", 20))

		#Create an entry box for filling in or typing infomation

		basic_button = Button(window, text="Basic", bg="blue", activebackground='white')

		weighted_button = Button(window, text="Weighted", bg="blue", activebackground='white')

		gpa_button = Button(window, text="GPA", bg="blue", activebackground='white')

		notes_button = Button(window, text="Notes", bg="blue", activebackground='white')

		#Grid method used for placing the widgets at respective positions in table like structure
		label1.place(relx=0.5, rely=0.1, anchor=CENTER)
		label2.place(relx=0.5, rely=0.2, anchor=CENTER)  
		basic_button.place(relx=0.5, rely=0.4, anchor=CENTER)
		weighted_button.place(relx=0.5, rely=0.5, anchor=CENTER)
		gpa_button.place(relx=0.5, rely=0.6, anchor=CENTER)
		notes_button.place(relx=0.5, rely=0.7, anchor=CENTER)






		#Start the GUI
		window.mainloop()
