from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

class Game:
    def __init__(self, num_players):
        self.num_players = num_players
        self.payoff_matrix = np.random.randint(low=-5, high=5, size=(num_players, num_players))

    def calculate_payoffs(self, choices):
        payoffs = []
        for i in range(len(choices)):
            payoff = 0
            for j in range(len(choices)):
                payoff += self.payoff_matrix[i][j]
            payoffs.append(payoff)
        return payoffs

    def find_mixed_strategy_nash_equilibrium(self):
        mixed_strategies = []
        for player in range(self.num_players):
            mixed_strategy = np.zeros(self.num_players)
            for i in range(self.num_players):
                if i == player:
                    continue
                mixed_strategy[i] = self.payoff_matrix[player][i] - self.payoff_matrix[player][i-1]
            mixed_strategies.append(mixed_strategy / sum(mixed_strategy))
        return mixed_strategies
    def get_num_players(self):
        return self.num_players
    def get_payoff_matrix(self):
        return self.payoff_matrix
    def set_payoff_matrix(self, matrix):
        self.payoff_matrix = matrix

game = Game(3)

@app.route("/")
def index():
    payoff_matrix = game.get_payoff_matrix()
    mixed_strategy_nash_equilibrium = game.find_mixed_strategy_nash_equilibrium()
    return render_template("index.html", payoff_matrix=payoff_matrix, mixed_strategy_nash_equilibrium=mixed_strategy_nash_equilibrium)

@app.route("/update", methods=["POST"])
def update():
    game.set_payoff_matrix(np.random.randint(low=-5, high=5, size=(game.get_num_players(), game.get_num_players())))
    payoff_matrix = game.get_payoff_matrix()
    mixed_strategy_nash_equilibrium = game.find_mixed_strategy_nash_equilibrium()
    return render_template("index.html", payoff_matrix=payoff_matrix, mixed_strategy_nash_equilibrium=mixed_strategy_nash_equilibrium)

if __name__ == "__main__":
    app.run(debug=True)