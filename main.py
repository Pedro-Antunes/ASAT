from random import random

import numpy

eps = 1e-08

def expRandom(m):
    return -m*log(random())   

def simulador(TFim, TReg, TMelh, TMut, In, path):
    
    populacao = Populacao(In)
    formula = Formula(path)
    N = formula.getVarCount()

    bestValoracao = Valoracao()
    bestCoef = (0, N)
    
    agenda = CAP()
    for individuo in populacao.getAll():
        individuo.setCoef(formula.evaluate(individuo.getValoracao))
        agenda.add(Evento("mut", 0, individuo.getId()))
        agenda.add(Evento("melh", 0, individuo.getId()))
    agenda.add(Evento("reg", 0, None))

    currentEvent = agenda.next()
    currentTime = currentEvent.getTime()
    
    while(currentTime < TFim and bestCoef[0] < bestCoef[1]):
        
        if currentEvent.kind == "mut":
            individuo = populacao.getIndividuo(currentEvent.getId())
            newValoracao = individuo.getValoracao()
            for i in range(N):
                if not individuo.isLocked(i) and random() < individuo.getPrMut():
                    newValoracao.flip(i)
                    #O Antunes não gosta
            newCoef = formula.evaluate(newValoracao)
            if newCoef >= individuo.getCoef():
                individuo.memorize(individuo.getValoracao())
                individuo.setValoracao(newValoracao)
                individuo.setCoef(newCoef)
                ##Problema com os coeficientes não inicializados
                if newCoef > bestCoef:
                    bestValoracao = newValoracao
                    bestCoef = newCoef
            agenda.add(Evento("mut", currentTime + expRandom(TMut), individuo.getId()))
        
        elif currentEvent.kind == "melh":

            individuo = populacao.getIndividuo(currentEvent.getId())
            newValoracao = individuo.getValoracao()
            for i in numpy.random.permutation(N):
                if not individuo.isLocked(i):
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
            agenda.add(Evento("melh", currentTime + expRandom(TMelh), individuo.getId()))
        
        elif currentEvent.kind == "reg":

            for individuo in populacao.getAll():
                if individuo.valCount() >= 10:
                    if individuo.uniqueValCount() < 3:
                        individuo = populacao.colonize(individuo.getId())
                        #Maybe
                        individuo.setCoef(formula.evaluate(individuo.getValoracao))
                    else:
                        individuo.lock()
                        individuo.forget()
                        individuo.setPrMut(individuo.getActvCount() / (2 * N))
                    newCoef = individuo.getCoef()
                    if newCoef > bestCoef:
                        bestValoracao = individuo.getValoracao()
                        bestCoef = newCoef
            agenda.add(Evento("reg", currentTime + expRandom(TReg), None))

        agenda.remove()
        currentEvent = agenda.next()
        currentTime = currentEvent.getTime()

    return 
        
        
        
    