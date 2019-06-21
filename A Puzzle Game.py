#interchange=[(0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (7, 8), (0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)]
#prime=(2,3,5,7.11,13,17,19)

interchange = [(0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (7, 8), (0, 3), (1, 4),
        (2, 5), (3, 6), (4, 7), (5, 8)]
prime = (2, 3, 5, 7, 11, 13, 17, 19)


def swapping(value,k):
    convert_list=list(value[:])
    convert_list[k[0]],convert_list[k[1]]=convert_list[k[1]],convert_list[k[0]]
    return tuple(convert_list)


def init_play():
    tup=(1,2,3,4,5,6,7,8,9) 
    list_tup=[tup]
    dic_tup={tup:0}
    for value in list_tup:
        for i in [(a, b) for a, b in interchange if value[a]+value[b] in prime]:
            new_value=swapping(value,i)
            if new_value in dic_tup:
                continue
            list_tup.append(new_value)
            dic_tup[new_value]=dic_tup[value]+1
    return dic_tup

my_play=init_play()
for T in range(int(input())):
    blank_line = input()
    play_board_list = [0]*9
    for i in range(0,9,3):
        play_board_list[i],play_board_list[i+1],play_board_list[i+2]=map(int,input().split()) # convert split string to int
    play_board_tuple=tuple(play_board_list)
    if play_board_tuple not in my_play:
        print(-1)
    else:
        print(my_play[play_board_tuple])
