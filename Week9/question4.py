input_set = {1, 2, 3, 4, 5 ,6 ,7 ,8 ,9 ,10}
for item in input_set:
    fact = 1
    for number in range(1,item+1):
        fact = fact * number
    print (item, "->",fact)