## This file gets imported by the other python scripts that build files

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--usetex', action='store_true')
parser.add_argument('--png', action='store_true')
parser.add_argument('--wz', type=int, default=10)
args = parser.parse_args()

import matplotlib as mpl
if args.png:
    mpl.use('AGG')
else:
    mpl.use('PDF')
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
from rootpy.plotting.views import SumView, FunctorView, StyleView, ScaleView
import rootpy.root2matplotlib as rplt
import matplotlib.pyplot as plt

colors_tranquility = [
    (182,193,177),
    (152,186,174),
    (32,199,191),
    (50,134,135),
    (100,81,104),
    ]

fig = plt.figure(dpi=150)
ax = plt.axes([0.125, 0.125, 0.845, 0.865])
fig.sca(ax)
