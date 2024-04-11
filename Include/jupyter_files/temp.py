# from sklearn.datasets import make_classification
# import matplotlib.pyplot as plt
# import tensorflow 
# from tensorflow import keras
# from keras import Sequential
# from keras.layers import Dense
# import numpy as np

# X,y=make_classification(n_samples=500,n_features=2,n_informative=2,n_redundant=0,n_classes=2,n_clusters_per_class=1,random_state=500)

# plt.scatter(X[:, 0], X[:, 1], marker='o', c=y,s=25, edgecolor='k')
# plt.show()

# model=Sequential()
# model.add(Dense(2,activation='relu',input_dim=2))
# model.add(Dense(1,activation='sigmoid'))

# model.summary()

# initial_weights=model.get_weights()
# initial_weights[0]=np.zeros(model.get_weights()[0].shape)
# initial_weights[1]=np.zeros(model.get_weights()[1].shape) 
# initial_weights[2]=np.zeros(model.get_weights()[2].shape)
# initial_weights[3]=np.zeros(model.get_weights()[3].shape)

# model.set_weights(initial_weights)
# model.get_weights()

# model.compile(optimizer='adam',metrics=['accuracy'],loss='binary_crossentropy')




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

# import streamlit as st
# import pandas as pd

# # Create a title and header for the app
# st.title("My First Streamlit App")
# st.header("This is a header")

# # Create a dataframe
# df = pd.DataFrame({
#   'name': ['Alice', 'Bob', 'Carol'],
#   'age': [25, 30, 35]
# })

# # Display the dataframe
# st.dataframe(df)

# # Add a text element
# st.write("This is some text")

# # Add a button
# if st.button('Click me'):
#   st.write("You clicked the button!")


import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification,make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def load_initial_graph(dataset,ax):
    if dataset == "Binary":
        X, y = make_blobs(n_features=2, centers=2,random_state=6)
        ax.scatter(X.T[0], X.T[1], c=y, cmap='rainbow')
        return X,y
    elif dataset == "Multiclass":
        X,y = make_blobs(n_features=2, centers=3,random_state=2)
        ax.scatter(X.T[0], X.T[1], c=y, cmap='rainbow')
        return X,y

def draw_meshgrid():
    a = np.arange(start=X[:, 0].min() - 1, stop=X[:, 0].max() + 1, step=0.01)
    b = np.arange(start=X[:, 1].min() - 1, stop=X[:, 1].max() + 1, step=0.01)

    XX, YY = np.meshgrid(a, b)

    input_array = np.array([XX.ravel(), YY.ravel()]).T

    return XX, YY, input_array


plt.style.use('fivethirtyeight')

st.sidebar.markdown("# Logistic Regression Classifier")

dataset = st.sidebar.selectbox(
    'Select Dataset',
    ('Binary','Multiclass')
)

penalty = st.sidebar.selectbox(
    'Regularization',
    ('l2', 'l1','elasticnet','none')
)

c_input = float(st.sidebar.number_input('C',value=1.0))

solver = st.sidebar.selectbox(
    'Solver',
    ('newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga')
)

max_iter = int(st.sidebar.number_input('Max Iterations',value=100))

multi_class = st.sidebar.selectbox(
    'Multi Class',
    ('auto', 'ovr', 'multinomial')
)

l1_ratio = int(st.sidebar.number_input('l1 Ratio'))

# Load initial graph
fig, ax = plt.subplots()

# Plot initial graph
X,y = load_initial_graph(dataset,ax)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
orig = st.pyplot(fig)

if st.sidebar.button('Run Algorithm'):
    orig.empty()

    clf = LogisticRegression(penalty=penalty,C=c_input,solver=solver,max_iter=max_iter,multi_class=multi_class,l1_ratio=l1_ratio)
    clf.fit(X_train,y_train)

    y_pred = clf.predict(X_test)

    XX, YY, input_array = draw_meshgrid()
    labels = clf.predict(input_array)

    ax.contourf(XX, YY, labels.reshape(XX.shape), alpha=0.5, cmap='rainbow')
    plt.xlabel("Col1")
    plt.ylabel("Col2")
    orig = st.pyplot(fig)
    st.subheader("Accuracy for Decision Tree  " + str(round(accuracy_score(y_test, y_pred), 2)))