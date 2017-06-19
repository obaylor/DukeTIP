import numpy as np
import matplotlib.pyplot as plt

x = [-40, -20, 0, 20, 40, 60, 80]
y = [61, 177.33, 296.33, 680.33, 651, 534.67, 24.67]

user_input = raw_input("Type an angle")

angle = int(user_input)

result = np.polyfit(x, y, 6)

print (result)

eq = np.poly1d(result)
print(eq)
print(eq(angle))

x2 = np.arange(-40, 90)
yfit = np.polyval(result, x2)
plt.plot(x, y, label = 'points')
plt.plot(x2, yfit, label = 'fit')
plt.savefig('rocket_graph')
