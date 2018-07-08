#!/usr/bin/python

# file: control/actions.py

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf fahcontrol_%s-1_all.deb" % (get.srcVERSION()))
    shelltools.system("tar xvf data.tar.xz")

def install():
    pisitools.insinto("/usr", "usr/bin")
    pisitools.insinto("/usr/lib/python2.7/site-packages",
                      "usr/lib/python2.7/dist-packages/fah")
    pisitools.insinto("/usr/lib/python2.7/site-packages",
                      "usr/lib/python2.7/dist-packages/FAHControl-0.0.0.egg-info")
    pisitools.insinto("/usr", "usr/share")
