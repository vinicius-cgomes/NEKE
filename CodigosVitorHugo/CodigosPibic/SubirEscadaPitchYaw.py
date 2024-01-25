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

force8v = [0]
force7v = [0]
force6v = [0]
force5v = [0]
force4v = [0]
force3v = [0]
force2v = [0]
force1v = [0]
force0v = [0]
force8h = [0]
force7h = [0]
force6h = [0]
force5h = [0]
force4h = [0]
force3h = [0]
force2h = [0]
force1h = [0]
force0h = [0]
position8v = [0]
position7v = [0]
position6v = [0]
position5v = [0]
position4v = [0]
position3v = [0]
position2v = [0]
position1v = [0]
position0v = [0]
position8h = [0]
position7h = [0]
position6h = [0]
position5h = [0]
position4h = [0]
position3h = [0]
position2h = [0]
position1h = [0]
position0h = [0]

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
flag = 0
x = 0
h = [0,0,0,0,0,0,0,0,0]
motorh = [0,0,0,0,0,0,0,0,0]
v = [0,0,0,0,0,0,0,0,0]
motorv = [0,0,0,0,0,0,0,0,0]

if clientID!=-1:
    print 'Connected'
else:
    print'Error'
    sys.exit('Error')   


errorCode,motorv[0]=vrep.simxGetObjectHandle(clientID,'motor_v0',vrep.simx_opmode_oneshot_wait)
errorCode,motorv[1]=vrep.simxGetObjectHandle(clientID,'motor_v1',vrep.simx_opmode_oneshot_wait)
errorCode,motorv[2]=vrep.simxGetObjectHandle(clientID,'motor_v2',vrep.simx_opmode_oneshot_wait)
errorCode,motorv[3]=vrep.simxGetObjectHandle(clientID,'motor_v3',vrep.simx_opmode_oneshot_wait)
errorCode,motorv[4]=vrep.simxGetObjectHandle(clientID,'motor_v4',vrep.simx_opmode_oneshot_wait)
errorCode,motorv[5]=vrep.simxGetObjectHandle(clientID,'motor_v5',vrep.simx_opmode_oneshot_wait)
errorCode,motorv[6]=vrep.simxGetObjectHandle(clientID,'motor_v6',vrep.simx_opmode_oneshot_wait)
errorCode,motorv[7]=vrep.simxGetObjectHandle(clientID,'motor_v7',vrep.simx_opmode_oneshot_wait)
errorCode,motorv[8]=vrep.simxGetObjectHandle(clientID,'motor_v8',vrep.simx_opmode_oneshot_wait)
errorCode,motorh[0]=vrep.simxGetObjectHandle(clientID,'motor_h0',vrep.simx_opmode_oneshot_wait)
errorCode,motorh[1]=vrep.simxGetObjectHandle(clientID,'motor_h1',vrep.simx_opmode_oneshot_wait)
errorCode,motorh[2]=vrep.simxGetObjectHandle(clientID,'motor_h2',vrep.simx_opmode_oneshot_wait)
errorCode,motorh[3]=vrep.simxGetObjectHandle(clientID,'motor_h3',vrep.simx_opmode_oneshot_wait)
errorCode,motorh[4]=vrep.simxGetObjectHandle(clientID,'motor_h4',vrep.simx_opmode_oneshot_wait)
errorCode,motorh[5]=vrep.simxGetObjectHandle(clientID,'motor_h5',vrep.simx_opmode_oneshot_wait)
errorCode,motorh[6]=vrep.simxGetObjectHandle(clientID,'motor_h6',vrep.simx_opmode_oneshot_wait)
errorCode,motorh[7]=vrep.simxGetObjectHandle(clientID,'motor_h7',vrep.simx_opmode_oneshot_wait)
errorCode,motorh[8]=vrep.simxGetObjectHandle(clientID,'motor_h8',vrep.simx_opmode_oneshot_wait)

"""
#######################################FAZ A BASE##################################################
"""
v[1] = -math.pi/10
vrep.simxSetJointTargetPosition(clientID,motorv[1],v[1],vrep.simx_opmode_streaming)

