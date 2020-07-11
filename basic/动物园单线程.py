import time
import datetime

def play():
    start_time = datetime.datetime.now()
    # 系统随机在10个房间中放入老虎或者羊
    rooms_list = [Room(i, [Cow(),Goat()][random.randint(0,1)]) for i in range(10)]
    finished_rooms = []
    # 然后随机给出房间号，要求游戏者选择敲门还是喂食。
    for i in range(10):
        room = rooms_list[random.randint(0,(9-i))]
        print(f'现在在{room.room_number}号房间')
    # 如果选择喂食：
        choice = input("请选择：feed/knock")
        if choice == 'feed':
            room.feed()
        else:
            room.knock()
            room.feed()
        rooms_list.remove(room)
        finished_rooms.append(room)
        print(f'{i}, 还剩间{len(rooms_list)}房间')
        if (datetime.datetime.now()-start_time).seconds > 3*60:
            print('时间到')
            break
    print('游戏结束：')        
    for room in finished_rooms:
        print(f'{room.room_number} 号房间里的 {room.animal.name} 体重为:{room.animal.weight}')
    if len(rooms_list)>0:
        for room in rooms_list:
            print(f'{room.room_number} 号房间里的 {room.animal.name} 体重为:{room.animal.weight}')
    # 游戏者强记每个房间的动物是什么，以便不需要敲门就可以喂正确的食物。 
    # 游戏3分钟结束后，显示每个房间的动物和它们的体重。

if __name__ == '__main__':
    play()