# Triangulo equilatero
import matplotlib.pyplot as plt

L = 6
x1, y1 = 0, 0
x2, y2 = L, 0
x3, y3 = L/2, (3**0.5)/2*L

fig, ax = plt.subplots()
ax.plot([x1, x2], [y1, y2])
ax.plot([x2, x3], [y2, y3])
ax.plot([x3, x1], [y3, y1])
ax.set_title('Triángulo equilátero')

plt.show()

