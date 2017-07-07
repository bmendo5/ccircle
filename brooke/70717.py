"""
def squared_list(list_of_integers):
    for i in range(len(list_of_integers)):
        list_of_integers[i] = list_of_integers[i]**2
    return list_of_integers

print(squared_list([1,2,3]))


def reverse(a_list):
    x = len(a_list)
    while x > 0 :
        x = x-1
            return [a_list[x] for elem in a_list]

def reverse(a_list):
    x = len(a_list)
    firstElem = a_list[0]
    for elem in range(x):
        a_list[elem] = a_list[x-1]
        x = x - 1
    a_list[len(a_list)-1] = firstElem
    return a_list

def reverseSean(a_list):
    newList = []
    for i in range(len(a_list)):


print(reverse([1,2,3]))

def hailstone(n):
    list=[]
    while n != 1:
        if n % 2 == 0:
            n=n/2
            list.append(n)
        else:
            n=3(n)+1
            list.append(n)
    print(list)
hailstone(256)
"""
