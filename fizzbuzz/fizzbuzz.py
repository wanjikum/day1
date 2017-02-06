"""A program implements the fizzbuzz app"""
def fizz_buzz(arg):
    """A function that tests if the number is divisible by 3 and 5"""
    if arg%3 == 0 and arg%5 == 0:
        return 'FizzBuzz'
    elif arg%5 == 0:
        return 'Buzz'
    elif arg%3 == 0:
        return 'Fizz'
    else:
        return arg
