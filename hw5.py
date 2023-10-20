class Witcher(Hero):
    def init(self, name, health, damage):
        super().init(name, health, damage, Ability.BLOCK_DAMAGE_AND_REVERT)
        self.__revive_used = False
        for hero in heroes:
            if hero.health <= 0:
                hero.health = 1
                print(f"{self.name} revived {hero.name}. {self.name} sacrificed himself.")
                break

    else:
    print(f"{self.name} can't revive anymore. He takes damage from the boss.")


def init(self, name, health, damage, ability):
    super().init(name, health, damage, ability)


def apply_super_power(self, boss, heroes):
    n = 5
    for hero in heroes:
        hero.damage += n

    print(f'{self.name} increases heroes\' attack by {n} after every round.')


class Thor(Hero):
    def init(self, name, health, damage):
        super().init(name, health, damage, Ability.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        if random.random() < 0.3:
            boss.stunned = True
            print(f"{self.name} stunned the boss for 1 round.")


class Witcher(Hero):
    def init(self, name, health, damage):
        super().init(name, health, damage, Ability.BLOCK_DAMAGE_AND_REVERT)
        self.__revive_used = False

    def apply_super_power(self, boss, heroes):

        if not self.__revive_used:
            self.__revive_used = True

            for hero in heroes:
                if hero.health <= 0:
                    hero.health = 1
                    print(f"{self.name} revived {hero.name}. {self.name} sacrificed himself.")
                    break
        else:
            print(f"{self.name} can't revive anymore. He takes damage from the boss.")