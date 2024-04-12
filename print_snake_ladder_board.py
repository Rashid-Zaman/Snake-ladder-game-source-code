lst=list()
for i in range(100,0,-1):
    lst.append(i)
def print_snake_ladder_board(current_position1,current_position2,player_1,player_2):
    for i in range(0,100,10):
        if i%2==0:
            value=lst[i]
            if i==90:
                for j in range(1,11):
                    if value==current_position1 and current_position1!=current_position2:
                        print("#P",player_1,end="       ")
                    elif value==current_position2 and current_position1!=current_position2:
                        print("#P",player_2,end="       ")
                    elif value==current_position1 and value==current_position2:
                        print("**",end="       ")
                    else:
                        if value==99 or value==65 or value==25:
                            print("\U0001F40D",end="       ")
                        elif value==70 or value==60 or value==13:
                            print("\U0001FA9C",end="       ")
                        else:
                            print(value,end="         ")
                    value=value-1
                print("\n")
            else:
                for j in range(1,11):
                    if value==current_position1 and current_position1 and current_position1!=current_position2:
                        print("#P",player_1,end="       ")
                    elif value==current_position2 and current_position1 and current_position1!=current_position2:
                        print("#P",player_2,end="       ")
                    elif value==current_position1 and value==current_position2:
                        print("**",end="       ")
                    else:
                        if value==99 or value==65 or value==25:
                            print("\U0001F40D",end="      ")
                        elif value==70 or value==60 or value==13:
                            print("\U0001FA9C",end="      ")
                        else:
                            print(value,end="        ")
                    value=value-1
                print("\n")
        else:
            value=lst[i]-9
            for j in range(1,11):
                if value==current_position1 and current_position1 and current_position1!=current_position2:
                    print("#P",player_1,end="       ")
                elif value==current_position2 and current_position1 and current_position1!=current_position2:
                    print("#P",player_2,end="       ")
                elif value==current_position1 and value==current_position2:
                    print("**",end="       ")
                else:
                    if value==99 or value==65 or value==25:
                        print("\U0001F40D",end="      ")
                    elif value==70 or value==60 or value==13:
                        print("\U0001FA9C",end="      ")
                    else:
                        print(value,end="        ")
                value=value+1
            print("\n")
        
