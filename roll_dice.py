import random
dice_noList=[4,3,2,6,3,6,5,6,1,1,4,6,6,5,2]
def roll_dice(loop):
    i=random.randint(0,14)
    if loop==0 and dice_noList[i] !=6:
        print("Your counter can move only if 6 comes")
        return 0,0,dice_noList[i]
    else:
        return 1,dice_noList[i],dice_noList[i]
