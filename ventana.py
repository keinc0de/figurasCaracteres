import tkinter as tk
from tkinter import ttk
from op import Operaciones


class Ventana(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        parent.title("holas")
        self.widgets()

    def widgets(self):
        self.pack(fill='both', expand=1)
        self.fr_top = ttk.Frame(self)
        self.fr_top.pack(fill='x', expand=1)
        self.fr_bot = ttk.Frame(self)
        self.fr_bot.pack(fill='both', expand=1)
        
        lb1 = ttk.Label(self.fr_top, text=' DIMENSIONES ').pack(side='left')
        self.vsp = tk.StringVar()
        spb = ttk.Spinbox(
            self.fr_top, textvariable=self.vsp, width=6,
            from_=1, to=40
        )
        spb.pack(side='left')
        self.vsp.set('4')
        lb2 = ttk.Label(self.fr_top, text=' CARACTER ').pack(side='left')
        self.vc  = tk.StringVar()
        en = ttk.Entry(self.fr_top, width=6, textvariable=self.vc)
        en.pack(side='left')
        self.vc.set('*')
        bt_a = ttk.Button(
            self.fr_top, text='a', width=6, command=self.grafica
        )
        bt_a.pack(side='right')

        self.wtxt = tk.Text(self.fr_bot, width=20)
        self.wtxt.pack(side='left', fill='both', expand=1)
        scroll = ttk.Scrollbar(self.fr_bot, command=self.wtxt.yview)
        scroll.pack(side='right', fill='y')
        self.wtxt.config(yscrollcommand=scroll.set)


        self.v_sld = tk.StringVar()
        lb3 = ttk.Label(self.fr_top, text='0', textvariable=self.v_sld)
        lb3.pack(side='left', padx=4)
        self.sld = ttk.Scale(
            self.fr_top, orient='horizontal',
            from_=0, to=10,
            command=self.verValor
        )
        self.sld.pack(side='left', fill='x', expand=1, padx=4)
        self.npre = 0

    def accion(self, npre=0):
        valor = int(self.vsp.get())
        caracter = self.vc.get()
        op = Operaciones(caracter)
        texto = op.figura(w=valor, pre=' '*npre)
        # print(texto)
        self.wtxt.delete('1.0', 'end')
        self.wtxt.insert(tk.END, texto)

    def verValor(self, n):
        num = int(round(float(n), 1))
        texto = ''
        if self.npre!=num:
            self.npre = num
            self.v_sld.set(str(self.npre))
            texto = self.accion(num)

    def grafica(self):
        self.accion()
        valor = int(self.vsp.get())
        # print(valor, valor*2)
        self.sld.config(to=valor*2)



if __name__=="__main__":
    rz = tk.Tk()
    app = Ventana(rz)
    s = ttk.Style()
    s.theme_use('clam')
    rz.geometry('400x150')
    app.mainloop()
