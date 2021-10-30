# Author: Ewa Zalewska
# Concept: BMI calculator in Python
# Github: https://github.com/Mewwaa


import math 

PI = math.pi


def square(num1):
    result = num1*num1
    print("Area of your square in square cm is: ",result)
    print(" ")
    print("**************************")
    print(" ")


def rectangle(num1,num2):
    result = num1*num2
    print("Area of your rectangle in square cm is: ",result)
    print(" ")
    print("**************************")
    print(" ")


def triangle(num1,num2):
    result = (num1*num2)/2
    print("Area of your triangle in square cm is: ",result)
    print(" ")
    print("**************************")
    print(" ")


def parallelogram(num1,num2):
    result = num1*num2
    print("Area of your parallelogram in square cm is: ",result)
    print(" ")
    print("**************************")
    print(" ")


def rhombus(num1,num2):
    result = (num1*num2)/2
    print("Area of your rhombus in square cm is: ",result)
    print(" ")
    print("**************************")
    print(" ")


def trapezoid(num1,num2,num3):
    result = ((num1+num2)*num3)/2
    print("Area of your trapezoid in square cm is: ",result)
    print(" ")
    print("**************************")
    print(" ")


def circle(num1):
    result = PI*(num1*num1)
    print("Area of your circle in square cm is: ",result)
    print(" ")
    print("**************************")
    print(" ")










def cylinder(num1,num2):
    result = (2*PI*(num1*num1))+(2*PI*num1*num2)
    print("Surface area of your circular cylinder in square cm is: ",result)
    print(" ")
    print("**************************")
    print(" ")


def cube(num1):
    result = 6*(num1*num1)
    print("Surface area of your cube in square cm is: ",result)
    print(" ")
    print("**************************")
    print(" ")


def pyramid(num1,num2):
    result = (num1*num1)+(4*((num1*num2)/2))
    print("Surface area of your pyramid in square cm is: ",result)
    print(" ")
    print("**************************")
    print(" ")


def sphere(num1):
    result = 4*PI*(num1*num1)
    print("Surface area of your sphere in square cm is: ",result)
    print(" ")
    print("**************************")
    print(" ")


def hemisphere(num1):
    result = 3*PI*(num1*num1)
    print("Surface area of your hemisphere in square cm is: ",result)
    print(" ")
    print("**************************")
    print(" ")




print("!!! Please write lengths only in centimetres, otherwise, this calculator won't count results right !!!")
print("-----------------")



while True:
    
    print("Chose if the area of shape you want to calculate is in 2D or in 3D")
    print("1. 2D")
    print("2. 3D")
    print(" ")    
    print("0. Exit")
    print("-----------------")
    choice=int(input("Enter your choice: "))

    if choice==1:
        print("1. square")
        print("2. rectangle")
        print("3. triangle")
        print("4. parallelogram")  
        print("5. rhombus")
        print("6. trapezoid")
        print("7. circle")  
        print(" ")   
        print("0. Go back to menu")
        print("-----------------")
        choice2=int(input("Enter your choice: "))
        
        if choice2==1:
            print(" ")
            num1=float(input("Enter the value of side length: "))
            print(" ")
            print("**************************")
            square(num1)


        elif choice2==2:
            print(" ")
            num1=int(input("Enter the value of length side a: "))
            num2=int(input("Enter the value of length side b: "))
            print(" ")
            print("**************************")
            rectangle(num1,num2)
        
        elif choice2==3:
            print(" ")
            num1=int(input("Enter the length of base: "))
            num2=int(input("Enter the value of height: "))
            print(" ")
            print("**************************")
            triangle(num1,num2)
        
        elif choice2==4:
            print(" ")
            num1=int(input("Enter the length of base:"))
            num2=int(input("Enter the value of height:"))
            print(" ")
            print("**************************")
            parallelogram(num1,num2)


        elif choice2==5:
            print(" ")
            num1=int(input("Enter the length of the shorter diagonal: "))
            num2=int(input("Enter the length of the longer diagonal: "))
            print(" ")
            print("**************************")
            rhombus(num1,num2)
        
        elif choice2==6:
            print(" ")
            num1=int(input("Enter the length of the shorter base: "))
            num2=int(input("Enter the length of the longer base: "))
            num3=int(input("Enter the value of height: "))
            print(" ")
            print("**************************")
            trapezoid(num1,num2,num3)
        
        elif choice2==7:
            print(" ")
            num1=int(input("Enter the radius of the circle:"))
            print(" ")
            print("**************************")
            circle(num1)

        elif choice==0:
            break

        else:
            print("Wrong choice")




    elif choice==2:
        print("1. circular cylinder")
        print("2. cube")
        print("3. square pyramid")
        print("4. sphere")  
        print("5. hemisphere")
        print(" ")   
        print("0. Go back to menu")
        print("-----------------")
        choice3=int(input("Enter your choice: "))
        
        if choice3==1:
            print(" ")
            num1=float(input("Enter the radius of cylinder's base: "))
            num2=float(input("Enter the cylinder's height: "))
            print(" ")
            print("**************************")
            cylinder(num1,num2)


        elif choice3==2:
            print(" ")
            num1=int(input("Enter the value of length side a: "))
            print(" ")
            print("**************************")
            cube(num1)
        
        elif choice3==3:
            print(" ")
            num1=int(input("Enter the length of base: "))
            num2=int(input("Enter the value of height: "))
            print(" ")
            print("**************************")
            pyramid(num1,num2)
        
        elif choice3==4:
            print(" ")
            num1=int(input("Enter the radius of sphere:"))
            print(" ")
            print("**************************")
            sphere(num1)


        elif choice3==5:
            print(" ")
            num1=int(input("Enter the radius of hemisphere: "))
            print(" ")
            print("**************************")
            hemisphere(num1)
        

        elif choice==0:
            break

        else:
            print("Wrong choice")
                
    elif choice==0:
        break
    else:
        print("Wrong Choice")


