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

import playable_countries as pc


player_names = ['Marcus', 'Kivi', 'Jacob', 'Smitaah', 'Amanda', 'Embla']
players = []
country_pool = pc.get_countries()

# Create the players
for name in player_names:
    players.append(Player(name))


def randomize_countries(players, countries):
    """
    Assign each player three possible countries to choose from
    Args: List containing elements of the Player class
    Return: A List of players with randomly assigned countries
    """
    import random as rng
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


randomized_players = randomize_countries(players, country_pool)

print_lineup(randomized_players)