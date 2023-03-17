import canopen
from can.interfaces.vector import VectorBus
import CANopen_network as cn

def main():
    network = cn.network()
    print(network.laadpaal.AC_Input_Current)


if __name__ == '__main__':
    main()