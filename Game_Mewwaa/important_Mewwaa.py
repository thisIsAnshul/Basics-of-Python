#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Author: Ewa Zalewska
# Concept: Simple terminal game
# Github: https://github.com/Mewwaa


import random

class Spell:
    def __init__(self, name, cost, dmg, magic_type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.magic_type = magic_type

    def generate_damage(self):
        min_wartosc = self.dmg - 15
        max_martosc = self.dmg + 15
        return random.randrange(min_wartosc,max_martosc)

class Item:
    def __init__(self, name, itemType, description, prop):
        self.name = name
        self.itemType = itemType
        self.description = description
        self.prop = prop

class specialItem:
    def __init__(self, name, specialItemType, description, prop):
        self.name = name
        self.specialItemType = specialItemType
        self.description = description
        self.prop = prop

class Person:
    def __init__(self, name, hp, mp, dmg, magic, items, specialItems):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.dmg = dmg
        self.magic = magic
        self.items = items
        self.maxhp = hp
        self.maxmp = mp
        self.actions = ["Attack", "Magic", "Items", "Special Items", "Give up"]
        self.specialItems = specialItems

    def generate_damage(self):
        min_wartosc = self.dmg - 15
        max_martosc = self.dmg + 15
        return random.randrange(min_wartosc,max_martosc)

    def generate_spell_damage(self, i):
        min_wartosc = self.magic[i]["dmg"] - 5
        max_martosc = self.magic[i]["dmg"] + 5
        return random.randrange(min_wartosc,max_martosc)
    
    def take_damage(self, dmg_loss):
        if (self.hp - dmg_loss < 0):
            self.hp = 0
        else:
            self.hp -= dmg_loss

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def reduce_mp(self, mp_loss):
        self.mp -= mp_loss

    def choose_action(self):
        i=1
        for action in self.actions:
            print(i, action)
            i+=1

    def heal(self, increased_hp):
        if(self.hp+increased_hp > self.maxhp):
            self.hp = self.maxhp
        else:
            self.hp += increased_hp

    def choose_magic(self):
        i=1
        print("Magic")
        for magicItem in self.magic:
            print(i, "Name:", magicItem.name, "-- cost: ", magicItem.cost, "--dmg: ", magicItem.dmg, "--type:", magicItem.magic_type)
            i+=1

    def choose_target(self, enemies):
        i=1
        for enemy in enemies:
            print(str(i) + ":", enemy.name, "hp:", enemy.hp)
            i+=1 
        choice = int(input("Choose target:")) - 1
        return choice

    def choose_item(self):
        i=1
        print("Items")
        for item in self.items:
            print(i, item["item"].name,"(description:", str(item["item"].description) + ", quantity: ", str(item["quantity"]), ")")
            i+=1


    def choose_specialItem(self):
        i=1
        print("Special items")
        for specialItem in self.specialItems:
            print(i, specialItem["item"].name,"(description:", str(specialItem["item"].description) + ", quantity: ", str(specialItem["quantity"]), ")")
            i+=1