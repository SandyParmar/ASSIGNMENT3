import math

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break

num = inputNumber("Enter a number: ")

sqrt_result = math.sqrt(num)

log_result = math.log(num)

sine_result = math.sin(num)

print(f"Square Root: {sqrt_result}")
print(f"Logarithm: {log_result}")
print(f"Sine: {sine_result}")
