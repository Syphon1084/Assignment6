# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 09:31:57 2026

@author: emmba
"""
import numpy as np
import matplotlib.pyplot as pp

#Part A: Gradient Maping

T0=100
sigma=1
dx=0.1
dy=0.1
x=np.arange(-3,3+dx,dx)
y=np.arange(-3,3+dy,dy)

X,Y=np.meshgrid(x,y)
Temp = T0*np.exp(-((X**2)+(Y**2))/(sigma**2))

pp.figure()
pp.contourf(X,Y,Temp,levels=1000,cmap='inferno')
pp.colorbar(label="Temp(K)")
pp.xlabel("x(m)")
pp.ylabel("y(m)")
pp.title("Temp Distribution")

pp.savefig("t_plate.png",dpi=300,bbox_inches="tight")
#Part B: Central Differencing

dTdx_cd = (Temp[:,2:] - Temp[:,:-2]) / (2*dx)
dTdy_cd = (Temp[2:,:] - Temp[:-2,:]) / (2*dy)

#Part C: Central Using np.gradient
dTdy_g,dTdx_g=np.gradient(Temp,dy,dx)

#Part D: Plotting
dTdx_analytic=(-2*X/sigma**2)*Temp
dTdy_analytic=(-2*Y/sigma**2)*Temp
middle=len(y)//2

pp.figure()
pp.plot(x,dTdx_analytic[middle,:],label="Analytic")
pp.plot(x[1:-1],dTdx_cd[middle,:],"--",label="Central Difference")
pp.plot(x,dTdx_g[middle,:],":",label="np.gradient")

pp.xlabel("x(m)")
pp.ylabel("partial (K/m)")
pp.title("Temp Derivative Along y=0")
pp.legend()
pp.grid()

pp.savefig("dtdx.png",dpi=300,bbox_inches="tight")

#point i
dTdx_g_interior=dTdx_g[:,1:-1] #np.gradient at inner points
max_diff=np.max(np.abs(dTdx_cd-dTdx_g_interior))
print("Max difference is ",max_diff)

#point ii
error_in=np.abs(dTdx_g[:,1:-1]-dTdx_analytic[:,1:-1])
error_edge=np.abs(dTdx_g[:,[0,-1]]-dTdx_analytic[:,[0,-1]])

print(np.max(error_in),np.max(error_edge))

#Part E: Heat flow vector field
heat_x=-dTdx_g
heat_y=-dTdy_g

pp.figure()
pp.contour(X,Y,Temp,levels=50,cmap="hot")
pp.colorbar(label="Temperature (K)")

#every fifth vector
pp.quiver(X[::5,::5],Y[::5,::5],heat_x[::5,::5],heat_y[::5,::5],color="green")
pp.xlabel("x(m)")
pp.ylabel("y(m)")
pp.title("Heat Flow Direction")
pp.savefig("heat_flow.png",dpi=300,bbox_inches="tight")