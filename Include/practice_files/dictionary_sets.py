dic={
    "respond":"giving answer", #string type
    "number":"100", #integer type
    "practise":{"trial":"same to do"},#multiple value type
    "list":[1,2,4,5,3], #listing  type
    1:4 # integer to integer type
}
print(dic['respond'])
print(dic['number'])# It print second bracket value 
print(dic['practise'])
print(dic['practise']['trial'])#it print value of trial of practise
print(dic['list'])
print(dic["list"])# both upper and this are valid for printing
print(dic[1])

dic['list']=[1,6,3,9] #list is taken new value 
print(dic['list'])

print(dic.keys()) # print all keys of dic
print(dic.values()) # print all keys' value of dic include dic.value
print(list(dic.values())) # print all keys' value of dic