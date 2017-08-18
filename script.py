
class Nebenkostenabrechnung:

    ht = None
    nt = None
    wohndauerfaktor = None
    stromHtPrev = None
    stromHtNew = None
    stromNtPrev = None
    stromHtNew = None
    wasserPrev = None
    wasserNew = None
    stromverbrauch = None
    wasserverbrauch = None
    stromkostenfaktor = None
    leistungspreis = None
    verrechnungspreis = None
    mwSt = None
    mwStWasser = None

def wohndauer(tage):
    faktor = tage/365.0
    print faktor

def stromverbrauchHT(stromHtPrev, stromHtNew):
    stromverbrauchHt = new - prev
    print stromverbrauchHt

def stromverbrauchNT(stromNtPrev, stromNtNew):
    stromverbrauchNt = new - prev
    print stromverbrauchNt    

def wasserverbrauchWarm(wasserWarmPrev, wasserWarmNew):
    wasserverbrauchWarm = new - prev
    print wasserverbrauchWarm

def wasserverbrauchKalt(wasserKaltPrev, wasserKaltNew):
    wasserverbrauchKalt = new - prev
    print wasserverbrauchKalt

def stromkostenFaktor(parteiverbrauch, gesamtverbrauch):
    faktor = float(parteiverbrauch) / float(gesamtverbrauch)
    print faktor

def stromkostenBerechnung(ht, nt, stromkostenfaktor, stromverbrauchHt, stromverbrauchNt):