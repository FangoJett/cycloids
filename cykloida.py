import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#cente of circle
xs = 0
ys1 = 0
#radius
r = 10
ys = r +ys1
#simulation time
t = 200
pulse = np.pi/180

circle1 = plt.Circle((xs, ys), r, color='r', fill=False)
  
fig, ax = plt.subplots()
plt.figure(fig).set_figwidth(13)
ax.cla() 
ax.add_patch(circle1) 
ax.set_xlim((0, 20*r))
#ax.set_ylim((0, 10))


#Not using pulse here for scaling purpouses
scl = 0.1
#xlist2 = [(r*(scl*kat-np.sin(scl*kat))+xs) for kat in range(0, t, 1)]
#ylist2 = [(r*(1-np.cos(scl*kat))+ys-r) for kat in range(0, t, 1)]

xlist2 = [(kat-r*np.sin(kat/r)) for kat in range(0, t, 1)]
ylist2 = [(r-r*np.cos(kat/r)) for kat in range(0, t, 1)]
# cykl -> final result
cykl = ax.plot(xlist2[0],xlist2[0])[0]
# list2 -> drawing radius
list2 = ax.plot([xs,xlist2[0]],[ys,ylist2[0]])[0]

def update(frame):
    xcenter = xs+(scl*frame)*r 
    xl = [xcenter,xlist2[frame]]
    yl = [ys,ylist2[frame]]
    xc = xlist2[:frame+1]       #adding 1 so cykloid doesnt look delayed
    yc = ylist2[:frame+1]
    cykl.set_xdata(xc)
    cykl.set_ydata  (yc)
    list2.set_xdata(xl)
    list2.set_ydata(yl)
    circle1.set(center = (xcenter,ys))
    return cykl,list2


          
ani = animation.FuncAnimation(fig=fig, func=update, frames=t-1, interval=10)
plt.show()
