function sysCall_init()
    sim1 = require('sim')
    
    joints_yaw={-1,-1,-1,-1}
    joints_pitch={-1,-1,-1,-1}
    indice = 1
    M1 = 9
    Manterior = 0
    Mposterior = 0
    J = 2000
    x = 1
    y = 0
    stat = -1
    delta = 0
    pi = 3.1415
    alphav = 30*(pi/180)
    alphah = 40*(pi/180)
    kv = 1.5
    kh = 1
    M = 2*5
    m = 2*6
    line = 4
    Mline = M*line
    mline = m*line
    kvline = kv*line
    khline = kh*line
    d0 = 18
    d2 = 2*d0
    d = 4*d0
    passo=100
    deltaphivh = 30 *(pi/180)
    l = M*2*d0
    H = 35
    A = pi/3
    phi=0
    phi2 = 0
    flag = 0
    v = 0
    v1 = 0
    v2 = 0

    --Parametros da curva de Hirose
    a = pi/10
    c  = 0
    k = 2
    b = 2*pi*k




    --reconhecer as juntas pitch e yaw do robô
    for i=1,M1 ,1 do
        joints_yaw[i]=sim.getObject('./yaw',{index=i-1})
        joints_pitch[i]=sim.getObject('./pitch',{index=i-1})
    end
end

function sysCall_actuation()
    if x < 700 then --700 repeticoes, ou seja, 7 ciclos completos da curva de hirose (passo = 100)
        pitchpitchWLifted(stat) --a variavel stat representa a junta que esta com acionada em 90 graus
    else
        if phi2 < math.pi/2 then
            adjustLiftedAngles(stat) --apos 7 ciclos ajusta as juntas da seguinte forma: stat passa de -pi/2 para 0; stat+1 passa de pi/2 para -pi/2; stat+2 passa de 0 para pi/2
            --pitchpitchWLiftedTransition(stat) --continua o movimento pitchpitch enquanto os angulos sao ajustados
        else
            phi2 = 0
            x = 1
            y = 0
            stat = stat + 1
        end
        y = y + 1
    end
    x = x + 1
end

--funcoes antigas---------------------------
function yawyaw ()
    for k = 1, M1 ,1 do
        v = 2*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((k)+(d0/d))))
        sim.setJointTargetPosition(joints_yaw[k], v)
        phi = phi + pi/passo
    end
end

function pitchpitch()
    for k = 1, M1 ,1 do
        v = 2*alphav*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((k)+(d0/d))))
        sim.setJointTargetPosition(joints_pitch[k], v/2)
        phi = phi + pi/passo
    end
end

function pitchyaw () 
    for k = 1, M1, 1 do
        v1 = 0.5*math.sin(phi+((2*pi*kvline/(Mline/2))*((k)+(d0/d))))
        v2 = 5*alphah*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((k)+(d0/d))))
        sim.setJointTargetPosition(joints_yaw[k], v1/2)
        sim.setJointTargetPosition(joints_pitch[k], v2/2)
        delta = delta + pi/passo
        phi = phi + pi/passo
    end
end

function pitchpitch2()
    for k = 2, M1 ,1 do
        v = 2*alphav*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((k)+(d0/d))))
        sim.setJointTargetPosition(joints_pitch[k], v/2)
        phi = phi + pi/passo
    end
end

function pitchpitchWLiftedDeprecated(liftedJoint)
    for k = 1, M1 ,1 do
        if not (k==liftedJoint) and not (k==liftedJoint+1) then
            --v = 2*alphav*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((k)+(d0/d))))
            v = -2*a*math.sin(b/(2*M1))*math.sin((phi)+(k*b/M1)) -c/M1
            sim.setJointTargetPosition(joints_pitch[k], v)
            if k == liftedJoint+2 and liftedJoint > 0 then
                sim.setJointTargetPosition(joints_pitch[k-1], math.pi/2 - v/2)
            end
            phi = phi + pi/passo
        end
    end
end
--fim funcoes antigas -------------------------------

--mantem as justas levantadas e cria a curva de hirose de acordo com o numero de modulos como dois robos, antes e depois
function pitchpitchWLifted(liftedJoint)
    Manterior = M1 - liftedJoint - 1
    Mposterior = liftedJoint - 1
    if Manterior > 1 then
        for k = liftedJoint+2, M1 ,1 do
            v = -2*a*math.sin(b/(2*Manterior))*math.sin((phi)+(k*b/Manterior)) -c/Manterior
            sim.setJointTargetPosition(joints_pitch[k], v)
            if k == liftedJoint+2 and liftedJoint > 0 then --ajusta angulo para manter pi/2 em relacao ao degrau
                sim.setJointTargetPosition(joints_pitch[k-1], math.pi/2 - v/2)
            end
            print(phi)
        end
    end
    if Mposterior > 1 then
        for k = 1, liftedJoint-1 ,1 do
            v = -2*a*math.sin(b/(2*Mposterior))*math.sin((phi)+(k*b/Mposterior)) -c/Mposterior
            sim.setJointTargetPosition(joints_pitch[k], v)
        end
    end
    phi = phi + pi/passo --passo para ciclo completo da curva de hirose
end

function pitchpitchWLiftedTransition(liftedJoint)
    for k = 1, M1 ,1 do
        if not (k==liftedJoint) and not (k==liftedJoint+1) and not (k == liftedJoint+2) then
            --v = 2*alphav*math.sin(pi*khline/(Mline/2))*math.sin(phi+((2*pi*kvline/(Mline/2))*((k)+(d0/d))))
            v = -2*a*math.sin(b/(2*M1))*math.sin((phi)+(k*b/M1)) -c/M1
            sim.setJointTargetPosition(joints_pitch[k], v)
            if k == liftedJoint+2 and liftedJoint > 0 then
                sim.setJointTargetPosition(joints_pitch[k-1], math.pi/2 - v/2)
            end
            phi = phi + pi/passo
        end
    end
end

--ajusta juntas dos modulos levantados, em 360 passos, atuar os motores diretamente causa instabilidade
function adjustLiftedAngles(liftedJoint)
    v = phi2
    if liftedJoint+2 > 0 then
        sim.setJointTargetPosition(joints_pitch[liftedJoint+2],v)
    end
    v = -math.pi/2 + phi2
    if liftedJoint > 0 then
        sim.setJointTargetPosition(joints_pitch[liftedJoint],v)
    end
    v = math.pi/2 - 2*phi2
    if liftedJoint+1 > 0 then
        sim.setJointTargetPosition(joints_pitch[liftedJoint+1],v)
    end
    phi2 = phi2 + math.pi/360   
end

    
    