for number in range(1,101):
     
    if number % 15 == 0:
       print("FizzBuzz")
     
    elif number % 3 == 0:
        print("Fizz")
        
    elif number % 5 == 0:
        print("Buzz")
        
    elif number % 15 != 0 and number % 3 != 0 and number % 5 != 0:
        print(number)
        
    else: 
        print("not is a multiple number")