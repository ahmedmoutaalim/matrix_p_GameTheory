from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def pareto_efficiency():
    return render_template("pareto_efficiency.html")

@app.route("/calculate", methods=["POST"])
def calculate():

    utility = request.form.to_dict()

    people = sorted(utility, key=utility.get, reverse=True)
    
    total_utility = 0
    allocation = {}
 
    for person in people:
        if total_utility == 0:
         
            allocation[person] = 1
            total_utility = str(utility[person])
        else:
      
            marginal_utility = int(utility[person]) / int(1 + len(allocation))
            if marginal_utility > 0:
            
                allocation[person] = 1 / int(1 + len(allocation))
                total_utility += str(marginal_utility)
            else:
              
                break
    return render_template("results.html", total_utility=total_utility, allocation=allocation)

if __name__ == "__main__":
    app.run()
