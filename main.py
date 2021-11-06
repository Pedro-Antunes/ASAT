from math import log
from random import random

import numpy

from cap import CAP
from evento_alt import Evento
from formula import Formula
from individuo import Individuo
from populacao import Populacao
from valoracao import Valoracao


def expRandom(m):
    return -m*log(random())


def simulador(TFim, TReg, TMelh, TMut, In, path):
    
    formula = Formula(path)
    N = formula.getVarCount()
    C = formula.getClauseCount()
    
    populacao = Populacao()
    for _ in range(In):
        firstValoracao = Valoracao(N)
        for i in range(N):
            if random() < 0.5:
                firstValoracao.flip(i)
        populacao.create(firstValoracao)
    
    for individuo in populacao.getAll():
        individuo.setEval(formula.evaluate(individuo.getValoracao()))

    agenda = CAP()
    for individuo in populacao.getAll():
        agenda.add(Evento("mut", expRandom(TMut), individuo.getId()))
        agenda.add(Evento("melh", expRandom(TMelh), individuo.getId()))
    agenda.add(Evento("reg", expRandom(TReg), None))

    currentEvent = agenda.next()
    currentTime = currentEvent.getTime()

    foundSolution = None
    
    
    while currentTime < TFim and not foundSolution:
        
        print(currentTime, currentEvent._info[0])

        if currentEvent.getKind() == "mut":
            
            individuo = populacao.getIndividuo(currentEvent.getTarget())
            newValoracao = individuo.getValoracao().copy()
            for i in range(N):
                if not individuo.isLocked(i) and random() < individuo.getPrMut():
                    newValoracao.flip(i)
            newEval = formula.evaluate(newValoracao)
            if newEval >= individuo.getEval():
                individuo.memorize(individuo.getValoracao())
                individuo.setValoracao(newValoracao)
                individuo.setEval(newEval)
                if newEval == C:
                    foundSolution = newValoracao

            agenda.add(Evento("mut", currentTime + expRandom(TMut), individuo.getId()))
        
        elif currentEvent.getKind() == "melh":

            individuo = populacao.getIndividuo(currentEvent.getTarget())
            
            newValoracao = individuo.getValoracao().copy()
            
            for i in numpy.random.permutation(N):
                if not individuo.isLocked(i):
                    compValoracao = newValoracao.copy()
                    compValoracao.flip(i)
                    if formula.evaluate(compValoracao) >= formula.evaluate(newValoracao):
                        newValoracao = compValoracao
            newEval = formula.evaluate(newValoracao)
            individuo.memorize(individuo.getValoracao())
            individuo.setValoracao(newValoracao)
            individuo.setEval(newEval)
            if newEval == C:
                foundSolution = newValoracao

            agenda.add(Evento("melh", currentTime + expRandom(TMelh), individuo.getId()))
        
        elif currentEvent.getKind() == "reg":

            for individuo in populacao.getAll():
                if individuo.valCount() >= 10:
                    if individuo.uniqueValCount() < 3:
                        # Rever isto <--
                        colonizer = populacao.getRandomOther(individuo.getId())
                        newValoracao = colonizer.getValoracao()
                        for i in numpy.random.permutation(N):
                            newValoracao.flip(i)
                            if formula.evaluate(newValoracao) < colonizer.getEval():
                                newValoracao.flip(i)
                        id = individuo.getId()
                        newIndividuo = Individuo(id, newValoracao)
                        newIndividuo.setEval(formula.evaluate(newValoracao))
                        populacao.colonize(id, newIndividuo)
                        if newIndividuo.getEval() == C:
                            foundSolution = newValoracao
                    else:
                        individuo.lockBits(N)
                        individuo.forget()
                        individuo.setPrMut(individuo.getActvCount() / (2 * N))

            agenda.add(Evento("reg", currentTime + expRandom(TReg), None))
        
        print(individuo.getId(), individuo.getEval())
        
        agenda.remove()
        currentEvent = agenda.next()
        currentTime = currentEvent.getTime()
        

    if foundSolution != None:
        return (1, foundSolution.display())
    else:
        maxEval = 0
        bestVal = None
        for individuo in populacao.getAll():
            if individuo.getEval() > maxEval:
                maxEval = individuo.getEval()
                bestVal = individuo.getValoracao()
        return (maxEval / C, bestVal.display())

print(simulador(100, 1000, 10, 10, 3, "ProblemSet/uf20-91/uf20-01.cnf"))


#for i in range(1,100):
    #print(simulador(100, 10, 5, 10, 10, f"ProblemSet/uf50-218/uf50-0{i}.cnf"))
