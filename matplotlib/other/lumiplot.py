import matplotlib as mpl
mpl.use('PDF')
import matplotlib.pyplot as plt
import matplotlib.dates as mpldates
import numpy as np

mpl.rcParams['figure.figsize'] = (8, 5)
mpl.rcParams['font.size'] = 20
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['xtick.major.pad'] = mpl.rcParams['font.size'] / 4
mpl.rcParams['ytick.major.pad'] = mpl.rcParams['font.size'] / 4
if True:
    mpl.rcParams['text.usetex'] = True
    mpl.rcParams['text.latex.preamble'] = r'\usepackage{MinionPro}'
    mpl.rcParams['font.family'] = 'serif'
    mpl.rcParams['font.serif'] = 'MinionPro'

from matplotlib.mlab import csv2rec
from datetime import datetime

rarray = csv2rec('lumivstime.csv')
def mytime(dt):
    return datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f')

fig = plt.figure()
ax = plt.gca()
delivered = [x[3] for x in rarray]
for i in range(len(delivered)):
    delivered[i] /= 1.e9
    if not i: continue
    delivered[i] += delivered[i - 1]
recorded = [x[4] for x in rarray]
for i in range(len(recorded)):
    recorded[i] /= 1.e9
    if not i: continue
    recorded[i] += recorded[i - 1]
plt.plot_date([mytime(x[1]) for x in rarray], delivered, 'r-', label='Delivered')
plt.plot_date([mytime(x[1]) for x in rarray], recorded, 'b-', label='Recorded')
ax.xaxis.set_major_formatter(mpldates.DateFormatter('%b 1'))
plt.legend(loc='upper left')
plt.ylabel('Integrated Luminosity / fb$^{-1}$')
plt.savefig('lumivstime', transparent=True)
