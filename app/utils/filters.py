from datetime import datetime

def format_datetime(value):
    if not value:
        return ""
    
    return value.strftime("%d/%m/%Y %H:%M")

def tempo_dentro(value):
    if not value:
        return ""
    
    agora  = datetime.now()
    diff = agora - value

    minutos = int(diff.total_seconds() /60)
    
    if minutos > 60 :
        return f"{minutos} min"
    horas = minutos // 60
    minutos_rest = minutos % 60

    return f"{horas}h {minutos_rest}m"