while (h[1] > -math.pi/2):
    h[1] = h[1] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[1],h[1],vrep.simx_opmode_streaming)
    time.sleep(0.05)  
    
    force1h.append(vrep.simxGetJointForce(clientID,motorh[1],vrep.simx_opmode_streaming))
    position1h.append(vrep.simxGetJointPosition(clientID,motorh[1],vrep.simx_opmode_streaming))

time.sleep(0.1)

while (h[0] > -math.pi/2):
    h[0] = h[0] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[0],h[0],vrep.simx_opmode_streaming)
    time.sleep(0.05)    
    
    force0h.append(vrep.simxGetJointForce(clientID,motorh[0],vrep.simx_opmode_streaming))
    position0h.append(vrep.simxGetJointPosition(clientID,motorh[0],vrep.simx_opmode_streaming))

v[1] = 0
vrep.simxSetJointTargetPosition(clientID,motorv[1],v[1],vrep.simx_opmode_streaming)

time.sleep(1)
"""
#############################LEVANTA A PARTE DA FRENTE##################################################
"""
while (v[8] > -math.pi/2):
    v[8] = v[8] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[8],v[8],vrep.simx_opmode_streaming)    
    time.sleep(0.01)
    
    force8v.append(vrep.simxGetJointForce(clientID,motorv[8],vrep.simx_opmode_streaming))
    position8v.append(vrep.simxGetJointPosition(clientID,motorv[8],vrep.simx_opmode_streaming))
    
time.sleep(1)

while (v[7] > -math.pi/2):
    v[7] = v[7] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[7],v[7],vrep.simx_opmode_streaming)
    time.sleep(0.01)    
    
    force7v.append(vrep.simxGetJointForce(clientID,motorv[7],vrep.simx_opmode_streaming))
    position7v.append(vrep.simxGetJointPosition(clientID,motorv[7],vrep.simx_opmode_streaming))    

time.sleep(1)
"""
while (v[6] > -math.pi/2):
    v[6] = v[6] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[6],v[6],vrep.simx_opmode_streaming)
    v[8] = v[8] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[8],v[8],vrep.simx_opmode_streaming)
    time.sleep(0.01)    
    
    force6v.append(vrep.simxGetJointForce(clientID,motorv[6],vrep.simx_opmode_streaming))
    position6v.append(vrep.simxGetJointPosition(clientID,motorv[6],vrep.simx_opmode_streaming))
    
    force8v.append(vrep.simxGetJointForce(clientID,motorv[8],vrep.simx_opmode_streaming))
    position8v.append(vrep.simxGetJointPosition(clientID,motorv[8],vrep.simx_opmode_streaming))

time.sleep(1)

while (v[7] < 0):
    v[7] = v[7] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[7],v[7],vrep.simx_opmode_streaming)
    time.sleep(0.01) 
    
    force7v.append(vrep.simxGetJointForce(clientID,motorv[7],vrep.simx_opmode_streaming))
    position7v.append(vrep.simxGetJointPosition(clientID,motorv[7],vrep.simx_opmode_streaming))
"""
while (v[8] < 0):
    v[8] = v[8] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[8],v[8],vrep.simx_opmode_streaming)
    time.sleep(0.01)
    
time.sleep(1)

while (h[8] < math.pi/2):
    h[8] = h[8] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[8],h[8],vrep.simx_opmode_streaming)
    time.sleep(0.01)    
    
    force7h.append(vrep.simxGetJointForce(clientID,motorh[7],vrep.simx_opmode_streaming))
    position7h.append(vrep.simxGetJointPosition(clientID,motorh[7],vrep.simx_opmode_streaming))

time.sleep(1)
"""
while (v[8] < math.pi/2):
    v[8] = v[8] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[8],v[8],vrep.simx_opmode_streaming)
    time.sleep(0.01)    
    
    force8v.append(vrep.simxGetJointForce(clientID,motorv[8],vrep.simx_opmode_streaming))
    position8v.append(vrep.simxGetJointPosition(clientID,motorv[8],vrep.simx_opmode_streaming))

time.sleep(0.1)
"""
while (v[6] > -math.pi/2):
    v[6] = v[6] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[6],v[6],vrep.simx_opmode_streaming)
    v[7] = v[7] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[7],v[7],vrep.simx_opmode_streaming)
    h[7] = h[7] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[7],h[7],vrep.simx_opmode_streaming)
    h[8] = h[8] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[8],h[8],vrep.simx_opmode_streaming)
    v[8] = v[8] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[8],v[8],vrep.simx_opmode_streaming)
    time.sleep(0.05)
    
