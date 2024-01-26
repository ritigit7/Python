# ----> always save as string (input() is working as Scanf)

c = input("Enter your Name:")
print(c)
print(type(c))
c = int(c)  # ------> convert into integer

# Program for Sumation
print("Enter the Number:")
a = input()
a = int(a)
b = input("Enter the Number:")
b = int(b)
print("Sum of a and b is :", a+b)

# langth function 
length="GoodBye"
print(len(length))

# end with function
end="My name is Ritik"
print(end.endswith("ritik")) # it return  false for string is end with ritik
print(end.endswith("Ritik")) # it return true  for string is end with Ritik

# charector counting function 
santans="How are you, I am fine and you ."
print(santans.count("i")) # this function is count how many "i" in string 
print(santans.count("you")) # this function is count how many "you" in string 

# capitalizing function 
santans="how are you. I am fine and you ."
print(santans.capitalize())

# finding function 
print(santans.find("fine")) # it return the number of place of "fine" 
print(santans.find("Ritik")) # it return -1 means "Ritik" is not in string 

# replacing function 
print(santans.replace("I am","Ritik is"))

#\n  \t  \'  \\ ------> Escape sequance carector
name="My name is\t Ritik.\n  \\I am learning \'python\'."
print(name)