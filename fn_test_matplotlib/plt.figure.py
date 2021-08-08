import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
input_values = [1, 2, 3, 4, 5]

#  Axes belong to figure  ||  gca == Get Current Axes
ax = plt.figure(figsize=(1, 1)).gca()  #figsize = width, height in inches 
ax.plot(input_values, squares, linewidth = 5)


f2 = plt.figure(num = 2)  # integer or string, optional, default: None
f3 = plt.figure(num = 'bobo', figsize=(1, 1))  #If num is a string, the window title will be set to string.

# gcf == Get Current figure  || the last one
a = plt.gcf()


plt.show()

