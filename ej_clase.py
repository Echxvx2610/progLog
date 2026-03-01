# hechos
enfermedades = {
    'gripe' : ['temperatura', 'tos', 'dolor de cabeza'],
    'alergia' : ['escurrimiento nasal', 'estornudos', 'dolor de cabeza'],
    'covid' : ['tos','fiebre','dolor de cabeza'],
    'influenza' :['estornudos','tos','fiebre']
}

def diagnostico(sintomas):
    # reglas
    for enfermedad in enfermedades:
        if sintomas == enfermedades[enfermedad]:
            return enfermedad
    return 'No se encontro una enfermedad que coincida con los sintomas'

# consultas
print(diagnostico(['tos','fiebre','dolor de cabeza']))
