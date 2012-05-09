import matplotlib as mpl
mpl.use('PDF')
if True:
    mpl.rcParams['text.usetex'] = True
    mpl.rcParams['text.latex.preamble'] = r'\usepackage{MinionPro}'
    mpl.rcParams['font.family'] = 'serif'
    mpl.rcParams['font.serif'] = 'MinionPro'
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

plot_width = 3.50

##################################################
#### Branching fraction pie charts

cmap = plt.get_cmap('Set3')
colors = [cmap(float(j)/5) for j in range(5)]
explode=[0.1, 0.1, 0, 0, 0]

bosons = ['W', 'Z']
labelsW = r'$e^\pm\nu$', r'$\mu^\pm\nu$', r'$\tau^\pm\nu$', 'Hadrons'
labelsZ = r'$e^+e^-$', r'$\mu^+\mu^-$', r'$\tau^+\tau^-$', r'$\nu\bar{\nu}$', 'Hadrons',
labels = [labelsW, labelsZ]
fracsW = [10.75, 10.57, 11.25, 67.6]
fracsZ = [ 3.36,  3.37,  3.37, 20.0, 69.91]
fracs = [fracsW, fracsZ]
for i, boson in enumerate(bosons):
    n_entries = len(labels[i])
    plt.figure(i, figsize=(plot_width, plot_width * 0.9))
    ax = plt.axes([0.0, 0.0, 0.9, 1.0])
    plt.pie(fracs[i], colors=colors[0:n_entries], explode=explode[0:n_entries],
          labels=labels[i], autopct='%1.1f%%', pctdistance=0.7, shadow=False)
    plt.savefig('pie-decays-%s' % boson)


##################################################
#### Higgs potential

step = 0.04
maxval = 1.0
fig = plt.figure(figsize=(4,3))
ax = Axes3D(fig)

# create supporting points in polar coordinates
r = np.linspace(0,1.25,50)
p = np.linspace(0,2*np.pi,50)
R,P = np.meshgrid(r,p)
# transform them to cartesian system
X,Y = R*np.cos(P),R*np.sin(P)

Z = ((R**2 - 1)**2)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0.5,
                cmap=plt.get_cmap('jet'))
ax.set_zlim3d(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')
ax.w_xaxis.set_ticklabels([''])
ax.w_yaxis.set_ticklabels([''])
ax.w_zaxis.set_ticklabels([''])
plt.savefig('higgs', transparent=True)
