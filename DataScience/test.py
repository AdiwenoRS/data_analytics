x = ['Mary', 'had', 'a', 'little', 'lamb']
a = []

def my_list(my_list):
    for i in my_list:
        a.append(i)
    return a
my_list(my_list)

print(a)