time.sleep(1)
"""
#############################COMECA A COLOCAR O RESTO##################################################
"""
while (v[5] > -math.pi/2):
    v[5] = v[5] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[5],v[5],vrep.simx_opmode_streaming)
    v[6] = v[6] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[6],v[6],vrep.simx_opmode_streaming)
    h[6] = h[6] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[6],h[6],vrep.simx_opmode_streaming)
    h[7] = h[7] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[7],h[7],vrep.simx_opmode_streaming)
    v[7] = v[7] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[7],v[7],vrep.simx_opmode_streaming)
    v[8] = v[8] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[8],v[8],vrep.simx_opmode_streaming)
    time.sleep(0.05)
    if   v[5] > -math.pi/4:  
        h[8] = h[8] - math.pi/240
        vrep.simxSetJointTargetPosition(clientID,motorh[8],h[8],vrep.simx_opmode_streaming)
    else:
        h[8] = h[8] + math.pi/240
        vrep.simxSetJointTargetPosition(clientID,motorh[8],h[8],vrep.simx_opmode_streaming)
        
    force5v.append(vrep.simxGetJointForce(clientID,motorv[5],vrep.simx_opmode_streaming))
    position5v.append(vrep.simxGetJointPosition(clientID,motorv[5],vrep.simx_opmode_streaming))
    force6v.append(vrep.simxGetJointForce(clientID,motorv[6],vrep.simx_opmode_streaming))
    position6v.append(vrep.simxGetJointPosition(clientID,motorv[6],vrep.simx_opmode_streaming))
    force7v.append(vrep.simxGetJointForce(clientID,motorv[7],vrep.simx_opmode_streaming))
    position7v.append(vrep.simxGetJointPosition(clientID,motorv[7],vrep.simx_opmode_streaming))
    force8v.append(vrep.simxGetJointForce(clientID,motorv[8],vrep.simx_opmode_streaming))
    position8v.append(vrep.simxGetJointPosition(clientID,motorv[8],vrep.simx_opmode_streaming))
    force6h.append(vrep.simxGetJointForce(clientID,motorh[6],vrep.simx_opmode_streaming))
    position6h.append(vrep.simxGetJointPosition(clientID,motorh[6],vrep.simx_opmode_streaming))
    force7h.append(vrep.simxGetJointForce(clientID,motorh[7],vrep.simx_opmode_streaming))
    position7h.append(vrep.simxGetJointPosition(clientID,motorh[7],vrep.simx_opmode_streaming))
    force8h.append(vrep.simxGetJointForce(clientID,motorh[8],vrep.simx_opmode_streaming))
    position8h.append(vrep.simxGetJointPosition(clientID,motorh[8],vrep.simx_opmode_streaming))
        
time.sleep(1)

