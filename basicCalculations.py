from tkinter import*
import json

class Calculations:

    def __init__(self, gradeList = [], weightList = [], creditList = []):
        self.gradeList = gradeList
        self.weightList = weightList
        self.creditList = creditList

    # def basicCalculation(self):

    #     while True:
    #         grade = input("Enter a grade (c to calculate) \n")
    #         if grade == "c":
    #             break
    #         self.gradeList.append(int(grade))
        
    #     totalGrade = sum(self.gradeList)

    #     print(totalGrade / len(self.gradeList))

    # def weightGradeCalculator(self):

    #     while True:
    #         grade = input("Enter a grade (c to calculate) \n")
    #         if grade == "c":
    #             break
    #         weight = input("Enter grade weight \n")
    #         mult = float(grade) * float(weight)/100
    #         self.weightList.append(float(mult))

    #     totalGrade = sum(self.weightList)
                
    #     print(self.weightList)
    #     print(totalGrade)

    def gpaCalculator(self):

        points = 0
        
        while True:
            credits = input("Enter the number of credits the class is worth (c to calculate)\n")
            if credits == "c":
                break
            self.creditList.append(float(credits))
            grade = input("Enter the letter grade you recived in the class\n")
            if grade == "A+" or grade == "a+":
                points = 4.3
                gradePoint = float(credits) * points
                self.weightList.append(gradePoint)
            # if grade == "A" or grade == "a":
            #     points = 4
            #     gradePoint = float(credits) * points
            #     self.weightList.append(gradePoint)
            # if grade == "A-" or grade == "a-":
            #     points = 3.7
            #     gradePoint = float(credits) * points
            #     self.weightList.append(gradePoint)
            # if grade == "B+" or grade == "b+":
            #     points = 3.3
            #     gradePoint = float(credits) * points
            #     self.weightList.append(gradePoint)
            # if grade == "B" or grade == "b":
            #     points = 3
            #     gradePoint = float(credits) * points
            #     self.weightList.append(gradePoint)
            # if grade == "B-" or grade == "b-":
            #     points = 2.7
            #     gradePoint = float(credits) * points
            #     self.weightList.append(gradePoint)
            # if grade == "C+" or grade == "c+":
            #     points = 2.3
            #     gradePoint = float(credits) * points
            #     self.weightList.append(gradePoint)
            # if grade == "C" or grade == "c":
            #     points = 2
            #     gradePoint = float(credits) * points
            #     self.weightList.append(gradePoint)
            # if grade == "C-" or grade == "c-":
            #     points = 1.7
            #     gradePoint = float(credits) * points
            #     self.weightList.append(gradePoint)
            # if grade == "D+" or grade == "d+":
            #     points = 1.3
            #     gradePoint = float(credits) * points
            #     self.weightList.append(gradePoint)
            # if grade == "D"  or grade == "d":
            #     points = 1
            #     gradePoint = float(credits) * points
            #     self.weightList.append(gradePoint)
            # if grade == "D-" or grade == "d-":
            #     points = 0.7
            #     gradePoint = float(credits) * points
            #     self.weightList.append(gradePoint)
            # if grade == "F" or grade == "f":
            #     points = 0
            #     gradePoint = float(credits) * points
            #     self.weightList.append(gradePoint)
            
        creditTotal = sum(self.creditList)
        gradePointTotal = sum(self.weightList)

        calculatedGpa = round((gradePointTotal / creditTotal), 2)

        gpaDict = {
            "gpa" : calculatedGpa,
            "credits" : creditTotal
        }

        with open("gpa.json", "w") as outfile:
            json.dump(gpaDict, outfile)

        print("Your GPA is " + str(calculatedGpa) + " after taking " + str(creditTotal))





            



            

            

