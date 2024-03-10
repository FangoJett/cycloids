import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
xs = 5
ys = 5
r1 = 2
r2 = 1
t = 361 
pulse = np.pi/180
circle1 = plt.Circle((xs, ys), r1, color='r', fill=False)
  
fig, ax = plt.subplots()
ax.cla() # clear things for fresh plot
ax.add_patch(circle1) 
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))


#radius that "rotates" outside circle
xlist = [(r1*np.cos(kat*pulse)+xs) for kat in range (0,t,1)]
ylist = [(r1*np.sin(kat*pulse)+ys) for kat in range(0,t,1)]


#centers of outside circle
xslist = [((r1+r2)*np.cos(kat*pulse)+xs) for kat in range (0,t,1)]
yslist = [((r1+r2)*np.sin(kat*pulse)+ys) for kat in range(0,t,1)]

line = ax.plot([xs,xlist[0]], [ys,ylist[0]])[0]
circle2= plt.Circle((xslist[0], yslist[0]), r2, color='r', fill=False)
ax.add_patch(circle2)


#final result/drawing radius
ilo = (r1+r2)/r2
xlist2 = [((r2)*-np.cos(ilo*kat*pulse)+xslist[kat]) for kat in range(0, t, 1)]
ylist2 = [((r2)*-np.sin(ilo*kat*pulse)+yslist[kat]) for kat in range(0, t, 1)]

line2 = ax.plot([xslist[0],xlist[0]], [yslist[0],ylist[0]])[0]

hipo = ax.plot(xlist2[0],ylist2[0])[0]


def update(frame):
    circle2.set(center = (xslist[frame],yslist[frame]))
    
    x = [xs,xlist[frame]]
    y = [ys,ylist[frame]]
    x2 = [xslist[frame],xlist2[frame]]
    y2 = [yslist[frame],ylist2[frame]]
    xhipo = xlist2[:frame+1]    #+1 so it doesnt look delayed
    yhipo = ylist2[:frame+1]
    # update lines plot:
    line.set_xdata(x)
    line.set_ydata(y)
    line2.set_xdata(x2)
    line2.set_ydata(y2)
    hipo.set_xdata(xhipo)
    hipo.set_ydata  (yhipo)
    return line,line2,hipo 


          
ani = animation.FuncAnimation(fig=fig, func=update, frames=t-1, interval=10)
plt.show()
