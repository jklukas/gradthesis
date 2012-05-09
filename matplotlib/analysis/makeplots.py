from rplt import *

class Source(object):
    def __init__(self, title, obj):
        self.obj = obj
        self.title = title
    def __getattr__(self, attr):
        return getattr(self.obj, attr)


class Target(object):
    def __init__(self, name, xlabel, log=True):
        self.name = name
        self.xlabel = xlabel
        self.log = log


f = File('histograms.root')

sources = [
    Source('Data', f.GetDirectory('data')),
    Source(r'$W/t\bar{t}$ + jets',
           SumView(f.GetDirectory('WJetsToLNu'), f.GetDirectory('TTJets'))),
    Source(r'$ZZ/WW/Z\gamma$',
           SumView(f.GetDirectory('ZZ'), f.GetDirectory('WWTo2L2Nu'),
                   f.GetDirectory('GVJets'))),
    Source(r'$Z$ + jets', f.GetDirectory('DYJetsToLL')),
    Source(r'$WZ$', f.GetDirectory('WZJetsTo3LNu')),
    Source(r"$W'$ (600 GeV/$c^2$)", f.GetDirectory('WprimeToWZTo3LNu_M-600')),
    ]

# dirs = [
#     f.GetDirectory('data'),
#     SumView(f.GetDirectory('WJetsToLNu'), f.GetDirectory('TTJets')),
#     SumView(f.GetDirectory('ZZ'), f.GetDirectory('WWTo2L2Nu'),
#             f.GetDirectory('GVJets')),
#     f.GetDirectory('DYJetsToLL'),
#     f.GetDirectory('WZJetsTo3LNu'),
#     f.GetDirectory('WprimeToWZTo3LNu_M-600'),
#     ]

linestyles = ['solid', 'dashed', 'dashdot', 'dotted'] * 3

targets = [
    Target('hHt_ValidWZCand',     r'$L_\mathrm{T} \cdot c$/GeV', log=False),
    Target('hWZMass_ValidWZCand', r'$M(WZ) \cdot c^2$/GeV',      log=False),
    Target('hMET_ValidW',         r'$E_\mathrm{T}^\mathrm{miss}$/GeV'),
    Target('hZMass_ValidW',       r'$M(Z) \cdot c^2$/GeV'),
    Target('hWTransMass_ValidW',  r'$M_\mathrm{T}(W) \cdot c^2$/GeV'),
    Target('hDiscriminantAngle',  r'$\tan^{-1}(\mathrm{Im}(p_z^\nu)/\mathrm{Re}(p_z^\nu))$'),
    Target('hNJets_ValidZ',       r'Jet Multiplicity'),
    Target('hNJets_ValidWZCand',  r'Jet Multiplicity'),
    Target('hNJets_Ht',           r'Jet Multiplicity'),
    Target('hZMass_ValidZ',       r'$M(Z)c^2$/GeV'),
    Target('hZMass_ValidWZCand',  r'$M(Z)c^2$/GeV'),
    Target('hZMass_Ht',           r'$M(Z)c^2$/GeV'),
    Target('hZpt_ValidZ',         r'$p_\mathrm{T}(Z)c$/GeV'),
    Target('hZpt_ValidWZCand',    r'$p_\mathrm{T}(Z)c$/GeV'),
    Target('hZpt_Ht',             r'$p_\mathrm{T}(Z)c$/GeV'),
    Target('hWTransMass_ValidW',  r'$M_\mathrm{T}(W)c^2$/GeV'),
    Target('hWTransMass_ValidWZCand',  r'$M_\mathrm{T}(W)c^2$/GeV'),
    Target('hWTransMass_Ht',           r'$M_\mathrm{T}(W)c^2$/GeV'),
    Target('hWZ3e0muMass_ValidWZCand', r'$M(WZ \to e^\pm + \nu_e + e^+ + e^-)$/(GeV/$c^2$)'),
    Target('hWZ2e1muMass_ValidWZCand', r'$M(WZ \to \mu^\pm + \nu_\mu + e^+ + e^-)$/(GeV/$c^2$)'),
    Target('hWZ1e2muMass_ValidWZCand', r'$M(WZ \to e^\pm + \nu_e + \mu^+ + \mu^-)$/(GeV/$c^2$)'),
    Target('hWZ0e3muMass_ValidWZCand', r'$M(WZ \to \mu^\pm + \nu_\mu + \mu^+ + \mu^-)$/(GeV/$c^2$)'),
    ]

def intticks(numticks):
    plt.xticks([x + 0.5 for x in range(numticks)], range(numticks))

for target in targets:
    histname, xlabel = target.name, target.xlabel
    rebin = lambda x: x.Rebin(1)
    if histname.startswith('hWZ'):
        rebin = lambda x: x.Rebin(5)
    if histname.startswith('hWTransMass'):
        rebin = lambda x: x.Rebin(2)
    hists = [FunctorView(source, rebin).Get(histname) for source in sources]
    for i, h in enumerate(hists):
        h.SetTitle(sources[i].title)
        h.SetLineStyle(linestyles[i])
    for i, h in enumerate(hists[1:-1]):
        h.SetFillColor(colors_tranquility[-i-1])
    hists[-1].SetFillStyle('hollow')
    if target.log:
        hists = hists[:-1]
    rplt.hist(hists[1:], log=target.log)
    rplt.errorbar(hists[0], xerr=False, capsize=1)
    ax.yaxis.set_label_coords(-0.11, 0.5)
    if target.log:
        if plt.ylim()[0] < 1e-2:
            plt.ylim(ymin=1.e-2)
        if plt.ylim()[1] < 1.5e3:
            plt.ylim(ymax=1.5e3)
    if histname.startswith('hNJets'):
        intticks(15)
    if histname.startswith('hWZ'):
        plt.xlim(xmax=1500)
    if histname.startswith('hZpt'):
        plt.xlim(xmax=650)
    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel('Events')
    plt.savefig(histname)
    plt.cla()
    plt.ylim((0., 1.))
