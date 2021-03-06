from base_entity import BaseEntity


class Agent(BaseEntity):

    def __init__(self, ID, current_state=None, location=None, globalstate=None):
        super().__init__(ID)
        self.current_state = current_state
        self.previous_state = None
        self.global_state = globalstate
        self.location = location
        self.money = 0
        self.thirst = 0
        self.fatigue = 0
        self.hunger = 0
        self.lonley = 0
        self.COMFORT_LEVEL = 5
        self.MAX_MONEY = 10
        self.THIRST_LEVEL = 30
        self.HUNGER_LEVEL = 40
        self.LONLEY_THRESHOLD = 50
        self.TIREDNESS_THRESHOLD = 40

    def update(self, tick_size):
        if self.global_state is not None:
            self.global_state.execute(self, tick_size)
        if self.current_state is not None:
            self.current_state.execute(self, tick_size)


    def handle_message(self, telegram):     
        self.current_state.on_message(self, telegram)
        self.global_state.on_message(self, telegram)

    def change_state(self, new_state):
        if not self.current_state and not new_state:
            return
        self.previous_state = self.current_state

        self.current_state.exit(self)

        self.current_state = new_state

        self.current_state.enter(self)

    def revert_to_previous_state(self):
        self.change_state(self.previous_state)

    def change_location(self, new_location):
        self.location = new_location

    def increase_money(self, money=1):
        self.money += money

    def set_money(self, money=0):
        self.money = money

    def pockets_full(self):
        return self.money >= self.MAX_MONEY

    def spend_money(self):
        self.money = 0

    def increase_thirst(self, thirst=1):
        self.thirst += thirst

    def is_thirsty(self):
        return self.thirst >= self.THIRST_LEVEL


    def increase_hunger(self, hunger=1):
        self.hunger += hunger

    def is_hungry(self):
        return self.hunger >= self.HUNGER_LEVEL
    
    def eat(self):
        self.hunger = 0

    def increase_fatigue(self, fatigue):
        self.fatigue += fatigue

    def decrease_fatigue(self, rest):
        self.fatigue -= rest

    def is_tired(self):
        return self.fatigue >= self.TIREDNESS_THRESHOLD

    def drink(self):
        self.thirst = 0
    
    def is_rich(self):
        return self.money >= self.MAX_MONEY 

    def is_lonley(self):
        return self.lonley >= self.LONLEY_THRESHOLD
    
    def decrease_lonley(self, amount):
        self.lonley -= amount
    
    def increase_lonley(self, amount):
        self.lonley += amount