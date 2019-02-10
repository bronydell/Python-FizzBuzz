def fizz_buzz(number):
    result = ''
    if number % 3 == 0:
        result += 'Fizz'
    if number % 5 == 0:
        result += 'Buzz'

    if result == '':
        return number

    return result
