import matplotlib.pyplot as plt
students_name=["jimmy", "Timmi", "Rayan", "bage", "louis"]
students_marks=[50,70,67,100,82]
marks_perc = []
for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)
    print(marks_perc)
def marks_line_chart():
    plt.plot(students_name,students_marks)
    plt.title("Math marks")
    plt.xlabel("student names")
    plt.ylabel("score")
    plt.show()
marks_line_chart()
def percentage_bar_chart():
    plt.bar(students_name,marks_perc)
    plt.title("Science marks")
    plt.xlabel("student names")
    plt.ylabel("score")
    plt.show()
percentage_bar_chart()