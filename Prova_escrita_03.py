"""
DocExercici 1 (2 punts)
Crea una funció afegir_edat_a_tots(persones, anys) que afegeixi els anys especificats a l'edat de totes les persones de la llista. Aquesta funció modifica la llista original i no retorna res. Valida que anys sigui un enter positiu.

persones = [
    {'nom': 'Anna Garcia', 'edat': 25},
    {'nom': 'Marc Puig', 'edat': 42},
    {'nom': 'Laura Martí', 'edat': 35},
    {'nom': 'Jordi Soler', 'edat': 58},
    {'nom': 'Marta Vidal', 'edat': 29}
]
"""

def afegir_edat_a_tots(persones, anys):
    if isinstance(anys, int) and anys > 0:
        for persona in persones:
            persona["edat"] += anys


persones = [
    {'nom': 'Anna Garcia', 'edat': 25},
    {'nom': 'Marc Puig', 'edat': 42},
    {'nom': 'Laura Martí', 'edat': 35},
    {'nom': 'Jordi Soler', 'edat': 58},
    {'nom': 'Marta Vidal', 'edat': 29}
]

afegir_edat_a_tots(persones, 5)

# =========================
# Exercici 2
# =========================

"""
Exercici 2 (3 punts)
Escriu una funció trobar_edat_maxima(persones) que rebi una llista de diccionaris amb claus 'nom' i 'edat' (int), i retorni l'edat més alta.
"""

def trobar_edat_maxima(persones):
    if not persones:
        return -1

    for persona in persones:
        if (
            not isinstance(persona, dict)
            or "nom" not in persona
            or "edat" not in persona
            or not isinstance(persona["edat"], int)
        ):
            return -1

    edats = [persona["edat"] for persona in persones]
    return max(edats)

persones_1 = [
    {'nom': 'Anna Garcia', 'edat': 25},
    {'nom': 'Marc Puig', 'edat': 42},
    {'nom': 'Laura Martí', 'edat': 35},
    {'nom': 'Jordi Soler', 'edat': 58},
    {'nom': 'Marta Vidal', 'edat': 29},
    {'nom': 'Pere Català', 'edat': 67},
    {'nom': 'Sofia Roca', 'edat': 31}
]

persones_2 = []

persones_3 = [
    {'nom': 'Anna Garcia', 'edat': 25},
    {'nom': 'Marc Puig'},
    {'nom': 'Laura Martí', 'edat': 35}
]

persones_4 = [
    {'nom': 'Anna Garcia', 'edat': 25},
    {'nom': 'Marc Puig', 'edat': '42'},
    {'nom': 'Laura Martí', 'edat': 35}
]
if __name__ == "__main__":
    print("=== Prova 1: ===")
    print(trobar_edat_maxima(persones_1))

    print("=== Prova 2: ===")
    print(trobar_edat_maxima(persones_2))

    print("=== Prova 3: ===")
    print(trobar_edat_maxima(persones_3))

    print("=== Prova 4: ===")
    print(trobar_edat_maxima(persones_4))


# =========================
# Exercici 3
# =========================

"""
Exercici 3 (2 punts)
Fes una funció trobar_producte_mes_car().
"""

productes = [
    {
        'nom': 'Portàtil Dell XPS 15',
        'preu': 1299.99,
        'categoria': 'Informàtica',
        'stock': 5
    },
    {
        'nom': 'Ratolí Logitech MX Master',
        'preu': 89.99,
        'categoria': 'Perifèrics',
        'stock': 15
    },
    {
        'nom': 'Monitor Samsung 27"',
        'preu': 349.50,
        'categoria': 'Monitors',
        'stock': 8
    }
]

def trobar_producte_mes_car():
    if not productes:
        return None

    preu_max = productes[0]["preu"]
    producte_mes_car = productes[0]

    for producte in productes:
        if producte["preu"] > preu_max:
            preu_max = producte["preu"]
            producte_mes_car = producte

    return producte_mes_car


print("=== Prova 1: ===")
print(trobar_producte_mes_car())

print("=== Prova 2: ===")
productes = []
print(trobar_producte_mes_car())


# =========================
# Exercici 4
# =========================

"""
Exercici 4 (3 punts)
Escriu una funció comptar_empleats_per_departament(empresa)
"""

empresa_de_prova = {
    'nom': 'TechCorp',
    'departaments': [
        {
            'nom': 'Informàtica',
            'empleats': [
                {'nom': 'Anna Garcia', 'càrrec': 'Desenvolupadora'},
                {'nom': 'Marc Puig', 'càrrec': 'Analista'},
                {'nom': 'Laura Martí', 'càrrec': 'DevOps'}
            ]
        },
        {
            'nom': 'Recursos Humans',
            'empleats': [
                {'nom': 'Jordi Soler', 'càrrec': 'Director RRHH'},
                {'nom': 'Marta Vidal', 'càrrec': 'Tècnica de selecció'}
            ]
        },
        {
            'nom': 'Vendes',
            'empleats': [
                {'nom': 'Pere Català', 'càrrec': 'Comercial'},
                {'nom': 'Sofia Roca', 'càrrec': 'Comercial'},
                {'nom': 'David Llop', 'càrrec': 'Cap de vendes'},
                {'nom': 'Carla Font', 'càrrec': 'Comercial'}
            ]
        },
        {
            'nom': 'Administració',
            'empleats': [
                {'nom': 'Joan Ferrer', 'càrrec': 'Comptable'}
            ]
        }
    ]
}


def comptar_empleats_per_departament(empresa):
    departaments = {}

    for departament in empresa["departaments"]:
        departaments[departament["nom"]] = len(departament["empleats"])

    return departaments


print("=== Prova 1: ===")
print(comptar_empleats_per_departament(empresa_de_prova))

print("=== Prova 2: ===")
empresa_de_prova["departaments"] = []
print(comptar_empleats_per_departament(empresa_de_prova))