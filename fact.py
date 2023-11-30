def fact1(f,a):
    f=f*a
    print(f)
    a=a+1
    if a<=7 :
        return fact1(f,a)
fact1(1,1)    