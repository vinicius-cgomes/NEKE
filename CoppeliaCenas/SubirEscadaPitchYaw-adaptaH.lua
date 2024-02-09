function sysCall_init()
    sim1 = require('sim')
    
    joints_yaw={-1,-1,-1,-1} --vetor de juntas yaw
    joints_pitch={-1,-1,-1,-1} --vetor de juntas pitch
    M1 = 9 --numero de juntas no mesmo plano
    Mid = 7 --junta do meio
    Manterior = M1 --numero de juntas no chão
    Mposterior = 0 --numero de juntas em cima do degrau 
    loopVariable = 1 --variavel de controle
    stat = 0 --controle da junta a ser levantada
    ppyy = 0 --alterna movimento entre pitch e yaw
    passo=360 --passos para um ciclo completo
    phi=0
    phi2 = 0
    v = 0
    flag = 3

    --Parametros da curva de Hirose
    a = 15*(math.pi/180)
    c  = 0
    k = 3
    b = 2*math.pi*k

    --altura do degrau
    H = 181 --altura do degrau em mm
    D0 = 181 --altura do modulo em mm
    alpha = math.asin(H/D0)





    --reconhecer as juntas pitch e yaw do robô
    for i=1,M1 ,1 do
        joints_yaw[i]=sim.getObject('./yaw',{index=i-1})
        joints_pitch[i]=sim.getObject('./pitch',{index=i-1})
    end
end

function sysCall_actuation()
    if stat == 0 then
        if phi > -math.pi/2 then
            createBase()
        else
            phi = 0
            stat = stat + 1
        end
    elseif ppyy == 0 and flag > 2 then
        if phi2 < alpha then
            adjustLiftedAngles(stat)
        else
            phi2 = 0
            ppyy = 1
        end
    elseif ppyy == 1 and flag > 2 then
        if phi2 < math.pi/2 then
            adjustYawAngles(stat-1)
        else
            phi2 = 0
            ppyy = 0
            stat = stat + 1
        end
    end
    if stat == Mid and (flag == 3 or flag == 1) then
        if phi < math.pi/2 then
            alteraBase()
            flag = 1
        else
            phi = 0
            flag = 4
        end
    end
    if stat > M1+3 then
        for k=1, M1, 1 do
            sim.setJointTargetPosition(joints_pitch[k],0)
            sim.setJointTargetPosition(joints_yaw[k],0)
        end
    end
end


--mantem as justas levantadas e cria a curva de hirose de acordo com o numero de modulos como dois robos, antes e depois
function pitchpitchWLifted(liftedJoint)
    Manterior = M1 - liftedJoint - 1
    Mposterior = liftedJoint - 1
    if Mposterior > 9 then
        Mposterior = 9
    end
    if Manterior > 1 then
        for k = liftedJoint+2, M1 ,1 do
            v = 2*a*math.sin(b/(2*M1))*math.sin((phi)+(k*b/M1)) -c/M1
            sim.setJointTargetPosition(joints_pitch[k], v)
            if k == liftedJoint+2 and liftedJoint > 0 then --ajusta angulo para manter alpha em relacao ao degrau
                sim.setJointTargetPosition(joints_pitch[k-1], alpha - v/2)
            end
            print(phi)
        end
    end
    if Mposterior > 3  then
        for k = 1, liftedJoint-1 ,1 do
            v = 2*a*math.sin(b/(2*M1))*math.sin((phi)+(k*b/M1)) -c/M1
            sim.setJointTargetPosition(joints_pitch[k], v)
        end
    end
    phi = phi + math.pi/passo --passo para ciclo completo da curva de hirose
end

function pitchpitchWLiftedTransition(liftedJoint)
    for k = 1, M1 ,1 do
        if not (k==liftedJoint) and not (k==liftedJoint+1) and not (k == liftedJoint+2) then
            v = 2*(20/15)*a*math.sin(b/(2*M1))*math.sin((phi)+(k*b/M1)) -c/M1
            sim.setJointTargetPosition(joints_pitch[k], v)
            if k == liftedJoint+2 and liftedJoint > 0  and liftedJoint < 8 then
                sim.setJointTargetPosition(joints_pitch[k-1], alpha - v/2)
            end
        end
    end
    phi = phi + math.pi/passo
end

--ajusta os angulos para o robo ter mais estabilidade na hora de executar a rotina adjustLiftedAngles
function layDown(liftedJoint)
    for k=1, M1, 1 do
        v = ((-1)^k)*(math.pi/45)
        if not(liftedJoint == k) and not(liftedJoint == k-1) then
            sim.setJointTargetPosition(joints_pitch[k],v)
        end
    end
end




function hangingModule(liftedJoint)
    v = -alpha + 2*phi2
    sim.setJointTargetPosition(joints_pitch[liftedJoint],v)
    v = phi2
    sim.setJointTargetPosition(joints_pitch[liftedJoint+1],v)
    phi2 = phi2 + math.pi/360   
end

------------------------------------funcoes pitchyaw---------

function createBase()
    sim.setJointTargetPosition(joints_yaw[M1], phi)
    sim.setJointTargetPosition(joints_yaw[M1-1], phi)
    phi = phi - math.pi/passo
end

function alteraBase()
    v = phi - math.pi/2
    sim.setJointTargetPosition(joints_yaw[M1], v)
    sim.setJointTargetPosition(joints_yaw[M1-1], v)
    sim.setJointTargetPosition(joints_yaw[3], phi)
    sim.setJointTargetPosition(joints_yaw[1], phi)
    phi = phi + math.pi/passo
end

--ajusta juntas dos modulos levantados, em 360 passos, atuar os motores diretamente causa instabilidade
function adjustLiftedAngles(liftedJoint)
    v = phi2
    if liftedJoint > 0 and liftedJoint < 10 then
        sim.setJointTargetPosition(joints_pitch[liftedJoint],v)
    end
    v = -alpha + phi2
    if liftedJoint-2 > 0  and liftedJoint-2 < 10 then
        sim.setJointTargetPosition(joints_pitch[liftedJoint-2],v)
    end
    v = alpha - 2*phi2
    if liftedJoint-1 > 0 and liftedJoint-1 < 10 then
        sim.setJointTargetPosition(joints_pitch[liftedJoint-1],v)
    end
    phi2 = phi2 + math.pi/360   
end

function adjustYawAngles(liftedJoint)
    v = phi2
    if liftedJoint > 0 and liftedJoint < 10 then
        sim.setJointTargetPosition(joints_yaw[liftedJoint],v)
    end
    v = -math.pi/2 + phi2
    if liftedJoint-2 > 0  and liftedJoint-2 < 10 then
        sim.setJointTargetPosition(joints_yaw[liftedJoint-2],v)
    end
    v = math.pi/2 - 2*phi2
    if liftedJoint-1 > 0 and liftedJoint-1 < 10 then
        sim.setJointTargetPosition(joints_yaw[liftedJoint-1],v)
    end
    phi2 = phi2 + math.pi/360 
end

    
    