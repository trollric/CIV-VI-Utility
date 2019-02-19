class Player:
    def __init__(self, name='unnamed'):
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


player_names = ['Marcus', 'Kivi', 'Jacob', 'Smitaah', 'Amanda', 'Embla', 'Benevides']
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
    #countries = pc.get_countries(all_expansions=True)
    countries = pc.get_countries()
    for player in players:
        for i in range(3):
            rand = rng.randint(0, len(countries) - 1)
            player.add_country(countries.pop(rand))
    return players

def print_lineup(players):
    """
    Takes a list of players and prints their assigned teams to the terminal/console
    Args: List containing elements of the Player class
    """
    for player in players:
        print('{} will be playing as either:'.format(player.name))
        for country in player.get_countries():
            print('{0} of {1}'.format(country["leader"],country["name"]))
        print("\n")


# Assign the players three countries each
players_lineup = assign_countries(players)


def post_player_frame(root_frame, player):
    """
    Takes a frame which to add the graphics and a player to draw information from.
    Args: root_frame (tkinter.frame), player (player class object)
    """
    player_frame = tk.Frame(root_frame)
    tk.Label(player_frame, text=player.get_name(), anchor=tk.CENTER, font=('times', 18)).grid(
        row=0,
        columnspan=3,
        sticky=tk.W+tk.E
        )

    i = 0
    for country in player.get_countries():
        text = '{0} of {1}'.format(country["leader"], country["name"])
        tk.Label(player_frame, text=text, relief='ridge', font=('times', 12), width=26).grid(row=1, column=i)

        img = Image.open(country["image_path"])
        img = img.resize((232,232), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(img)

        img_logo = tk.Label(player_frame, image=logo, width=232)
        img_logo.image = logo #Keep the image reference
        img_logo.grid(row=2, column=i)
        i += 1

    player_frame.pack(fill=tk.BOTH, expand=True, side=tk.TOP)


def onFrameConfiguration(canvas):
    """ Reset te scroll region to encompass the inner frame"""
    canvas.configure(scrollregion=canvas.bbox("all"))


# Create GUI
import tkinter as tk
from PIL import ImageTk, Image

# Create a root frame with a set size
root = tk.Tk()
root.title('Civilization VI Three pool picker')
root.geometry("725x600+50+50")
root.resizable(0, 0)

#Create the scrollable canvas and add a mainframe to it
canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
main_player_frame = tk.Frame(canvas, background="#ffffff")
scroll = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scroll.set)

scroll.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((0,0), window=main_player_frame, anchor="nw")

main_player_frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfiguration(canvas))

# Fill the frame with the player layout
for player in players_lineup:
    post_player_frame(main_player_frame, player)


root.mainloop()