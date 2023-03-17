import canopen

class laadpaal(canopen.RemoteNode):
    def __init__(self, node_id, object_dictionary):
        super().__init__(node_id, object_dictionary)

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
    def Available_power(self):
        return self.sdo[0x214B].raw     

    @property
    def Maximum_DC_current(self):
        return self.sdo[0x214D].raw 
    
    @Maximum_DC_current.setter
    def Maximum_DC_current(self, Maximum_DC_current):
        self.sdo[0x214D].raw = Maximum_DC_current   

      
    

    
