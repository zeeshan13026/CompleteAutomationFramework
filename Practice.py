# Variable arguments
def sum(*a):
    total = 0
    for a1 in a:
        total = total + a1
    return total


print(sum(2, 3, 6, 3, 4, 5, 6, 7))


# kwargs  ---> Return dictionary
def diplay(**kwargs):
    print(kwargs)


diplay(a1=1, a2=2, a3=30, a4='abd')
