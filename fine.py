from ttkbootstrap import Style
from tkinter import Label, StringVar, Widget, ttk

style = Style(theme = 'journal')

window = style.master
window.iconbitmap('icon/icon.ico')
window.title('Fine')

# I am creating a frame for 'spending'

frame_left = ttk.Frame(window, padding = (20, 20, 10, 20))

# Spending's labels

label_payment = ttk.Label(frame_left, text = 'Jövedelem') 
label_overhead = ttk.Label(frame_left, text = 'Számlák, rezsi')
label_shopping = ttk.Label(frame_left, text = 'Bevásárlás')
label_clothes = ttk.Label(frame_left, text = 'Ruházat')
label_traffic = ttk.Label(frame_left, text = 'Közlekedés')
label_health = ttk.Label(frame_left, text = 'Egészség')
label_entertainment = ttk.Label(frame_left, text = 'Szórakozás')
label_spending = ttk.Label(frame_left, text = 'Költés')

# Entrys

entry_payment = ttk.Button(frame_left, text = '0Ft')
entry_overhead = ttk.Entry(frame_left)
entry_shopping = ttk.Entry(frame_left)
entry_clothes = ttk.Entry(frame_left)
entry_traffic = ttk.Entry(frame_left)
entry_health = ttk.Entry(frame_left)
entry_entertainment = ttk.Entry(frame_left)
entry_spending = ttk.Button(frame_left, text = '0Ft')

# I am drawing all labels and entrys on the screen with grid system

frame_left.grid(column = 0, row = 0)

label_payment.grid(column = 0, row = 0, columnspan = 2, pady = (0, 10))
label_overhead.grid(column = 0, row = 2, pady = (0, 10))
label_shopping.grid(column = 1, row = 2, pady = (0, 10))
label_clothes.grid(column = 0, row = 4, pady = (0, 10))
label_traffic.grid(column = 1, row = 4, pady = (0, 10))
label_health.grid(column = 0, row = 6, pady = (0, 10))
label_entertainment.grid(column = 1, row = 6, pady = (0, 10))
label_spending.grid(column = 0, row = 8, columnspan = 2, pady = (0, 10))

entry_payment.grid(column = 0, row = 1, columnspan = 2, pady = (0, 20))
entry_overhead.grid(column = 0, row = 3, pady = (0, 20), padx = (0, 5))
entry_shopping.grid(column = 1, row = 3, pady = (0, 20), padx = (5, 0))
entry_clothes.grid(column = 0, row = 5, pady = (0, 20), padx = (0, 5))
entry_traffic.grid(column = 1, row = 5, pady = (0, 20), padx = (5, 0))
entry_health.grid(column = 0, row = 7, pady = (0, 20), padx = (0, 5))
entry_entertainment.grid(column = 1, row = 7, pady = (0, 20), padx = (5, 0))
entry_spending.grid(column = 0, row = 9, columnspan = 2, pady = (0, 20))

# Another side

frame_right = ttk.Frame(window, padding = (10, 20, 20, 20))

month_previous_b = ttk.Button(frame_right, text = '⯇')
month_next_b = ttk.Button(frame_right, text = '⯈')
current_month = ttk.Button(frame_right, text = 'November', style = 'secondary.TButton', width = 15)

# Saving frame

saving_frame = ttk.LabelFrame(frame_right, text = 'Megtakarítás', padding = (20, 20, 20, 20))

so_far_label = ttk.Label(saving_frame, text = 'Eddig')
so_far_entry = ttk.Entry(saving_frame, width = 15)
so_far_progressbar = ttk.Progressbar(saving_frame, value = 75, length = 200)

goal_label = ttk.Label(saving_frame, text = 'Cél') 
goal_entry = ttk.Entry(saving_frame, width = 15)
goal_progressbar = ttk.Progressbar(saving_frame, value = 40, length = 200)

# Adds options

sp_options = [
    'Számlák, rezsi',
    'Bevásárlás',
    'Ruházat',
    'Közlekedés',
    'Egészség',
    'Szórakozás'
]
sp_option = StringVar()
sp_option.set(sp_options[0])

goal_add_e = ttk.Entry(frame_right, width = 15)
goal_add_b = ttk.Button(frame_right, text = 'Új m. cél', style = 'secondary.TButton', width = 15)

payment_add_e = ttk.Entry(frame_right, width = 15)
payment_add_b = ttk.Button(frame_right, text = '+ Jövedelem', style = 'secondary.TButton', width = 15)

spending_add_e = ttk.Entry(frame_right, width = 15)
spending_add_mb = ttk.OptionMenu(frame_right, sp_option, *sp_options)
spending_add_b = ttk.Button(frame_right, text = '+ Költés', style = 'secondary.TButton', width = 15)

# Drawing all widgets on the screen

frame_right.grid(column = 1, row = 0)

month_previous_b.grid(column = 0, row = 0, pady = (0, 20))
month_next_b.grid(column = 2, row = 0, pady = (0, 20))
current_month.grid(column = 1, row = 0, pady = (0, 20))

saving_frame.grid(column = 0, row = 1, columnspan = 3, pady = (0, 20))

so_far_label.grid(column = 0, row = 0, pady = (0, 10), padx = (0, 5), sticky = 'e')
so_far_entry.grid(column = 1, row = 0, pady = (0, 10), padx = (5, 5))
so_far_progressbar.grid(column = 2, row = 0, pady = (0, 10), padx = (5, 0))

goal_label.grid(column = 0, row = 1, padx = (0, 5), sticky = 'e')
goal_entry.grid(column = 1, row = 1, padx = (5, 5))
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