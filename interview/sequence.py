

"""
--- ALGORITHM:
--- This program calculates the Fibonacci sequence up to the 50th term and then sums all the terms to get the total sum of the first 50 Fibonacci numbers.
"""




def fibonacci_sum(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    print("first 50 Fibonacci numbers:", fib_sequence)
    return sum(fib_sequence)

# Calculate the sum of the first 50 Fibonacci numbers
sum_first_50 = fibonacci_sum(50)
print("Sum of the first 50 Fibonacci numbers:", sum_first_50)
