from ttkbootstrap import Style
from tkinter import StringVar, ttk

style = Style(theme = 'cosmo')

window = style.master


user_datas = [
    {'Szamla':43670, 'Ruha':12490, 'Etel': 41850},
    {'Szamla':55470, 'Ruha':8380, 'Etel': 38910},
    {'Szamla':47290, 'Ruha':7060, 'Etel': 55050}
    ]


e_szamla = ttk.Entry(window)
e_szamla.pack()
e_ruha = ttk.Entry(window)
e_ruha.pack()
e_etel = ttk.Entry(window)
e_etel.pack()

option_lists = [1, 1, 2, 3]
value_inside = StringVar(window)
value_inside.set('Select')

menu_button = ttk.OptionMenu(window, value_inside, *option_lists)
menu_button.pack()

def get_option(index):
    global e_szamla, e_ruha, e_etel, user_datas

    e_szamla.delete(0, 10)
    e_ruha.delete(0, 10)
    e_etel.delete(0, 10)

    e_szamla.insert(0, user_datas[int(index)-1]['Szamla'])
    e_ruha.insert(0, user_datas[int(index)-1]['Ruha'])
    e_etel.insert(0, user_datas[int(index)-1]['Etel'])

submit_button = ttk.Button(window, text = 'Submit', style = 'primary.Outline.TButton', command = lambda: get_option(value_inside.get()))
submit_button.pack()

window.mainloop()