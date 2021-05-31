# Write the function between the START and END tags
# START
def FibonacciAdder(n) :
    sum = 0
    fib1 = 0
    fib2 = 1
    fib3 = 0
    for i in range(1,n):
        fib3 = fib1+fib2
        fib1=fib2
        fib2=fib3
        sum += fib1
        return sum

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(FibonacciAdder(2) == 1))
print("Test 2 Passed: " + str(FibonacciAdder(5) == 7))
print("Test 3 Passed: " + str(FibonacciAdder(10) == 88))