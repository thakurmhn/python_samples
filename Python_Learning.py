'''
- Zip Function In Python
Zip function is used to combine two list
Create Dictionary by combining two list
'''

friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

D1 = dict(zip(friends, time_since_seen))
print(D1)

'''
- Functions in Python
'''
def greet():
  name = input("Enter your name: ")
  print(f"Hello {name}")

greet()

# Passing argument to the function 
cars = [
  {"make": "Ford", "model": "Fiesta", "mileage": 2300, "fuel_consumed": 460},
  {"make": "Ford", "model": "Figo", "mileage": 17000, "fuel_consumed": 350},
  {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
  {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235}
]

def calculate_mpg(car):
  mpg = car["mileage"]  / car["fuel_consumed"]
  name = f"{car['make']} {car}['model']"
  print(f"{name} does {mpg} miles per gallon")

for car in cars: 
  calculate_mpg(car)  # passed list of dictionares as argument
  
  ## Return Value and looping functions  Example 
  
  cars = [
  {"make": "Ford", "model": "Fiesta", "mileage": 2300, "fuel_consumed": 460},
  {"make": "Ford", "model": "Figo", "mileage": 17000, "fuel_consumed": 350},
  {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
  {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235}
]

def calculate_mpg(car):
  mpg = car["mileage"]  / car["fuel_consumed"]
  return mpg

def car_name(car):  
  name = f"{car['make']} {car}['model']"
  return name

def print_car_info(car):
  name = car_name(car)
  mpg = calculate_mpg(car)
  
  print(f"{name} does {mpg} miles per gallon")

for car in cars: 
  print_car_info(car)
 
# e.g 2 
def devide():
  if y == 0:
    return "You tried to devide by zero"
  else: 
    return x / y

print(devide(10, 2))
devide(6, 0)



  
  
  
