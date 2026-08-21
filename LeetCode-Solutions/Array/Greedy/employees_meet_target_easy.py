def meet_target(hours , target):
    count = 0
    for hour in hours:
        if hour >= target:
            count += 1
    return count

hours = [1, 2, 3, 4, 5]
print(meet_target(hours , 2))