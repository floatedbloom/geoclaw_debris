
"""
Module to create topo and qinit data files for this example.
"""

from clawpack.geoclaw import topotools
from pylab import *

def maketopo_block():

    x1b = -1.
    x2b = 1.
    y1b = -1.
    y2b = 1.
    zb = 2.0  # height of block
    x = linspace(x1b-0.1, x2b+0.1, 101)
    y = linspace(y1b-0.1, y2b+0.1, 101)
    X,Y = meshgrid(x,y)
    Z = where(logical_and(logical_and(X>=x1b, X<=x2b),
                          logical_and(Y>=y1b, Y<=y2b)),  zb, 0.)
    Z = Z - 1.
    
    topo = topotools.Topography()
    topo.set_xyZ(x,y,Z.T)
    
    topo.write('block.tt3', Z_format='%.3f', topo_type=3)


def maketopo_pwlinear():
    """
    Output topography file for the entire domain
    """
    nxpoints = 501
    nypoints = 5
    xlower = -10.e0
    xupper = 10.e0
    ylower = -3.e0
    yupper = 3.e0
    outfile= "wavetank.tt3"     
    topotools.topo3writer(outfile,topo_pwlinear,xlower,xupper,ylower,yupper,nxpoints,nypoints)

def topo_pwlinear(x,y):
    """
    piecewise linear
    """
    
    if 1:
        # flat bottom
        z = -1. * ones(x.shape)
    else:
        # piecewise linear
        z = zeros(x.shape)
        z = where(x<10., z, (x-10)/15.)
        z = where(x<17.5, z, 0.5 + (x-17.5)/30.)
        z = where(x<32.5, z, 1.0) 
        z = z - 0.9056  # adjust so sea level at 0
    return z


if __name__=='__main__':
    maketopo_block()
    maketopo_pwlinear()
