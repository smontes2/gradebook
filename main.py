from tkinter import*
from basicCalculations import Calculations
import json
from homepage import HomePage

def main():

    # c = Calculations()

    # with open('gpa.json', 'r') as json_file:
    #     load_file = json.load(json_file)
    # currentGpa = load_file['gpa']
    # currentCredits = load_file['credits']

    # print("\nCurrent GPA: " + str(currentGpa))
    # print("Current number of credits: " + str(currentCredits) + "\n")
    # mode = input("Enter basic, weighted or gpa to continue \n")

    # if mode == "basic":
    #     c.basicCalculation()
    # if mode == "weighted":
    #     c.weightGradeCalculator()
    # if mode == "gpa":
    #     c.gpaCalculator()

    pass
     
if __name__ == '__main__':
    main()
    HomePage().create_window()
    

    



