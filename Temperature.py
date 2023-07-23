class Temperature:
    def __init__(self, temperature):
        self.title = temperature
        self.match_counter = 0
        self.total_goal = 0
        self.home_goal = 0
        self.away_goal = 0
        self.total_card = 0
        self.total_yellow_card = 0
        self.total_red_card = 0
        self.home_yellow_card = 0
        self.home_red_card = 0
        self.away_yellow_card = 0
        self.away_red_card = 0

    def match_adder(self):
        self.match_counter += 1

    def add_goal(self, side, amount):
        self.total_goal += amount

        if side == "Home":
            self.home_goal += amount
        elif side == "Away":
            self.away_goal += amount

    def add_card(self, side, color, amount):
        self.total_card += amount

        if side == "Home" and color == "Red":
            self.total_red_card += amount
            self.home_red_card += amount
        elif side == "Home" and color == "Yellow":
            self.total_yellow_card += amount
            self.home_yellow_card += amount
        elif side == "Away" and color == "Red":
            self.total_red_card += amount
            self.away_red_card += amount
        elif side == "Away" and color == "Yellow":
            self.total_yellow_card += amount
            self.away_yellow_card += amount
