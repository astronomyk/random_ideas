import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter


def austrian_tax_rate():
    # in 1000s of €
    mon_netto = np.array([1.0,   1.2,  1.4,  1.7,  2.0,  2.4, 2.7,    3.,   4.,   5.,   8.,  12.])
    mon_brutt = np.array([1.18, 1.47,  1.8,  2.4,  3.0,  3.8, 4.4,    5.,  6.9,  8.8, 14.8,  23.])
    netto     = np.array([13.9, 16.8, 19.7, 24.2, 28.7, 34.7, 39.3, 43.9, 59.3,  75., 121., 181.])
    brutto    = np.array([16.5, 20.5, 25.5, 33.7, 41.6, 53.1, 61.9, 70.7, 96.7, 124., 208., 320.])

    x = np.logspace(3, 4, 50)
    y = np.interp(x, mon_netto*1E3, 1-netto/brutto) * 100
    yb = np.interp(x, mon_netto*1E3, 1-mon_netto/mon_brutt) * 100

    plt.figure(figsize=(8, 6))

    plt.plot(x, y, label="ink. 13./14. Gehälte")
    plt.plot(x, yb, label="exk. 13./14. Gehälte")
    plt.text(1030, 2, "Quelle: https://onlinerechner.haude.at/bmf/brutto-netto-rechner.html")

    plt.semilogx()
    plt.xlim(1E3, 1E4)
    plt.ylim(0, 50)
    plt.legend(loc=2)

    ax = plt.gca()
    ax.set_xticklabels(labels=ax.get_xticklabels(), rotation=30)
    plt.setp(ax.xaxis.get_minorticklabels(), rotation=30)
    ax.xaxis.set_major_formatter(ScalarFormatter())
    ax.xaxis.set_minor_formatter(ScalarFormatter())

    plt.xlabel("Monatliches Nettogehalt (€)")
    plt.ylabel("Effektive Steuerrate (%) in Österreich")

    plt.grid(True)
    plt.grid(True, which="minor")
    plt.savefig("Austrian_tax_rate.png")


austrian_tax_rate()
