import canopen
from can.interfaces.vector import VectorBus
from node import laadpaal
import os, sys
from pathlib import Path

class network(canopen.Network):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.bus = VectorBus(channel=0, bitrate=500000, app_name='CANopen_network')
        self.connect(bustype='vector', channel=0, bitrate=500000)  
        eds = os.path.join(Path(sys.path[0]).parent, "V2G500V30A.eds")
        self.laadpaal = laadpaal(node_id=48, object_dictionary=eds)
        self.add_node(self.laadpaal)

    def setSetpoint(self, voltage, current):
        """
        Set the setpoint of the laadpaal
        """
        self.laadpaal.DC_Input_Current_Setpoint = current
        self.laadpaal.DC_Input_Voltage_Setpoint = voltage
        self.laadpaal.Power_Module_Enable = 'Enable'

    def getSetpoint(self):
        return self.laadpaal.IDC_setpoint, self.laadpaal.UDC_setpoint

    def disablePower(self):
        self.laadpaal.Power_Module_Enable = 'Disable'

    def getStatus(self):
        for status in self.laadpaal.Power_Module_Status:
            print(status)

    
