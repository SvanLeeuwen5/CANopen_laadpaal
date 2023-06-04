# CANopen_laadpaal

## install

pip install python-can  
pip install canopen  

## Info
https://python-can.readthedocs.io/en/stable/  
https://canopen.readthedocs.io/en/latest/

## Setup
Binnen je eigen .py bestand moeten de volgende onderdelen worden toegevoegd
Eerst het importeren van de modules, daarna het toevoegen van de Object dictionary en het maken van de laadpaal Class.
```{, python}
from node import laadpaal
import os, sys
from pathlib import Path

eds = os.path.join(Path(sys.path[0]).parent, "V2G500V30A.eds")
lp = laadpaal(node_id=48, object_dictionary=eds)
```
## Tutorial

De gegevens zijn uit te lezen door de Class lp.{variabele}
```{, python}
#Lezen 
print(lp.AC_Input_Current)

#Schrijven
lp.Power_Module_Enable = "Enabled"
```

Er zijn ook functies voor het instellen van het setpoint

```{, python}
#Lezen 
lp.setPoint( {voltage} , {current} )

#Schrijven
lp.getSetpoint()
```

## Unimplemented objects
```{, python}
Object 0x2102: Power Module Status Extended
Object 0x210F: Power Module DC Undervoltage Setpoint
Object 0x2121: Power Module AC Input Voltage L1
Object 0x2122: Power Module AC Input Voltage L2
Object 0x2123: Power Module AC Input Voltage L3
Object 0x2124: Power Module AC Input Current L1
Object 0x2125: Power Module AC Input Current L2
Object 0x2126: Power Module AC Input Current L3
Object 0x2130: Warning status
Object 0x2132: Error source
Object 0x2137: Temperature secondary
Object 0x2138: Temperature primary
Object 0x2139: Temperature transformer
Object 0x2139: Temperature heatsink AC
Object 0x214E: Maximum DC current (V2G)
Object 0x2150: Switch OFF reason
Object 0x2151: Module uptime
Object 0x2152: Switch OFF reason timestamp
Object 0x2241: Time to reconnection
Object 0x2242: Reconnect reset reason
Object 0x2552: AC switch-off reason
Object 0x2553: AC switch-off timestamp
Object 0x2FFF: Restart
Object 0x2FF0: Configuration Node ID
```
