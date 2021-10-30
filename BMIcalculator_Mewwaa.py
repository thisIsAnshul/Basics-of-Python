# Author: Ewa Zalewska
# Concept: BMI calculator in Python
# Github: https://github.com/Mewwaa



name=input("Please enter your name: ")
print(" ")
print("Hi "+name+", let's check your current BMI")
print(" ")
print("-----------------------------")
print(" ")
w=float(input("Enter your weight in kilograms: "))
print("-----------------------------")
h=float(input("Enter your height in centimeters: "))
print("-----------------------------")

sm = float(h/100)*float(h/100)

bmi=(w/sm)

if bmi>=25:
    score="overweight, you should consider changing your diet"
elif bmi>18.5 and bmi<=24.9:
    score="optimal, your diet is good"
else:
    score="underweight, you should consider changing your diet"

print("-----------------------------")
print(name+" your BMI is : "+str(bmi))
print("You're "+score)
print("-----------------------------")


input("Press Enter to continue...")