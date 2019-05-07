def tens():#if u could ignore this
    p=[]
    list=[1,2,3,4,5,6,7,8,9]
    for i in list:
        p.append(i)
        n=(p)**2
        return n

        

def squares():#if u could ignore this
    c=[x**2 for x in [2,4,6,8,10,12] ]:
    print (c)


def sort():#if u could ignore this
    a=[9,1,4,7,3]
    b=[5,2,6,80]
    c=a+b
    c.sort()





def range_sum(number):#if u could ignore this
    y=[]
    for x in range(1,number+1):
        y.append(x)
        z= sum(y)
    return z



def largest(list):#if u could ignore this
    max=list[o]
    for a  in list:
        if a> max:
            max=a
    return max




def smallest(list):#if u could ignore this
    min=list[o]
    for a  in list:
        if a< min:
            min=a
    return min


def my_modulus():#if u could ignore this
    for i in range(10,20):
        if i % 3==0:
            print (i)


def student():#if u could ignore this
    student1= {'name':'Naima','balance':3000}
    student2 = {'name':'Irene','balance':1000}
    student3 = {'name':'Pauline','balance':2000}
    students=[student1,student2,student3]
    for i in students:
        message = " hello {}, your balance {}".format(i['name'],i['balance'])
        print(message)

