from rplt import *

datafiles = [
    'DataTreeTrilepton-DoubleElectron-Run2011A-05Aug2011-v1.root',
    'DataTreeTrilepton-DoubleElectron-Run2011A-May10ReReco-v1.root',
    'DataTreeTrilepton-DoubleElectron-Run2011A-PromptReco-v4.root',
    'DataTreeTrilepton-DoubleElectron-Run2011A-PromptReco-v6.root',
    'DataTreeTrilepton-DoubleElectron-Run2011B-PromptReco-v1.root',
    'DataTreeTrilepton-DoubleMu-Run2011A-05Aug2011-v1.root',
    'DataTreeTrilepton-DoubleMu-Run2011A-May10ReReco-v1.root',
    'DataTreeTrilepton-DoubleMu-Run2011A-PromptReco-v4.root',
    'DataTreeTrilepton-DoubleMu-Run2011A-PromptReco-v6.root',
    ]
datadirs = [File(x) for x in datafiles]
data = SumView(datadirs)

lumi = 4700.

zzdirs = [
    ScaleView(File('ZZTo2e2mu_7TeV-powheg-pythia6.root'), lumi * 0.0308 / 499917.0),
    ScaleView(File('ZZTo2e2tau_7TeV-powheg-pythia6.root'), lumi * 0.0308 / 484063.0),
    ScaleView(File('ZZTo2mu2tau_7TeV-powheg-pythia6.root'), lumi * 0.0308 / 486266.0),
    ScaleView(File('ZZTo4e_7TeV-powheg-pythia6.root'), lumi * 0.0154 / 499929.0),
    ScaleView(File('ZZTo4mu_7TeV-powheg-pythia6.root'), lumi * 0.0154 / 499918.0),
    ScaleView(File('ZZTo4tau_7TeV-powheg-pythia6.root'), lumi * 0.0154 /473838.0),
    ]
zz = SumView(zzdirs)

zjets = ScaleView(File('DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola.root'), lumi * 3050 / 36209629.0)
gv = ScaleView(File('GVJets_7TeV-madgraph.root'), lumi * 173 / 1067879.0)
#tt = ScaleView(File('TTJets_TuneZ2_7TeV-madgraph-tauola.root'), lumi * 158. / 50098875.0)
#wjets = ScaleView(File('WJetsToLNu_TuneZ2_7TeV-madgraph-tauola.root'), lumi * 31300 / 68447497.0)
ww = ScaleView(File('WWJetsTo2L2Nu_TuneZ2_7TeV-madgraph-tauola.root'), lumi * 4.89 / 1197558.0)
wz = ScaleView(File('WZJetsTo3LNu_TuneZ2_7TeV-madgraph-tauola.root'), lumi * .879 / 1221134.0)
vv = SumView(zz, ww)

wzscale = args.wz

titles = [
    r'Data',
    r'$WZ \times\,%i$' % wzscale,
    r'$Z$ + jets',
    r'$ZZ + WW$',
    r'$t\bar{t}$ + jets',
    ]
linestyles = ['solid', 'dashed', 'dashdot', 'dotted'] * 3
linestyles = ['solid'] * 20

colors_tranquility = [
    (182,193,177),
    (152,186,174),
    (32,199,191),
    (50,134,135),
    (100,81,104),
    ]
# mcdirs = [tt, vv, zjets, wz]
mcdirs = [wz]
for i, d in enumerate(mcdirs):
    # mcdirs[i] = StyleView(d, markercolor=colors_tranquility[i], fillcolor=None)
    mcdirs[i] = StyleView(d, fillcolor=colors_tranquility[i])
    mcdirs[i] = ScaleView(mcdirs[i], wzscale)
# data = NormalizeView(data)
dirs = [data] + mcdirs


histnames = [
    'hb_pt',
    'hb_sieie',
    'hb_detain',
    'hb_dphiin',
    'hb_nmiss',
    'hb_dist',
    'hb_dcot',
    'hb_iso',
    'he_pt',
    'he_sieie',
    'he_detain',
    'he_dphiin',
    'he_nmiss',
    'he_dist',
    'he_dcot',
    'he_iso',
    'hm_pt',
    'hm_npix',
    'hm_ntrk',
    'hm_nmuo',
    'hm_nseg',
    'hm_chi2',
    'hm_d0',
    'hm_iso',
]

xlabels = [
    r'Muon pt/GeV',
    r'Muon Chi2',
    ] * 20

