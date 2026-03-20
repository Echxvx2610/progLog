# mascotas.py
# Autor: Cristian Echevarria 
# Fecha: 2026-03-20
# Descripcion: Sistema experto basico, basado en leyes para gestion de mascotas


# Leyes
"""
Ley de Identificación: Si tiene branquias, es un Pez.
Ley de Clasificación Felina: Si maúlla y tiene garras retráctiles, es un Gato.
Ley de Clasificación Canina: Si ladra y es fiel, es un Perro.
Ley de Espacio (Grande): Si es un perro y pesa más de 25kg, requiere patio grande.
Ley de Espacio (Pequeño): Si es un gato o un perro de menos de 10kg, es apto para departamento.
Ley de Salud (Vacunación): Si es cachorro (< 1 año), requiere refuerzo de vacunas.
Ley de Actividad: Si es un perro de raza "Border Collie" o "Husky", requiere ejercicio de alta intensidad.
Ley de Alimentación: Si es un reptil, requiere dieta insectívora o específica.
Ley de Convivencia: Si es un ave y vive en jaula pequeña, requiere vuelo supervisado diario.
Ley de Higiene: Si tiene pelo largo, requiere cepillado diario para evitar nudos.
"""

# Hechos (Base de datos de mascotas registradas)
mascotas = [
    {"nombre": "Thor", "especie": "perro", "raza": "Husky", "peso": 30, "edad": 0.5, "pelo": "largo"},
    {"nombre": "Luna", "especie": "gato", "raza": "Siamés", "peso": 4, "edad": 3, "pelo": "corto"},
    {"nombre": "Nemo", "especie": "pez", "rasgo": "branquias", "peso": 0.1, "edad": 1, "pelo": "ninguno"},
    {"nombre": "Chispa", "especie": "perro", "raza": "Chihuahua", "peso": 2, "edad": 5, "pelo": "corto"}
]

# Motor de Reglas (Leyes)
def evaluar_leyes(mascota):
    recomendaciones = []
    
    # Ley 1: Identificación por rasgos
    if mascota.get("rasgo") == "branquias":
        recomendaciones.append("Clasificación: Pez")

    # Ley 4 y 5: Requerimiento de Espacio
    if mascota["especie"] == "perro" and mascota["peso"] > 25:
        recomendaciones.append("Espacio: Requiere patio grande por su tamaño.")
    elif mascota["especie"] == "gato" or (mascota["especie"] == "perro" and mascota["peso"] < 10):
        recomendaciones.append("Espacio: Apto para vivir en departamento.")

    # Ley 6: Salud
    if mascota["edad"] < 1:
        recomendaciones.append("Salud: Alerta! Requiere esquema de vacunación de cachorro.")

    # Ley 7: Actividad física
    if mascota.get("raza") in ["Husky", "Border Collie"]:
        recomendaciones.append("Actividad: Requiere 2 horas de ejercicio intenso al día.")

    # Ley 10: Higiene
    if mascota["pelo"] == "largo":
        recomendaciones.append("Higiene: Necesita cepillado diario.")

    return recomendaciones

# Consultas
if __name__ == "__main__":
    print("....::: Realizando consultas :::....")
    for m in mascotas:
        print(f"\n{m['nombre']} ({m['especie'].capitalize()})")
        reglas_activadas = evaluar_leyes(m)
        
        if reglas_activadas:
            for regla in reglas_activadas:
                print(f" > {regla}")
        else:
            print(" > No hay recomendaciones especiales para esta mascota.")
