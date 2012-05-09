# Instructions

These plots compare data to WZ Monte Carlo, with the WZ scaled up by some factor.  Sometimes, a factor of 10 looks better, sometimes 100, so I create both.  I put them in subfolders scale10 and scale100:

    python makeplots.py --usetex --wz=10
    mkdir scale10
    mv *.pdf scale10/

I ended up making these particular figures as pngs because they fill up whole pages of the document.  If they are kept as pdfs, issues arise with printer timeouts.

