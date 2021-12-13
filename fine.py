from os import extsep
from types import LambdaType
from ttkbootstrap import Style
from tkinter import Frame, Label, StringVar, Widget, ttk
import ast

style = Style(theme = 'cosmo')

window = style.master
window.iconbitmap('icon/icon.ico')
window.title('Fine')
window.resizable(False, False)

# user's datas in a dictionary

user_datas = {
    'Január':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Cél':0},
    'Február':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Cél':0}, 
    'Március':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Cél':0}, 
    'Április':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Cél':0}, 
    'Május':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Cél':0}, 
    'Június':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Cél':0}, 
    'Július':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Cél':0}, 
    'Augusztus':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Cél':0},
    'Szeptember':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Cél':0},
    'Október':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Cél':0},
    'November':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Cél':0},
    'December':{'Jövedelem':0, 'Számlák, rezsi':0, 'Bevásárlás':0, 'Ruházat':0, 'Közlekedés':0, 'Egészség':0, 'Szórakozás':0, 'Cél':0}
    }

actual_month = 1
months = ('Január', 'Február', 'Március', 'Április', 'Május', 'Június', 'Július', 'Augusztus', 'Szeptember', 'Október', 'November', 'December')

def total_spending():
    global user_datas, actual_month, months
    total = 0

    for key, value in user_datas[months[actual_month]].items():
        if key != 'Jövedelem' and key != 'Eddig' and key != 'Cél':
            total += value

    return total

def next_month():
    # i am changing actual month and drawing all items on screen again
    global user_datas, actual_month, months, current_month_l, so_far_number_label, goal_number_label, so_far_progressbar, goal_progressbar
    global l_overhead, l_shopping, l_clothes, l_traffic, l_health, l_entertainment, l_payment, l_spending

    if actual_month == 11:
        actual_month = 0
    else:
        actual_month += 1

    l_overhead = ttk.Label(l_overhead_frame, text = str(user_datas[months[actual_month]]['Számlák, rezsi']) + 'Ft', width = 15, anchor = 'center')
    l_shopping = ttk.Label(l_shopping_frame, text = str(user_datas[months[actual_month]]['Bevásárlás']) + 'Ft', width = 15, anchor = 'center')
    l_clothes = ttk.Label(l_clothes_frame, text = str(user_datas[months[actual_month]]['Ruházat']) + 'Ft', width = 15, anchor = 'center')
    l_traffic = ttk.Label(l_traffic_frame, text = str(user_datas[months[actual_month]]['Közlekedés']) + 'Ft', width = 15, anchor = 'center')
    l_health = ttk.Label(l_health_frame, text = str(user_datas[months[actual_month]]['Egészség']) + 'Ft', width = 15, anchor = 'center')
    l_entertainment = ttk.Label(l_entertainment_frame, text = str(user_datas[months[actual_month]]['Szórakozás']) + 'Ft', width = 15, anchor = 'center')
    l_payment = ttk.Label(l_payment_frame, text = str(user_datas[months[actual_month]]['Jövedelem']) + 'Ft', style = 'primary.Inverse.TLabel', width = 15, anchor = 'center')
    l_spending = ttk.Label(l_spending_frame, text = str(total_spending()) + 'Ft', style = 'primary.Inverse.TLabel', width = 15, anchor = 'center') 

    current_month_l = ttk.Label(current_month_frame, text = months[actual_month], style = 'primary.Inverse.TLabel', width = 20, anchor = 'center')
    so_far_number_label = ttk.Label(so_far_number_frame, width = 15, text = str(user_datas[months[actual_month]]['Jövedelem'] - total_spending()) + 'Ft', anchor = 'center', style = 'secondary.Inverse.TLabel')
    so_far_progressbar = ttk.Progressbar(saving_frame, value = s_progressbar_value(), length = 160, style = 'primary.Striped.Horizontal.TProgressbar')
    goal_number_label = ttk.Label(goal_number_frame, width = 15, text = str(user_datas[months[actual_month]]['Cél']) + 'Ft', anchor = 'center', style = 'secondary.Inverse.TLabel')
    goal_progressbar = ttk.Progressbar(saving_frame, value = g_progressbar_value(), length = 160, style = 'primary.Striped.Horizontal.TProgressbar')

    l_overhead.grid(column = 0, row = 0)
    l_shopping.grid(column = 0, row = 0)
    l_clothes.grid(column = 0, row = 0)
    l_traffic.grid(column = 0, row = 0)
    l_health.grid(column = 0, row = 0)
    l_entertainment.grid(column = 0, row = 0)
    l_payment.grid(column = 0, row = 0)
    l_spending.grid(column = 0, row = 0)

    current_month_l.grid(column = 0, row = 0)
    so_far_number_label.grid(column = 0, row = 0)
    so_far_progressbar.grid(column = 2, row = 0, pady = (0, 10), padx = (5, 0))
    goal_number_label.grid(column = 0, row = 0)
    goal_progressbar.grid(column = 2, row = 1, padx = (5, 0))

    save()

