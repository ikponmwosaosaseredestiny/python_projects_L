# GPA calculator
# grades equivalent value
# A --- 5
# B --- 4
# C --- 3
# D --- 2
# E --- 1


# input your grades here
grades = [
    {
        "course title": "Chm11",
        "grade": "A",
        "credit": 3
    },
    {
        "course title": "Chm11",
        "grade": "A",
        "credit": 3
    },
    {
        "course title": "Chm11",
        "grade": "B",
        "credit": 3
    },
    {
        "course title": "Chm11",
        "grade": "B",
        "credit": 2
    },
]


def calculate_GPA():

    list_reducer = []
    total_credit = 0

    # validate if list is empty
    if len(grades) == 0:
        return print('Please input your grades before you continue!')

    # sum up all credit and new list for grades/credits
    for index in range(len(grades)):
        grade_value = 0
        total_credit += grades[index]["credit"]

        if grades[index]["grade"].upper() == "A":
            grade_value = grades[index]["credit"] * 5
        elif grades[index]["grade"].upper() == "B":
            grade_value = grades[index]["credit"] * 4
        elif grades[index]["grade"].upper() == "C":
            grade_value = grades[index]["credit"] * 3
        elif grades[index]["grade"].upper() == "D":
            grade_value = grades[index]["credit"] * 2
        elif grades[index]["grade"].upper() == "E":
            grade_value = grades[index]["credit"] * 1

        list_reducer.append(grade_value)

    # calculate all grades total
    list_reducer_sum = 0
    for index in list_reducer:
        list_reducer_sum += int(index)
    # calculate final gpa
    final_gpa = list_reducer_sum / total_credit
    print(round(final_gpa, 2))


# run function
calculate_GPA()
