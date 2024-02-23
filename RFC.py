#Cristian Ovando Gómez
#221256
#RFC = OAGC

import tkinter as tk
import networkx as nx

class AutomataRFC:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Validación de RFC ")
        self.root.geometry("650x530")

        self.entry_label = tk.Label(self.root, text="Ingrese la cadena RFC OAGC:")
        self.entry_label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        self.validate_button = tk.Button(self.root, text="Validar", command=self.validar_rfc_and_show)
        self.validate_button.pack()

        self.canvas = tk.Canvas(self.root, bg="white", width=600, height=400)
        self.canvas.pack()

        self.root.mainloop()

    def validar_rfc_and_show(self):
        rfc = self.entry.get().upper()

        try:
            if self.validar_cadena_rfc(rfc):
                self.result_label.config(text="Cadena RFC válida.")
                self.mostrar_automata(rfc)
            else:
                self.result_label.config(text="Cadena RFC inválida.")
        except ValueError as e:
            self.result_label.config(text=str(e))

    def validar_cadena_rfc(self, rfc):
        if not rfc:
            raise ValueError("Cadena RFC no válida. Debe ingresar al menos un carácter.")

        if len(rfc) > 4:
            raise ValueError("Cadena RFC no válida. La longitud máxima es de 4 caracteres.")

        validas = {'OAGC', 'OAG', 'OA', 'O'}
        invalidas = {'OAC', 'OG', 'OC'}

        if rfc in validas and rfc not in invalidas:
            return True
        else:
            return False

    def mostrar_automata(self, rfc):
        self.canvas.delete("all")

        G = nx.DiGraph()
        G.add_node('inicio')

        current_node = 'inicio'
        for i, char in enumerate(rfc):
            next_node = f'q{i}'
            G.add_node(next_node)
            G.add_edge(current_node, next_node, label=char)
            current_node = next_node

        last_node = current_node

        pos = {}
        num_nodes = len(G.nodes)
        y = 200
        x_spacing = 500 / (num_nodes - 1)
        for i, node in enumerate(G.nodes):
            x = 50 + x_spacing * i
            pos[node] = (x, y)

        for node in G.nodes:
            x, y = pos[node]
            if node == last_node:
                self.canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill="yellow", outline="black", width=2)
                self.canvas.create_oval(x - 25, y - 25, x + 25, y + 25, fill="yellow", outline="black", width=2)
            else:
                self.canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill="yellow", outline="black", width=2)
            self.canvas.create_text(x, y - 15, text=node, font=("Arial", 12, "bold"), fill="black")

        for u, v, data in G.edges(data=True):
            x1, y1 = pos[u]
            x2, y2 = pos[v]
            self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, width=3, fill="black")
            if 'label' in data:
                label_x = (x1 + x2) / 2
                label_y = (y1 + y2) / 2 - 25
                self.canvas.create_text(label_x, label_y, text=data['label'], font=("Arial", 14), fill="black")

if __name__ == "__main__":
    automata = AutomataRFC()
