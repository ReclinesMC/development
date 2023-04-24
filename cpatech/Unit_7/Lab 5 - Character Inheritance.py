# Sean A
# Character Inheritance
# Using RPG characters, make a lab that allows us to practice class inheritance
import random as r

try:
    import CharacterHandler as ch
except:
    from cpatech.Unit_7.handlers import CharacterHandler as ch


def main():
    # create all the characters whee
    sean = ch.Fighter("Sean", 13, 16, 7, 17, 12)
    rogue = ch.Rogue("CoolRogue", r.randint(10, 15), r.randint(10, 20), r.randint(5, 15), r.randint(15, 25),
                     r.randint(10, 15))
    sorcerer = ch.Sorcerer("CoolSorcerer", r.randint(10, 15), r.randint(10, 20), r.randint(5, 15), r.randint(15, 25),
                           r.randint(10, 15))
    bard = ch.Bard("CoolBard", r.randint(10, 15), r.randint(10, 20), r.randint(5, 15), r.randint(15, 25),
                   r.randint(10, 15))
    wizard = ch.Wizard("CoolWizard", r.randint(10, 15), r.randint(10, 20), r.randint(5, 15), r.randint(15, 25),
                       r.randint(10, 15))

    # Let's make sure I can block hits
    print("[ Fighter Damage Blocking ]".center(50, "="))
    for i in range(6):
        sean.take_damage(r.randint(5, 20))
    print(sean, "\n")

    # K now we make sure rogue can do the same
    print("[ Rogue Damage Dodging ]".center(50, "="))
    for i in range(6):
        rogue.take_damage(r.randint(5, 20))
    print(rogue, "\n")

    # Sorcerer casting fireball
    print("[ Sorcerer Fireball ]".center(50, "="))
    sorcerer.print_stat("SP")
    sorcerer.cast_fireball()
    sorcerer.print_stat("SP")
    print()

    # Wizard's healing hands
    print("[ Wizard's Sorcery ]".center(50, "="))
    wizardWorking = wizard.cast_healingHands(sean)
    while not wizardWorking:
        wizard = ch.Wizard("CoolWizard", r.randint(10, 15), r.randint(10, 20), r.randint(5, 15), r.randint(15, 25),
                           r.randint(10, 15))
        wizardWorking = wizard.cast_healingHands(sean)
    print()

    # Bard's life stealing >:)
    print("[ Bard's Thievery ]".center(50, "="))
    bard.take_damage(20)
    print()
    for i in range(6):
        bard.gift_of_life(sean)
    print()
    print(sean)
    print(bard)


if __name__ == "__main__":
    main()