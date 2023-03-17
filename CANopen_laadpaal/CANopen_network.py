import canopen
from can.interfaces.vector import VectorBus
from node import laadpaal

class network(canopen.Network):
    def __init__(self, channel=None, bitrate=None, fd=None, **kwargs):
        super().__init__(channel=channel, bitrate=bitrate, fd=fd, **kwargs)
        self.bus = VectorBus(channel=0, unique_hardware_id='', bitrate=0)
        self.connect(bustype='vector', channel=0, bitrate=125000)
        self.laadpaal = laadpaal(node_id=48, object_dictionary=None)#add object dictionary
        self.add_node(self.laadpaal)
