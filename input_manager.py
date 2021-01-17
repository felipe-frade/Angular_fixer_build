import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button_tempo = tk.Button(self)
        self.button_tempo["text"] = "Estou com tempo"
        self.button_tempo["command"] = self.tenho_tempo
        self.button_tempo.pack(side="top")

        self.button_n_tempo = tk.Button(self)
        self.button_n_tempo["text"] = "Estou com pouco tempo"
        self.button_n_tempo["command"] = self.nao_tenho_tempo
        self.button_n_tempo.pack(side="top")

    def create_button_exit(self):
        self.quit = tk.Button(self, text="EXIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def tenho_tempo(self):
        print('tenho tempo')
    
    def nao_tenho_tempo(self):
        print('não tenho tempo')

def config():
    root = tk.Tk()
    app = Application(master=root)
    # app.create_button_exit()
    app.master.title("Configuration setup")
    app.master.geometry("400x300+300+300")
    app.mainloop()