def previous_month():
    # i am changing actual month and drawing all items on screen again
    global user_datas, actual_month, months, current_month_l, so_far_number_label, goal_number_label, so_far_progressbar, goal_progressbar
    global l_overhead, l_shopping, l_clothes, l_traffic, l_health, l_entertainment, l_payment, l_spending


    if actual_month == 0:
        actual_month = 11
    else:
        actual_month -= 1

    l_overhead = ttk.Label(l_overhead_frame, text = str(user_datas[months[actual_month]]['Számlák, rezsi']) + 'Ft', width = 15, anchor = 'center')
    l_shopping = ttk.Label(l_shopping_frame, text = str(user_datas[months[actual_month]]['Bevásárlás']) + 'Ft', width = 15, anchor = 'center')
    l_clothes = ttk.Label(l_clothes_frame, text = str(user_datas[months[actual_month]]['Ruházat']) + 'Ft', width = 15, anchor = 'center')
    l_traffic = ttk.Label(l_traffic_frame, text = str(user_datas[months[actual_month]]['Közlekedés']) + 'Ft', width = 15, anchor = 'center')
    l_health = ttk.Label(l_health_frame, text = str(user_datas[months[actual_month]]['Egészség']) + 'Ft', width = 15, anchor = 'center')
    l_entertainment = ttk.Label(l_entertainment_frame, text = str(user_datas[months[actual_month]]['Szórakozás']) + 'Ft', width = 15, anchor = 'center')
    l_payment = ttk.Label(l_payment_frame, text = str(user_datas[months[actual_month]]['Jövedelem']) + 'Ft', style = 'primary.Inverse.TLabel', width = 15, anchor = 'center')
    l_spending = ttk.Label(l_spending_frame, text = str(total_spending()) + 'Ft', style = 'primary.Inverse.TLabel', width = 15, anchor = 'center') 

    current_month_l = ttk.Label(current_month_frame, text = months[actual_month], style = 'primary.Inverse.TLabel', width = 20, anchor = 'center')
    so_far_number_label = ttk.Label(so_far_number_frame, width = 15, text = str(user_datas[months[actual_month]]['Jövedelem'] - total_spending()) + 'Ft', anchor = 'center', style = 'secondary.Inverse.TLabel')
    so_far_progressbar = ttk.Progressbar(saving_frame, value = s_progressbar_value(), length = 160, style = 'primary.Striped.Horizontal.TProgressbar')
    goal_number_label = ttk.Label(goal_number_frame, width = 15, text = str(user_datas[months[actual_month]]['Cél']) + 'Ft', anchor = 'center', style = 'secondary.Inverse.TLabel')
    goal_progressbar = ttk.Progressbar(saving_frame, value = g_progressbar_value(), length = 160, style = 'primary.Striped.Horizontal.TProgressbar')

    l_overhead.grid(column = 0, row = 0)
    l_shopping.grid(column = 0, row = 0)
    l_clothes.grid(column = 0, row = 0)
    l_traffic.grid(column = 0, row = 0)
    l_health.grid(column = 0, row = 0)
    l_entertainment.grid(column = 0, row = 0)
    l_payment.grid(column = 0, row = 0)
    l_spending.grid(column = 0, row = 0)

    current_month_l.grid(column = 0, row = 0)
    so_far_number_label.grid(column = 0, row = 0)
    so_far_progressbar.grid(column = 2, row = 0, pady = (0, 10), padx = (5, 0))
    goal_number_label.grid(column = 0, row = 0)
    goal_progressbar.grid(column = 2, row = 1, padx = (5, 0))

    save()

