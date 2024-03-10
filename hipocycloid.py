import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
xs = 5
ys = 5
r1 = 5
r2 = 1
t = 361 

circle1 = plt.Circle((xs, ys), r1, color='b', fill=False)
  
fig, ax = plt.subplots()
ax.cla() # clear things for fresh plot
ax.add_patch(circle1) 
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))



xlist = [((r1-2*r2)*np.cos(kat*np.pi/180)+xs) for kat in range (0,t,1)]
ylist = [((r1-2*r2)*np.sin(kat*np.pi/180)+ys) for kat in range(0,t,1)]



xslist = [((r1-r2)*np.cos(kat*np.pi/180)+xs) for kat in range (0,t,1)]
yslist = [((r1-r2)*np.sin(kat*np.pi/180)+ys) for kat in range(0,t,1)]

line = ax.plot([xs,xlist[0]], [ys,ylist[0]])[0]
circle2= plt.Circle((xslist[0], yslist[0]), r2, color='r', fill=False)
ax.add_patch(circle2)


ilo = (r1-r2)/r2
xlist2 = [((r2)*+np.cos(ilo*kat*np.pi/180)+xslist[kat]) for kat in range(0, t, 1)]
ylist2 = [((r2)*-np.sin(ilo*kat*np.pi/180)+yslist[kat]) for kat in range(0, t, 1)]

line2 = ax.plot([xslist[0],xlist[0]], [yslist[0],ylist[0]])[0]

epi = ax.plot(xlist2[0],ylist2[0])[0]


def update(frame):
    circle2.set(center = (xslist[frame],yslist[frame]))
    x = [xs,xlist[frame]]
    y = [ys,ylist[frame]]
    x2 = [xslist[frame],xlist2[frame]]
    y2 = [yslist[frame],ylist2[frame]]
    xepi = xlist2[:frame+1]     #+1 so it doesnt look delayed
    yepi = ylist2[:frame+1]
    # update the line plot:
    line.set_xdata(x)
    line.set_ydata(y)
    line2.set_xdata(x2)
    line2.set_ydata(y2)
    epi.set_xdata(xepi)
    epi.set_ydata  (yepi)
    return line,line2,epi


          
ani = animation.FuncAnimation(fig=fig, func=update, frames=t-1, interval=1)
plt.show()
















