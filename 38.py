import matplotlib.pyplot as plt
students_name=["brook", "Luke", "Clix", "sokka", " Nolan"]
students_marks=[50,70,67,100,82]
marks_perc = []
for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)
    print(marks_perc)
def marks_line_chart():
    plt.plot(students_name,students_marks)
    plt.title("age analysis")
    plt.xlabel("patients")
    plt.ylabel("Disease numbers")
    plt.show()
marks_line_chart()
def percentage_bar_chart():
    plt.bar(students_name,marks_perc)
    plt.title("age analysis")
    plt.xlabel("patients")
    plt.ylabel("Disease numbers")
    plt.show()
percentage_bar_chart()
