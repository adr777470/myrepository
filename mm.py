import numpy as np

def cal_mohit(a,b,c):
    ab = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5
    bc = ((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2 + (c[2] - b[2]) ** 2) ** 0.5
    ac = ((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2 + (a[2] - c[2]) ** 2) ** 0.5
    return ab + bc + ac

def cal_masahat(a,b,c):
    ab = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5
    bc = ((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2 + (c[2] - b[2]) ** 2) ** 0.5
    ac = ((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2 + (a[2] - c[2]) ** 2) ** 0.5
    P = (ab + bc + ac) / 2
    return (P * (P - ab) * (P - bc) * (P - ac)) ** 0.5

a = np.arange(3)
b = np.arange(3)
c = np.arange(3)

for i in range(0,3):
    print("Please enter the number" , i+1 , " point :")
    x = float(input("enter x:"))
    y = float(input("enter y:"))
    z = float(input("enter z:"))
    if(i==0):
        a[0] = x
        a[1] = y
        a[2] = z
    elif(i==1):
        b[0] = x
        b[1] = y
        b[2] = z
    elif(i==2):
        c[0] = x
        c[1] = y
        c[2] = z

print("masahat: ",cal_masahat(a,b,c))
if(cal_masahat(a,b,c) == 0):
    print("mohit: ",cal_mohit(a,b,c) / 2)
else:
    print("mohit: ",cal_mohit(a,b,c))
