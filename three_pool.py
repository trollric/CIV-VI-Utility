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
root.title('Civilization VI Three pool picker')
root.resizable(0, 1)
#logo_img = ImageTk.PhotoImage(Image.open("assets/chandragupta.png"))

#w1 = tk.Label(root, image=logo_img)
#w1.pack(side="right")
#explanation = """Chandragupta was a leader of India a long time ago"""

#w2 = tk.Label(root, justify=tk.LEFT, padx=10, text=explanation)
#w2.pack(side="left")

#b1 = tk.Button(root, text='Stop', width=25, command=root.destroy)
#b1.pack()

# Button frame.
#frame = tk.Frame(root)
#frame.pack()

#b2 = tk.Button(frame, text='QUIT', fg='red', bg='white', command=w1.destroy)
#b2.pack(side=tk.LEFT)

#b3 = tk.Button(frame, text='?', fg='white', bg='red', command=b3.destroy)
#b3.pack()

#msg = "Whatever you do will be insignificant, but it is very important that you do it. \nMahatma Gandhi"
#w3 = tk.Message(root, text=msg)
#w3.config(bg='navy', font=('times', 24, 'italic'),fg='white')
#w3.pack()

# special label
#counter = 0
#def counter_label(label):
#   counter = 0
#    def count():
#        global counter
#        counter += 1
#        label.config(text=str(counter))
#        label.after(1000, count)
#    count()


# Test to create a frame format!
player_frame = tk.Frame(root)
player_frame.pack()

player_name = "<Player names goes here>"
country_name = ['Gerogia', 'Canada', 'Netherlands']

img = Image.open("assets/chandragupta.png")
img = img.resize((100,100), Image.ANTIALIAS)
resize_logo = ImageTk.PhotoImage(img)

name_frame = tk.Frame(player_frame, height="32", width="450")
name_frame.propagate(False)
name_frame.grid(row=0, column=0)
tk.Label(name_frame, text=player_name, relief='ridge', font=('times', 12), anchor=tk.CENTER).pack(anchor=tk.CENTER)
i = 0
for country in players_lineup[0].get_countries():
    f = tk.Frame(player_frame, height="32", width="150")
    f.propagate(False)
    f.grid(row=1, column=i)
    text = '{0} of {1}'.format(country[1], country[0])
    tk.Label(f, text=text, relief='ridge', font=('times', 12), anchor=tk.CENTER).pack()
    i += 1
root.mainloop()