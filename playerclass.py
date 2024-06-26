class Player:
    count=200
    def __init__(self,pid=0,pname='',spe='',charges=0,tname=''):
        Player.count=Player.count+1
        self.__pid=Player.count
        self.__pname=pname
        self.__spe=spe
        self.__charges=charges
        self.__tname=tname
        
    #setter funtions
    def set_pname(self,pname):
        self.__pname=pname
    def set_spe(self,spe):
        self.__spe=spe
    def set_charges(self,charges):
        self.__charges=charges
    def set_tname(self,tname):
        self.__tname=tname
        
    #setter funtions
    def get_pid(self):
        return self.__pid
    def get_pname(self):
        return self.__pname
    def get_spe(self):
        return self.__spe
    def get_charges(self):
        return self.__charges
    def get_tname(self):
        return self.__tname    
        
    
    def __str__(self):
        return f"""
Player ID = {self.__pid} 
Player Name = {self.__pname}
Specialisation = {self.__spe}
Charges = {self.__charges}
Team Name = {self.__tname}"""

mumbai_indians=Player()

