import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))


# Valores de x entre 0 e 4 (com incremento de 0.1)
x = np.linspace(0, 4, 100)

# Calcula os valores correspondentes de y
for func in [lambda t: 100 + 40*np.exp(-3*t) - 120*np.exp(-t),
             lambda t: 100 - 80*(2*t + 1)*np.exp(-2*t),
             lambda t: 100 - 80/3*np.exp(-2*t)*(3*np.cos(3*t) + 2*np.sin(3*t))]:
             # lambda t: 100 - 40*np.exp(-2*t)*(2*np.cos(4*t) + np.sin(4*t))]:

    y = func(x)
    plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Temperatura')
plt.legend(["Superamortecido","Criticamenter amortecido", "Subamortecido"])

plt.grid(True)
# plt.show()
plt.savefig("figura_controlador_integral.eps")