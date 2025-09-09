# import SciPy modules
import matplotlib.pyplot as plt

import spicepy.netlist as ntl
from spicepy.netsolve import net_solve

plt.ion()


# read netlist
net = ntl.Network("ac_band_pass_filter.net")

# compute the circuit solution
net_solve(net)

# plot bode diagrams
net.bode()
