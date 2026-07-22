def stack_validate(input , output):
    stack = []
    j = 0
    for num in input:
        stack.append(num)
        while stack and stack[-1] == output[j]:
            stack.pop()
            j+=1
    print(j)
    return j == len(output)

pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
print(stack_validate(pushed , popped))