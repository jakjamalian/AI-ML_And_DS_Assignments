class clsLibrary():

    def DisplayAISubFeilds():
        aiSubFeilds = ("Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing" )
        for aiSubFeild in aiSubFeilds:
            print(aiSubFeild)

    def CheckForODDorEven(inputNumber):
        if ((inputNumber %2) == 0):
            print("Even")
        else:
            print("ODD")

    def checkMarriageEligibility(age, gender):
        print("Your Gender : ", gender)
        print("Your Age : ", age)
        if ((gender == "Male") and (age > 20)):
            print("ELIGIBLE")
        elif ((gender == "Female") and (age > 17)):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def calculatePercentage(M1,M2,M3,M4,M5):
        total = M1+M2+M3+M4+M5
        percentage = total/5
        print("Subject 1 : ", M1)
        print("Subject 2 : ", M2)
        print("Subject 3 : ", M3)
        print("Subject 4 : ", M4)
        print("Subject 5 : ", M5)
        print("Total Marks : ", total)
        print("Percentage : ", percentage)

    def AreaOfTriangle(Height, Breadth):
        Area = (Height*Breadth)/2
        print("Height : ", Height)
        print("Breadth : ", Breadth)
        print("Area of Triangle : ", Area)   

    def Perimeter(Height1, Height2, Breadth):
        Perimeter = Height1+Height2+Breadth
        print("Height 1: ", Height1)
        print("Height 2: ", Height2)
        print("Breadth : ", Breadth)
        print("Perimeter of Triangle : ", Perimeter)   