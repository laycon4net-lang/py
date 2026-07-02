import matplotlib.pyplot as plt
Buisness_name=["Neymar", "bob", "pele", "bage", "louis"]
students_marks=[50,70,67,100,82]
marks_perc = []
for x in Buisness_name:
    res = (x/50)*100
    marks_perc.append(res)
    print(marks_perc)
def marks_line_chart():
    plt.plot(Buisness_name,Buisness_name)
    plt.title("Buisness analysis")
    plt.xlabel("workers")
    plt.ylabel("progress")
    plt.show()
marks_line_chart()
def percentage_bar_chart():
    plt.bar(Buisness_name,marks_perc)
    plt.title("Buisness analysis")
    plt.xlabel("workers")
    plt.ylabel("progress")
    plt.show()
percentage_bar_chart()
