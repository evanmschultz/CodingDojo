players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32, "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33, "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32, "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "",
        "age": 16,
        "position": "P",
        "team": "en"
    }
]


class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.age = dict['age']
        self.position = dict['position']
        self.team = dict['team']

    def display_attributes(self):
        for key, attribute in self.__dict__.items():
            if key == 'name':
                continue
            print(f'{self.name}\'s {key} is {attribute}')

        print('\n')

        return self

    @classmethod
    def get_team(cls, team_list):
        # list comprehension to create list of players
        new_team = [cls(player) for player in team_list]

        return new_team


kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32, "position": "Point Guard",
    "team": "Brooklyn Nets"
}

# Create your Player instances here!
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

player_kevin.display_attributes()
player_jason.display_attributes()
player_kyrie.display_attributes()


new_team = [Player(player) for player in players]

# for player in new_team:
#     player.display_attributes()

team_two = Player.get_team(players)

for player in team_two:
    player.display_attributes()
