class Player:
    def __init__(self,name='unnamed'):
        """
        Creates a new player
        Args: name(str)
        """
        self.countries = []
        self.name = name

    def get_countries(self):
        """
        Fetch playable countries
        Return: list of countries
        """
        return self.countries

    def add_country(self, country):
        """
        Adds a country to the players list
        Args: country(string)
        """
        self.countries.append(country)


player_names = ['Marcus', 'Kivi', 'Jacob', 'Smitaah', 'Amanda', 'Embla']
players = []

# Create the players
for name in player_names:
    players.append(Player(name))


def assign_countries(players):
    """
    Assign each player three possible countries to choose from
    Args: List containing elements of the Player class
    Return: A List of players with randomly assigned countries
    """
    import random as rng
    import playable_countries as pc
    countries = pc.get_countries(all_expansions=True)
    for player in players:
        for i in range(3):
            rand = rng.randint(0, len(countries) - 1)
            player.add_country(countries.pop(rand))
    return players

def print_lineup(players):
    """
    Takes a list of players and prints their assigned teams
    Args: List containing elements of the Player class
    """
    for player in players:
        print('{} will be playing as either:'.format(player.name))
        for country in player.get_countries():
            print('{0} of {1}'.format(country[1],country[0]))
        print("\n")


players_lineup = assign_countries(players)

# Experimenting with GUI
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

logo_img = ImageTk.PhotoImage(Image.open("assets/chandragupta.png"))

w1 = tk.Label(root, image=logo_img)
w1.pack(side="right")
explanation = """Chandragupta was a leader of India a long time ago"""

w2 = tk.Label(root, justify=tk.LEFT, padx=10, text=explanation)
w2.pack(side="left")

root.mainloop()