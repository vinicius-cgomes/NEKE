# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 17:56:53 2017

@author: vitor
"""

import sys
import vrep
import math
import time

vrep.simxFinish(-1)
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5)

x = 0
delta = 0
pi = 3.1415
alphav = 30*(pi/180)
alphah = 30*(pi/180)
kv = 1.5
kh = 1
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
phi2 = 0
flag = 0
v = [0,0,0,0,0,0,0,0,0]
motorv = [0,0,0,0,0,0,0,0,0]

if clientID!=-1:
    print 'Connected'
else:
    print'Error'
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

for x in range (0,2000):
    v[x%9] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((x%9)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[x%9],v[x%9],vrep.simx_opmode_streaming)
    phi = phi + pi/passo
    time.sleep(0.005)
    
time.sleep(1)

for x in range (0,9):
    v[x%9] = (pow(-1,x))*(math.pi/90)
    vrep.simxSetJointTargetPosition(clientID,motorv[x%9],v[x%9],vrep.simx_opmode_streaming)
    time.sleep(0.001)  
    
time.sleep(1)    
phi = 0

while (phi > -math.pi/2):
    v[0] = phi
    vrep.simxSetJointTargetPosition(clientID,motorv[0],v[0],vrep.simx_opmode_streaming)
    phi = phi - pi/passo
  
time.sleep(1)
  
for x in range (0,1000):

    v[1] = -2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((2)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[1],v[1],vrep.simx_opmode_streaming)
    v[2] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((2)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[2],v[2],vrep.simx_opmode_streaming)
    v[3] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((3)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[3],v[3],vrep.simx_opmode_streaming)
    v[4] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((4)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[4],v[4],vrep.simx_opmode_streaming)
    v[5] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((5)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[5],v[5],vrep.simx_opmode_streaming)
    v[6] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((6)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[6],v[6],vrep.simx_opmode_streaming)
    v[7] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((7)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[7],v[7],vrep.simx_opmode_streaming)    
    v[8] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((8)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[8],v[8],vrep.simx_opmode_streaming)    
    phi = phi + pi/passo
    time.sleep(0.005)      
 
time.sleep(1)
 
for x in range (1,8):
    v[x] = (pow(-1,x))*(math.pi/90)
    vrep.simxSetJointTargetPosition(clientID,motorv[x],v[x],vrep.simx_opmode_streaming)
    time.sleep(0.005)

phi = 0
time.sleep(1)

while (phi > -math.pi/2):
    v[1] = phi
    vrep.simxSetJointTargetPosition(clientID,motorv[1],v[1],vrep.simx_opmode_streaming)
    v[0] = -math.pi/2 - phi
    vrep.simxSetJointTargetPosition(clientID,motorv[0],v[0],vrep.simx_opmode_streaming)
    phi = phi - pi/passo   
    time.sleep(0.005)

time.sleep(1)

for x in range (0,1500):

    v[2] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((2)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[2],v[2],vrep.simx_opmode_streaming)
    v[3] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((3)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[3],v[3],vrep.simx_opmode_streaming)
    v[4] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((4)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[4],v[4],vrep.simx_opmode_streaming)
    v[5] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((5)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[5],v[5],vrep.simx_opmode_streaming)
    v[6] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((6)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[6],v[6],vrep.simx_opmode_streaming)
    v[7] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((7)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[7],v[7],vrep.simx_opmode_streaming)    
    v[8] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((8)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[8],v[8],vrep.simx_opmode_streaming)    
    phi = phi + pi/passo
    time.sleep(0.005)      
 
time.sleep(1)
 
for x in range (2,9):
    v[x] = (pow(-1,x))*(math.pi/90)
    vrep.simxSetJointTargetPosition(clientID,motorv[x],v[x],vrep.simx_opmode_streaming)
    time.sleep(0.005)
    
phi = 0

while (phi < math.pi/2):
   v[0] = phi
   vrep.simxSetJointTargetPosition(clientID,motorv[0],v[0],vrep.simx_opmode_streaming)
   phi = phi + pi/passo   
   time.sleep(0.005)   

phi = 0
time.sleep(1)

while (phi > -math.pi/2):
   v[2] = phi
   vrep.simxSetJointTargetPosition(clientID,motorv[2],v[2],vrep.simx_opmode_streaming)
   v[1] = -math.pi/2 - 2*phi
   vrep.simxSetJointTargetPosition(clientID,motorv[1],v[1],vrep.simx_opmode_streaming)
   v[0] = math.pi/2 + phi
   vrep.simxSetJointTargetPosition(clientID,motorv[0],v[0],vrep.simx_opmode_streaming)
   phi = phi - pi/passo   
   time.sleep(0.005)

time.sleep(3)

for x in range (0,1500):
    v[3] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((3)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[3],v[3],vrep.simx_opmode_streaming)
    v[4] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((4)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[4],v[4],vrep.simx_opmode_streaming)
    v[5] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((5)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[5],v[5],vrep.simx_opmode_streaming)
    v[6] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((6)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[6],v[6],vrep.simx_opmode_streaming)
    v[7] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((7)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[7],v[7],vrep.simx_opmode_streaming)    
    v[8] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((8)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[8],v[8],vrep.simx_opmode_streaming)    
    phi = phi + pi/passo
    time.sleep(0.005) 

for x in range (3,9):
    v[x] = (pow(-1,x))*(math.pi/45)
    vrep.simxSetJointTargetPosition(clientID,motorv[x],v[x],vrep.simx_opmode_streaming)
    time.sleep(0.005)

phi = 0
time.sleep(1)

while (phi > -math.pi/2):
   v[3] = phi
   vrep.simxSetJointTargetPosition(clientID,motorv[3],v[3],vrep.simx_opmode_streaming)
   v[1] = math.pi/2 + phi
   vrep.simxSetJointTargetPosition(clientID,motorv[1],v[1],vrep.simx_opmode_streaming)
   v[2] = -math.pi/2 - 2*phi
   vrep.simxSetJointTargetPosition(clientID,motorv[2],v[2],vrep.simx_opmode_streaming)
   phi = phi - pi/passo   
   time.sleep(0.005)
  
phi = 0
time.sleep(1)

for x in range (0,4000):    
    v[4] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((4)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[4],v[4],vrep.simx_opmode_streaming)
    v[5] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((5)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[5],v[5],vrep.simx_opmode_streaming)
    v[6] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((6)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[6],v[6],vrep.simx_opmode_streaming)
    v[7] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((7)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[7],v[7],vrep.simx_opmode_streaming)    
    v[8] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((8)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[8],v[8],vrep.simx_opmode_streaming)    
    phi = phi + pi/passo
    time.sleep(0.005)
    
phi = 0
time.sleep(1)

for x in range (4,9):
    v[x] = (pow(-1,x))*(math.pi/45)
    vrep.simxSetJointTargetPosition(clientID,motorv[x],v[x],vrep.simx_opmode_streaming)
    time.sleep(0.005)

phi = 0
time.sleep(1)    
    
while (phi > -math.pi/2):
   v[4] = phi
   vrep.simxSetJointTargetPosition(clientID,motorv[4],v[4],vrep.simx_opmode_streaming)
   v[2] = math.pi/2 + phi
   vrep.simxSetJointTargetPosition(clientID,motorv[2],v[2],vrep.simx_opmode_streaming)
   v[3] = -math.pi/2 - 2*phi
   vrep.simxSetJointTargetPosition(clientID,motorv[3],v[3],vrep.simx_opmode_streaming)
   phi = phi - pi/passo   
   time.sleep(0.005)
   
phi = 0
time.sleep(1)   
   
for x in range (0,1500):    
    v[5] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((5)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[5],v[5],vrep.simx_opmode_streaming)
    v[6] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((6)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[6],v[6],vrep.simx_opmode_streaming)
    v[7] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((7)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[7],v[7],vrep.simx_opmode_streaming)    
    v[8] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((8)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[8],v[8],vrep.simx_opmode_streaming) 
    
    v[0] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((0)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[0],v[0],vrep.simx_opmode_streaming)
    v[1] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((1)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[1],v[1],vrep.simx_opmode_streaming)
    v[2] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((2)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[2],v[2],vrep.simx_opmode_streaming)
    phi = phi + pi/passo
    time.sleep(0.005)
    
phi = 0
time.sleep(1)

for x in range (0,3):
    v[x] = (pow(-1,x))*(math.pi/45)
    vrep.simxSetJointTargetPosition(clientID,motorv[x],v[x],vrep.simx_opmode_streaming)
    time.sleep(0.005)
    
for x in range (5,9):
    v[x] = (pow(-1,x))*(math.pi/45)
    vrep.simxSetJointTargetPosition(clientID,motorv[x],v[x],vrep.simx_opmode_streaming)
    time.sleep(0.005)

phi = 0
time.sleep(1)
    
while (phi > -math.pi/2):
   v[5] = phi
   vrep.simxSetJointTargetPosition(clientID,motorv[5],v[5],vrep.simx_opmode_streaming)
   v[3] = math.pi/2 + phi
   vrep.simxSetJointTargetPosition(clientID,motorv[3],v[3],vrep.simx_opmode_streaming)
   v[4] = -math.pi/2 - 2*phi
   vrep.simxSetJointTargetPosition(clientID,motorv[4],v[4],vrep.simx_opmode_streaming)
   phi = phi - pi/passo   
   time.sleep(0.005)
   
for x in range (0,1500):    
    v[6] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((6)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[6],v[6],vrep.simx_opmode_streaming)
    v[7] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((7)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[7],v[7],vrep.simx_opmode_streaming)    
    v[8] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((8)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[8],v[8],vrep.simx_opmode_streaming) 
    
    v[0] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((0)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[0],v[0],vrep.simx_opmode_streaming)   
    v[1] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((1)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[1],v[1],vrep.simx_opmode_streaming)
    v[2] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((2)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[2],v[2],vrep.simx_opmode_streaming)
    v[3] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((3)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[3],v[3],vrep.simx_opmode_streaming)
    phi = phi + pi/passo
    time.sleep(0.005)
    
phi = 0
time.sleep(1)

for x in range (0,4):
    v[x] = (pow(-1,x))*(math.pi/45)
    vrep.simxSetJointTargetPosition(clientID,motorv[x],v[x],vrep.simx_opmode_streaming)
    time.sleep(0.005)
    
for x in range (6,9):
    v[x] = (pow(-1,x))*(math.pi/45)
    vrep.simxSetJointTargetPosition(clientID,motorv[x],v[x],vrep.simx_opmode_streaming)
    time.sleep(0.005)

phi = 0
time.sleep(1)

while (phi > -math.pi/2):
   v[6] = phi
   vrep.simxSetJointTargetPosition(clientID,motorv[6],v[6],vrep.simx_opmode_streaming)
   v[4] = math.pi/2 + phi
   vrep.simxSetJointTargetPosition(clientID,motorv[4],v[4],vrep.simx_opmode_streaming)
   v[5] = -math.pi/2 - 2*phi
   vrep.simxSetJointTargetPosition(clientID,motorv[5],v[5],vrep.simx_opmode_streaming)
   phi = phi - pi/passo   
   time.sleep(0.005)
   
phi = 0
time.sleep(1)

for x in range (0,1500):    
    v[0] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((0)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[0],v[0],vrep.simx_opmode_streaming)   
    v[1] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((1)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[1],v[1],vrep.simx_opmode_streaming)
    v[2] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((2)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[2],v[2],vrep.simx_opmode_streaming)
    v[3] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((3)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[3],v[3],vrep.simx_opmode_streaming)
    v[4] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((4)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[4],v[4],vrep.simx_opmode_streaming)
    phi = phi + pi/passo
    time.sleep(0.005)
    
phi = 0
time.sleep(1)

for x in range (0,5):
    v[x] = (pow(-1,x))*(math.pi/45)
    vrep.simxSetJointTargetPosition(clientID,motorv[x],v[x],vrep.simx_opmode_streaming)
    time.sleep(0.005)
    
while (phi > -math.pi/2):
   v[7] = phi
   vrep.simxSetJointTargetPosition(clientID,motorv[7],v[7],vrep.simx_opmode_streaming)
   v[5] = math.pi/2 + phi
   vrep.simxSetJointTargetPosition(clientID,motorv[5],v[5],vrep.simx_opmode_streaming)
   v[6] = -math.pi/2 - 2*phi
   vrep.simxSetJointTargetPosition(clientID,motorv[6],v[6],vrep.simx_opmode_streaming)
   phi = phi - pi/passo   
   time.sleep(0.005)
   
phi = 0
time.sleep(1)

for x in range (0,1500):    
    v[0] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((0)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[0],v[0],vrep.simx_opmode_streaming)   
    v[1] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((1)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[1],v[1],vrep.simx_opmode_streaming)
    v[2] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((2)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[2],v[2],vrep.simx_opmode_streaming)
    v[3] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((3)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[3],v[3],vrep.simx_opmode_streaming)
    v[4] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((4)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[4],v[4],vrep.simx_opmode_streaming)
    v[5] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((5)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[5],v[5],vrep.simx_opmode_streaming)
    phi = phi + pi/passo
    time.sleep(0.005)
    
phi = 0
time.sleep(1)

for x in range (0,6):
    v[x] = (pow(-1,x))*(math.pi/45)
    vrep.simxSetJointTargetPosition(clientID,motorv[x],v[x],vrep.simx_opmode_streaming)
    time.sleep(0.005)
    
while (phi > -math.pi/2):
   v[8] = phi
   vrep.simxSetJointTargetPosition(clientID,motorv[8],v[8],vrep.simx_opmode_streaming)
   v[6] = math.pi/2 + phi
   vrep.simxSetJointTargetPosition(clientID,motorv[6],v[6],vrep.simx_opmode_streaming)
   v[7] = -math.pi/2 - 2*phi
   vrep.simxSetJointTargetPosition(clientID,motorv[7],v[7],vrep.simx_opmode_streaming)
   phi = phi - pi/passo   
   time.sleep(0.005)
   
phi = 0
time.sleep(1)

for x in range (0,1500):    
    v[0] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((0)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[0],v[0],vrep.simx_opmode_streaming)   
    v[1] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((1)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[1],v[1],vrep.simx_opmode_streaming)
    v[2] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((2)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[2],v[2],vrep.simx_opmode_streaming)
    v[3] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((3)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[3],v[3],vrep.simx_opmode_streaming)
    v[4] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((4)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[4],v[4],vrep.simx_opmode_streaming)
    v[5] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((5)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[5],v[5],vrep.simx_opmode_streaming)
    v[6] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((6)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[6],v[6],vrep.simx_opmode_streaming)
    phi = phi + pi/passo
    time.sleep(0.005)
    
phi = 0
time.sleep(1)

for x in range (0,7):
    v[x] = (pow(-1,x))*(math.pi/45)
    vrep.simxSetJointTargetPosition(clientID,motorv[x],v[x],vrep.simx_opmode_streaming)
    time.sleep(0.005)

phi = 0
time.sleep(1)

while (phi > -math.pi/2):
   v[7] = math.pi/2 + phi
   vrep.simxSetJointTargetPosition(clientID,motorv[7],v[7],vrep.simx_opmode_streaming)
   v[8] = -math.pi/2 - 2*phi
   vrep.simxSetJointTargetPosition(clientID,motorv[8],v[8],vrep.simx_opmode_streaming)
   phi = phi - pi/passo   
   time.sleep(0.005)
   
phi = 0
time.sleep(1)

for x in range (0,1500):    
    v[0] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((0)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[0],v[0],vrep.simx_opmode_streaming)   
    v[1] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((1)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[1],v[1],vrep.simx_opmode_streaming)
    v[2] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((2)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[2],v[2],vrep.simx_opmode_streaming)
    v[3] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((3)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[3],v[3],vrep.simx_opmode_streaming)
    v[4] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((4)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[4],v[4],vrep.simx_opmode_streaming)
    v[5] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((5)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[5],v[5],vrep.simx_opmode_streaming)
    v[6] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((6)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[6],v[6],vrep.simx_opmode_streaming)
    v[7] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((7)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[7],v[7],vrep.simx_opmode_streaming)
    phi = phi + pi/passo
    time.sleep(0.005)
    
phi = 0
time.sleep(1)

for x in range (0,8):
    v[x] = (pow(-1,x))*(math.pi/45)
    vrep.simxSetJointTargetPosition(clientID,motorv[x],v[x],vrep.simx_opmode_streaming)
    time.sleep(0.005)

phi = 0
time.sleep(1)

while (phi > -math.pi/2):
   v[8] = math.pi/2 + phi
   vrep.simxSetJointTargetPosition(clientID,motorv[8],v[8],vrep.simx_opmode_streaming)
   phi = phi - pi/passo   
   time.sleep(0.005)
   
phi = 0
time.sleep(1)

for x in range (0,1500):    
    v[0] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((0)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[0],v[0],vrep.simx_opmode_streaming)   
    v[1] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((1)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[1],v[1],vrep.simx_opmode_streaming)
    v[2] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((2)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[2],v[2],vrep.simx_opmode_streaming)
    v[3] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((3)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[3],v[3],vrep.simx_opmode_streaming)
    v[4] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((4)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[4],v[4],vrep.simx_opmode_streaming)
    v[5] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((5)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[5],v[5],vrep.simx_opmode_streaming)
    v[6] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((6)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[6],v[6],vrep.simx_opmode_streaming)
    v[7] = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((7)+(d0/d))))
    vrep.simxSetJointTargetPosition(clientID,motorv[7],v[7],vrep.simx_opmode_streaming)
    phi = phi + pi/passo
    time.sleep(0.005)
    
phi = 0
time.sleep(1)

for x in range (0,9):
    v[x] = (pow(-1,x))*(math.pi/45)
    vrep.simxSetJointTargetPosition(clientID,motorv[x],v[x],vrep.simx_opmode_streaming)
    time.sleep(0.005)