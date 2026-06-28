import matplotlib.pyplot as plt
students_name=["bags", "banana", "sports", "lamp", "jars", "toys", "consoles"]
students_marks=[35,50,20,45,25,100,25]
marks_perc = []
for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)
    print(marks_perc)
def marks_line_chart():
    plt.plot(students_name,students_marks)
    plt.title("product sales")
    plt.xlabel("stuff")
    plt.ylabel("profit")
    plt.show()
marks_line_chart()
def percentage_bar_chart():
    plt.bar(students_name,marks_perc)
    plt.title("product sales")
    plt.xlabel("stuff")
    plt.ylabel("profit")
    plt.show()
percentage_bar_chart()