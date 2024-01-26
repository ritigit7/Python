a=2
b=5
c=a+b
print("Sum of a and b is:",a+b,c)

a+=3 #------>a=a+3
print(a)

d=4>5
print(d) #----> It return False
e=4>2
print(e) #----> It return True

# logical Oparetor
bool1=True
bool2=False
print("The boolian orparetor and is",bool1 and bool2) #--->and orparetor working as AND gate
print("The boolian orparetor or is",bool1 or bool2)   #--->or orparetor working as OR gate
print("The boolian orparetor not is",not bool2)       #--->not orparetor working as NOT gate

# type casting ------> convert data type
a="35"   #----> It look like an interger but denoted as a string because of ""
print(type(a))
# print(a+4) ----> It will not working because a is string

b="34"
b=int(b) #-----> string is convert into integer (if it is capeble )
print(type(b))   #                                       !
print(b+3)#                                              !--->  b="alkd43422" ---> Itis invalid fir integer