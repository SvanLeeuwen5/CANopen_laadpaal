import CANopen_network as cn

def main():
    network = cn.network()
    
    network.laadpaal.Power_Module_Enable = 'Enable'


if __name__ == '__main__':
    main()