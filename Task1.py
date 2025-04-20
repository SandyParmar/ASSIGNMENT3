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


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

sample_number = inputNumber("Enter a number :")
print("Enter value",sample_number)

result = factorial(sample_number)

print(f"The factorial of {sample_number} is {result}")
