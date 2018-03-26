from matplotlib import pyplot as plt
import numpy as np

data = np.loadtxt("data/lampada.dat").T
fig = plt.figure(dpi=100)
ax = fig.add_subplot(1,1,1)
ax.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
#ax.scatter(data[0],data[1], label="Corrente")
ax.plot(data[0],data[1])
#ax.scatter(-1,-1, label="Resistência")
#ax.legend(loc=0)
ax.set_title("Lâmpada incandescente")
ax.set_xlabel('Tensão aplicada (V)')
ax.set_ylabel('Corrente (A)')
ax.axis([0,data[0][-1],0,data[1][-1]+data[1][-1]*0.05])
ax2=ax.twinx()
#ax2.scatter(data[0],data[0]/data[1],c='orange')
ax2.plot(data[0],data[0]/data[1],c='orange')
a = data[0]/data[1]
ax2.axis([0,data[0][-1],0,a[-1]+a[-1]*0.05])
ax2.set_ylabel("Resistência ($\Omega$)")
#ax.legend('Corrente')
#ax2.legend('Resistência')
