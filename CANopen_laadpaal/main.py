from node import laadpaal
import os, sys
from pathlib import Path

def main():
    eds = os.path.join(Path(sys.path[0]).parent, "V2G500V30A.eds")
    lp = laadpaal(node_id=48, object_dictionary=eds)
    
    lp.setSetpoint(150, 1)
    print(lp.getSetpoint())
    print(lp.Power_Module_Status)
    lp.disablePower()



if __name__ == '__main__':
    main()