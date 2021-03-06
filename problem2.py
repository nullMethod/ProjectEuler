
# Project Euler - Problem 2

# Each new term in the Fibonacci sequence is generated by adding the
# previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.

# 1st attempt

def fibonacci_up_to(limit):
    fibonacci = [1,2]

    while True:
        n1 = fibonacci[len(fibonacci)-2]
        n2 = fibonacci[len(fibonacci)-1]

        nth = n1 + n2

        if nth >= limit:
            break

        fibonacci.append(nth)
        
    return fibonacci

print sum([x for x in fibonacci_up_to(4000000) if x % 2 == 0])

# Answer is 4613732
