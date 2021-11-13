from math import log
from random import random
import numpy
import copy

from cap import CAP
from evento import Evento
from formula_alt import Formula
from individuo import Individuo
from populacao import Populacao
from valoracao import Valoracao

def expRandom(m):
    return -m*log(random())


def simulador(TFim, TMut, TMelh, TReg, In, path):
    
    formula = Formula(path)
    N = formula.getVarCount()
    C = formula.getClauseCount()

    foundSolution = False
    solution = None
    
    populacao = Populacao()
    for idt in range(In):
        firstValoracao = Valoracao(N)
        for i in range(N):
            if random() < 0.5:
                firstValoracao.flip(i)
        populacao.add(Individuo(idt, firstValoracao))
    
    for individuo in populacao.getAll():
        individuo.setEval(formula.evaluate(individuo.getValoracao()))
        if individuo.getEval() == C:
            foundSolution = True
            solution = individuo.getValoracao()

    agenda = CAP()
    for individuo in populacao.getAll():
        agenda.add(Evento("mut", expRandom(TMut), individuo.getId()))
        agenda.add(Evento("melh", 0, individuo.getId()))
    agenda.add(Evento("reg", expRandom(TReg), None))

    currentEvent = agenda.next()
    currentTime = currentEvent.getTime()

    while currentTime < TFim and not foundSolution:


        if currentEvent.getKind() == "mut":
            
            individuo = populacao.getIndividuo(currentEvent.getTarget())
            newValoracao = copy.deepcopy(individuo.getValoracao())
            
            for i in range(N):
                if not individuo.isLocked(i) and random() < individuo.getPrMut():
                    newValoracao.flip(i)
            newEval = formula.evaluate(newValoracao)

            if newEval >= individuo.getEval():
                individuo.memorize(individuo.getValoracao())
                individuo.setValoracao(newValoracao)
                individuo.setEval(newEval)
                if newEval == C:
                    foundSolution = True
                    solution = newValoracao

            agenda.add(Evento("mut", currentTime + expRandom(TMut), individuo.getId()))
        

        elif currentEvent.getKind() == "melh":

            individuo = populacao.getIndividuo(currentEvent.getTarget())
            newValoracao = copy.deepcopy(individuo.getValoracao())
            newEval = individuo.getEval()
            
            for i in numpy.random.permutation(N):
                if not individuo.isLocked(i):
                    compValoracao = copy.deepcopy(newValoracao)
                    compValoracao.flip(i)
                    compEval = formula.evaluate(compValoracao)
                    if compEval >= newEval:
                        newValoracao = compValoracao
                        newEval = compEval
            individuo.memorize(individuo.getValoracao())
            individuo.setValoracao(newValoracao)
            individuo.setEval(newEval)
            if newEval == C:
                foundSolution = True
                solution = newValoracao

            agenda.add(Evento("melh", currentTime + expRandom(TMelh), individuo.getId()))
        

        elif currentEvent.getKind() == "reg":

            for individuo in populacao.getAll():
                if individuo.valCount() >= 10:

                    if individuo.uniqueValCount() < 3:
                        if In == 1:
                            newValoracao = Valoracao(N)
                            for i in range(N):
                                if random() < 0.5:
                                    newValoracao.flip(i)
                        else:
                            colonizer = populacao.getRandomOther(individuo.getId())
                            if colonizer.valCount() == 0:
                                newValoracao = copy.deepcopy(colonizer.getValoracao())
                            else:
                                newValoracao = copy.deepcopy(colonizer.getRandomMemVal())

                        newEval = formula.evaluate(newValoracao)
                        for i in numpy.random.permutation(N):
                            compValoracao = copy.deepcopy(newValoracao)
                            compValoracao.flip(i)
                            compEval = formula.evaluate(compValoracao)
                            if compEval >= newEval:
                                newValoracao = compValoracao
                                newEval = compEval
                        idt = individuo.getId()
                        newIndividuo = Individuo(idt, newValoracao)
                        newIndividuo.setEval(newEval)
                        populacao.replace(idt, newIndividuo)
                        if newEval == C:
                            foundSolution = True
                            solution = newValoracao

                    else:
                        individuo.lockBits()
                        individuo.forget()
                        individuo.setPrMut(individuo.getActvCount() / (2 * N))

            agenda.add(Evento("reg", currentTime + expRandom(TReg), None))
        
        
        agenda.remove()
        currentEvent = agenda.next()
        currentTime = currentEvent.getTime()
        
    if foundSolution:
        maxEval = C
        bestVal = solution
    else:
        maxEval = -1
        bestVal = solution
        for individuo in populacao.getAll():
            if individuo.getEval() > maxEval:
                maxEval = individuo.getEval()
                bestVal = individuo.getValoracao()
    
    return (maxEval / C, bestVal.display())


#print(simulador(100, 5, 5, 5, 10, "ProblemSet/uf250-1065/uf250-01.cnf"))
