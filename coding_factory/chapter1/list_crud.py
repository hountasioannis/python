grades = [1,4,10,7,5]

grades.append(8)
grades[1] = 5
grades.remove(1)
print(grades)

if (10 in grades):
    print("Wow!!")


if 1 in grades:
    position_to_update = grades.index(1)
    grades[position_to_update] = 9.5


print(grades)