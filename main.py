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
    N = formula.getVarCount()
    
    agenda = CAP()
    for i in range(In):
        agenda.push(Evento("mut", 0, i))
        agenda.push(Evento("melh", 0, i))
    
    currentTime = 0
    currentEvent = Evento("reg", 0, None)
    # Verificar se vale a pena meter current_kind e current_id.
    
    while(currentTime < TFim and bestCoef[0] < ):
        
        if currentEvent.kind == "mut":
            individuo = populacao.getIndividuo(currentEvent.getId())
            newValoracao = individuo.getValoracao()
            for i in range(N):
                if individuo.actv.get(i) and random() < individuo.getPrMut():
                    newValoracao.flip(i)
            newCoef = formula.evaluate(newValoracao)
            if newCoef >= individuo.getCoef():
                individuo.memorize(individuo.getValoracao())
                individuo.setValoracao(newValoracao)
                individuo.setCoef(newCoef)
                if newCoef > bestCoef:
                    bestValoracao = newValoracao
                    bestCoef = newCoef
            agenda.push(Evento("mut", currentTime + expRandom(TMut), individuo.id))
        
        elif currentEvent.kind == "melh":

            individuo = populacao.getIndividuo(currentEvent.getId())
            newValoracao = individuo.getValoracao()
            for i in numpy.random.permutation(N):
                if individuo.actv.get(i):
                    newValoracao.flip(i)
                    if formula.evaluate(newValoracao) < individuo.getCoef():
                        newValoracao.flip(i)
            newCoef = formula.evaluate(newValoracao)
            individuo.memorize(individuo.getValoracao())
            individuo.setValoracao(newValoracao)
            individuo.setCoef(newCoef)
            if newCoef > bestCoef:
                bestValoracao = newValoracao
                bestCoef = newCoef
            agenda.push(Evento("melh", currentTime + expRandom(TMelh), individuo.id))
        
        elif currentEvent.kind == "reg":

 



        currentEvent = agenda.top()
        currentTime = currentEvent.getTime()

    return 
        
        
        
    