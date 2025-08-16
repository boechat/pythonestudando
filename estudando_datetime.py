#### LIDANDO COM DATA, HORA E FUSO HORARIO
## Usando módulo datetime
# Datetime é usado para lidar com datas e horas. Possui varias classes uteis como date, time e timedelta

import datetime
d = datetime.date(2023,7,19)
print(d)
print('--------------------')

## pra usar somente date 

from datetime import date
datado = date(2023, 7, 10)
print(datado)

# Hoje
print('--------------------')
print(date.today())

# Date time - pega horario também
from datetime import date, datetime, time
print('--------------------')
print(datetime.today())
print(datetime.now())
data_hora = datetime(2023, 7 , 10, 10, 30, 20)
print(data_hora)
e = datetime.now().time()
print(e)


print('--------------------')
# Manipulação data e Horas no Python  !!!!  TIMEDELTA  !!!

import datetime
# Criando data e hora
d = datetime.datetime(2023, 7 , 19, 13, 45)
print(d)

# Adcionando uma semana
d = d + datetime.timedelta(weeks=1)
print(d)

# Adcionando uma hora, 30 min, 2 dias
d = d + datetime.timedelta(hours=1, minutes = 30, days = 2)
print(d)

print('--------------------')
from datetime import timedelta, datetime

tipo_carro = 'p'
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
## UTC NOW traz o fuso horario
#data_atual = datetime.utcnow()
data_atual = datetime.now()

tipo_carro = input('Diga tipo do carro')

if tipo_carro =='p':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'|Data_atual : {data_atual} |\n| Data de Entrega Estimada para Tipo de Carro "{tipo_carro.upper()}" = {data_estimada}|')
elif tipo_carro =='m':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'|Data_atual : {data_atual} |\n| Data de Entrega Estimada para Tipo de Carro "{tipo_carro.upper()}" = {data_estimada}|')
elif tipo_carro =='g':
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'|Data_atual : {data_atual} |\n| Data de Entrega Estimada para Tipo de Carro "{tipo_carro.upper()}" = {data_estimada}|')
else:
    print('Carro nao identificado')
    
##################### FORMATANDO E CONVERTENDO DATAS COM STRFTIME STRPTIME
    print('-------------------------------------')
#strftime - string format time
#srtptime - string parse time
import datetime 

d = date(2023, 7, 10)
print(datado)

print(d.strftime('%d/%m/%Y %H:%M'))

####### Convertendo string para datetime 
date_string = '20/07/2023 15:30'

d=datetime.datetime.strptime(date_string, '%d/%m/%Y %H:%M')
print(d)

from datetime import datetime
### Strftime pode cortar parte do datetime
mascara_ptbr = '%d/%m/%Y %a' #%a = dia da semana
data_agora = datetime.now()
data_str = '2024-13-12 10:20'
mascara_en = '%Y-%d-%m %H:%M'
print('-------------------')
print(datetime.strptime(data_str, mascara_en))
print(data_agora.strftime(mascara_ptbr))

print('\n-------------------------------------- FUSO HORARIO / TIMEZONE --------------------------------------')
###### Trabalhando com Antecedencia
# Quando trabalhamos com data e hora, lidar com fusos horarios é uma necessidade comum. Python facilita isso através do módulo 'pytz'

## pip install pytz
import datetime
import pytz

# Criando datetime com timezone
d = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
print('Date time e TimeZone',d)  
# Pode ser acessado a lista de timezones em en.wikipedia.org/wiki/List_of_tz_database_time_zones
# boa pratica olhar o Relogio Utc no google
#################################

from datetime import datetime, timezone
import pytz

# Agora em UTC
data_utc = datetime.now(timezone.utc)

# Agora em Oslo convertido a partir do UTC
oslo_tz = pytz.timezone("Europe/Oslo")
data_oslo = data_utc.astimezone(oslo_tz)

# Diferença de horas e minutos entre Oslo e UTC
diferenca = data_oslo - data_utc
diferenca_horas = int(diferenca.total_seconds() // 3600)
diferenca_minutos = int((diferenca.total_seconds() % 3600) // 60)

print("UTC AGORA:   ", data_utc.strftime("%H:%M"))
print("HORA EM OSLO:", data_oslo.strftime("%H:%M"))
print(f"Diferença: {diferenca_horas}h {diferenca_minutos}min")

print('------------------')

from datetime import datetime
import pytz

# Timezone de Oslo
oslo_tz = pytz.timezone("Europe/Oslo")
data_oslo = datetime.now(oslo_tz)

# Diferença de Oslo para UTC em horas
diferenca_horas = data_oslo.utcoffset().total_seconds() / 3600

print("HORA EM OSLO:", data_oslo.strftime("%H:%M"))
print(f"Diferença para UTC: {diferenca_horas:.0f}h")

#####################




