#script_enfermedades.py
# autor: Cristian Echevarria
# fecha: 2026-03-18
# descripcion: Ejercicio de programacion logica

# Hechos
sintomas_por_enfermedad = {
    "gripe": ["tos", "dolor de cabeza"],
    "alergia": ["congestion nasal", "dolor de cabeza"],
    "resfriado": ["congestion nasal", "tos", "fiebre"],
    "covid": ["perdida de olfato", "tos", "fiebre"],
    "migraña": ["dolor de cabeza", "nauseas"]
}

# Regla de diagnóstico
def diagnostico(sintomas):
    for enfermedad, sintomas_enf in sintomas_por_enfermedad.items():
        if set(sintomas) == set(sintomas_enf):
            return enfermedad
    return "No se encontró una enfermedad que coincida con los síntomas"


#Consultas
if __name__ == "__main__":
    print("Caso 1:")
    print(diagnostico(["tos", "dolor de cabeza"]))  # gripe

    print("Caso 2:")
    print(diagnostico(["congestion nasal", "tos", "fiebre"]))  # resfriado

    print("Caso 3:")
    print(diagnostico(["dolor de cabeza", "nauseas"]))  # migraña
