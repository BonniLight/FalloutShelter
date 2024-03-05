import random
#possibly add None to the health and whatnot
class Survivor:
    def __init__(self, name, health=10, food=10, money=10, radiation=10):
        self.name = name
        self.health = health
        self.food = food
        self.money = money
        self.radiation = radiation

    def eat(self, amount):
        self.food -= amount
        self.health += amount

    def rest(self, days):
        self.health += days * 2

    def spend_money(self, amount):
        self.money -= amount

class Family_Members(Survivor):
    def __init__(self, name, health, food, money):
        super().__init__(name, health, food, money)

    def special_ability(self):
        pass


class Gameplay:  
    def __init__(self, player):
        self.player = player

    def player_turn(self):
        print(f"Current Health: {self.player.health}, Current Food: {self.player.food}, Current Money: {self.player.money}")
        user_choice = input("Choose an option (1. Eat, 2. Rest, 3. Continue Traveling): ")
        self.action(user_choice)

    def action(self, user_choice):
        if user_choice == "1":
            self.handle_eating()
        elif user_choice == "2":
            self.handle_resting()
        elif user_choice == "3":
            self.handle_traveling()

    def handle_eating(self):
        food_amount = int(input("Enter the amount of food to eat: "))
        self.player.eat(food_amount)

    def handle_resting(self):
        rest_days = int(input("Enter the number of days to rest: "))
        self.player.rest(rest_days)

    def handle_traveling(self):
        distance = random.randint(1, 100)
        travel_days = distance // 20
        self.player.eat(travel_days * 2)
        self.player.spend_money(travel_days * 5)
        print(f"You travel {distance} miles in {travel_days} days...")

        if self.player.food <= 0:
            print(f"{self.player.name} YOU DIED - Starved")
        elif self.player.health <= 0:
            print(f"{self.player.name} YOU DIED - Passed")
        elif self.player.money <= 0:
            print(f"{self.player.name} YOU DIED - Went Broke")


class Game_System:
    def __init__(self, members):
        self.players = [Family_Members(*member) for member in members]
        self.days_in_bunker = 0

    def game_beginning(self): 
        print("Welcome to Fallout Don't Die or Lose all your Money!!!")
        while self.days_in_bunker < 7:
            self.days_in_bunker += 1
            print(f"\nDay {self.days_in_bunker}")
            for player in self.players:
                print(f"\n{player.name}'s turn:")
                gameplay = Gameplay(player)
                gameplay.player_turn()

if __name__ == "__main__":
    default_family_members = [
        ("Dad-Bob", 150, 50, 200),
        ("Mom-Joddy", 100, 100, 300),
        ("Daughter-Sammy", 100, 40, 200),
        ("Son-Will", 100, 100, 100)
    ]

    game_run = Game_System(default_family_members)
    game_run.game_beginning()
