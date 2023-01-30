from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        payoff_matrix_A = np.array([[float(x) for x in row.split(",")] for row in request.form["payoff_matrix_A"].split("\n")])
        payoff_matrix_B = np.array([[float(x) for x in row.split(",")] for row in request.form["payoff_matrix_B"].split("\n")])
        # Perform the calculation of correlated equilibrium
        # ...
        result = "Calculation result"
        return render_template("index.html", result=result)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
