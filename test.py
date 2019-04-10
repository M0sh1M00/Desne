import random
random.seed(1)
mylist = list()
loops= 0
while True:
    loops+=1
    mylist.append(random.random())
    random.seed(random.random())
    if random.random() in mylist:
        break
    if loops == 1000:
        print(mylist)
print(len(mylist))
