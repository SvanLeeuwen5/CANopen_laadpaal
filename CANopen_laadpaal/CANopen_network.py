import canopen
from can.interfaces.vector import VectorBus
from node import laadpaal
import os, sys
from pathlib import Path

class network(canopen.Network):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.bus = VectorBus(channel=0, bitrate=250000)
        self.connect(bustype='vector', channel=0, bitrate=250000)    
        eds = os.path.join(Path(sys.path[0]).parent, "V2G500V30A.eds")
        self.laadpaal = laadpaal(node_id=48, object_dictionary=eds)
        self.add_node(self.laadpaal)