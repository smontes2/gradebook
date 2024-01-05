from tkinter import*
import json

'This function opens the json file and reads the data and feeds that data to the update_list and calculate_grade functions'
def get_grades():
    try:
        with open('test.json', 'r') as file:
            data = json.load(file)
            update_listbox(data)
            calculate_grade(data)
    except FileNotFoundError:
        print("error")

def add_grades():
    grade_input = float(grades.get())

    with open('test.json', 'r') as file:
        data = json.load(file)
    
    data.append(grade_input)

    with open('test.json', 'w') as file:
        json.dump(data, file)

    new_input = [grade_input]

    update_listbox(new_input)

    grades.delete(0,END)

def delete_grades():
    selected_grade = list_box.curselection()

    if selected_grade:
        selected_grade = selected_grade[0]

        with open('test.json', 'r') as file:
            data = json.load(file)

        deleted_grade = data.pop(selected_grade)

        with open('test.json', 'w') as file:
            json.dump(data, file)

        list_box.delete(0, END)
        update_listbox(data)

def calculate_grade(data):
    list_size = len(data)
    sum_grades = sum(data)

    if list_size == 0:
        return
    
    calculated_grade = round((sum_grades/list_size), 2)
    label1.config(text=f"Calculated Grade: {calculated_grade}")

def update_grade():
    with open('test.json', 'r') as file:
        data = json.load(file)
        calculate_grade(data)

def update_listbox(data):
     for item in data:
          list_box.insert(END, item)

def delete_all():
    with open('test.json','w') as file:
        file.write("[]")
    
    label1.config(text="Current grade: 0")
    list_box.delete(0 , END)

# Create a gui window
window = Tk()

#Set the background color
window.configure(background = 'light blue')

#Set the window size
window.geometry("700x500")

#Give the application a title
window.title("Grade Book: Basic")

#Creates a text label
label1 = Label(window, text="Calculated Grade : 0")

#Create an entry box for filling in or typing infomation
grades = Entry(window)

enter_button = Button(window, text="Add", command=add_grades)

list_box = Listbox(window)

delete_buttom = Button(window, text="Delete", command=delete_grades)

update_button = Button(window, text="Update Grade", command=update_grade)

delete_all_button = Button(window, text="Clear all", command=delete_all)

#Grid method used for placing the widgets at respective positions in table like structure
label1.grid(row = 1, column = 0, padx = 10, pady = 10)  

grades.grid(row = 1, column = 1, padx = 10, pady = 10) 

enter_button.grid(row = 2, column = 1, padx = 10, pady = 10)

list_box.grid(row = 3, column = 1, padx = 10, pady = 10)

delete_buttom.grid(row = 4, column = 1, padx = 10, pady = 10)

update_button.grid(row = 5, column = 1, padx = 10, pady = 10)

delete_all_button.grid(row = 6, column = 1, padx = 10, pady = 10)


#Loads grade data on open
get_grades()

#Start the GUI
window.mainloop()
