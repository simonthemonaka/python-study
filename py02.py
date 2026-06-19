
def hp(p, e):
    if p <= 0:
        return False
    elif e <= 0:
        return False
    return True

def main():

    playerhp = 100
    playersheild = 1
    playeratk = 30
    enemyhp = 100

    while hp(playerhp, enemyhp):

        print("enter atk or def")
        a = input("your turn : ")
        if (a == "atk"):
            print('attack the enemy')
            enemyhp -= playeratk
            if enemyhp < 0: break
        elif(a == "def"):
            print("protect yourself")
            playersheild += 1
        print("enemy's turn")
        playerhp -= 20 - playersheild
        print("your hp is ", playerhp)
        print("enemy hp is ", enemyhp)
        print("--------------------")

    if(enemyhp > 0):
        print("your defeat")
    else:
        print("your win")
main()