# loading last saves and save function

def save():
    global user_datas, actual_month

    with open('user_saves.txt', 'w', encoding = 'utf-8') as file:
        file.write(str(actual_month) + '\n')
        file.write(repr(user_datas))

with open('user_saves.txt', 'r', encoding = 'utf-8') as file:
    actual_month = int(file.readline().strip())
    
    saves = file.read()
    user_datas = ast.literal_eval(saves)

def clicked_goal(goal):
    global user_datas, actual_month, months, goal_number_label, goal_add_e, goal_progressbar

    goal_add_e.delete(0, 'end')

    try:
        user_datas[months[actual_month]]['Cél'] = int(goal)
        goal_number_label = ttk.Label(goal_number_frame, width = 15, text = str(user_datas[months[actual_month]]['Cél']) + 'Ft', anchor = 'center', style = 'secondary.Inverse.TLabel')
        goal_progressbar = ttk.Progressbar(saving_frame, value = g_progressbar_value(), length = 160, style = 'primary.Striped.Horizontal.TProgressbar')
        
        goal_number_label.grid(column = 0, row = 0)
        goal_progressbar.grid(column = 2, row = 1, padx = (5, 0))

        save()
    except:
        print('A megadott értékek hibásak!')

def clicked_payment(payment):
    global user_datas, actual_month, months, l_payment, so_far_number_label, so_far_progressbar, goal_progressbar

    payment_add_e.delete(0, 'end')

    try: 
        user_datas[months[actual_month]]['Jövedelem'] += int(payment)
        
        l_payment = ttk.Label(l_payment_frame, text = str(user_datas[months[actual_month]]['Jövedelem']) + 'Ft', style = 'primary.Inverse.TLabel', width = 15, anchor = 'center')
        so_far_number_label = ttk.Label(so_far_number_frame, width = 15, text = str(user_datas[months[actual_month]]['Jövedelem'] - total_spending()) + 'Ft', anchor = 'center', style = 'secondary.Inverse.TLabel')
        so_far_progressbar = ttk.Progressbar(saving_frame, value = s_progressbar_value(), length = 160, style = 'primary.Striped.Horizontal.TProgressbar')
        goal_progressbar = ttk.Progressbar(saving_frame, value = g_progressbar_value(), length = 160, style = 'primary.Striped.Horizontal.TProgressbar')

        l_payment.grid(column = 0, row = 0)
        so_far_number_label.grid(column = 0, row = 0)
        so_far_progressbar.grid(column = 2, row = 0, pady = (0, 10), padx = (5, 0))
        goal_progressbar.grid(column = 2, row = 1, padx = (5, 0))

        save()
    except:
        print('A megadott értékek hibásak!')