while (v[4] > -math.pi/2):
    v[4] = v[4] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[4],v[4],vrep.simx_opmode_streaming)
    v[5] = v[5] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[5],v[5],vrep.simx_opmode_streaming)
    h[5] = h[5] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[5],h[5],vrep.simx_opmode_streaming)
    h[6] = h[6] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[6],h[6],vrep.simx_opmode_streaming)
    v[6] = v[6] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[6],v[6],vrep.simx_opmode_streaming)
    v[7] = v[7] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[7],v[7],vrep.simx_opmode_streaming)
    time.sleep(0.05)
    if   v[4] > -math.pi/4:  
        h[7] = h[7] - math.pi/230
        vrep.simxSetJointTargetPosition(clientID,motorh[7],h[7],vrep.simx_opmode_streaming)
    else:
        h[7] = h[7] + math.pi/230
        vrep.simxSetJointTargetPosition(clientID,motorh[7],h[7],vrep.simx_opmode_streaming)
    
    force4v.append(vrep.simxGetJointForce(clientID,motorv[4],vrep.simx_opmode_streaming))
    position4v.append(vrep.simxGetJointPosition(clientID,motorv[4],vrep.simx_opmode_streaming))    
    force5v.append(vrep.simxGetJointForce(clientID,motorv[5],vrep.simx_opmode_streaming))
    position5v.append(vrep.simxGetJointPosition(clientID,motorv[5],vrep.simx_opmode_streaming))
    force6v.append(vrep.simxGetJointForce(clientID,motorv[6],vrep.simx_opmode_streaming))
    position6v.append(vrep.simxGetJointPosition(clientID,motorv[6],vrep.simx_opmode_streaming))
    force7v.append(vrep.simxGetJointForce(clientID,motorv[7],vrep.simx_opmode_streaming))
    position7v.append(vrep.simxGetJointPosition(clientID,motorv[7],vrep.simx_opmode_streaming))
    force5h.append(vrep.simxGetJointForce(clientID,motorh[5],vrep.simx_opmode_streaming))
    position5h.append(vrep.simxGetJointPosition(clientID,motorh[5],vrep.simx_opmode_streaming))
    force6h.append(vrep.simxGetJointForce(clientID,motorh[6],vrep.simx_opmode_streaming))
    position6h.append(vrep.simxGetJointPosition(clientID,motorh[6],vrep.simx_opmode_streaming))
    force7h.append(vrep.simxGetJointForce(clientID,motorh[7],vrep.simx_opmode_streaming))
    position7h.append(vrep.simxGetJointPosition(clientID,motorh[7],vrep.simx_opmode_streaming))
    
time.sleep(1)

while (v[3] > -math.pi/2):
    v[3] = v[3] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[3],v[3],vrep.simx_opmode_streaming)
    v[4] = v[4] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[4],v[4],vrep.simx_opmode_streaming)
    h[4] = h[4] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[4],h[4],vrep.simx_opmode_streaming)
    h[5] = h[5] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[5],h[5],vrep.simx_opmode_streaming)
    v[5] = v[5] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[5],v[5],vrep.simx_opmode_streaming)
    v[6] = v[6] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[6],v[6],vrep.simx_opmode_streaming)
    time.sleep(0.05)
    if   v[3] > -math.pi/4:  
        h[6] = h[6] - math.pi/200
        vrep.simxSetJointTargetPosition(clientID,motorh[6],h[6],vrep.simx_opmode_streaming)
    else:
        h[6] = h[6] + math.pi/200
        vrep.simxSetJointTargetPosition(clientID,motorh[6],h[6],vrep.simx_opmode_streaming)
    
    force3v.append(vrep.simxGetJointForce(clientID,motorv[3],vrep.simx_opmode_streaming))
    position3v.append(vrep.simxGetJointPosition(clientID,motorv[3],vrep.simx_opmode_streaming))
    force4v.append(vrep.simxGetJointForce(clientID,motorv[4],vrep.simx_opmode_streaming))
    position4v.append(vrep.simxGetJointPosition(clientID,motorv[4],vrep.simx_opmode_streaming))    
    force5v.append(vrep.simxGetJointForce(clientID,motorv[5],vrep.simx_opmode_streaming))
    position5v.append(vrep.simxGetJointPosition(clientID,motorv[5],vrep.simx_opmode_streaming))
    force6v.append(vrep.simxGetJointForce(clientID,motorv[6],vrep.simx_opmode_streaming))
    position6v.append(vrep.simxGetJointPosition(clientID,motorv[6],vrep.simx_opmode_streaming))
    force4h.append(vrep.simxGetJointForce(clientID,motorh[4],vrep.simx_opmode_streaming))
    position4h.append(vrep.simxGetJointPosition(clientID,motorh[4],vrep.simx_opmode_streaming))
    force5h.append(vrep.simxGetJointForce(clientID,motorh[5],vrep.simx_opmode_streaming))
    position5h.append(vrep.simxGetJointPosition(clientID,motorh[5],vrep.simx_opmode_streaming))
    force6h.append(vrep.simxGetJointForce(clientID,motorh[6],vrep.simx_opmode_streaming))
    position6h.append(vrep.simxGetJointPosition(clientID,motorh[6],vrep.simx_opmode_streaming))
        
