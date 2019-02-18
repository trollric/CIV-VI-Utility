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

    def get_name(self):
        """
        Return: self.name (str)
        """
        return self.name

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
root.title('Civilization VI Three pool picker')
root.geometry("710x600")
root.resizable(0, 1)


def post_player_frame(root_frame, player):
    """
    Takes a root frame which to add the graphics and a player to draw information from.
    Args: frame (tkinter.frame), player (player class object)
    """
    player_frame = tk.Frame(root_frame)
    tk.Label(player_frame, text=player.get_name(), anchor=tk.CENTER).grid(row=0, columnspan=3, sticky=tk.W+tk.E)

    img = Image.open("assets/norway.png")
    img = img.resize((231,231), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(img)

    i = 0
    for country in player.get_countries():
        text = '{0} of {1}'.format(country[1], country[0])
        tk.Label(player_frame, text=text, relief='ridge', font=('times', 12), width=25).grid(row=1, column=i)
        img_logo = tk.Label(player_frame, image=logo, relief='ridge', width=231)
        img_logo.image = logo #Keep the image reference
        img_logo.grid(row=2, column=i)
        i += 1

    player_frame.pack(fill=tk.BOTH, expand=True, side=tk.TOP)


# Test to create a frame format!
player_frame = tk.Frame(root)


player_name = "<Player names goes here>"

img = Image.open("assets/chandragupta.png")
img = img.resize((231,231), Image.ANTIALIAS)
resize_logo = ImageTk.PhotoImage(img)

name_label = tk.Label(player_frame, text=player_name, anchor=tk.CENTER)
name_label.grid(row=0, columnspan=3, sticky=tk.W+tk.E)

i = 0
for country in players_lineup[0].get_countries():
    text = '{0} of {1}'.format(country[1], country[0])
    tk.Label(player_frame, text=text, relief='ridge', font=('times', 12), width=25).grid(row=1, column=i)
    img_logo = tk.Label(player_frame, image=resize_logo, relief='ridge', width=231)
    img_logo.image = resize_logo #keep the image reference
    img_logo.grid(row=2, column=i)

    i += 1

player_frame.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

post_player_frame(root, players_lineup[1])
root.mainloop()