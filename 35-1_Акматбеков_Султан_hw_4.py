from enum import Enum
from random import randint, choice


class Ability(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    HEAL = 3
    BLOCK_DAMAGE_AND_REVERT = 4


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} HEALTH: {self.__health} DAMAGE: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if hero.ability == Ability.BLOCK_DAMAGE_AND_REVERT and self.defence != Ability.BLOCK_DAMAGE_AND_REVERT:
                    hero.blocked_damage = int(self.damage / 5)
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        if type(ability) == Ability:
            self.__ability = ability
        else:
            raise ValueError('Wrong data type for attribute ability')

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeff = randint(2, 6)
        boss.health -= self.damage * coeff
        print(f'Warrior {self.name} hits critically {self.damage * coeff}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BOOST)

    def apply_super_power(self, boss, heroes):
        pass


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, Ability.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BLOCK_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted blocked damage {self.blocked_damage}')


round_number = 0


def start_game():
    warrior_1 = Warrior('Viking', 280, 20)
    warrior_2 = Warrior('Warrio', 270, 15)
    doc = Medic('Hendolf', 250, 5, 15)
    assistant = Medic('Herrold', 300, 5, 5)
    berserk = Berserk('Olaf', 260, 10)
    magic = Magic('Potter', 290, 15)

    heroes_list = [warrior_1, warrior_2, magic, doc, berserk, assistant]

    boss = Boss('Baron Nashor', 1000, 50)

    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


def show_statistics(boss, heroes):
    print(f'ROUND {round_number} --------')
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and hero.ability != boss.defence:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print('Boss won!!!')

    return all_heroes_dead


start_game()

import random


class Hero:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_dead(self):
        return self.health == 0


class Magic(Hero):
    def __init__(self, name, health, attack, magic_attack):
        super().__init__(name, health, attack)
        self.magic_attack = magic_attack

    def increase_attack(self):
        self.attack += self.magic_attack


class Thor(Hero):
    def __init__(self, name, health, attack, stun_chance):
        super().__init__(name, health, attack)
        self.stun_chance = stun_chance

    def attack_boss(self, boss):
        damage = self.attack
        if random.random() < self.stun_chance:
            boss.stunned = True
        boss.take_damage(damage)


class Witcher(Hero):
    def __init__(self, name, health, attack, revive_chance):
        super().__init__(name, health, attack)
        self.revive_chance = revive_chance

    def attack_boss(self, boss):
        if not self.is_dead():
            boss.take_damage(self.attack)

    def revive_hero(self, heroes):
        if not self.is_dead():
            return
        for hero in heroes:
            if hero.is_dead() and random.random() < self.revive_chance:
                hero.health = 1
                self.health = 0
                break


class Golem(Hero):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

    def take_damage(self, damage):
        damage_taken = damage * 4 // 5  # принимает 1/5 часть урона
        self.health -= damage_taken
        if self.health < 0:
            self.health = 0


class Avrora(Hero):
    def __init__(self, name, health, attack, invisible_rounds):
        super().__init__(name, health, attack)
        self.invisible_rounds = invisible_rounds
        self.invisible = False

    def take_damage(self, damage):
        if self.invisible:
            self.health -= damage
            self.invisible_rounds -= 1
            if self.invisible_rounds <= 0:
                self.invisible = False
        else:
            self.health -= damage


class Druid(Hero):
    def __init__(self, name, health, attack, heal_amount, crow_aggression):
        super().__init__(name, health, attack)
        self.heal_amount = heal_amount
        self.crow_aggression = crow_aggression
        self.has_summoned = False

    def summon_angel(self, heroes):
        if not self.has_summoned:
            for hero in heroes:
                if isinstance(hero, Witcher):
                    hero.attack += self.heal_amount
                    break
            self.has_summoned = True

    def summon_crow(self, boss):
        if not self.has_summoned and boss.health < boss.full_health / 2:
            boss.attack += boss.attack * self.crow_aggression
            self.has_summoned = True