time.sleep(1)
"""
#######################################FAZ BASE EM CIMA##################################################
"""
h[7] = -math.pi/20
vrep.simxSetJointTargetPosition(clientID,motorh[7],h[7],vrep.simx_opmode_streaming)

while (v[8] > -math.pi/2):
    v[8] = v[8] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[8],v[8],vrep.simx_opmode_streaming)
    time.sleep(0.02)    
    
    force8v.append(vrep.simxGetJointForce(clientID,motorv[8],vrep.simx_opmode_streaming))
    position8v.append(vrep.simxGetJointPosition(clientID,motorv[8],vrep.simx_opmode_streaming))

time.sleep(1)
    
while (v[7] > -math.pi/2):
    v[7] = v[7] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[7],v[7],vrep.simx_opmode_streaming)
    time.sleep(0.02)   
    
    force7v.append(vrep.simxGetJointForce(clientID,motorv[7],vrep.simx_opmode_streaming))
    position7v.append(vrep.simxGetJointPosition(clientID,motorv[7],vrep.simx_opmode_streaming))

time.sleep(1)

"""
####################################DESFAZ A BASE##################################################
"""
v[1] = -math.pi/10
vrep.simxSetJointTargetPosition(clientID,motorv[1],v[1],vrep.simx_opmode_streaming)

while (h[0] < 0):
    h[0] = h[0] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[0],h[0],vrep.simx_opmode_streaming)
    time.sleep(0.02)  
    
    force0h.append(vrep.simxGetJointForce(clientID,motorh[0],vrep.simx_opmode_streaming))
    position0h.append(vrep.simxGetJointPosition(clientID,motorh[0],vrep.simx_opmode_streaming))

time.sleep(1)
    
while (h[1] < 0):
    h[1] = h[1] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[1],h[1],vrep.simx_opmode_streaming)
    time.sleep(0.02) 
    
    force1h.append(vrep.simxGetJointForce(clientID,motorh[1],vrep.simx_opmode_streaming))
    position1h.append(vrep.simxGetJointPosition(clientID,motorh[1],vrep.simx_opmode_streaming))

time.sleep(1)

v[1] = 0
vrep.simxSetJointTargetPosition(clientID,motorv[1],v[1],vrep.simx_opmode_streaming)

time.sleep(3)

"""
#################################COLOCA O RESTO EM CIMA##################################################
"""
while (v[2] > -math.pi/2):
    v[2] = v[2] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[2],v[2],vrep.simx_opmode_streaming)
    v[3] = v[3] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[3],v[3],vrep.simx_opmode_streaming)
    h[3] = h[3] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[3],h[3],vrep.simx_opmode_streaming)
    h[4] = h[4] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[4],h[4],vrep.simx_opmode_streaming)
    v[4] = v[4] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[4],v[4],vrep.simx_opmode_streaming)
    v[5] = v[5] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[5],v[5],vrep.simx_opmode_streaming)
    if   v[2] > -math.pi/4:  
        h[5] = h[5] - math.pi/200
        vrep.simxSetJointTargetPosition(clientID,motorh[5],h[5],vrep.simx_opmode_streaming)
    else:
        h[5] = h[5] + math.pi/200   
        vrep.simxSetJointTargetPosition(clientID,motorh[5],h[5],vrep.simx_opmode_streaming)
    time.sleep(0.05)
    
    force2v.append(vrep.simxGetJointForce(clientID,motorv[2],vrep.simx_opmode_streaming))
    position2v.append(vrep.simxGetJointPosition(clientID,motorv[2],vrep.simx_opmode_streaming))
    force3v.append(vrep.simxGetJointForce(clientID,motorv[3],vrep.simx_opmode_streaming))
    position3v.append(vrep.simxGetJointPosition(clientID,motorv[3],vrep.simx_opmode_streaming))
    force4v.append(vrep.simxGetJointForce(clientID,motorv[4],vrep.simx_opmode_streaming))
    position4v.append(vrep.simxGetJointPosition(clientID,motorv[4],vrep.simx_opmode_streaming))    
    force5v.append(vrep.simxGetJointForce(clientID,motorv[5],vrep.simx_opmode_streaming))
    position5v.append(vrep.simxGetJointPosition(clientID,motorv[5],vrep.simx_opmode_streaming))
    force3h.append(vrep.simxGetJointForce(clientID,motorh[3],vrep.simx_opmode_streaming))
    position3h.append(vrep.simxGetJointPosition(clientID,motorh[3],vrep.simx_opmode_streaming))
    force4h.append(vrep.simxGetJointForce(clientID,motorh[4],vrep.simx_opmode_streaming))
    position4h.append(vrep.simxGetJointPosition(clientID,motorh[4],vrep.simx_opmode_streaming))
    force5h.append(vrep.simxGetJointForce(clientID,motorh[5],vrep.simx_opmode_streaming))
    position5h.append(vrep.simxGetJointPosition(clientID,motorh[5],vrep.simx_opmode_streaming))

