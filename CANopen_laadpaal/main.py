import canopen
from can.interfaces.vector import VectorBus

def main():
    network = canopen.Network()
    network.bus = VectorBus(channel=0, unique_hardware_id='', bitrate=0) #TODO
    network.connect(bustype='vector', channel=0, bitrate=125000) #TODO
    node = canopen.RemoteNode(node_id=0, object_dictionary=None) #TODO
    network.add_node(node)

    #read
    data = node.sdo[0x2001].raw 

    #write
    node.sdo[0x2000].raw = 1000
    

if __name__ == '__main__':
    main()