from types import LambdaType
from ttkbootstrap import Style
from tkinter import Frame, Label, StringVar, Widget, ttk

style = Style(theme = 'cosmo')

window = style.master
window.iconbitmap('icon/icon.ico')
window.title('Fine')

# user's datas in a dictionary

user_datas = {
    'Január':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Eddig':0, 'Cél':0},
    'Február':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Eddig':0, 'Cél':0}, 
    'Március':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Eddig':0, 'Cél':0}, 
    'Április':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Eddig':0, 'Cél':0}, 
    'Május':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Eddig':0, 'Cél':0}, 
    'Június':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Eddig':0, 'Cél':0}, 
    'Július':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Eddig':0, 'Cél':0}, 
    'Augusztus':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Eddig':0, 'Cél':0},
    'Szeptember':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Eddig':0, 'Cél':0},
    'Október':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Eddig':0, 'Cél':0},
    'November':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Eddig':0, 'Cél':0},
    'December':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Eddig':0, 'Cél':0}
    }

actual_month = 'December'

# loading last saves and save function

with open('user_saves.txt', 'r') as file:
    saves = file.read()
    user_datas = saves

def save():
    global user_datas

    with open('user_saves.txt', 'w') as file:
        file.write(repr(user_datas))

# I am creating a frame for 'spending'

frame_left = ttk.Frame(window, padding = (20, 20, 10, 20))

# Spending's labels

label_overhead = ttk.Label(frame_left, text = 'Számlák, rezsi')
label_shopping = ttk.Label(frame_left, text = 'Bevásárlás')
label_clothes = ttk.Label(frame_left, text = 'Ruházat')
label_traffic = ttk.Label(frame_left, text = 'Közlekedés')
label_health = ttk.Label(frame_left, text = 'Egészség')
label_entertainment = ttk.Label(frame_left, text = 'Szórakozás')
label_payment = ttk.Label(frame_left, text = 'Jövedelem') 
label_spending = ttk.Label(frame_left, text = 'Költés')

# Entrys

l_payment_frame = ttk.Frame(frame_left, padding = (5, 5, 5, 5), style = 'primary.TFrame')
l_overhead_frame = ttk.Frame(frame_left, padding = (5, 5, 5, 5))
l_shopping_frame = ttk.Frame(frame_left, padding = (5, 5, 5, 5))
l_clothes_frame = ttk.Frame(frame_left, padding = (5, 5, 5, 5))
l_traffic_frame = ttk.Frame(frame_left, padding = (5, 5, 5, 5))
l_health_frame = ttk.Frame(frame_left, padding = (5, 5, 5, 5))
l_entertainment_frame = ttk.Frame(frame_left, padding = (5, 5, 5, 5))
l_spending_frame = ttk.Frame(frame_left, padding = (5, 5, 5, 5), style = 'primary.TFrame')

l_payment = ttk.Label(l_payment_frame, text = '0Ft', style = 'primary.Inverse.TLabel', width = 15, anchor = 'center') 
l_overhead = ttk.Label(l_overhead_frame, text = '0Ft', width = 15, anchor = 'center')
l_shopping = ttk.Label(l_shopping_frame, text = '0Ft', width = 15, anchor = 'center')
l_clothes = ttk.Label(l_clothes_frame, text = '0Ft', width = 15, anchor = 'center')
l_traffic = ttk.Label(l_traffic_frame, text = '0Ft', width = 15, anchor = 'center')
l_health = ttk.Label(l_health_frame, text = '0Ft', width = 15, anchor = 'center')
l_entertainment = ttk.Label(l_entertainment_frame, text = '0Ft', width = 15, anchor = 'center')
l_spending = ttk.Label(l_spending_frame, text = '0Ft', style = 'primary.Inverse.TLabel', width = 15, anchor = 'center') 

# I am drawing all labels and entrys on the screen with grid system

frame_left.grid(column = 0, row = 0)

label_overhead.grid(column = 0, row = 0, pady = (0, 10))
label_shopping.grid(column = 1, row = 0, pady = (0, 10))
label_clothes.grid(column = 0, row = 2, pady = (0, 10))
label_traffic.grid(column = 1, row = 2, pady = (0, 10))
label_health.grid(column = 0, row = 4, pady = (0, 10))
label_entertainment.grid(column = 1, row = 4, pady = (0, 10))
label_payment.grid(column = 0, row = 6, pady = (0, 10))
label_spending.grid(column = 1, row = 6, pady = (0, 10))

l_overhead_frame.grid(column = 0, row = 1, pady = (0, 30), padx = (0, 10))
l_shopping_frame.grid(column = 1, row = 1, pady = (0, 30), padx = (10, 0))
l_clothes_frame.grid(column = 0, row = 3, pady = (0, 30), padx = (0, 10))
l_traffic_frame.grid(column = 1, row = 3, pady = (0, 30), padx = (10, 0))
l_health_frame.grid(column = 0, row = 5, pady = (0, 30), padx = (0, 10))
l_entertainment_frame.grid(column = 1, row = 5, pady = (0, 30), padx = (10, 0))
l_payment_frame.grid(column = 0, row = 7, pady = (0, 30), padx = (0, 10))
l_spending_frame.grid(column = 1, row = 7, pady = (0, 30), padx = (10, 0))

