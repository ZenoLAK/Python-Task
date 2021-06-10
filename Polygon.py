import matplotlib.pyplot as plt
import numpy as np

sizeV = int(input('what are the number of vertices '))
while sizeV < 4:
    print("please enter more than 3 vertices ")
    sizeV = int(input('what are the number of vertices '))

polygon = []

for i in range(0, sizeV):  # Entering the value of the vertices
    values = [float(input("Enter x coordinate ")), float(input("Enter y coordinate "))]
    polygon.append(values)

polygon.append(polygon[0])  # Appending again for a closed shape
xs, ys = zip(*polygon)  # create lists of x and y values
plt.figure(figsize=(10, 8))
plt.plot(xs, ys)
plt.title("Polygon")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

print("Do you want to make its size bigger or smaller ")
answer1 = input("Type yes if you want to or no otherwise ")
if answer1 == 'yes':
    answer2 = input("if you want to make it bigger type 'big' else type 'small' ")
    if answer2 == 'big':
        an_array = np.array(polygon)
        Resized_polygon = an_array * 2  # for making the values of vertices larger
        xs, ys = zip(*Resized_polygon)
        plt.figure(figsize=(10, 8))
        plt.plot(xs, ys)
        plt.title("Resized Bigger Polygon")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.show()
    elif answer2 == 'small':
        an_array = np.array(polygon)
        Resized_polygon = an_array / 2  # for making the values of vertices smaller
        xs, ys = zip(*Resized_polygon)
        plt.figure(figsize=(10, 8))
        plt.plot(xs, ys)
        plt.title("Resized Smaller Polygon")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.show()
