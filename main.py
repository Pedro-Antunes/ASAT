from random import random

import numpy

eps = 1e-08

def expRandom(m):
    return -m*log(random())   

def simulador(TFim, TReg, TMelh, TMut, In, path):
    
    populacao = Populacao(In)
    formula = Formula(path)
    bestValoracao = Valoracao()
    bestCoef = 0
    N = formula.varCount
    
    agenda = CAP()
    for i in range(In):
        agenda.push(Evento("mut", 0, i))
        agenda.push(Evento("melh", 0, i))
    
    currentTime = 0
    currentEvent = Evento("reg", 0, None)
    # Verificar se vale a pena meter current_kind e current_id.
    
    while(currentTime < TFim and bestCoef < 1 - eps):
        
        if currentEvent.kind == "mut":
            individuo = populacao.getIndividuo(currentEvent.id)
            newValoracao = individuo.valoracao
            for i in range(N):
                if individuo.actv.get(i) and random() < individuo.PrMut:
                    newValoracao.flip(i)
            newCoef = formula.evaluate(newValoracao)
            if newCoef >= individuo.coef:
                individuo.mem.append(individuo.valoracao)
                individuo.valoracao = newValoracao
                individuo.coef = newCoef
                if newCoef > bestCoef:
                    bestValoracao = newValoracao
                    bestCoef = newCoef
            agenda.push(Evento("mut", currentTime + expRandom(TMut), individuo.id))
        
        elif currentEvent.kind == "melh":

            individuo = populacao.getIndividuo(currentEvent.id)
            newValoracao = individuo.valoracao
            for i in numpy.random.permutation(N):
                if individuo.actv.get(i):
                    newValoracao.flip(i)
                    if formula.evaluate(newValoracao) < individuo.coef:
                        newValoracao.flip(i)
            newCoef = formula.evaluate(newValoracao)
            individuo.mem.append(individuo.valoracao)
            individuo.valoracao = newValoracao
            individuo.coef = newCoef
            if newCoef > bestCoef:
                bestValoracao = newValoracao
                bestCoef = newCoef
            agenda.push(Evento("melh", currentTime + expRandom(TMelh), individuo.id))
        
        elif currentEvent.kind == "reg":

            for i in range(In):
                individuo = populacao.getIndividuo(i)
                if len(individuo.mem) >= 10:
                    setValr = set()
                    for valr in individuo.mem:
                        setValr.add(valr)
                    if len(setValr) < 3:

                    else:



        currentEvent = agenda.top()
        currentTime = currentEvent.time

    return 
        
        
        
    