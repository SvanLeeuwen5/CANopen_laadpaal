import canopen
"""
TODO / Unimplemented:
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
Object 0x2149: UDC setpoint (real)
Object 0x214A: IDC setpoint (real)
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
"""
class laadpaal(canopen.RemoteNode):
    def __init__(self, node_id, object_dictionary):
        super().__init__(node_id, object_dictionary)

    @property
    def Power_Module_Enable(self) -> str:
        if self.sdo[0x2100].bits[0] == 0: #TODO test
            return "Disabled"
        else:
            return "Enabled"
    
    @Power_Module_Enable.setter
    def Power_Module_Enable(self, Power_Module_Enable:str):
        if Power_Module_Enable == "Enable":
            self.sdo[0x2100].raw = 1
        elif Power_Module_Enable == "Disable":
            self.sdo[0x2100].raw = 0
        else:
            print("Error; Value can only be Disable or Enable")      

    @property
    def Power_Module_Status(self) -> list:  #TODO
        returnlist = []
        if self.sdo[0x2101].bits[0] == 1:
            returnlist.append("Charger on")
        else:
            returnlist.append("Charger off")
        if self.sdo[0x2101].bits[1] == 1:
            returnlist.append("Power error")
        if self.sdo[0x2101].bits[2] == 1:
            returnlist.append("Input over voltage detect")
        if self.sdo[0x2101].bits[3] == 1:
            returnlist.append("Input under voltage detect")
        if self.sdo[0x2101].bits[4] == 1:
            returnlist.append("Output over voltage detect")
        if self.sdo[0x2101].bits[5] == 1:
            returnlist.append("Output under voltage detect")
        if self.sdo[0x2101].bits[7] == 1:
            returnlist.append("Over temperature detect")
        if self.sdo[0x2101].bits[8] == 1:
            returnlist.append("Uaux error, UV / OV")
        if self.sdo[0x2101].bits[10] == 1:
            returnlist.append("V2G mode")
        else:
            returnlist.append("CHARGE mode")           
        if self.sdo[0x2101].bits[11] == 1:
            returnlist.append("Grid error (AC voltage, frequency, phase)")
        if self.sdo[0x2101].bits[12] == 1:
            returnlist.append("HW interlock error")
        if self.sdo[0x2101].bits[13] == 1:
            returnlist.append("Service mode enabled")
        return returnlist

    @property
    def Power_Module_Temperature(self):
        return self.sdo[0x2104].raw

    @property
    def AC_Input_Voltage(self):
        return self.sdo[0x2105].raw

    @property
    def AC_Input_Current(self):
        return self.sdo[0x2106].raw

    @property
    def DC_Output_Voltage(self):
        return self.sdo[0x2107].raw   

    @property
    def DC_Output_Current(self):
        return self.sdo[0x2108].raw  
    
    @property
    def DC_Input_Voltage_Setpoint(self):
        return self.sdo[0x2109].raw
    
    @DC_Input_Voltage_Setpoint.setter
    def DC_Input_Voltage_Setpoint(self, DC_Input_Voltage_Setpoint):
        self.sdo[0x2109].raw = DC_Input_Voltage_Setpoint    

    @property
    def DC_Input_Current_Setpoint(self):
        return self.sdo[0x210A].raw 
    
    @DC_Input_Current_Setpoint.setter
    def DC_Input_Current_Setpoint(self, DC_Input_Current_Setpoint):
        self.sdo[0x210A].raw = DC_Input_Current_Setpoint

    @property
    def DC_Bus_Voltage(self):
        return self.sdo[0x210D].raw 
    
    @property
    def Available_power_charge_mode(self):
        return self.sdo[0x214B].raw  
       
    @property
    def Available_power_V2G_mode(self):
        return self.sdo[0x214C].raw
    
    @property
    def Maximum_DC_current(self):
        return self.sdo[0x214D].raw 
    
    @Maximum_DC_current.setter
    def Maximum_DC_current(self, Maximum_DC_current):
        self.sdo[0x214D].raw = Maximum_DC_current   
      



    
