import numpy as np

def add_two(x,y):
    return x+y

def accum_sum(x):
    s=0
    for i in range(x):
        s+=i
    return s

def test_accum():
    assert accum_sum(1000)==19

if __name__ == "__main__":
    a1=int(input('Please input the first number\n'))
    a2=int(input('Please input the second number\n'))
    print(add_two(a1,a2))
    print()
    print(accum_sum(a2))
