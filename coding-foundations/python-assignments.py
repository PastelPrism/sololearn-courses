# Game Messages - Display 'Game Over' on the screen 

message = "Game over"
message = print(message)

# Shopping Prices - Create a variable to store numerical value and display it on screen

price = 139
print(price)

# The Semester Grade - Display expected result (133) on the screen 

midterm = 55
final = 78
semester_grade = midterm + final
print(semester_grade)

# And The Winner Is ... - Fix the bugs

name = "Anna"
score = 96
print(name)
print(score)

# Flight Tracker - Make use of comments 
flight_n = "BA0117"
destination = "New York"
distance = 1580
print(flight_n)
print(destination)
print(distance)

# Snowflake - Debug the code 

p1 = "  *  "
p2 = " *** "
p3 = "*****"

print(p1)
print(p2)
print(p3)
print(p2)
print(p1)

#It's payday! - Expected result: 160000

salary = 150000
pay_raise = 10000

new_salary = salary + pay_raise


print(new_salary)

#Chatbot vs1 - Ask the user's name and siplay it on the screen

name = input()
print(name)


#Messaging app - Ask the user for their name and age and display it on the screen

name = input()
print(name)
age = input()
print(age)

#Chatbot vs1.1 - Use string concatenation to join string and display message
name = input()
message = "Nice to meet you, " + name
print(message)

#Finance app - Complete the code to take the savings, calculate the end amount, then display a message on the screen

savings = input()
savings = float(savings)
balance = savings * 1.05 
balance = str(balance)
message = "Amount in 1 year: " + balance
print(message)

#Chess Tournament -Convert the inputted values into numbers, then calculate and display score from player. 

wins = int(input())
ties = int(input())
score = wins * 3 + ties
print("Score: " + str(score))

#Level Up!- Complete the code to display True if score is greater than 100

score = int(input())
print(score > 100)  

#Fitness Goals! - Display true is steps is greater than 10000 or active minutes is greater than 30

steps = int(input())
active_minutes = int(input())
print(steps >= 10000 or active_minutes >= 30)
