import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#parameters
start = -2
end = -1.092
r = 1
t=1000          
#-------------------


funcc = input("Give function:")
start = float(input("Give bottom x:"))
end = float(input("Give upper x:"))
r = float(input("Give radius:"))


#fun definition
def funkcja(x):
    #return ((x*x-x*x*x/10+np.exp(x)))
    #return(x*x*x/4+2)
    #return (x)
    #return(x-np.sin(x))
    #return (14 * x * np.exp(-8 * x)) / ((10**6) * (4 * x + 13 * np.exp(x)))
    return eval(funcc)

def gradient_fun(y,x):          #gradient fun
    dy_dx = np.gradient(y, x)
    return dy_dx

def circle_mid(x0,y0,m):            #calculating positions of circles
    alpha = np.arctan(m)                
    xs = x0 - np.sin(alpha)*r           
    ys = y0 + np.cos(alpha)*r
    return xs,ys




x_values = np.linspace(start,end, t)  
y_values = funkcja(x_values)           
grad = gradient_fun(y_values,x_values)  

odl = 0          
ilo = [0]
for i in range(1,t):            #calculating lenght of line
    xdiff = x_values[i]-x_values[i-1]
    ydiff = y_values[i]- y_values[i-1]      
    odl = odl + np.sqrt(xdiff*xdiff+ydiff*ydiff)
    ilo.append(odl)                 
  



xs1,ys1 = circle_mid(x_values,y_values,grad)   
xlist2 = [(x_values[j]-((r*grad[j])/(np.sqrt(1+grad[j]*grad[j])))+r*np.sin((-ilo[j]/r)+np.arctan(grad[i]))) for j in range(0, t, 1)]
ylist2 = [(y_values[j]+((r)/(np.sqrt(1+grad[j]*grad[j])))-r*np.cos((-ilo[j]/r)+np.arctan(grad[i]))) for j in range(0, t, 1)]




circle1t = plt.Circle((circle_mid(x_values[0],y_values[0],grad[0])), r, color='b', fill=False)

fig, ax = plt.subplots()
ax.axis('equal')
ax.add_patch(circle1t)
#ax.set_aspect('equal', adjustable='datalim')
ax.plot(xlist2,ylist2)
ax.plot(x_values,y_values)



line = ax.plot([xs1[0],xlist2[0]], [ys1[0],ylist2[0]])[0]
line_circ = ax.plot([xs1[0],x_values[0]], [ys1[0],y_values[0]])[0]      

#line_c = ax.plot(xlist2[0],ylist2[0])[0]

def update(frame):    
    #print(ani.event_source.interval)
    circle1t.set(center = circle_mid(x_values[frame],y_values[frame],grad[frame]))
    x12 = [xs1[frame],xlist2[frame]]
    y12 = [ys1[frame],ylist2[frame]]
    xcc = [xs1[frame],x_values[frame]]
    ycc = [ys1[frame],y_values[frame]]
    line.set_xdata(x12)
    line.set_ydata(y12)
    line_circ.set_xdata(xcc)
    line_circ.set_ydata(ycc)
    return line, line_circ


          
ani = animation.FuncAnimation(fig=fig, func=update, frames=len(x_values), interval=1)
plt.show()