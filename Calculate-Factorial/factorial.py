def calculate_factorial(number):
  """
  Purpose:
    This function calculates the factorial of number.
      1. If 0 or 1 is passed to the function it returns 1.
      2. Else it returns the factorial value of the number

  Args:
    number (int): integer number whose factorial is to be calculated
  
  Returns:
    int: factorial of the number
  """
  product = 1


  if number in (0, 1):
    return 1
  else:
    while number > 0:
      product *= number
      number -=1
    
    return product

if __name__ == "__main__":

  while True:
    try:
      number = int(input("Enter a number: "))
      factorial = calculate_factorial(number)
    except ValueError:
      print("Either Negative or Non-Integer Value is passed. Please pass a positive Number. ")
    else:
      print(f"The factorial of {number} is: {factorial}")
      break
