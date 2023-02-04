from flask import Flask, render_template, request
import nashpy as nash
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/matrix", methods=["POST"])
def matrix():
    strategy_choice = request.form["strategy_choice"]
    return render_template("matrix.html", strategy_choice=strategy_choice)

@app.route("/result", methods=["POST"])
def result():
    strategy_choice = request.form["strategy_choice"]
    matrix = np.array(eval(request.form["matrix"]))
    if strategy_choice == "pure":
        # Pure strategy
        game = nash.Game(matrix)
        result = game.support_enumeration()
    elif strategy_choice == "mixed":
        # Mixed strategy
        game = nash.Game(matrix)
        result = game.vertex_enumeration()
    else:
        return "Invalid choice, please try again."

    equilibria = [list(eq) for eq in result]
    return render_template("result.html", equilibria=equilibria)

if __name__ == "__main__":
    app.run(debug=True)
