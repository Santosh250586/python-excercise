def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean

student_grades = {"marry": 9.1, "sim": 8.2, "john": 7.5}
print("student grades:")
print(mean(student_grades))

monday_temp = {8.8, 9.1, 9.9}
print("monday Temperature:")
print(mean(monday_temp))