# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09 17:21:48 2017

@author: VitorUnB

"""

"""
simExtRemoteApiStart(19999)
"""
import sys
import vrep
import math
import time

vrep.simxFinish(-1)
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5)

    
force = [0]
delta = 0
pi = 3.1415
alphav = 20*(pi/180)
alphah = 10*(pi/180)
kv = 1.5
kh = 2
M = 2*5
m = 2*6
line = 4
Mline = M*line
mline = m*line
kvline = kv*line
khline = kh*line
d0 = 30
d2 = 2*d0
d = 4*d0
passo=360
deltaphivh = 30 *(pi/180)
l = M*2*d0
H = 35
A = pi/3
phi=0
flag = 0
x = 1
v = [0,0,0,0,0,0,0,0,0]
motorv = [0,0,0,0,0,0,0,0,0]

if clientID!=-1:
    print ('Connected')
else:
    print('Error')
    sys.exit('Error')   


errorCode,motorv[0]=vrep.simxGetObjectHandle(clientID,'motor_v1',vrep.simx_opmode_oneshot_wait)
errorCode,motorv[1]=vrep.simxGetObjectHandle(clientID,'motor_v2',vrep.simx_opmode_oneshot_wait)
errorCode,motorv[2]=vrep.simxGetObjectHandle(clientID,'motor_v3',vrep.simx_opmode_oneshot_wait)
errorCode,motorv[3]=vrep.simxGetObjectHandle(clientID,'motor_v4',vrep.simx_opmode_oneshot_wait)
errorCode,motorv[4]=vrep.simxGetObjectHandle(clientID,'motor_v5',vrep.simx_opmode_oneshot_wait)
errorCode,motorv[5]=vrep.simxGetObjectHandle(clientID,'motor_v6',vrep.simx_opmode_oneshot_wait)
errorCode,motorv[6]=vrep.simxGetObjectHandle(clientID,'motor_v7',vrep.simx_opmode_oneshot_wait)
errorCode,motorv[7]=vrep.simxGetObjectHandle(clientID,'motor_v8',vrep.simx_opmode_oneshot_wait)
errorCode,motorv[8]=vrep.simxGetObjectHandle(clientID,'motor_v9',vrep.simx_opmode_oneshot_wait)


while (flag ==0):
    v[x%9] = 2*alphav*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((x%9)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[x%9],v[x%9],vrep.simx_opmode_streaming)
    force.append(vrep.simxGetJointForce(clientID,motorv[0],vrep.simx_opmode_streaming))
    x = x+1
    delta = delta + pi/passo
    phi = phi + pi/passo 
    time.sleep(0.005)  
