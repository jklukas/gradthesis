from rplt import *

f = File('histograms.root')
h = f.Get('pileup')
h.SetFillColor(colors_tranquility[0])
rplt.hist(h)
plt.xlabel('Reconstructed Collision Vertex Multiplicity')
plt.ylabel('Events')
plt.savefig('pileup')
sys.exit(0)
