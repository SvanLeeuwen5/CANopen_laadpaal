# CANopen_laadpaal

## install

pip install python-can
pip install canopen

## Info
https://python-can.readthedocs.io/en/stable/
https://canopen.readthedocs.io/en/latest/

## Tutorial

```{,python}

#connect to network
network = canopen.Network()
network.bus = IXXATBus(channel=0, unique_hardware_id='HW604548', bitrate=125000)
network.connect(bustype='ixxat', channel=0, bitrate=125000)

#connect node
node = canopen.RemoteNode()
network.add_node(network)

#read data
data = node.sdo[0x1017]

#write data
node.sdo[0x1017].raw = data

```