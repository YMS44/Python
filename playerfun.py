from playerclass import *
Team={}
sumcharge=0
lst_team = []
#add new employee in the dictionary
def addnewplayer():
    pn=input("enter player name:")
    ps=input("enter player specification:")
    pc=int(input("enter charges:"))
    ptn=input("enter team name:")
    pobj=Player(Player.count,pn,ps,pc,ptn)
    lst_team.append(pobj)
    Team[pobj.get_tname()].extend(lst_team)

def deleteteam(ch):
    j=Team.pop(ch,-1)
    if j==-1:
        print("team not found!!!")
    else:
        print("team deleted succesfully!!!")
    
def modifycharges(pid):
    for i in Team.values():
        if i.get_pid() == pid:
            n_cha = int(input("Enter new charges : "))
            i.set_charges(n_cha)
            print("charges updated succesfully!!!")
        else:
            print("Palyer ID does not exists :\ ")

def calcchanges(tname):
    for i in Team.values():
        if i.get_tname() == tname:
            print(i.get_charges())
        else:
            print("team not found!!!")
            
    


def displayall():
        for v in Team.values():
            print(v)
            
