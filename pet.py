import random

class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.health = 10
        self.direction = 0
        self.is_alive = True

    def eat(self):
        print("Mmmmmm, so good!")

    def sleep(self):
        print("I'm schleeep...")

    def play(self):
        print("YEET!")

    def hug(self, other):
        print(str(self.name) + " hugs " + str(other.name))

    def destroy(self, other):
        if self.name == "Adolf":
            print(str(self.name) + " annihilates " + str(other.name) + " with an atom bomb that he stole from America.")
        else:
            print(str(self.name) + " destroys " + str(other.name) + " with cuddles.")

    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1

    def attack(self, other):
        attacking = True
        while attacking == True:
            if attacking == True:
                damage = random.randint(1,3)
                print(self.name + " attacks " + other.name + "!")
                print("It does " + str(damage) + " damage.")
                other.health -= damage
                if other.health > 0:
                    pass
                else:
                    attacking = False
                print(other.name + " now has " + str(other.health) + " health.")
                damage = random.randint(1,3)
                print("But " + other.name + " retaliates and does " + str(damage) + " damage!")
                self.health -= damage
                if self.health > 0:
                    pass
                else:
                    attacking = False
                print(self.name + " now has " + str(self.health) + " health.")
                damage = random.randint(1,3)
                print(self.name + " takes another swing, though, and does " + str(damage) + " damage!")
                other.health -= damage
                if other.health > 0:
                    pass
                else:
                    attacking = False
                print(other.name + " now has " + str(other.health) + " health.")
                damage = random.randint(1,3)
                print(other.name + " won't go down easy though, and does " + str(damage) + " more damage to " + self.name + "!")
                self.health -= damage
                if self.health > 0:
                    pass
                else:
                    attacking = False
                print(self.name + " now has " + str(self.health) + " health.")
                damage = random.randint(1,3)
                print(self.name + " is enraged and strikes back dealing " + str(damage) + " damage!")
                other.health -= damage
                if other.health > 0:
                    pass
                else:
                    attacking = False
                print(other.name + " now has " + str(other.health) + " health.")
                damage = random.randint(1,3)
                print("This causes " + other.name + " to fight back, attacking " + self.name + " and dealing " + str(damage) + " damage!")
                self.health -= damage
                if self.health > 0:
                    pass
                else:
                    attacking = False
                print(self.name + " now has " + str(self.health) + " health.")
            else:
                break
        while attacking == False:
            if self.health <= 0:
                print(self.name + " has fallen after engaging " + other.name + " in vicious combat")
                self.is_alive = False
            elif other.health <= 0:
                print(other.name + " has been slaughtered after being attacked by " + self.name)
                other.is_alive = False
            break

    def __repr__(self):
        return "Name: " + self.name + \
               " x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"
    
    
pet1 = Pet("Adolf")
pet2 = Pet("Stalin")
pet3 = Pet("Trump")
