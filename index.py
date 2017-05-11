def digital_root(number):
    sum = 0
    numberLength = len(str(number))
    firstIteration = True
    
    while numberLength > 1 or firstIteration:
        sum = 0
        firstIteration = False
        for i in range(0, numberLength):
            num = str(number)
            sum = sum + int(num[i])

        numberLength = len(str(sum))
        number = sum
        
    return sum

print(digital_root(888))
print(digital_root(111))
print(digital_root(16))
print(digital_root(7))