def max(e,f,g):
    if(e>f) and (e>g):
        print("e =",e,"is greater")
    elif (f>e) and (f>g):
        print("f =",f,"is greater")
    else:
        print("g =",g,"is greater")
e=int(input("enter e value:"))
f=int(input("enter f value:"))
g=int(input("enter g value:"))
max(e,f,g)
