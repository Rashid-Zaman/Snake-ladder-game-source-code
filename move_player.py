dict={99:1,65:40,25:9,70:93,60:83,13:42}
def move_token(dice_num,old_position):
    current_pos=dice_num+old_position
    if current_pos>100:
        return old_position
    if current_pos in dict.keys():
        current_pos=dict[current_pos]
    return current_pos
    
