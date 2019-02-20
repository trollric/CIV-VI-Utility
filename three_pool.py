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

    def reset_counties(self):
        """Resets the countries list"""
        self.countries.clear()



def assign_countries(players):
    """
    Assign each player three possible countries to choose from
    Args: List containing elements of the Player class
    Return: A List of players with randomly assigned countries
    """
    import random as rng
    import playable_countries as pc

    countries = pc.get_countries(rise_and_fall.get(), global_storm.get(), all_expansions.get())
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


def post_player_frame(root_frame, player):
    """
    Takes a frame which to add the graphics and a player to draw information from.
    Args: root_frame (tkinter.frame), player (player class object)
    """
    global element_handles
    player_frame = tk.Frame(root_frame)
    element_handles.append(player_frame)

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


def button_draw_teams():
    """Erases all handles in the element_handles list. Resets and fetches players country pool. Updates graphics"""
    global element_handles
    global players
    global main_player_frame
    # Delete all old labels etc inside the main frame.
    for e in element_handles:
        e.destroy()

    # Reset existing countires for players
    for player in players:
        player.reset_counties()
    
    # Reassign the players countries based on checkboxes
    players_lineup = assign_countries(players)
    
    #Post graphics to the main frame
    for player in players_lineup:
        post_player_frame(main_player_frame, player)


# Create GUI
import tkinter as tk
from PIL import ImageTk, Image

# Create a root frame with a set size
root = tk.Tk()
root.title('Civilization VI Three pool picker')
root.geometry("740x620+50+50")
root.resizable(0, 0)

#Country pool variables
rise_and_fall = tk.IntVar()
global_storm = tk.IntVar()
all_expansions = tk.IntVar()

# Creating a list to hold the graphics handles
element_handles = []


#Create top bar with button and checkboxes
top_frame = tk.Frame(root, background="#ffffff", relief='ridge')
top_frame.pack(side='top', fill='x')

c_box1 = tk.Checkbutton(top_frame, text="Rise & Fall", variable=rise_and_fall, background="#ffffff")
c_box1.pack(side='left', padx='5')
c_box2 = tk.Checkbutton(top_frame, text="Global Storm", variable=global_storm, background="#ffffff")
c_box2.pack(side='left', padx='5')
c_box3 = tk.Checkbutton(top_frame, text="All Expansions", variable=all_expansions, background="#ffffff")
c_box3.pack(side='left', padx='5')

b1 = tk.Button(top_frame, text="Generate teams", command=button_draw_teams, background="#ffffff")
b1.pack(side='left', padx='5')

#Create the scrollable canvas and add a mainframe to it
canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
main_player_frame = tk.Frame(canvas, background="#ffffff")
scroll = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scroll.set)

scroll.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((0,0), window=main_player_frame, anchor="nw")

main_player_frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfiguration(canvas))

#Set game objects
#Set players
player_names = ['Marcus', 'Kivi', 'Jacob', 'Smitaah', 'Amanda', 'Embla', 'Benevides']
players = []

# Create the player classes and add to list
for name in player_names:
    players.append(Player(name))

# Assign the players three countries each
players_lineup = assign_countries(players)

# Fill the frame with the player layout
for player in players_lineup:
    post_player_frame(main_player_frame, player)


# Spin up the graphics
root.mainloop()