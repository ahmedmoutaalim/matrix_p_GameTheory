import random
import numpy as np
import tkinter as tk
from tkinter import messagebox

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

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.game = Game(3)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.payoff_matrix_label = tk.Label(self, text="Payoff matrix:")
        self.payoff_matrix_label.grid(row=0, column=0)
        self.payoff_matrix_text = tk.Text(self, height=4, width=20)
        self.payoff_matrix_text.grid(row=1, column=0)
        self.payoff_matrix_text.insert(tk.END, self.game.get_payoff_matrix())
        self.mixed_strategy_nash_equilibrium_label = tk.Label(self, text="Mixed strategy Nash equilibrium:")
        self.mixed_strategy_nash_equilibrium_label.grid(row=2, column=0)
        self.mixed_strategy_nash_equilibrium_text = tk.Text(self, height=4, width=20)
        self.mixed_strategy_nash_equilibrium_text.grid(row=3, column=0)
        mixed_strategy_nash_equilibrium = self.game.find_mixed_strategy_nash_equilibrium()
        self.mixed_strategy_nash_equilibrium_text.insert(tk.END, mixed_strategy_nash_equilibrium)
        self.update_button = tk.Button(self, text="Update", command=self.update_payoff_matrix)
        self.update_button.grid(row=4, column=0)

    def update_payoff_matrix(self):
        num_players = self.game.get_num_players()
        new_matrix = np.random.randint(low=-5, high=5, size=(num_players, num_players))
        self.game.set_payoff_matrix(new_matrix)
        self.payoff_matrix_text.delete(1.0, tk.END)
        self.payoff_matrix_text.insert(tk.END, self.game.get_payoff_matrix())
        self.mixed_strategy_nash_equilibrium_text.delete(1.0, tk.END)
        mixed_strategy_nash_equilibrium = self.game.find_mixed_strategy_nash_equilibrium()
        self.mixed_strategy_nash_equilibrium_text.insert(tk.END, mixed_strategy_nash_equilibrium)
        messagebox.showinfo("Success", "Payoff matrix and mixed strategy Nash equilibrium have been updated.")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

