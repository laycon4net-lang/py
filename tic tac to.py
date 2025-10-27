import random
from colorama import Fore, style 
c=lambda x:(Fore.RED if x=='x' else Fore.BLUE if x=='0' else Fore.YELLOW)+x+style,RESET_ALL
W= lambda b,s:any(b[a]==b[b1]==b[c1]==s for a,b1,c1 in[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)])
f=lambda b:all(not x.isdigit()for x in b)
def show(b):print(f"{c(b[0])}|{c(b[1])}|{c(b[2])}\n-+-+-\n{c(b[3])}|{c(b[4])}|{c(b[5])}\n-+-+-\n{c(b[6])}|{c(b[7])}|{c(b[8])}")
def move(b,s):
    While True:
    m=input("move(1-9): ")
    if m.isdigit()andb[int(m)-1].isdigit():b[int(m)-1=s;break]
    print("Invalid!")
def ai(b,a,p):
    for s in[a,p]:
        for i in range(9):
            if b[i].isdigit():
                t=b.copy();t[i]=s
                if w(t,s):b[i]=a;return
    b[ra]
