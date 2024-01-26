# store value in a[0], a[1],...
a=[1,2,3,4,5] # -----> it is working as contener , it store sunm value
print(a)
print(a[2]) # ----> it pirnt third stored value
print(a[-1]) # ----> it pirnt fifth stored value {1,2,3,4,5}---{-5,-4,-3,-2,-1}
print(type(a)) #data type list

#changing list value 
a[0]=6
print(a)# it overwriting first stored value

# storing multiple type value
b=[4,"Ritik",False,5.5]  # [ integer,string,bolian,float]
print(b)# it  is valid and it store multiple type value

#slicing 
print(a[0:3]) # it print 0 ,1 ,2 value of a


#list methods

#sorting & reversing
c=[1,5,2,8,3,9]
d=c.sort()
print(d)# it return NONE because it is not valid

c.sort()# it is valid
print(c)# it print sorted value ( incrising ) order 

c.reverse()
print(c) # it return reverse value

#append ----> it means add somthing at the and of the list
c.append(34)
print(c)

#insert
c.insert(2,43) #---->it insert 43 at 2 place
print(c)

#removing value from place
c.pop(3)#---> it remove fourth value
print(c)

#removing value
c.remove(9)
print(c)

#making tuple using () 
t=(1,5,2,2,2,3)
# print(t[2]) #---->It print only t[2] value
# t[3]=31
# print(t)# tuple is not allow to change value of 'd'

t1=()#empty tuple
t2=(1) # wrong way to declare a tuple with single element
t3=(1,)# write way to declare a tuple with single element
print(t1)
print(t2)
print(t3)

print(t.count(2))# It count how many 2 in string
print(t.index(3))# find place of 3 in string

#sumation 
s=[6,2,8,4,3,7]
print(sum(s))#mothod 1
print(s[0]+s[1]+s[2])#method 2