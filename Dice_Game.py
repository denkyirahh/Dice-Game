# -*- coding: utf-8 -*-
""" 
Created on Wed Mar 15 17:13:53 2023

@author: asoma
"""
import random
''' DECK???
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
random.shuffle(list1)
print(list1)
'''
class Dice_Game:
    def __init__(self):
        ''' START OF THE DICE GAME '''
        print("DICE GAME")
        print('ENTER "Y" TO PLAY OR "N" TO STOP')
        play = input()
        print()
        #play = "y"
        while play == "Y" or play =="y":
            enemy_health = 10
            self.__enemy_health = enemy_health
            player_health = 10
            self.__player_health = player_health
            
            while self.__player_health > 0 and self.__enemy_health > 0:
                enemy1_six_die = random.randint(1, 6)
                enemy2_six_die = random.randint(1, 6)
                enemy3_six_die = random.randint(1, 6)
                enemy_list = [enemy1_six_die, enemy2_six_die, enemy3_six_die]
                self.__enemy_list = enemy_list
        
                player1_six_die = random.randint(1, 6)
                player2_six_die = random.randint(1, 6)
                player3_six_die = random.randint(1, 6)
                player_list = [player1_six_die, player2_six_die, player3_six_die]
                self.__player_list = player_list
            
                self.display_stats()
                self.get_player_attack()
                self.get_player_defend()
                self.get_enemey_stats()
                self.calculate()
                self.results()
            
            if self.__player_health <= 0: print("player lost")
            if self.__enemy_health <= 0: print("PLAYER WON")
            
            print('ENTER "Y" TO KEEP PLAYING OR "N" TO STOP')
            play = input()
        
    def get_player_attack(self):
        print('ENTER ONE OF YOUR NUMBERS TO ATTACK')
        #GETS THE player ATTACK
        player_attack_attempt = False
        while player_attack_attempt == False:
            player_attack = int(input())
            self.__player_attack = player_attack
            for x in self.__player_list:
                if self.__player_attack == x:
                    self.__player_list.remove(x)
                    player_attack_attempt = True
                    break
            if player_attack_attempt != True:
                print("Enter one of your numbers to attack.")
                print(self.__player_list)

    def get_player_defend(self):
        print('ENTER ONE OF YOUR NUMBERS TO DEFEND')
        print(self.__player_list)
        #GETS THE player DEFEND
        player_defend_attempt = False
        while player_defend_attempt == False:
            player_defend = int(input())
            self.__player_defend = player_defend
            for x in self.__player_list:
                if self.__player_defend == x:
                    self.__player_list.remove(x)
                    player_defend_attempt = True
                    break
            if player_defend_attempt != True: 
                print("Enter one of your numbers to defend.")
                print(self.__player_list)
                
    def get_enemey_stats(self):
        enemy_attack = 0
        enemy_defend = 0
        self.__enemy_attack = enemy_attack
        self.__enemy_defend = enemy_defend
        #Focus on attack
        #GETS THE enemy ARRACK
        self.__enemy_attack = max(self.__enemy_list)
        self.__enemy_list.remove(self.__enemy_attack)
        #GETS THE enemy DEFEND
        self.__enemy_defend = max(self.__enemy_list)
        self.__enemy_list.remove(self.__enemy_defend)
        
    def calculate(self):
        temp_attack = 0
        temp_attack = self.__enemy_attack - self.__player_defend
        
        if temp_attack > 0: self.__player_health = self.__player_health - temp_attack

        temp_attack = 0
        temp_attack = self.__player_attack - self.__enemy_defend
        if temp_attack > 0: self.__enemy_health = self.__enemy_health - temp_attack
            
        if self.__player_health < 0: self.__player_health = 0    
        if self.__enemy_health < 0: self.__enemy_health = 0
    
    def display_stats(self):
        print("ENEMY", "HEALTH:", self.__enemy_health)
        print("DICE", self.__enemy_list),print()
        print("player", "health:",self.__player_health)
        print("dice:",self.__player_list),print()
            
    def results(self):
        '''END OF DICE GAME '''
        print("ENEMY", "HEALTH:", self.__enemy_health)
        print(self.__enemy_attack, "STRENGTH", self.__enemy_defend, "DEFENCE"),print()
        print("player", "health:",self.__player_health)
        print(self.__player_attack, "STRENGTH", self.__player_defend, "DEFENCE"),print()

Dice_Game()
