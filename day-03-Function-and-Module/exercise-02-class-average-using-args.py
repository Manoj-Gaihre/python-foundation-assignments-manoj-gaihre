def class_average(*scores):
    length = len(scores)
    if length:
        average = (sum(scores)/length)
        return round(average, 2)
    else:
        return 0

print(class_average(80, 90, 70))
print(class_average(55, 60, 65, 70, 75))
print(class_average())