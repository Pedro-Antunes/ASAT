import random

def expRandom(m):
    return -m*log(random())   

def simulador(TFim, TReg, TMelh, TMut, In, path):
    
    populacao = Populacao(In)
    formula = Formula(path)
    
    agenda = CAP()
    for i in range(In):
        agenda.push(Evento("mut", 0, i))
        agenda.push(Evento("melh", 0, i))
    agenda.push(Evento("reg", 0, None))
    
    current_time = 0
    current_event = agenda.top()
    # Verificar se vale a pena meter current_kind e current_id.
    
    while(current_time < TFim):
        
        if current_event.kind == "mut":
            for i in range(formula.var_count):
                if expRandom(populacao(current_event.id).PrMut):
                    
                    
            
        
        elif current_event.kind == "melh":
            
        
        elif current_event.kind == "reg":
            
            
    return 
        
        
        
    