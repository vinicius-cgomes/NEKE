function sysCall_init()
    sim1 = require('sim')
    
    joints_yaw={-1,-1,-1,-1} --vetor de juntas yaw
    joints_pitch={-1,-1,-1,-1} --vetor de juntas pitch
    M1 = 9 --numero de juntas no mesmo plano
    Manterior = 0 --numero de juntas no chão
    Mposterior = 0 --numero de juntas em cima do degrau 
    loopVariable = 1 --variavel de controle
    stat = -1 --controle da junta a ser levantada
    passo=100 --passos para um ciclo completo da curva de hirose
    ciclos = 4
    H = 35
    phi=0
    phi2 = 0
    v = 0

    --Parametros da curva de Hirose
    a = 15*(math.pi/180)
    c  = 0
    k = 3
    b = 2*math.pi*k




    --reconhecer as juntas pitch e yaw do robô
    for i=1,M1 ,1 do
        joints_yaw[i]=sim.getObject('./yaw',{index=i-1})
        joints_pitch[i]=sim.getObject('./pitch',{index=i-1})
    end
end

function sysCall_actuation()
    if loopVariable < ciclos*passo or stat > 9 then --700 repeticoes, ou seja, 7 ciclos completos da curva de hirose (passo = 100)
        pitchpitchWLifted(stat) --a variavel stat representa a junta que esta com acionada em 90 graus
    elseif loopVariable == ciclos*passo then
        layDown(stat)
    else
        if phi2 < math.pi/2 then
            adjustLiftedAngles(stat) --apos 7 ciclos ajusta as juntas da seguinte forma: stat passa de -pi/2 para 0; stat+1 passa de pi/2 para -pi/2; stat+2 passa de 0 para pi/2
            if stat > M1-3 then
                pitchpitchWLiftedTransition(stat) --continua o movimento pitchpitch enquanto os angulos sao ajustados
            end
        else
            phi2 = 0
            loopVariable = 1
            stat = stat + 1
            if stat < 6 then
                ciclos = ciclos + 1
            else
                ciclos = ciclos-2
            end
        end
    end
    loopVariable = loopVariable + 1
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
            if k == liftedJoint+2 and liftedJoint > 0 then --ajusta angulo para manter pi/2 em relacao ao degrau
                sim.setJointTargetPosition(joints_pitch[k-1], math.pi/2 - v/2)
            end
            print(phi)
        end
    end
    if Mposterior > 1  then
        for k = 1, liftedJoint-1 ,1 do
            v = 2*a*(20/15)*math.sin(b/(2*M1))*math.sin((phi)+(k*b/M1)) -c/M1
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
                sim.setJointTargetPosition(joints_pitch[k-1], math.pi/2 - v/2)
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

--ajusta juntas dos modulos levantados, em 360 passos, atuar os motores diretamente causa instabilidade
function adjustLiftedAngles(liftedJoint)
    v = phi2
    if liftedJoint+2 > 0 and liftedJoint+2 < 10 then
        sim.setJointTargetPosition(joints_pitch[liftedJoint+2],v)
    end
    v = -math.pi/2 + phi2
    if liftedJoint > 0  and liftedJoint < 10 then
        sim.setJointTargetPosition(joints_pitch[liftedJoint],v)
    end
    v = math.pi/2 - 2*phi2
    if liftedJoint+1 > 0 and liftedJoint+1 < 10 then
        sim.setJointTargetPosition(joints_pitch[liftedJoint+1],v)
    end
    phi2 = phi2 + math.pi/360   
end


function hangingModule(liftedJoint)
    v = -math.pi/2 + 2*phi2
    sim.setJointTargetPosition(joints_pitch[liftedJoint],v)
    v = phi2
    sim.setJointTargetPosition(joints_pitch[liftedJoint+1],v)
    phi2 = phi2 + math.pi/360   
end


    
    