l_payment.grid(column = 0, row = 0)
l_overhead.grid(column = 0, row = 0)
l_shopping.grid(column = 0, row = 0)
l_clothes.grid(column = 0, row = 0)
l_traffic.grid(column = 0, row = 0)
l_health.grid(column = 0, row = 0)
l_entertainment.grid(column = 0, row = 0)
l_spending.grid(column = 0, row = 0)

# Another side

frame_right = ttk.Frame(window, padding = (10, 20, 20, 20))

month_previous_b = ttk.Button(frame_right, text = '⯇', style = 'primary.Outline.TButton',)
month_next_b = ttk.Button(frame_right, text = '⯈', style = 'primary.Outline.TButton',)
current_month_frame = ttk.Frame(frame_right, padding = (5, 5, 5, 5), style = 'primary.TFrame')
current_month_l = ttk.Label(current_month_frame, text = 'December', style = 'primary.Inverse.TLabel', width = 20, anchor = 'center')

# Saving frame

saving_frame = ttk.Frame(frame_right, style = 'secondary.TFrame', padding = (20, 20, 20, 20))

so_far_label = ttk.Label(saving_frame, text = 'Eddig megtakarított', style = 'secondary.Inverse.TLabel')
so_far_number_frame = ttk.Frame(saving_frame, padding = (5, 5, 5, 5), style = 'secondary.TFrame')
so_far_number_label = ttk.Label(so_far_number_frame, width = 15, text = '0Ft', anchor = 'center', style = 'secondary.Inverse.TLabel')
so_far_progressbar = ttk.Progressbar(saving_frame, value = 75, length = 160)

goal_label = ttk.Label(saving_frame, text = 'Megtakarítási cél', style = 'secondary.Inverse.TLabel') 
goal_number_frame = ttk.Frame(saving_frame, padding = (5, 5, 5, 5), style = 'secondary.TFrame')
goal_number_label = ttk.Label(goal_number_frame, width = 15, text = '0Ft', anchor = 'center', style = 'secondary.Inverse.TLabel')
goal_progressbar = ttk.Progressbar(saving_frame, value = 40, length = 160)

# Adds options

sp_options = ['Kategória','Számlák, rezsi','Bevásárlás','Ruházat','Közlekedés','Egészség','Szórakozás']
sp_option = StringVar()
sp_option.set('Bevásárlás')

goal_add_e = ttk.Entry(frame_right, width = 15)
goal_add_b = ttk.Button(frame_right, text = 'Új m. cél', style = 'primary.Outline.TButton', width = 15)

payment_add_e = ttk.Entry(frame_right, width = 15)
payment_add_b = ttk.Button(frame_right, text = '+ Jövedelem', style = 'primary.Outline.TButton', width = 15)

spending_add_e = ttk.Entry(frame_right, width = 15)
spending_add_mb = ttk.OptionMenu(frame_right, sp_option, *sp_options)
spending_add_b = ttk.Button(frame_right, text = '+ Költés', style = 'primary.Outline.TButton', width = 15)

# Drawing all widgets on the screen

frame_right.grid(column = 1, row = 0)

month_previous_b.grid(column = 0, row = 0, pady = (0, 20))
month_next_b.grid(column = 2, row = 0, pady = (0, 20))
current_month_frame.grid(column = 1, row = 0, pady = (0, 20))
current_month_l.grid(column = 0, row = 0)

saving_frame.grid(column = 0, row = 1, columnspan = 3, pady = (0, 20))

so_far_label.grid(column = 0, row = 0, pady = (0, 10), padx = (0, 5), sticky = 'e')
so_far_number_frame.grid(column = 1, row = 0, pady = (0, 10), padx = (5, 5))
so_far_number_label.grid(column = 0, row = 0)
so_far_progressbar.grid(column = 2, row = 0, pady = (0, 10), padx = (5, 0))

goal_label.grid(column = 0, row = 1, padx = (0, 5), sticky = 'e')
goal_number_frame.grid(column = 1, row = 1, padx = (5, 5))
goal_number_label.grid(column = 0, row = 0)
goal_progressbar.grid(column = 2, row = 1, padx = (5, 0))

goal_add_e.grid(column = 0, row = 2, sticky = 'e', padx = (0, 5), pady = (0, 20))
goal_add_b.grid(column = 2, row = 2, sticky = 'w', padx = (5, 0), pady = (0, 20))

payment_add_e.grid(column = 0, row = 3, sticky = 'e', padx = (0, 5), pady = (0, 20))
payment_add_b.grid(column = 2, row = 3, sticky = 'w', padx = (5, 0), pady = (0, 20))

spending_add_e.grid(column = 0, row = 4, sticky = 'e', padx = (0, 5), pady = (0, 10))
spending_add_mb.grid(column = 1, row = 4, pady = (0, 10))
spending_add_b.grid(column = 2, row = 4, sticky = 'w', padx = (5, 0), pady = (0, 10))

rights = Label(window, text = 'Created by Lekner Norbert - ™ All rights reserved.')
rights.grid(column = 0, row = 4, columnspan = 3, sticky = 'se')

window.mainloop()