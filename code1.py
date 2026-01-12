import numpy as np
import pandas as pd


print(a)

arr1=np.array(1,2,3,4)

print(arr1)


data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]}

df1 = pd.DataFrame(data)

print(df1)

# Creating a dictionary
my_dict = {"apple": 1, "banana": 2, "cherry": 3}


# Accessing a value
print(my_dict["banana"]) # Output: 2


# Adding an item
my_dict["date"] = 4


# Iterating through keys
for key in my_dict:
    print(key)


# Iterating through key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")



d2=pd.plot()
print(d2)


d3=np.plot()
print(d3)


d4=np.array()
print(d4)


