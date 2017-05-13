def solution(digits):
    slicesArray = []
    digits = str(digits)
    for i in range(0, len(digits) - 4):
        slice = digits[i: i + 5]
        print(slice)
        slicesArray.append(int(slice))

    max = slicesArray[0]
    for i in range(1, len(slicesArray)):
        if slicesArray[i] > max:
            max = slicesArray[i]

    return max

print(solution(35421234523))