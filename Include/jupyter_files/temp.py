from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
import tensorflow 
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense
import numpy as np

X,y=make_classification(n_samples=500,n_features=2,n_informative=2,n_redundant=0,n_classes=2,n_clusters_per_class=1,random_state=500)

plt.scatter(X[:, 0], X[:, 1], marker='o', c=y,s=25, edgecolor='k')
plt.show()

model=Sequential()
model.add(Dense(2,activation='relu',input_dim=2))
model.add(Dense(1,activation='sigmoid'))

model.summary()

initial_weights=model.get_weights()
initial_weights[0]=np.zeros(model.get_weights()[0].shape)
initial_weights[1]=np.zeros(model.get_weights()[1].shape) 
initial_weights[2]=np.zeros(model.get_weights()[2].shape)
initial_weights[3]=np.zeros(model.get_weights()[3].shape)

model.set_weights(initial_weights)
model.get_weights()

model.compile(optimizer='adam',metrics=['accuracy'],loss='binary_crossentropy')




# from sklearn.datasets import make_classification
# import matplotlib.pyplot as plt

# X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_classes=2, random_state=80)
# print(X,y)
# plt.scatter(X[:, 0], X[:, 1], marker='o', c=y,s=25, edgecolor='k')
# plt.show()



# print(type(a))

# if type(a)==str:
#     print("ok")



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