def clicked_spending(a, spending):
    global user_datas, actual_month, months, spending_add_e, so_far_number_label, so_far_progressbar, goal_progressbar
    global l_overhead, l_shopping, l_clothes, l_traffic, l_health, l_entertainment, l_payment, l_spending

    try:
        user_datas[months[actual_month]][a] += int(spending)

        spending_add_e.delete(0, 'end')

        l_overhead = ttk.Label(l_overhead_frame, text = str(user_datas[months[actual_month]]['Számlák, rezsi']) + 'Ft', width = 15, anchor = 'center')
        l_shopping = ttk.Label(l_shopping_frame, text = str(user_datas[months[actual_month]]['Bevásárlás']) + 'Ft', width = 15, anchor = 'center')
        l_clothes = ttk.Label(l_clothes_frame, text = str(user_datas[months[actual_month]]['Ruházat']) + 'Ft', width = 15, anchor = 'center')
        l_traffic = ttk.Label(l_traffic_frame, text = str(user_datas[months[actual_month]]['Közlekedés']) + 'Ft', width = 15, anchor = 'center')
        l_health = ttk.Label(l_health_frame, text = str(user_datas[months[actual_month]]['Egészség']) + 'Ft', width = 15, anchor = 'center')
        l_entertainment = ttk.Label(l_entertainment_frame, text = str(user_datas[months[actual_month]]['Szórakozás']) + 'Ft', width = 15, anchor = 'center')
        l_payment = ttk.Label(l_payment_frame, text = str(user_datas[months[actual_month]]['Jövedelem']) + 'Ft', style = 'primary.Inverse.TLabel', width = 15, anchor = 'center')
        l_spending = ttk.Label(l_spending_frame, text = str(total_spending()) + 'Ft', style = 'primary.Inverse.TLabel', width = 15, anchor = 'center') 
        so_far_number_label = ttk.Label(so_far_number_frame, width = 15, text = str(user_datas[months[actual_month]]['Jövedelem'] - total_spending()) + 'Ft', anchor = 'center', style = 'secondary.Inverse.TLabel')
        so_far_progressbar = ttk.Progressbar(saving_frame, value = s_progressbar_value(), length = 160, style = 'primary.Striped.Horizontal.TProgressbar')
        goal_progressbar = ttk.Progressbar(saving_frame, value = g_progressbar_value(), length = 160, style = 'primary.Striped.Horizontal.TProgressbar')

        l_overhead.grid(column = 0, row = 0)
        l_shopping.grid(column = 0, row = 0)
        l_clothes.grid(column = 0, row = 0)
        l_traffic.grid(column = 0, row = 0)
        l_health.grid(column = 0, row = 0)
        l_entertainment.grid(column = 0, row = 0)
        l_payment.grid(column = 0, row = 0)
        l_spending.grid(column = 0, row = 0)
        so_far_number_label.grid(column = 0, row = 0)
        so_far_progressbar.grid(column = 2, row = 0, pady = (0, 10), padx = (5, 0))
        goal_progressbar.grid(column = 2, row = 1, padx = (5, 0))

        save()
    except:
        spending_add_e.delete(0, 'end')
        print('A megadott értékek hibásak!')

def s_progressbar_value():
    global user_datas, actual_month, months

    try:
        return int((user_datas[months[actual_month]]['Jövedelem'] - total_spending()) / (user_datas[months[actual_month]]['Jövedelem'] / 100))
    except ZeroDivisionError:
        return 0
    
def g_progressbar_value():
    global user_datas, actual_month, months

    try:
        return (user_datas[months[actual_month]]['Jövedelem'] - total_spending()) / (user_datas[months[actual_month]]['Cél'] / 100)
    except ZeroDivisionError:
        return 100

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
 
l_overhead = ttk.Label(l_overhead_frame, text = str(user_datas[months[actual_month]]['Számlák, rezsi']) + 'Ft', width = 15, anchor = 'center')
l_shopping = ttk.Label(l_shopping_frame, text = str(user_datas[months[actual_month]]['Bevásárlás']) + 'Ft', width = 15, anchor = 'center')
l_clothes = ttk.Label(l_clothes_frame, text = str(user_datas[months[actual_month]]['Ruházat']) + 'Ft', width = 15, anchor = 'center')
l_traffic = ttk.Label(l_traffic_frame, text = str(user_datas[months[actual_month]]['Közlekedés']) + 'Ft', width = 15, anchor = 'center')
l_health = ttk.Label(l_health_frame, text = str(user_datas[months[actual_month]]['Egészség']) + 'Ft', width = 15, anchor = 'center')
l_entertainment = ttk.Label(l_entertainment_frame, text = str(user_datas[months[actual_month]]['Szórakozás']) + 'Ft', width = 15, anchor = 'center')
l_payment = ttk.Label(l_payment_frame, text = str(user_datas[months[actual_month]]['Jövedelem']) + 'Ft', style = 'primary.Inverse.TLabel', width = 15, anchor = 'center')
l_spending = ttk.Label(l_spending_frame, text = str(total_spending()) + 'Ft', style = 'primary.Inverse.TLabel', width = 15, anchor = 'center') 

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

