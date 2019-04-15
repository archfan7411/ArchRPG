from random import randint

default_inventory_size = 15

item_types = ["Dagger", "Sword", "Bow", "Staff", "Spear", "Elixir"]
item_origins = ["Targean", "Asnaudia", "Khaladari", "Scanardian"]
item_rarities = ["Common", "Uncommon", "Stout", "Rare", "Heirloom", "Legendary"]

classes = ["Burglar", "Swordsman", "Archer", "Guardsman", "Mage"]

players = {}

def getplayer(user):
    return players[user.id]

def addplayer(user):
    players[user.id] = Player(user)

def playerexists(user):
    return user.id in players.keys()

class Player:

    def __init__(self, user):
        self._user = user
        self._class = ""
        self._can_change_class = True
        self._inv = [Item(0,0,0)] * default_inventory_size
        self._bal = 0
        self._tokens = []
        self._equipped_item = self._inv[1]
        self._inventory_size = default_inventory_size

    def setClass(self, _class):
        self._class = _class
        self._can_change_class = False

    def set_inv_slot(self, slot, item):
        self._inv[slot] = item

    def get_inv_slot(self, slot):
        return self._inv[slot]

    def equip(self, slot):
        self._equipped_item = self._inv[slot]

    def increase_inventory_size(self, number):
        for i in range(self._inventory_size, self._inventory_size + number - 1):
            self._inv[i] = Item(0, 0, 0)
    
    # Returns True on success
    def add_item(self, item):
        for slot in self._inv:
            if slot == Item(0,0,0):
                slot = item
                return True
        return False

    def get_inventory_empty_space(self):
        space = 0
        for slot in self._inv:
            if slot == Item(0,0,0):
                space += 1
        return space

    def clear_slot(self, slot):
        self._inv[slot] = Item(0,0,0)

class Item:

    def __init__(self, type, origin, rarity):
        self._type = type
        self._origin = origin
        self._rarity = rarity

    def __str__(self):
        return item_origins[self._origin] + " " + item_types[self._type] + " (" + item_rarities[self._rarity] + ")"
    
    def is_weapon(self):
        return False

class Weapon(Item):

    def rng_weighted(self):
        return randint(1, 20) * (1+(self._rarity/10))

    def is_weapon(self):
        return True

class Location:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def _setorigin(self, origin):
        self._origin = origin

    def coords_as_list(self):
        return [self._x, self._y]

class Town(Location):

    def __init__(self, x, y, name, origin):
        self._name = name
        self._origin = origin
        super.__init__(x, y)
    