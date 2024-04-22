import pandas as pd
import matplotlib.pyplot as plt
x=[0,2,4,6,8,10,12,14,16]
y=[0,4,16,36,64,100,144,196,216]




plt.plot(x,y)
plt.title("example -scatter plot")
plt.show()
plt.scatter(x,y)
plt.title("example -scatter plot")
plt.show()

plt.bar(x,y)
plt.title("example -scatter plot")
plt.show()

fig=plt.figure(figsize=(18,5))
first_plot=fig.add_subplot(1,3,1)
first_plot.plot(x,y,color="red")
plt.show()
fig=plt.figure(figsize=(18,5))
first_plot=fig.add_subplot(1,3,1)
first_plot.plot(x,y,color="red")
plt.show()
data=pd.read_csv("student.csv")
plt.scatter(data["time_study"],data["Marks"])
plt.show()