replacements = [
    ('dist', r'Conversion Distance $d$/cm'),
    ('dcot', r'$\Delta\cot{(\theta)}$'),
    ('dphiin', r'$\Delta\phi_\mathrm{in}$'),
    ('detain', r'$\Delta\eta_\mathrm{in}$'),
    ('iso', r'$R_\mathrm{iso}$'),
    ('pT', r'$p_\mathrm{T}$/GeV'),
    ('sieie', r'$\sigma_{i\eta i\eta}$'),
    ('chi2', r'Normalized $\chi^2$'),
    ('d0', r'$d_0$'),
    ('nmiss', r'Number of Missing Hits'),
    ('nmuo', r'$N$ Muon System Hits'),
    ('npix', r'$N$ Pixel Tracker Hits'),
    ('ntrk', r'$N$ Tracker System Hits'),
    ('nseg', r'$N$ Matched Muon Segments'),
    ]

def myrep(string):
    for args in replacements:
        string = string.replace(args[0], args[1])
    return string

def exclude(histname, minmax, *args):
    if len(args) == 4:
        if 'hb' in histname:
            args = args[0::2]
        else:
            args = args[1::2]
    for bound in args:
        if bound is None:
            continue
        if minmax == 'min':
            plt.axvspan(0., bound, linewidth=0., facecolor='k', alpha=0.15)
            plt.axvspan(-bound, 0, linewidth=0., facecolor='k', alpha=0.15)
        else:
            plt.axvspan(bound, 3000., linewidth=0., facecolor='k', alpha=0.15)
            plt.axvspan(-3000, -bound, linewidth=0., facecolor='k', alpha=0.15)

def intticks(numticks):
    plt.xticks([x + 0.5 for x in range(numticks)], range(numticks))

for histname, xlabel in zip(histnames, xlabels):
    hists = [d.Get(histname) for d in dirs]
    for i, h in enumerate(hists):
        h.SetTitle(titles[i])
        h.SetLineStyle(linestyles[i])
    for i, h in enumerate(hists[1:]):
        # h.SetFillColor(['#900','#090','#009',][i%3])
        # h.SetFillColor(str((i+1.)/len(hists)))
        h.SetFillColor(colors_tranquility[i])
    if True:
        # hists[-1].SetFillStyle('hollow')
        hists[1].SetMarkerColor((100,81,104))
        hists[1].SetMarkerStyle('square')
        # rplt.bar(hists[1], linewidth=0, log=True)
        # rplt.errorbar(hists[1], xerr=False, capsize=1)
        rplt.hist(hists[1:], reverse=True)
        rplt.errorbar(hists[0], xerr=False, capsize=1)
        ax.yaxis.set_label_coords(-0.11, 0.5)
        plt.ylim(ymin=0.01)
        plt.legend()
        xlabel = myrep(hists[0].GetXaxis().GetTitle())
        if histname.startswith('he'):
            xlabel = 'Endcap ' + xlabel
        if histname.startswith('hb'):
            xlabel = 'Barrel ' + xlabel
        plt.xlabel(xlabel)
        plt.ylabel('Events')
        if 'sieie' in histname:
            exclude(histname, 'max', 0.012, 0.031, 0.010, 0.031)
        if '_pt' in histname:
            exclude(histname, 'min', 10., 20.)
        if 'dphiin' in histname:
            exclude(histname, 'max', 0.800, 0.700, 0.027, 0.021)
        if 'detain' in histname:
            exclude(histname, 'max', 0.007, 0.011, 0.005, 0.006)
            plt.xlim(-0.01,0.01)
        if 'nmiss' in histname:
            exclude(histname, 'max', 1, 1)
            plt.xlim(0,6)
            intticks(6)
        if 'dist' in histname:
            exclude(histname, 'min', None, None, 0.02, 0.02)
        if 'dcot' in histname:
            exclude(histname, 'min', None, None, 0.02, 0.02)
        if 'iso' in histname:
            if histname.startswith('hm'):
                exclude(histname, 'max', 0.15, 0.1)
            else:
                exclude(histname, 'max', 0.15, 0.10, 0.07, 0.06)
        if 'd0' in histname:
            exclude(histname, 'max', 0.2)
        if 'chi2' in histname:
            exclude(histname, 'max', 10.)
        if histname == 'hm_npix':
            exclude(histname, 'min', 1)
            intticks(8)
        if histname == 'hm_ntrk':
            exclude(histname, 'min', 11)
        if histname == 'hm_nmuo':
            exclude(histname, 'min', 1)
        if histname == 'hm_nseg':
            exclude(histname, 'min', 2)
            intticks(5)
            # plt.axvspan(0.010, 1., linewidth=0., facecolor='k', alpha=0.15)
            # plt.axvspan(0.012, 1., linewidth=0., facecolor='k', alpha=0.15)
        # for label in plt.gca().get_xaxis().get_ticklabels():
        #     label.set_verticalalignment('baseline')
        # for label in plt.gca().get_yaxis().get_ticklabels():
        #     label.set_verticalalignment('baseline')
        # # # rplt.col(hists[0])
        # plt.ylim(ymin=0.01)
        plt.savefig(histname)
        plt.cla()
        plt.ylim((0,1))
