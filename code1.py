import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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


# Sample data
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]


# Create the scatter plot
plt.scatter(x, y)

# Add labels and a title
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Basic Scatter Plot in Python')


# Display the plot
plt.show()


#pie chart
# Data for the pie chart
sizes = np.array([35, 25, 25, 15]) 
labels = ["Apples", "Bananas", "Cherries", "Dates"]

# Create the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Ensure the pie chart is a perfect circle
plt.axis('equal') 

# Add a title
plt.title('Fruit Preferences')

# Display the chart
plt.show()



d4=np.array()
print(d4)


d5=np.array()
print(d5)

