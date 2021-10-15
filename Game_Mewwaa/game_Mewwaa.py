#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Author: Ewa Zalewska
# Concept: Simple terminal game
# Github: https://github.com/Mewwaa



from important_Mewwaa import Item, Person, Spell, specialItem
import random

fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")

cure = Spell("Cure", 10, 100, "white")

potion = Item("Potion","potion", "Heals 50HP", 50)
healingPotion = Item("healingPotion","potion", "Heals 100HP", 100)
superHealingPotion = Item("superHealingPotion","potion", "Heals 500HP", 500)
manaElixir = Item("manaElixir","manaElixir", "Restores MP", 300)
meteor = Item("meteor","attack", "Attack with 700 damage", 700)

poison = specialItem("Poison","poison", "Attack with 400 damage", 400)
extraPoison = specialItem("extraPoison","extraPoison","Attack with 700 damage", 700)
superExtraPoison = specialItem("superExtraPoison","superExtraPoison", "Attack with 900 damage", 900)

player_magic = [fire, thunder, blizzard, cure]
player_items = [{"item": potion, "quantity": 5},
                {"item": healingPotion, "quantity": 5},
                {"item": superHealingPotion, "quantity": 5},
                {"item": manaElixir, "quantity": 5},
                {"item": meteor, "quantity": 5}]

player_specialItems = [{"item": poison, "quantity": 1},
                {"item": extraPoison, "quantity": 1},
                {"item": superExtraPoison, "quantity": 1}]

player = Person("Marchewka", 700, 65, 60, player_magic, player_items, player_specialItems)

enemy1 = Person("Enemy 1", 1200, 65, 12, player_magic, [],[])
enemy2 = Person("Enemy 2", 300, 65, 100, player_magic, [],[])
enemy3 = Person("Enemy 3", 1200, 65, 405, player_magic, [],[])
enemy4 = Person("Enemy 4", 1000,400, 100, player_magic, [],[])

enemies = [enemy1, enemy2, enemy3, enemy4]


running = True

while running:
    print("Let's start the game (☆^O^☆)" )
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        print("Let's attack!!!")
        dmg = player.generate_damage()
        enemy_id = player.choose_target(enemies)
        enemies[enemy_id].take_damage(dmg)
        print("You attacked", enemies[enemy_id].name, " for: ", dmg, "points of damage, enemy HP: ", enemies[enemy_id].get_hp())
    elif index == 1:
        print("Let's use magic spell")
        player.choose_magic()
        magic_choice = int(input("Choose magic ")) - 1
        spell = player.magic[magic_choice]
        magic_property = spell.generate_damage()

        current_mp = player.get_mp()
        if spell.cost > current_mp:
            print("Not enaugh mana")
        else:
            player.reduce_mp(spell.cost)

            if spell.magic_type == "white":
                print("Healing")
                player.heal(magic_property)
                print("Player heals for", magic_property, "current HP:", player.get_hp())
            elif spell.magic_type == "black":
                print("Attack!!!")
                enemy_id = player.choose_target(enemies)
                enemies[enemy_id].take_damage(magic_property)
                print("You attacked", enemies[enemy_id].name, " for: ", magic_property, "points of damage, enemy HP: ", enemies[enemy_id].get_hp())
    elif index == 2:
        print("Use items")
        player.choose_item()
        item_choice = int(input("Choose item ")) - 1

        item = player.items[item_choice]["item"]
        item_quantity = player.items[item_choice]["quantity"]

        if item_quantity == 0:
            print("You have no such item in your inventory")
        else:
            player.items[item_choice]["quantity"] -= 1


            if item.itemType == "potion":
                player.heal(item.prop)
                print("Player heals for", item.prop, "current HP:", player.get_hp())
                if item_quantity <=3:
                    print("WARNING!!! Less than 3 items")
            elif item.itemType == "elixir":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print("Player hp and mp fully restored")
                
            elif item.itemType == "attack":
                enemy_id = player.choose_target(enemies)
                enemies[enemy_id].take_damage(item.prop)
                print("You attacked", enemies[enemy_id].name, " for: ", item.prop, "points of damage, enemy HP: ", enemies[enemy_id].get_hp())
    elif index == 3:
        print("Use special items")
        player.choose_specialItem()
        specialItem_choice = int(input("Choose special item")) - 1

        specialItem = player_specialItems[specialItem_choice]["item"]
        specialItem_quantity = player_specialItems[specialItem_choice]["quantity"]

        if specialItem_quantity == 0:
            print("You have no such item in your inventory")
        else:
            player.specialItems[specialItem_choice]["quantity"] -= 1
        
            if specialItem.specialItemType == "poison":
                enemy_id = player.choose_target(enemies)
                enemies[enemy_id].take_damage(specialItem.prop)
                print("You attacked", enemies[enemy_id].name, " for: ", specialItem.prop, "points of damage, enemy HP: ", enemies[enemy_id].get_hp())


            elif specialItem.specialItemType == "extraPoison":
                enemy_id = player.choose_target(enemies)
                enemies[enemy_id].take_damage(specialItem.prop)
                print("You attacked", enemies[enemy_id].name, " for: ", specialItem.prop, "points of damage, enemy HP: ", enemies[enemy_id].get_hp())
            elif specialItem.specialItemType == "extraPoison2":
                enemy_id = player.choose_target(enemies)
                enemies[enemy_id].take_damage(specialItem.prop)
                print("You attacked", enemies[enemy_id].name, " for: ", specialItem.prop, "points of damage, enemy HP: ", enemies[enemy_id].get_hp())
    elif index == 4:
        running = False
        print("You gave up")
        print("┏༼ ◉ ╭╮ ◉༽┓")
        

    enemy_id = random.choice([1,1,1,1,0,0,0,2,3,3,3])
    enemy_choice = random.choice([0,0,0,1,1,1,1,1,0,1,1])
    enemy = enemies[enemy_id]

    if enemy_choice == 0:
        print("Enemy attack!!!")
        enemy_dmg = enemy.generate_damage()
        player.take_damage(enemy_dmg)
        print("Enemy", enemy.name ," attacked for: ", enemy_dmg, "points of damage, Your HP: ", player.get_hp())
    elif enemy_choice == 1:
        print("Enemy use magic spell")
        magic_choice = random.randrange(0, len(enemy.magic)-1)
        spell = enemy.magic[magic_choice]
        magic_property = spell.generate_damage()

        if enemy.mp < spell.cost:
            print("Not enought mp to create magic attack")
        else:
            enemy.reduce_mp(spell.cost)
            if spell.magic_type == "white":
                enemy.heal(magic_property)
                print("enemy heals for", magic_property, "current enemy hp:", enemy.get_hp())
            elif spell.magic_type == "black":
                player.take_damage(magic_property)
                print("Enemy", enemy.name ," attacked for: ", magic_property, "points of damage, Your HP: ", player.get_hp())

    defeated_enemies = 0 
    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1
                                
    if defeated_enemies == len(enemies):
        print("You win")
        running = False
    elif player.get_hp() <= 0:
        print("You fail  ┏༼ ◉ ╭╮ ◉༽┓")
        running = False
