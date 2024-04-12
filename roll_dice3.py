import random
dice_noList=[4,3,2,6,3,6,5,6,1,1,4,6,6,5,2]
def roll_dice3(player_):
    i=random.randint(0,14)
    print()
    print(dice_noList[i],"comes for player",player_)
    print()
    if dice_noList[i]==6:
        print("You have got three consecutive six, so 0 point gained this time")
        return 0
    else:
        return dice_noList[i]
