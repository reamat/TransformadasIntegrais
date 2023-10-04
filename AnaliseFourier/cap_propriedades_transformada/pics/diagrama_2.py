import matplotlib.pyplot as plt
import numpy as np

#f0 = 100  # Hz
w0 = 300 # rad/s

C = [5, 0, 20, 10] # Começa em C0

corte = lambda x: 0 if x < 1e-5 else np.exp(-1.0/(x/200)**2)
escala = lambda w: corte(w*a)/a
envelope = lambda w : 1_000*escala(w+a)*escala(a-w)
w = np.linspace(0, w0*len(C), 50*len(C))



lista_a = [50, 100]
fig, ax = plt.subplots(1, 1)
"""
for a, ex in zip(lista_a, ax):
    A = np.zeros(len(w))
    for i in range(len(w)):
        # n = 1
        A[i] = sum(C[n]*envelope(w[i] - n*w0) for n in range(len(C)))


    ex.plot(w, A)

    for i in range(len(C)):
        if C[i] != 0:
            w_n = i*w0
            amplitude = sum(C[n]*envelope((i-n)*w0) for n in range(len(C)))
            ex.vlines([w_n], 0, amplitude, color='red', linestyle='dashed')

    ex.set_xlabel("Frequência angular em rad/s")

ax[0].set_title(r"$|F(\omega)|$", fontsize=16)
ax[1].set_title(r"$|G(\omega)|$", fontsize=16)
fig.set_size_inches(10, 3)

"""

a = lista_a[-1]
A = np.zeros(len(w))
for i in range(len(w)):
    # n = 1
    A[i] = sum(C[n]*envelope(w[i] - n*w0) for n in range(len(C)))


ax.plot(w, A)

for i in range(len(C)):
    if C[i] != 0:
        w_n = i*w0
        amplitude = sum(C[n]*envelope((i-n)*w0) for n in range(len(C)))
        ax.vlines([w_n], 0, amplitude, color='red', linestyle='dashed')

ax.set_xlabel("Frequência angular em rad/s")

ax.set_title(r"$|F(\omega)|$", fontsize=16)

fig.set_size_inches(5, 3)



# fig.set_size_inches(10, 5)
# plt.show()
plt.savefig("diagrama_FG_2.eps", bbox_inches = "tight")




