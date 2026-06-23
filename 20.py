import matplotlib.pyplot as plt
students_name=["legend of 67", "bob", "pepe", "bage", "louis"]
students_marks=[50,70,67,100,82]
marks_perc = []
for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)
    print(marks_perc)
def marks_line_chart():
    plt.plot(students_name,students_marks)
    plt.title("school performance")
    plt.xlabel("participants")
    plt.ylabel("votes")
    plt.show()
marks_line_chart()
def percentage_bar_chart():
    plt.bar(students_name,marks_perc)
    plt.title("school performance")
    plt.xlabel("participants")
    plt.ylabel("votes")
    plt.show()
percentage_bar_chart()
