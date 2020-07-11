import time
import datetime
class Tiger:
    name='tiger'
    weight=200
    food='meat'
    def get_weight(self):
        print(self.weight)
    def gain_weight(self):
        self.weight+=10
    def lose_weight(self):
        self.weight-=5
    def yell(self):
        print('Wow!!')
        self.lose_weight()
    def eat(self, food):
        if self.food == food:
            self.gain_weight()
        else:
            self.lose_weight()
            self.lose_weight()
class Goat:
    name='goat'
    weight=100
    food='grass'
    def get_weight(self):
        print(self.weight)
    def gain_weight(self):
        self.weight+=10
    def lose_weight(self):
        self.weight-=5
    def yell(self):
        print('mie~~!!')
        self.lose_weight()
    def eat(self, food):
        if self.food == food:
            self.gain_weight()
        else:
            self.lose_weight()
            self.lose_weight()
class Room:
    def __init__(self, room_number, animal):
        self.room_number = room_number
        self.animal = animal
    def knock(self):
        self.animal.yell()
    def feed(self):
        food = input("请输入需要投喂的食物(grass/meat): ")
        self.animal.eat(food)
        
def play():
    start_time = datetime.datetime.now()
    # 系统随机在10个房间中放入老虎或者羊
    rooms_list = [Room(i, [Tiger(),Goat()][random.randint(0,1)]) for i in range(10)]
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


