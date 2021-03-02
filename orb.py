import random as random
import matplotlib.pyplot as plt
import numpy as np
import math


def wavefunction(x, y, z, state):
    R = 0                      # parte radiale
    Y = 0                      # parte angolare
    r = math.sqrt(x*x+y*y+z*z)  # coordinata radiale

    if (state == 1):  # n=1,l=0,m=0
        R = math.exp(-r)
        Y = 1

    elif (state == 2):  # n=2,l=0,m=0
        R = math.exp(-r/2)*(1-r/2)
        Y = 1

    elif (state == 3):  # n=2,l=1,m=0
        R = math.exp(-r/2)*r
        Y = z/r

    elif (state == 4):  # n=2,l=1,m=+-1 R
        R = math.exp(-r/2)*r
        Y = x/r

    elif (state == 5):  # n=2,l=1,m=+-1 I
        R = math.exp(-r/2)*r
        Y = y/r

    elif (state == 6):  # n=3,l=0,m=0
        R = math.exp(-r/3)*(1-2*r/3.0+2*r*r/27.0)/3
        Y = 1

    elif (state == 7):  # n=3,l=1,m=0
        R = math.exp(-r/3)*r*(1-r/6)
        Y = z/r

    elif (state == 8):  # n=3,l=1,m=+-1 R
        R = math.exp(-r/3)*r*(1-r/6)
        Y = x/r

    elif (state == 9):  # n=3,l=1,m=+-1 I
        R = math.exp(-r/3)*r*(1-r/6)
        Y = y/r

    elif (state == 10):  # n=3,l=2,m=0
        R = math.exp(-r/3)*r*r
        Y = (z*z-1)/(r*r)

    elif (state == 11):  # n=3,l=2,m=+-1 R
        R = math.exp(-r/3)*r*r
        Y = x*z/(r*r)

    elif (state == 12):  # n=3,l=2,m=+-1 I
        R = math.exp(-r/3)*r*r
        Y = y*z/(r*r)

    elif (state == 13):  # n=3,l=2,m=+-2 R
        R = math.exp(-r/3)*r*r
        Y = (x*x-y*y)/(r*r)

    elif (state == 14):  # n=3,l=2,m=+-2 I
        R = math.exp(-r/3)*r*r
        Y = x*y/(r*r)

    return(Y*R)


print('1: n=1;l=0;m=0 \n' +
      '2: n=2;l=0;m=0 \n' +
      '3: n=2;l=1;m=0 \n' +
      '4: n=2;l=1;m=+-1 R \n' +
      '5: n=2;l=1;m=+-1 I \n' +
      '6: n=3;l=0;m=0 \n' +
      '7: n=3;l=1;m=0 \n' +
      '8: n=3;l=1;m=+-1 R \n' +
      '9: n=3;l=1;m=+-1 I \n' +
      '10: n=3;l=2;m=0 \n' +
      '11: n=3;l=2;m=+-1 R \n' +
      '12: n=3;l=2;m=+-1 I \n' +
      '13: n=3;l=2;m=+-2 R \n' +
      '14: n=3;l=2;m=+-2 I')

# parametri
N = int(1e4)      # numero punti (max 10'000)
L = float(20)     # dimensione del "box" contente l'atomo
S = int(8)        # stato da disegnare

# salviamo le posizioni su un file di testo per velocizzare il plot
file = open('positions.txt', 'w')

# generiamo coordinate casuali (x,y,z) nel box LxLxL. Valutiamo la psi(x,y,z) e
# facciamo un Monte-Carlo, salviamo il punto solo se il modulo quadro di psi è
# maggiore di un numero casuale (scarsa possibilità di plottare punti con una
# |psi|^2 molto bassa il che di traduce in punti più diradati in zone dello
# spazio meno probabili)
i = 0
while (i < N):
    x = round((random.uniform(0, 1)-0.5)*L*2, 6)
    y = round((random.uniform(0, 1)-0.5)*L*2, 6)
    z = round((random.uniform(0, 1)-0.5)*L*2, 6)
    psi = round(wavefunction(x, y, z, S), 6)
    rnd = round(random.uniform(0, 1), 6)
    if(rnd <= (psi*psi)):
        file.write('{}'.format(x*0.529)+' '+'{}'.format(y*0.529) +
                   ' '+'{}'.format(z*0.529)+' '+'{}'.format(psi*psi)+'\n')
        i += 1

file.close()

# caricare il file ed estrarre le posizioni dei punti
text = np.loadtxt('positions.txt')
X = text[:, 0]
Y = text[:, 1]
Z = text[:, 2]

# plot

fig = plt.figure(figsize=(10, 30))
# ax = fig.add_subplot(111, projection='3d')

# piano XY
ax = fig.add_subplot(131)
ax.scatter(X, Y, s=.5, marker='.', color='black')
ax.set_aspect(1)

# piano XY
ax = fig.add_subplot(132)
ax.scatter(Y, Z, s=.5, marker='.', color='black')
ax.set_aspect(1)

# piano XY
ax = fig.add_subplot(133)
ax.scatter(X, Z, s=.5, marker='.', color='black')
ax.set_aspect(1)

plt.show()