l_overhead.grid(column = 0, row = 0)
l_shopping.grid(column = 0, row = 0)
l_clothes.grid(column = 0, row = 0)
l_traffic.grid(column = 0, row = 0)
l_health.grid(column = 0, row = 0)
l_entertainment.grid(column = 0, row = 0)
l_payment.grid(column = 0, row = 0)
l_spending.grid(column = 0, row = 0)

# Another side

frame_right = ttk.Frame(window, padding = (10, 20, 20, 20))

month_previous_b = ttk.Button(frame_right, text = '⯇', style = 'primary.Outline.TButton', command = previous_month)
month_next_b = ttk.Button(frame_right, text = '⯈', style = 'primary.Outline.TButton', command = next_month)
current_month_frame = ttk.Frame(frame_right, padding = (5, 5, 5, 5), style = 'primary.TFrame')
current_month_l = ttk.Label(current_month_frame, text = months[actual_month], style = 'primary.Inverse.TLabel', width = 20, anchor = 'center')

# Saving frame

saving_frame = ttk.Frame(frame_right, style = 'secondary.TFrame', padding = (20, 20, 20, 20))

so_far_label = ttk.Label(saving_frame, text = 'Eddig megtakarított', style = 'secondary.Inverse.TLabel')
so_far_number_frame = ttk.Frame(saving_frame, padding = (5, 5, 5, 5), style = 'secondary.TFrame')
so_far_number_label = ttk.Label(so_far_number_frame, width = 15, text = str(user_datas[months[actual_month]]['Jövedelem'] - total_spending()) + 'Ft', anchor = 'center', style = 'secondary.Inverse.TLabel')
so_far_progressbar = ttk.Progressbar(saving_frame, value = s_progressbar_value(), length = 160, style = 'primary.Striped.Horizontal.TProgressbar')

goal_label = ttk.Label(saving_frame, text = 'Megtakarítási cél', style = 'secondary.Inverse.TLabel') 
goal_number_frame = ttk.Frame(saving_frame, padding = (5, 5, 5, 5), style = 'secondary.TFrame')
goal_number_label = ttk.Label(goal_number_frame, width = 15, text = str(user_datas[months[actual_month]]['Cél']) + 'Ft', anchor = 'center', style = 'secondary.Inverse.TLabel')
goal_progressbar = ttk.Progressbar(saving_frame, value = g_progressbar_value(), length = 160, style = 'primary.Striped.Horizontal.TProgressbar')

# Adds options

sp_options = ['Kategória','Számlák, rezsi','Bevásárlás','Ruházat','Közlekedés','Egészség','Szórakozás']
sp_option = StringVar()
sp_option.set('Bevásárlás')

goal_add_e = ttk.Entry(frame_right, width = 15)
goal_add_b = ttk.Button(frame_right, text = 'Új m. cél', style = 'primary.Outline.TButton', width = 15, command = lambda:clicked_goal(goal_add_e.get()))

payment_add_e = ttk.Entry(frame_right, width = 15)
payment_add_b = ttk.Button(frame_right, text = '+ Jövedelem', style = 'primary.Outline.TButton', width = 15, command = lambda: clicked_payment(payment_add_e.get()))

spending_add_e = ttk.Entry(frame_right, width = 15)
spending_add_mb = ttk.OptionMenu(frame_right, sp_option, *sp_options)
spending_add_b = ttk.Button(frame_right, text = '+ Költés', style = 'primary.Outline.TButton', width = 15, command = lambda:clicked_spending(sp_option.get(), spending_add_e.get()))

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