from random

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
        agenda.add(Evento("mut", 0, i))
        agenda.add(Evento("melh", 0, i))
    agenda.add(Evento("reg", 0, None))

    currentEvent = agenda.next()
    currentTime = currentEvent.getTime()
    # Verificar se vale a pena meter current_kind e current_id.
    
    while(currentTime < TFim and bestCoef[0] < bestCoef[1]):
        
        if currentEvent.kind == "mut":
            individuo = populacao.getIndividuo(currentEvent.getId())
            newValoracao = individuo.getValoracao()
            for i in range(N):
                if individuo.getActv().get(i) and random() < individuo.getPrMut():
                    newValoracao.flip(i)
            newCoef = formula.evaluate(newValoracao)
            if newCoef >= individuo.getCoef():
                individuo.memorize(individuo.getValoracao())
                individuo.setValoracao(newValoracao)
                individuo.setCoef(newCoef)
                if newCoef > bestCoef:
                    bestValoracao = newValoracao
                    bestCoef = newCoef
            agenda.add(Evento("mut", currentTime + expRandom(TMut), individuo.id))
        
        elif currentEvent.kind == "melh":

            individuo = populacao.getIndividuo(currentEvent.getId())
            newValoracao = individuo.getValoracao()
            for i in numpy.random.permutation(N):
                if individuo.getActv().get(i):
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
        
        
        
    