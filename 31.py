import matplotlib.pyplot as plt
viewer_name=["20,00"]
viewer_marks=[35,231]
viewer_perc = []
for x in viewer_marks:
    res = (x/50)*100
    viewer_perc.append(res)
    print(viewer_perc)
def marks_line_chart():
    plt.title("shares 2000")
    plt.xlabel("likes")
    plt.ylabel("comment")
    plt.show()
marks_line_chart()
def percentage_bar_chart():
    plt.title("shares 2000")
    plt.xlabel("likes")
    plt.ylabel("comment")
    plt.show()
percentage_bar_chart()