




def trobar_min_max_rendiment(*nombres):
    if len(nombres) == 0:
        return 0, 0
    else:
        millor_rendiment = min(nombres)
        pitjor_rendiment = max(nombres)
        return millor_rendiment, pitjor_rendiment

def comptar_estudiants(estudiants):
    return len(estudiants)

notes_estudiants = {
    "Anna": {"Matemàtiques": 8, "Història": 7}, 
    "Marc": {"Matemàtiques": 6}, 
    "Laura": {"Ciències": 9, "Matemàtiques": 10}, 
    "Jordi": {"Història": 5}} 

def comptar_estudiants_matèria(notes, matèria):
    return len([estudiant for estudiant in notes if matèria in notes[estudiant]])

def comptar_estudiants_matèria_v2(notes, matèria):  
    comptador = 0
    for estudiant in notes:
        if matèria in notes[estudiant]:
            comptador += 1
    return comptador    

