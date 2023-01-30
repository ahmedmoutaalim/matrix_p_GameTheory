# Flask code
from flask import Flask, render_template, request
import numpy as np
from scipy.optimize import linprog

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def nash():
    num_players = int(request.form['players'])
    strategies = []
    for i in range(num_players):
        strategies.append(request.form.getlist('strategies'+str(i+1)))
    payoffs = []
    for i in range(num_players):
        payoffs.append([])
        for j in range(num_players):
            payoffs[i].append([float(x) for x in request.form['payoff'+str(i+1)+str(j+1)].split()])
    nash_eqs = []
    for i in range(num_players):
        c = [-1] * len(strategies[i])
        A_ub = [[0 if i != j else 1 for j in range(len(strategies[i]))] for _ in range(num_players)]
        b_ub = [1] * num_players
        b_eq = np.array([0] * num_players)
        A_eq = [[payoffs[i][j][k] for k in range(len(strategies[i]))] for j in range(num_players) if num_players == len(b_eq)]
        result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq , b_eq=b_eq)
        nash_eqs.append(result.x)
    return "Nash equilibrium for players: {}".format(nash_eqs)

if __name__ == '__main__':
    app.run()
