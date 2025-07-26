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

#Chess Tournament -Convert the inputted values into numbers, then calculate and display score from player

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

#Houston! We Have Had a Problem - Check if candidate's score meet the qualifications. Display true otherwise false

physic_test = int(input())
flight_test = int(input())
result = physic_test > 90 and flight_test > 85
print(result)

#Fasten Your Seat Belt! Display "Faste your seat belt!" message 3 times 

for i in range(3):
    print("Fasten your seat belt")

#Times Up! - Create a timer program  - This one keeps failing the test...

number = int(input())


while number > 0:
    print(number)
    number -= 1


# Cell Growth - Calculate cell population at the end of each day

cells = int(input())
days = int(input())
counter = 1
while counter <= days:
    cells *= 2 
    print("Day " + str(counter) + ": " + str(cells))
    counter += 1

# Smart parking lot - Display messages based on available parking spots

spaces = int(input())
if spaces > 0:
    print("Available spaces")
else:
    print("Sorry, the parking lot is full")

# Medical Software - Display different messages based on blood sugar level

glucose_level = int(input())
if glucose_level < 70:
    print("Low glucose level")
if glucose_level > 140:
    print("High glucose level")
if glucose_level >= 70 and glucose_level <= 140:
    print("Normal range")

# Game Machine - Utput the game from the list that corresponds to that index

games = [
  'Soccer', 'Tic Tac Toe', 'Snake',
  'Puzzle', 'Rally'
]
choice = int(input())
if 0 <= choice < len(games):
    print(games[choice])
else:
    print("Invalid choice")

# Pancakes - Replace the menu items and display the new menu 

breakfasts = [
  'Donuts', 'Waffles', 'Yogurt', 
  'Burrito', 'Toast']
item = int(input())
breakfasts[item] = "Pancakes"
print(breakfasts)

# Relay Race - Perform the necessary slicing and display the groups 

players = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
g1 = players[0:2]
g2 = players[2:4]
g3 = players[4:6]

print("Group 1:")
print(g1)

print("Group 2:")
print(g2)

print("Group 3:")
print(g3)


# Step Counter - Output Adam's step counts for the past three days 

steps = [1513, 5035, 7891, 1212, 2534, 4648, 3785]
last_3 = steps[-3:]
print(last_3)
text = input()
text = text.upper()
print(text)

# Queue Management - Take a name and add it to the end of the queue 

queue = ['John', 'Amy', 'Bob', 'Adam']
name = input()
queue.append(name)
print(queue)

# Shipping Costs - Take the weight as an argument and calculate the shipping cost based on the weight

weight = int(input())
def shipping_cost(w):
    print(w * 5)
shipping_cost(weight)

#Hashtag Generator - Complete the hashtag function to return the input word starting with the hashtag

word = input()
def hashtag(word):
    return "#" + word
print(hashtag(word))
