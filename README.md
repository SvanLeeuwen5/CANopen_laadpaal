# CANopen_laadpaal

## install

pip install python-can  
pip install canopen  

## Info
https://python-can.readthedocs.io/en/stable/  
https://canopen.readthedocs.io/en/latest/

## Setup

```{,python}

'''
CANopen_network.py
channel en bitrate zijn nog niet getest
'''
self.bus = VectorBus(channel=0, bitrate=250000)
self.connect(bustype='vector', channel=0, bitrate=250000)

```

## Tutorial

```{, python}

'''
De gegevens uit node.py zijn uit te lezen in main.py
doormiddel van network.laadpaal.{variabele}
bijvoorbeeld:
'''
print(network.laadpaal.AC_Input_Current)
'''
En te schrijven door network.laadpaal.{variabele} = {waarde}
'''
network.laadpaal.Power_Module_Enable = "Enabled"

```
