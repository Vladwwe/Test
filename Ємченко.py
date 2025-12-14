
def bubble_sort(a):
    n = len(a)
    for num in range(n-1):
        for i in range(n-1):
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
    return a

def selection_sort(a):
    n = len(a)
    for num in range(n-1):
        min_index = num
        for i in range(num+1,n):
            if a[i] < a[min_index]:
                min_index = i
    a[num],a[min_index] = a[min_index],a[num]
    return a
def insertion_sort(a):
    n = len(a)
    for num in range (1,n):
        for i in range(num,0,-1):
            if a[i]<a[i-1]:
                a[i],a[i-1]=a[i-1],a[i]
    return a


mass = [5,3,2,1,4,6,9,8,3,2,1]
print(bubble_sort(mass))
print(selection_sort(mass))
print(insertion_sort(mass))
