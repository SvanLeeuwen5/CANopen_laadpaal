import canopen
from can.interfaces.vector import VectorBus
from node import laadpaal

class network(canopen.Network):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.bus = VectorBus(channel=0, unique_hardware_id='', bitrate=0)       #add uhid and bitrate
        self.connect(bustype='vector', channel=0, bitrate=0)                    #add bitrate
        self.laadpaal = laadpaal(node_id=48, object_dictionary=None)            #add object dictionary
        self.add_node(self.laadpaal)
