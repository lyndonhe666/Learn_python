# 菱形
import string
def make_rhombus(letter):
    full_string = string.ascii_lowercase
    letter_dict = {letter:ind for ind,letter in enumerate(full_string)}
    pos = letter_dict[letter]
    number_of_rows = 2*pos-1
    for row in list(range(pos))+list(range(pos,-1,-1)):
        # print(full_string[:row+1]+full_string[row+1::-1])
        print(f'{full_string[:row]:>{pos}}'+f'{full_string[row::-1]}'+'\n')

# 找不同
def where_is_wired(ary):
    row, col=(len(ary),len(ary[0]))
    letter_dict = {}
    for i in range(row):
        for j in range(col):
            if ary[i][j] not in letter_dict:
                letter_dict[ary[i][j]] = 1
            else:
                letter_dict[ary[i][j]] += 1
    target = [key for key in letter_dict.keys() if letter_dict[key]==1][0]
    
    for i in range(row):
        for j in range(col):
            if ary[i][j] == target:
                print([i+1,j+1])