#create and use functions to show variable locality

def thisfunc(a, b):
    print(a)
    print(b)

def thatfunc(a, b):
    thisfunc(a, b)

thisfunc(1,2)
thatfunc(2, 5)
