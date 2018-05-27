#!/usr/bin/env python3.5

# Use of Function to calculate BMI 
# BMI = (Weight in kg / height in meters squared)
# Imperial Version : BMI * 703
def gather_info():
    height = float(input("What is your height? (inches or meters?)"))
    weight = float(input("What is your weight? (pounds or killograms?)"))
    system = input("Are your measurments in metrics or imperial units?").lower().strip()  ## convert into lower and removes white spaces
    return (height, weight, system)   # Returns multiple values as tuples 

def calc_bmi(weight, height, system='metric'):  # set default system to metric
    '''
    Return the Body Mass Index (BMI) for the given 
    values of height, weight and measurment system.
    '''
    if system == 'metric':
        bmi = (weight / (height ** 2)) 
        return bmi
    else:
        bmi = 703 * (weight / (height ** 2))
        return bmi
while True:
    height, weight, system = gather_info() # calling function gather info and assigns returned values to variables
    if system.startswith('i'):
        bmi = calc_bmi(weight, height, system)
        print("Your BMI is", bmi)
        break ## Break the loop if condition matches
    elif system.startswith('m'):
        bmi = calc_bmi(weight, height)
        print("Your BMI is", bmi)
        break
    else:
        print("Unknown measurment system, Please use Metric or Imperials")