time.sleep(1)
    
while (v[1] > -math.pi/2):
    v[1] = v[1] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[1],v[1],vrep.simx_opmode_streaming)
    v[2] = v[2] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[2],v[2],vrep.simx_opmode_streaming)
    h[2] = h[2] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[2],h[2],vrep.simx_opmode_streaming)
    h[3] = h[3] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[3],h[3],vrep.simx_opmode_streaming)
    v[3] = v[3] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[3],v[3],vrep.simx_opmode_streaming)
    v[4] = v[4] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[4],v[4],vrep.simx_opmode_streaming)
    time.sleep(0.05)
    if   v[1] > -math.pi/4:  
        h[4] = h[4] - math.pi/260
        vrep.simxSetJointTargetPosition(clientID,motorh[4],h[4],vrep.simx_opmode_streaming)
    else:
        h[4] = h[4] + math.pi/260
        vrep.simxSetJointTargetPosition(clientID,motorh[4],h[4],vrep.simx_opmode_streaming)
        
    
    force1v.append(vrep.simxGetJointForce(clientID,motorv[1],vrep.simx_opmode_streaming))
    position1v.append(vrep.simxGetJointPosition(clientID,motorv[1],vrep.simx_opmode_streaming))
    force2v.append(vrep.simxGetJointForce(clientID,motorv[2],vrep.simx_opmode_streaming))
    position2v.append(vrep.simxGetJointPosition(clientID,motorv[2],vrep.simx_opmode_streaming))
    force3v.append(vrep.simxGetJointForce(clientID,motorv[3],vrep.simx_opmode_streaming))
    position3v.append(vrep.simxGetJointPosition(clientID,motorv[3],vrep.simx_opmode_streaming))
    force4v.append(vrep.simxGetJointForce(clientID,motorv[4],vrep.simx_opmode_streaming))
    position4v.append(vrep.simxGetJointPosition(clientID,motorv[4],vrep.simx_opmode_streaming))    
    force2h.append(vrep.simxGetJointForce(clientID,motorh[2],vrep.simx_opmode_streaming))
    position2h.append(vrep.simxGetJointPosition(clientID,motorh[2],vrep.simx_opmode_streaming))
    force3h.append(vrep.simxGetJointForce(clientID,motorh[3],vrep.simx_opmode_streaming))
    position3h.append(vrep.simxGetJointPosition(clientID,motorh[3],vrep.simx_opmode_streaming))

time.sleep(1)
   
