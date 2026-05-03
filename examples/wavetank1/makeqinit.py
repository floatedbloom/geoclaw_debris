from clawpack.geoclaw.topotools import Topography
from numpy import * 

def makeqinit():
    """
    Create qinit data file
    """
    nxpoints = 121
    nypoints = 5
    xlower = -10.e0
    xupper = -2.e0
    ylower = -3.e0
    yupper = 3.e0
    outfile= "qinit.xyz"

    topography = Topography(topo_func=qinit)
    topography.x = linspace(xlower,xupper,nxpoints)
    topography.y = linspace(ylower,yupper,nypoints)
    topography.write(outfile, topo_type=1)

def qinit(x,y):
    """
    Jump discontinuity
    """
    from numpy import where
    z = where(x < -3., 1., 0.)
    return z
    
if __name__=='__main__':
    makeqinit()
