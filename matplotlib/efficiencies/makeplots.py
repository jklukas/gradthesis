import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--usetex', action='store_true')
parser.add_argument('--png', action='store_true')
args = parser.parse_args()

import matplotlib as mpl
if args.png:
    mpl.use('AGG')
else:
    mpl.use('PDF')
#mpl.rcParams['figure.figsize'] = 3.5, 3
mpl.rcParams['figure.figsize'] = (8, 5)
mpl.rcParams['font.size'] = 20
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['xtick.major.pad'] = mpl.rcParams['font.size'] / 4
mpl.rcParams['ytick.major.pad'] = mpl.rcParams['font.size'] / 4
if args.usetex:
    mpl.rcParams['text.usetex'] = True
    mpl.rcParams['text.latex.preamble'] = r'\usepackage{MinionPro}'
    mpl.rcParams['font.family'] = 'serif'
    mpl.rcParams['font.serif'] = 'MinionPro'

from rootpy.io import File
from rootpy.plotting.views import SumView, FunctorView, StyleView
import rootpy.root2matplotlib as rplt
import matplotlib.pyplot as plt

fig = plt.figure(dpi=150)
ax = plt.axes([0.125, 0.125, 0.845, 0.865])
fig.sca(ax)

files = [
    File('effs-el.root'),
    File('effs-mu.root'),
    ]

histnames = [
    'turnon-electron',
    'turnon-muon',
    ]

for f, histname in zip(files, histnames):
    turnon = f.Get('data_Hlt8')
    rplt.errorbar(turnon)
    plt.xlabel('$p_\mathrm{T} \cdot c$/GeV')
    plt.ylabel('$\epsilon_\mathrm{HLT}$')
    plt.xlim(xmin=0.)
    plt.ylim(ymin=0.80, ymax=1.0)
    fig.savefig(histname)
    plt.cla()
