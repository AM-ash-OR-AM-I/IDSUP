from matplotlib import pyplot as plt

x = range(1, 6)
sgpa = [10, 9.79, 9.5, 9.89, 9.85]
cgpa = [sum(sgpa[:i])/i for i in range(1, len(sgpa)+1)]

plt.plot(x, sgpa)
plt.plot(x, cgpa)
plt.legend(['SGPA', 'CGPA'])
plt.show(dpi=200)
