import random
import os
import time

class Forest:
    def __init__(self, number, animal):
        self.number = number
        self.animal = animal

class Soldier:
    def __init__(self, name):
        self.name=name
    def heal(self, hp):
        self.current_life+=hp
        if self.current_life > self.max_life:
            print("超出上限，请出入其他数值")
            self.current_life-=hp
            return 0
        else:
            print(f'{self.name}当前生命值为: {self.current_life}')

class Bowman(Soldier):
    s_type = '1'
    max_life = 100
    cost = 100
    current_life = max_life
    def hit(self,animal):
        if animal=='hawl':
            self.current_life-=20
        if animal=='wolf':
            self.current_life-=80

class Axeman(Soldier):
    s_type = '2'
    max_life = 120
    cost = 120
    current_life = max_life
    def hit(self,animal):
        if animal=='hawl':
            self.current_life-=80
        if animal=='wolf':
            self.current_life-=20

class Player:
    stone=1000
    current_soldier = '暂无选中的雇佣兵'
    soldiers_list = []
    def __init__(self, name):
        self.name = name
    def choose_current_soldier(self):
        name = input("请选择要出战的士兵: ")
        self.current_soldier = [soldier for soldier in self.soldiers_list if soldier.name==name][0]
        self.soldiers_list.remove(self.current_soldier)
        return self.current_soldier
    def get_soldier_back(self):
        self.soldiers_list.append(self.current_soldier)
        self.current_soldier = '暂无选中的雇佣兵'
    def heal(self):
        hp = int(input("请选择需要回复的生命值:(1生命值消耗1灵石)"))
        while hp>self.stone:
            hp=int(input("灵石不足，请重新选择需要回复的生命值:(1生命值消耗1灵石)"))
        if self.current_soldier.heal(hp)!=0:
            self.stone-=hp
        else:
            self.heal()
    def buy_soldier(self):
        while self.stone>=0:
            s_type = input("请选择想要的雇佣兵:\n1:弓兵\n2:斧王\n0:结束挑选: ")
            if s_type=='1':
                name=input("请为这弓兵取名: ")
                soldier = Bowman(name)
                self.soldiers_list.append(soldier)
                self.stone-=soldier.cost
            elif s_type=='2':
                name=input("请为这斧王取名: ")
                soldier = Axeman(name)
                self.soldiers_list.append(soldier)
                self.stone-=soldier.cost
            else:
                return
        print('灵石不足')
        player.stone+=(player.soldiers_list.pop().cost)

def play_one_round(forest, player):
    if len(player.soldiers_list)>0:
        print(f'\n----Now in forest {forest.number}----')
        soldier = player.choose_current_soldier()
        soldier.hit(forest.animal)
        if soldier.current_life>=0:
            print(f'恭喜通过foreset{forest.number}')
            heal=input(f"您当前的灵石数为: {player.stone}\n士兵{soldier.name}的生命值为:{soldier.current_life}\n请选择是否需要治疗{soldier.name}:1(是)/0(否) ")
            if heal=='1':
                player.heal()
            else:
                pass
            # 当前战士归位
            player.get_soldier_back()
            # 提示还有哪些雇佣兵
            print(f'当前还有士兵: {[s.name for s in player.soldiers_list]}')
            return 1
        else:
            print(f'{soldier.name}已阵亡')
            player.current_soldier='暂无选中的雇佣兵'
            play_one_round(forest, player)
    else:
        return 0

def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
      # for windows platfrom
        _ = os.system('cls')

def play_one_round_new(forest, player):
    print(f'\n----Now in forest {forest.number}----')
    soldier = player.choose_current_soldier()
    soldier.hit(forest.animal)
    if soldier.current_life>=0:
        print(f'恭喜通过foreset{forest.number}')
        heal=input(f"您当前的灵石数为: {player.stone}\n士兵{soldier.name}的生命值为:{soldier.current_life}\n请选择是否需要治疗{soldier.name}:1(是)/0(否) ")
        if heal=='1':
            player.heal()
        else:
            pass
        # 当前战士归位
        player.get_soldier_back()
        # 提示还有哪些雇佣兵
        print(f'当前还有士兵: {[s.name for s in player.soldiers_list]}')
        return 1
    else:
        print(f'{soldier.name}已阵亡')
        player.current_soldier='暂无选中的雇佣兵'
        play_one_round(forest, player)
def play():
    forests=[]
    for i in range(7):
        res = random.randint(0,1)
        if res == 0:
            forests.append(Forest(i, 'hawl'))
        else:
            forests.append(Forest(i, 'wolf'))
        print(f'森林{i}的妖怪是:{forests[-1].animal}')
    time.sleep(1)
    screen_clear()
    player = Player('p1')
    player.buy_soldier()
    print(player.current_soldier)
    print(f'当前有雇佣兵: {[s.name for s in player.soldiers_list]}')
    keep=1
    i=0
    while keep==1:
        keep = play_one_round(forests[i], player)
        i+=1
        if i==7:
            print(f'游戏胜利，玩家{player.name}还剩{player.stone}灵石')
            return None
    print('无兵可用，游戏结束')

def play_new():
    forests=[]
    for i in range(7):
        res = random.randint(0,1)
        if res == 0:
            forests.append(Forest(i, 'hawl'))
        else:
            forests.append(Forest(i, 'wolf'))
        print(f'森林{i}的妖怪是:{forests[-1].animal}')
    time.sleep(1)
    screen_clear()
    player = Player('p1')
    player.buy_soldier()
    print(player.current_soldier)
    print(f'当前有雇佣兵: {[s.name for s in player.soldiers_list]}')

    i=0
    while len(player.soldiers_list)>0:
        play_one_round_new(forests[i], player)
        i+=1
        if i==7:
            print(f'游戏胜利，玩家{player.name}还剩{player.stone}灵石')
            return None
    print('无兵可用，游戏结束')




if __name__ == '__main__':
    play()