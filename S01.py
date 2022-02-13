import matplotlib.pyplot as plt
import numpy as np


logw = []
ss=[]
ssd=[]
A=2
C = 0.716
R = 1
a = 1/(R*C)
ww=np.linspace(0.1,10,100)

for w in ww:
  t = np.linspace(0, 2 * np.pi / w, 100)
  s=A*(a*np.sin(w*t)-w*np.cos(w*t))/(w**2+a**2)
  sd=A*(a*w*np.cos(w*t)+w*w*np.sin(w*t))/(w**2+a**2)
  ss.append(max(s))
  ssd.append(max(sd))
  logw.append(np.log10(w))

fig,ax=plt.subplots()
ax.plot(logw,ss,logw,ssd)
plt.legend(['ss', 'ssd'])
plt.show()
plt.style.use('seaborn-pastel')
