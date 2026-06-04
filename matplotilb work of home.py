import matplotlib.pyplot as plt
students_name=["bob", "bobby", "billy", "tilly", "chilli", "lily", "zilli"]
students_marks=[35,50,20,45,25,440,25]
marks_perc = []
for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)
    print(marks_perc)
def marks_line_chart():
    plt.plot(students_name,students_marks)
    plt.title("Jobpeople Marks Graph")
    plt.xlabel("Jobpeople Names")
    plt.ylabel("Jobpeople Marks")
    plt.show()
marks_line_chart()
def percentage_bar_chart():
    plt.bar(students_name,marks_perc)
    plt.title("Jobpeople Percentage Graph")
    plt.xlabel("Jobpeople Names")
    plt.ylabel("Jobpeople percentage")
    plt.show()
percentage_bar_chart()