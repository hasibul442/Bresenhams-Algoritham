X0 , Y0 = input().split(" ")
X1 , Y1 = input().split(" ")

X0 =int(X0)
Y0 =int(Y0)
X1 =int(X1)
Y1 =int(Y1)

del_x = X1 - X0
del_y = Y1 - Y0
m = (del_x/del_y)
del_2y = 2*del_y
del_2x = 2*del_x
p0 = del_2y-del_x

print("X \t","Y \t\t","P")
print(X0,"\t",Y0,"\t",p0)


for i in range(X0,X1):
        if p0>= 0:
            p0 = p0 + del_2y-del_2x
            X0 = X0+1
            Y0 = Y0+1
            print(X0, "\t", Y0, "\t", p0)
        elif p0<0:
            p0 = p0 + del_2y
            X0 = X0 + 1
            Y0 = Y0
            print(X0, "\t", Y0, "\t", p0)
