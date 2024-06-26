from playerfun import *            

choice=0    
while choice!=6:
        choice=int(input("""
1. Add Player
2. Delete Team
3. Modify charges by ID
4. Display toatl charge of a particular team
5. Display all players
6. Exit
Enter your choice:"""))

        match choice:
            case 1:
                addnewplayer()
            case 2:
                ch=input("Enter the team name to delete:")
                deleteteam(ch)
            case 3:
                pid=int(input("Enter player id to modify charges:"))
                modifycharges(pid)
            case 4:
                ch=input("Enter the team name to delete:")
                calcchanges(ch)
                
            case 6:
                print("BYE BYE!!!")  
            case 5:
                displayall()

