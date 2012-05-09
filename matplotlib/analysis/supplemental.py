from rplt import *

f = File('supplemental.root')

samplenames = [
    'data',
    'wjets',
    'tt',
    'zz',
    'ww',
    'zg',
    'zjets',
    'wz',
    'WPrime600',
    ]

titles = [
    r'Data',
    r'$W/t\bar{t}$ + jets',
    r'$ZZ/WW/Z\gamma$',
    r'$Z$ + jets',
    r'$WZ$',
    r"$W'$ (600 GeV/$c^2$)",
    ]
linestyles = ['solid', 'dashed', 'dashdot', 'dotted'] * 3

histnames = [
    'jetPtFirst',
    'jetPtSecond',
    'hHT',
    ]

xlabels = [
    r'Leading Jet $E_\mathrm{T}$/GeV',
    r'Next-to-Leading Jet $E_\mathrm{T}$/GeV',
    r'$L_\mathrm{T} \cdot c$/GeV',
    ]

suffixes = ['2e', '2mu', '3e', '3mu', 'COMB']


for histname, xlabel in zip(histnames, xlabels):
    for suffix in suffixes:
        rebin = lambda x: x.Rebin(1)
        if histname.startswith('jetPt'):
            if suffix != 'COMB':
                continue
            rebin = lambda x: x.Rebin(5)
        if histname.startswith('hHT'):
            rebin = lambda x: x.Rebin(20)
        hists = [FunctorView(f, rebin).Get(
            '%s_%s_%s' % (histname, x, suffix)) for x in samplenames]
        hists = [hists[0], sum(hists[1:3]), sum(hists[3:6]), hists[6], hists[7], hists[8]]
        for i, h in enumerate(hists):
            h.SetTitle(titles[i])
            h.SetLineStyle(linestyles[i])
        for i, h in enumerate(hists[1:-1]):
            # h.SetFillColor(['#900','#090','#009',][i%3])
            # h.SetFillColor(str((i+1.)/len(hists)))
            h.SetFillColor(colors_tranquility[-i-1])
        hists[-1].SetFillStyle('hollow')
        log = False
        if histname.startswith('jetPt'):
            log = True
        rplt.hist(hists[1:-1], log=log)
        rplt.errorbar(hists[0], xerr=False, capsize=1)
        ax.yaxis.set_label_coords(-0.11, 0.5)
        if log:
            if plt.ylim()[0] < 1e-1:
                plt.ylim(ymin=1.e-1)
            plt.ylim(ymax=5.e4)
            # if plt.ylim()[1] < 1.5e3:
            #     plt.ylim(ymax=1.5e3)
        myxlabel = xlabel
        if histname.startswith('hHT'):
            plt.ylim(ymax=49)
            if suffix == '3e':
                myxlabel += r' $(W + Z \to e^\pm + \nu_e + e^+ + e^-)$'
            if suffix == '2e':
                myxlabel += r' $(W + Z \to \mu^\pm + \nu_\mu + e^+ + e^-)$'
            if suffix == '2mu':
                myxlabel += r' $(W + Z \to e^\pm + \nu_e + \mu^+ + \mu^-)$'
            if suffix == '3mu':
                myxlabel += r' $(W + Z \to \mu^\pm + \nu_\mu + \mu^+ + \mu^-)$'
        plt.legend()
        plt.xlabel(myxlabel)
        plt.ylabel('Events')
        plt.savefig('%s_%s' % (histname, suffix))
        plt.cla()
        plt.ylim((0., 1.))
