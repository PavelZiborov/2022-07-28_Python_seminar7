from datetime import datetime as dt
from unittest import result

def Save(data, result):
    time =dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};=;{}\n'
                    .format(data, result))