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

def add_number():
    global user_datas
    actualm = 'Január'

    user_datas[actualm]['Cél'] = 50

add_number()

print(user_datas['Január']['Cél'])