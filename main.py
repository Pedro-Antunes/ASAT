from math import log
from random import random

import numpy

from cap import CAP
from evento import Evento
from formula import Formula
from populacao import Populacao


def expRandom(m):
    return -m*log(random())   


def simulador(TFim, TReg, TMelh, TMut, In, path):
    
    formula = Formula(path)
    N = formula.getVarCount()
    
    # Verificar se não estamos a atrofiar camadas
    populacao = Populacao()
    for _ in range(In):
        firstValoracao = Valoracao()
        for i in range(N):
            if random() < 0.5:
                firstValoracao.flip(i)
        populacao.create(firstValoracao)
    
    for individuo in populacao.getAll():
        individuo.setCoef(formula.evaluate(individuo.getValoracao()))

    agenda = CAP()
    for individuo in populacao.getAll():
        
        agenda.add(Evento("mut", 0, individuo.getId()))
        agenda.add(Evento("melh", 0, individuo.getId()))
    agenda.add(Evento("reg", 0, None))

    currentEvent = agenda.next()
    currentTime = currentEvent.getTime()
    
    while currentTime < TFim:
        
        if currentEvent.getKind() == "mut":
            individuo = populacao.getIndividuo(currentEvent.getTarget())
            newValoracao = individuo.getValoracao()
            for i in range(N):
                if not individuo.isLocked(i) and random() < individuo.getPrMut():
                    newValoracao.flip(i)
            newCoef = formula.evaluate(newValoracao)
            if newCoef >= individuo.getCoef():
                individuo.memorize(individuo.getValoracao())
                individuo.setValoracao(newValoracao)
                individuo.setCoef(newCoef)

            agenda.add(Evento("mut", currentTime + expRandom(TMut), individuo.getId()))
        
        elif currentEvent.getKind() == "melh":

            individuo = populacao.getIndividuo(currentEvent.getTarget())
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

            agenda.add(Evento("melh", currentTime + expRandom(TMelh), individuo.getId()))
        
        elif currentEvent.getKind() == "reg":

            for individuo in populacao.getAll():
                if individuo.valCount() >= 10:
                    if individuo.uniqueValCount() < 3:
                        # Rever isto <--
                        colonizer =  populacao.getRandomOther(individuo.getId())
                        newValoracao = colonizer.getValoracao()
                        for i in numpy.random.permutation(N):
                            newValoracao.flip(i)
                            if formula.evaluate(newValoracao) < colonizer.getCoef():
                                newValoracao.flip(i)
                        newIndividuo = Individuo(id, newValoracao)
                        newIndividuo.setCoef(formula.evaluate(newValoracao))
                        populacao.colonize(id, newIndividuo)
                    else:
                        individuo.lock()
                        individuo.forget()
                        individuo.setPrMut(individuo.getActvCount() / (2 * N))

            agenda.add(Evento("reg", currentTime + expRandom(TReg), None))

        agenda.remove()
        currentEvent = agenda.next()
        currentTime = currentEvent.getTime()

    return ...

simulador(1000, 1, 1, 1, 100, "uf250-01.cnf")
