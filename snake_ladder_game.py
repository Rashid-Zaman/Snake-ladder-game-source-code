import roll_dice
import roll_dice2
import roll_dice3
import move_player
import print_snake_ladder_board
print("----------------------------------------------------------------------------------------")
print("                            Welcome TO Snake Ladder game                                ")
print("----------------------------------------------------------------------------------------")
print()
player=1
curr_pos1,curr_pos2,loop1,loop2=0,0,0,0
while(1):
    if player==1:
        input("Press enter key to roll a dice")
        print()
        loop1,points,dice_no=roll_dice.roll_dice(loop1)
        print(dice_no,"comes for player",player)
        print()
        curr_pos1=move_player.move_token(points,curr_pos1)
        print_snake_ladder_board.print_snake_ladder_board(curr_pos1,curr_pos2,player,player+1)
        if curr_pos1==100:
            print("\n")
            print("player",player,"wins")
            print("Congrats! Player",player)
            print("Hope! You enjoyed the game")
            print("Thank You")
            break
        if points==6:
            input("Press enter key to roll a dice")
            points=roll_dice2.roll_dice2(player)
            curr_pos1=move_player.move_token(points,curr_pos1)
            print_snake_ladder_board.print_snake_ladder_board(curr_pos1,curr_pos2,player,player+1)
            if curr_pos1==100:
                print("\n")
                print("player",player,"wins")
                print("Congrats! Player",player)
                print("Hope! You enjoyed the game")
                print("Thank You")
                break
            if points==6:
                input("Press enter key to roll a dice")
                points=roll_dice3.roll_dice3(player)
                curr_pos1=move_player.move_token(points,curr_pos1)
                print_snake_ladder_board.print_snake_ladder_board(curr_pos1,curr_pos2,player,player+1)
                if curr_pos1==100:
                    print("\n")
                    print("player",player,"wins")
                    print("Congrats! Player",player)
                    print("Hope! You enjoyed the game")
                    print("Thank You")
                    break
    if player==2:
        input("Press enter key to roll a dice")
        print()
        loop2,points,dice_no=roll_dice.roll_dice(loop2)
        print(dice_no,"comes for player",player)
        print()
        curr_pos2=move_player.move_token(points,curr_pos2)
        print_snake_ladder_board.print_snake_ladder_board(curr_pos2,curr_pos1,player,player-1)
        if curr_pos2==100:
            print("\n")
            print("player",player,"wins")
            print("Congrats! Player",player)
            print("Hope! You enjoyed the game")
            print("Thank You")
            break
        if points==6:
            input("Press enter key to roll a dice")
            points=roll_dice2.roll_dice2(player)
            curr_pos2=move_player.move_token(points,curr_pos2)
            print_snake_ladder_board.print_snake_ladder_board(curr_pos2,curr_pos1,player,player-1)
            if curr_pos2==100:
                print("\n")
                print("player",player,"wins")
                print("Congrats! Player",player)
                print("Hope! You enjoyed the game")
                print("Thank You")
                break
            if points==6:
                input("Press enter key to roll a dice")
                points=roll_dice3.roll_dice3(player)
                curr_pos2=move_player.move_token(points,curr_pos2)
                print_snake_ladder_board.print_snake_ladder_board(curr_pos2,curr_pos1,player,player-1)
                if curr_pos2==100:
                    print("\n")
                    print("player",player,"wins")
                    print("Congrats! Player",player)
                    print("Hope! You enjoyed the game")
                    print("Thank You")
                    break
    if player==1:
        player=2
    else:
        player=1
                
        




    
