a="fjkd"
print(type(a))

if type(a)==str:
    print("ok")



# from pymongo import MongoClient

# client = MongoClient()
# db = client.PySimpleGUI
# collection = db.GUI_collection_1
# all_data=collection.find()
# dicarr=[]
# fl=open('D:\python programs\All\.venv\Include\jupyter_files\PysimpleGUI_student_data.txt','r+')
# # print(fl.read())
# for i in all_data:
#     # dicarr.append(f"Name:{i['Name']}")
#     fl.write(str(i))


# # st=str(dicarr)
# # print(type(st))
# fl.close()
# print(dicarr)


# type ipython
# print(hash("dlksjf"))

# def f(x):
#     for i in range(0,x):
#         return i**2
# def g(x):
#     return x**4
# def h(x):
#     return x**8

# import timeit
# print(timeit.timeit('[func(1) for func in (f,g,h)]', globals=globals()))