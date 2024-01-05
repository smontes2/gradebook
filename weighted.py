from tkinter import*
import json

def get_vars():
	with open('weighted.json', 'r') as file:
		data = json.load(file)
		for i in data["Grade"]:
			grade_box.insert(END, i)
		for i in data["Weight"]:
			weight_box.insert(END, i)

def add():

	grade = grade_entry.get()
	weight = weight_entry.get()

	with open('weighted.json', 'r') as file:
		data = json.load(file)

	grade_list = data["Grade"]
	grade_list.append(float(grade))

	weight_list = data["Weight"]
	weight_list.append(float(weight))

	with open('weighted.json', 'w') as file:
		json.dump(data, file)

	grade_box.insert(END, grade)
	weight_box.insert(END, weight)

	grade_entry.delete(0, END)
	weight_entry.delete(0,END)

def delete():
	
	selected_grade = grade_box.curselection()
	selected_weight = weight_box.curselection()

	with open('weighted.json', 'r') as file:
		data = json.load(file)

	
	'Not sure what this does if I am being honest, will look into'

	if "Grade" in data and isinstance(data["Grade"], list):
		new_grades = []
		for i, grade in enumerate(data["Grade"]):
			if i not in selected_grade:
				new_grades.append(grade)
			data["Grade"] = new_grades

	if "Weight" in data and isinstance(data["Weight"], list):
		new_weight = []
		for i, weight in enumerate(data["Weight"]):
			if i not in selected_weight:
				new_weight.append(weight)
			data["Weight"] = new_weight


	with open('weighted.json', 'w') as file:
		json.dump(data, file)

	grade_box.delete(0, END)
	weight_box.delete(0, END)
	grade_box.insert(END, data["Grade"])
	weight_box.insert(END, data["Weight"])

def delete_all():

	# with open('weighted.json', 'r') as file:
	# 	data = json.load(file)

	# if 'your_key' in data and isinstance(data['your_key'], list):
	# 	if variable_to_delete in data['your_key']:
	# 		data['your_key'].remove(variable_to_delete)

	# with open('weighted.json', 'w') as file:
	# 	file.write(test)

	# grade_box.delete(0, END)
	pass

def get_grades_and_weights():
	try:
		with open('weighted.json', 'r') as file:
			data = json.load(file)
			grade_calculation(data)
	except FileNotFoundError:
		print("error")

def grade_calculation(data):

	if len(data) == 0:
		return
	
	with open('weighted.json', 'r') as file:
		data = json.load(file)

	grade_and_weight_values = []

	for i, num in enumerate(data["Grade"]):
		grade_and_weight_values.append(data["Grade"][i] * data["Weight"][i]/100)

	totalGrade = sum(grade_and_weight_values)

	label1.config(text=f"Calculated Grade: {totalGrade}")
		


window = Tk()

window.config(background='light blue')

window.geometry("700x500")

window.title("Grade Book: Weighted")

label1 = Label(window, text="Calculated grade: 0")

grade_entry = Entry(window)

weight_entry = Entry(window)

grade_box = Listbox(window)

weight_box = Listbox(window)

entry_button = Button(window, text="Calculate", command=get_grades_and_weights)

delete_button = Button(window, text="Delete", command=delete)

add_button = Button(window, text="Add", command=add)

clear_all_button = Button(window, text="Clear all", command=delete_all)

label1.grid(row = 1, column = 0, padx = 10, pady = 10)  

grade_entry.grid(row = 1, column = 1, padx = 10, pady = 10) 

weight_entry.grid(row = 1, column = 2, padx = 10, pady = 10)  

grade_box.grid(row = 2, column = 1, padx = 10, pady = 10)  

weight_box.grid(row = 2, column = 2, padx = 10, pady = 10)  

entry_button.grid(row = 2, column = 3, padx = 10, pady = 10)

delete_button.grid(row = 2, column= 0, padx = 10)

add_button.grid(row = 1, column = 3, padx = 10, pady = 10)

clear_all_button.grid(row = 3, column = 0, padx = 10)

get_vars()

window.mainloop()




