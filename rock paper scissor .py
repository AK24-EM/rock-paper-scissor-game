import tkinter as tk

class RockPaperScissor:
    def __init__(self, root):
        self.root = root
        self.root.title("rock paper scissor game")
        self.create_name_panel()

    def create_name_panel(self):
        self.clear()
        tk.Label(self.root, text="enter your name ").pack(pady=5)
        self.first_player_entry = tk.Entry(self.root)
        self.first_player_entry.pack(pady=5)
        tk.Label(self.root, text="enter your name ").pack(pady=5)
        self.second_player_entry = tk.Entry(self.root)
        self.second_player_entry.pack(pady=5)
        self.button = tk.Button(self.root , text="game start" , command = self.create_game_panel)
        self.button.pack(pady=5)

    def create_game_panel(self):
        tk.Label(self.root , text="enter your choice ").pack(pady=5)
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)
        tk.Label(self.root , text="enter your choice").pack(pady=5)
        self.entry1 =  tk.Entry(self.root)
        self.entry1.pack(pady=5)
        tk.Button(self.root , text="check result" , command = self.game).pack(pady=5)
        self.result = tk.Label(self.root , text=" ")
        self.result.pack(pady=5)

        tk.Button(self.root , text="BACK" , command = self.create_name_panel).pack(pady=5)


    def game(self):
        first_name = self.first_player_entry.get()
        second_name = self.second_player_entry.get()
        entry1 = self.entry.get()
        entry2 = self.entry1.get()
        choice = ["rock" , "paper" , "scissor"]
        if entry1 not in choice or entry2 not in choice :
            self.result.config(text="pls enter the valid choice" ,fg='red')
            return

        if entry1 == entry2:
            self.result.config(text="its ties " , fg='blue')
        elif (entry1 == "rock" and entry2 == "scissor") or (entry1 =="scissor" and entry2== "paper") or (entry1=="paper" and entry2== "rock"):
            self.result.config(text=f"{first_name} own the match" , fg='green')
        else:
            self.result.config(text=f"{second_name} wins the match")

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissor(root)
    root.mainloop()












