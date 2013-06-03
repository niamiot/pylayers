# -*- coding: utf-8 -*-

from pylayers.simul.simulem import *
from pylayers.antprop.rays import *
from pylayers.antprop.channel import *
from pylayers.antprop.signature import *
import pylayers.util.pyutil as pyu
from pylayers.gis.layout import *
import pylayers.signal.bsignal as bs
import pylayers.signal.waveform as wvf
from datetime import datetime
import time
import ConfigParser
import pickle
def showr2d(L,r2d,tx,rx):
    """
    r2d['pt'] : nd,ni,nr
    """
    L.display['thin']=False
    col = ['r','b','g','c','m','k','y']
    fig,ax = L.showG('')
    for k in r2d:
        r = r2d[k]
        pts = r['pt']
        sh = np.shape(pts)
        for r in range(sh[2]):
            x = np.hstack((tx[0],pts[0,:,r],rx[0]))
            y = np.hstack((tx[1],pts[1,:,r],rx[1]))
            plt.plot(x,y,col[eval(k)])

def showr(L,r2d,tx,rx,k,l,color='b'):
    """
    r2d['pt'] : nd,ni,nr
    """
    L.display['thin']=False
    fig,ax = L.showG('')
    r = r2d[str(k)]
    pts = r['pt']
    sh = np.shape(pts)
    x = np.hstack((tx[0],pts[0,:,l],rx[0]))
    y = np.hstack((tx[1],pts[1,:,l],rx[1]))
    plt.plot(x,y,color=color)




S = Simul()
filestr = 'WHERE1'
#S.layout(filestr+'.ini','matDB.ini','slabDB.ini')
S.L.loadini(filestr+'.ini')
S.L.dumpr()

Ctx= 78
Crx=34
#if not os.path.exists('r2d.pickle'):
Si = Signatures(S.L,Ctx,Crx)
Si.run3(cutoff=2)
#r2d = Si.rays(tx,rx)
#file=open("r2d.pickle","w")
#pickle.dump(r2d,file)
#file.close()
##else:
##    file = open("r2d.pickle","r")
##    r2d = pickle.load(file)
#r3d = r2d.to3D()
#r3d.locbas(S.L)
#r3d.fillinter(S.L)

#config = ConfigParser.ConfigParser()
#_filesimul = 'default.ini'
#filesimul = pyu.getlong(_filesimul, "ini")
#config.read(filesimul)
#fGHz = np.linspace(eval(config.get("frequency", "fghzmin")), 
#                     eval(config.get("frequency", "fghzmax")), 
#                     eval(config.get("frequency", "nf")))

#Cn=r3d.eval(fGHz)
#Cn.freq=Cn.fGHz
#sco=Cn.prop2tran(a='theta',b='theta')
#wav = wvf.Waveform()
#ciro = sco.applywavB(wav.sfg)

#raynumber = 4

#fig=plt.figure('Cpp')
#f,ax=Cn.Cpp.plot(fig=fig,iy=np.array(([raynumber])))

#r3d.info(raynumber)
# plt.show()

#=======


#
#c11 = r3d.Ctilde[:,:,0,0]
#c12 = r3d.Ctilde[:,:,0,1]
#c21 = r3d.Ctilde[:,:,1,0]
#c22 = r3d.Ctilde[:,:,1,1]
#
#
#
#Cn=Ctilde()
#Cn.Cpp = bs.FUsignal(r3d.I.f, c11)
#Cn.Ctp = bs.FUsignal(r3d.I.f, c12)
#Cn.Cpt = bs.FUsignal(r3d.I.f, c21)
#Cn.Ctt = bs.FUsignal(r3d.I.f, c22)
#Cn.nfreq = r3d.I.nf
#Cn.nray = r3d.nray
#Cn.tauk=r3d.delays
#
#raynumber = 4
#
#fig=plt.figure('Cpp')
#f,ax=Cn.Cpp.plot(fig=fig,iy=np.array(([raynumber])))
#