while (v[0] > -math.pi/2):
    v[0] = v[0] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[0],v[0],vrep.simx_opmode_streaming)
    v[1] = v[1] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[1],v[1],vrep.simx_opmode_streaming)
    h[1] = h[1] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[1],h[1],vrep.simx_opmode_streaming)
    h[2] = h[2] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[2],h[2],vrep.simx_opmode_streaming)
    v[2] = v[2] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[2],v[2],vrep.simx_opmode_streaming)
    v[3] = v[3] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[3],v[3],vrep.simx_opmode_streaming)
    time.sleep(0.05)
    if   v[0] > -math.pi/4:  
        h[3] = h[3] - math.pi/260
        vrep.simxSetJointTargetPosition(clientID,motorh[3],h[3],vrep.simx_opmode_streaming)
    else:
        h[3] = h[3] + math.pi/260
        vrep.simxSetJointTargetPosition(clientID,motorh[3],h[3],vrep.simx_opmode_streaming)    
    
    
    force0v.append(vrep.simxGetJointForce(clientID,motorv[0],vrep.simx_opmode_streaming))
    position0v.append(vrep.simxGetJointPosition(clientID,motorv[0],vrep.simx_opmode_streaming)) 
    force1v.append(vrep.simxGetJointForce(clientID,motorv[1],vrep.simx_opmode_streaming))
    position1v.append(vrep.simxGetJointPosition(clientID,motorv[1],vrep.simx_opmode_streaming))
    force2v.append(vrep.simxGetJointForce(clientID,motorv[2],vrep.simx_opmode_streaming))
    position2v.append(vrep.simxGetJointPosition(clientID,motorv[2],vrep.simx_opmode_streaming))
    force3v.append(vrep.simxGetJointForce(clientID,motorv[3],vrep.simx_opmode_streaming))
    position3v.append(vrep.simxGetJointPosition(clientID,motorv[3],vrep.simx_opmode_streaming))
    force1h.append(vrep.simxGetJointForce(clientID,motorh[1],vrep.simx_opmode_streaming))
    position1h.append(vrep.simxGetJointPosition(clientID,motorh[1],vrep.simx_opmode_streaming))
    force2h.append(vrep.simxGetJointForce(clientID,motorh[2],vrep.simx_opmode_streaming))
    position2h.append(vrep.simxGetJointPosition(clientID,motorh[2],vrep.simx_opmode_streaming))

time.sleep(1)

while (v[8] > -math.pi/60):
    v[8] = v[8] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[8],v[8],vrep.simx_opmode_streaming)
    time.sleep(0.05)


while (h[1] > -math.pi/60):
    h[1] = h[1] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorh[1],h[1],vrep.simx_opmode_streaming)
    time.sleep(0.05)
    
    force1h.append(vrep.simxGetJointForce(clientID,motorh[1],vrep.simx_opmode_streaming))
    position1h.append(vrep.simxGetJointPosition(clientID,motorh[1],vrep.simx_opmode_streaming))
    

while (v[2] > 0):
    v[2] = v[2] - math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[2],v[2],vrep.simx_opmode_streaming)
    time.sleep(0.05)
    
    force2v.append(vrep.simxGetJointForce(clientID,motorv[2],vrep.simx_opmode_streaming))
    position2v.append(vrep.simxGetJointPosition(clientID,motorv[2],vrep.simx_opmode_streaming))

time.sleep(1)

"""
##################################TERMINA A POHA TODA#############################################
"""

h[7] = -math.pi/20
vrep.simxSetJointTargetPosition(clientID,motorh[7],h[7],vrep.simx_opmode_streaming)

while (v[8] < 0):
    v[8] = v[8] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[8],v[8],vrep.simx_opmode_streaming)
    time.sleep(0.02)    
    
    force8v.append(vrep.simxGetJointForce(clientID,motorv[8],vrep.simx_opmode_streaming))
    position8v.append(vrep.simxGetJointPosition(clientID,motorv[8],vrep.simx_opmode_streaming))

time.sleep(1)
    
while (v[7] < 0):
    v[7] = v[7] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[7],v[7],vrep.simx_opmode_streaming)
    time.sleep(0.02)  
    
    force7v.append(vrep.simxGetJointForce(clientID,motorv[7],vrep.simx_opmode_streaming))
    position7v.append(vrep.simxGetJointPosition(clientID,motorv[7],vrep.simx_opmode_streaming))

time.sleep(1)

h[7] = 0
vrep.simxSetJointTargetPosition(clientID,motorh[7],h[7],vrep.simx_opmode_streaming)

while (v[0] < 0):
    v[0] = v[0] + math.pi/180
    vrep.simxSetJointTargetPosition(clientID,motorv[0],v[0],vrep.simx_opmode_streaming)
    time.sleep(0.02)  
    
    force0v.append(vrep.simxGetJointForce(clientID,motorv[0],vrep.simx_opmode_streaming))
    position0v.append(vrep.simxGetJointPosition(clientID,motorv[0],vrep.simx_opmode_streaming))