import unittest

# =========================
# DADES DEL PROGRAMA
# =========================

videojocs = [
    {
        "titol": "The Legend of Zelda",
        "any_llancament": 2017,
        "genere": "Aventura",
        "plataforma": "Nintendo Switch",
        "puntuacio": 9.7,
        "desenvolupador": {"nom": "Nintendo", "pais": "Japó"},
        "dlcs": ["Master Trials", "Champions' Ballad"],
        "preu": 59.99
    },
    {
        "titol": "Cyberpunk 2077",
        "any_llancament": 2020,
        "genere": "RPG",
        "plataforma": "PC",
        "puntuacio": 7.8,
        "desenvolupador": {"nom": "CD Projekt Red", "pais": "Polònia"},
        "dlcs": ["Phantom Liberty"],
        "preu": 29.99
    },
    {
        "titol": "FIFA 24",
        "any_llancament": 2023,
        "genere": "Esports",
        "plataforma": "PlayStation",
        "puntuacio": 8.2,
        "desenvolupador": {"nom": "EA Sports", "pais": "Estats Units"},
        "dlcs": [],
        "preu": 69.99
    }
]

# Biblioteca personal inicialment buida
biblioteca_personal = []

# =========================
# FUNCIONS PRINCIPALS
# =========================

def buscar_per_titol(titol, videojocs):
    """
    Cerca un videojoc pel títol (insensible a majúscules).
    Retorna el diccionari del joc o None si no existeix.
    """
    for joc in videojocs:
        if joc["titol"].lower() == titol.lower():
            return joc
    return None


def afegir_a_biblioteca(titol, videojocs, biblioteca):
    """
    Afegeix un videojoc a la biblioteca amb validacions.
    """
    joc = buscar_per_titol(titol, videojocs)

    if joc is None:
        return "❌ Joc no trobat"

    if joc in biblioteca:
        return "⚠️ Ja està a la biblioteca"

    biblioteca.append(joc)
    return "✅ Joc afegit!"


def joc_mes_car(videojocs):
    """
    Retorna el videojoc amb el preu més alt.
    """
    return max(videojocs, key=lambda x: x["preu"])


def mostrar_videojoc(joc):
    """
    Mostra un videojoc amb format visual.
    """
    estrelles = "⭐" * int(joc["puntuacio"])
    print(f"🎮 {joc['titol'].upper()} ({joc['any_llancament']}) - {estrelles} - {joc['preu']}€")

def crear_sequencia(inici, final):
    """
    Genera una llista de números entre inici i final.
    """
    if not isinstance(inici, int) or not isinstance(final, int):
        return []

    if inici <= 0 or final <= 0 or inici >= final:
        return []

    return list(range(inici, final + 1))

def numeros_senars_majors(llista, limit):
    """
    Retorna números senars majors que limit.
    """
    if not isinstance(llista, list) or not llista:
        return []

    if not isinstance(limit, int):
        return []

    return [x for x in llista if x % 2 != 0 and x > limit]

def primera_posicio(llista, element):
    """
    Retorna la primera posició d'un element.
    """
    for i in range(len(llista)):
        if llista[i] == element:
            return i
    return -1

def diagonal_principal(matriu):
    """
    Retorna diagonal principal d'una matriu quadrada.
    """
    if not isinstance(matriu, list) or not matriu:
        return []

    n = len(matriu)

    for fila in matriu:
        if len(fila) != n:
            return []

    return [matriu[i][i] for i in range(n)]

# =========================
# TESTS UNITARIS
# =========================

class TestProvaEscrita01(unittest.TestCase):

    def test_buscar_per_titol_existeix(self):
        """
        Comprova que la funció trobar un videojoc existent correctament.
        """
        # Busquem un joc que existeix
        resultat = buscar_per_titol("Cyberpunk 2077", videojocs)

        # Verifiquem que no és None
        self.assertIsNotNone(resultat)

        # Verifiquem que el títol és correcte
        self.assertEqual(resultat["titol"], "Cyberpunk 2077")

    def test_buscar_per_titol_no_existeix(self):
        """
        Comprova que la funció retorna None si el joc no existeix.
        """
        # Busquem un joc que NO existeix
        resultat = buscar_per_titol("Minecraft", videojocs)

        # Ha de retornar None
        self.assertIsNone(resultat)

    def test_afegir_a_biblioteca_afegit(self):
        """
        Comprova que s'afegeix correctament un joc a la biblioteca.
        """
        # Creem biblioteca buida per evitar errors entre tests
        biblioteca = []

        # Afegim un joc existent
        resultat = afegir_a_biblioteca("FIFA 24", videojocs, biblioteca)

        # Comprovem missatge correcte
        self.assertEqual(resultat, "✅ Joc afegit!")

        # Comprovem que s'ha afegit a la llista
        self.assertEqual(len(biblioteca), 1)

    def test_afegir_a_biblioteca_no_existeix(self):
        """
        Comprova que no s'afegeix un joc inexistent.
        """
        biblioteca = []

        resultat = afegir_a_biblioteca("Minecraft", videojocs, biblioteca)

        # Ha de retornar error
        self.assertEqual(resultat, "❌ Joc no trobat")

        # Biblioteca ha de seguir buida
        self.assertEqual(len(biblioteca), 0)

    def test_joc_mes_car(self):
        """
        Comprova que es retorna correctament el joc més car.
        """
        resultat = joc_mes_car(videojocs)

        # FIFA 24 és el més car
        self.assertEqual(resultat["titol"], "FIFA 24")
        self.assertEqual(resultat["preu"], 69.99)

class TestProvaEscrita02(unittest.TestCase):

    # =========================
    # TEST 1: crear_sequencia
    # =========================
    def test_crear_sequencia_valid(self):
        """Comprova seqüència correcta amb valors vàlids"""
        self.assertEqual(crear_sequencia(5, 10), [5, 6, 7, 8, 9, 10])

    def test_crear_sequencia_invalid(self):
        """Comprova casos invàlids"""
        self.assertEqual(crear_sequencia(10, 5), [])
        self.assertEqual(crear_sequencia(-2, 5), [])

    # =========================
    # TEST 2: numeros_senars_majors
    # =========================
    def test_numeros_senars_majors(self):
        """Comprova filtratge de senars majors que limit"""
        llista = [3, -1, 7, 2, 9, 4, 7]
        self.assertEqual(numeros_senars_majors(llista, 3), [7, 9, 7])

    def test_numeros_senars_majors_invalid(self):
        """Comprova llista buida o invalidesa"""
        self.assertEqual(numeros_senars_majors([], 3), [])
        self.assertEqual(numeros_senars_majors("error", 3), [])

    # =========================
    # TEST 3: primera_posicio
    # =========================
    def test_primera_posicio(self):
        """Comprova cerca correcta"""
        llista = [3, -1, 7, 2, 9, 4, 7]
        self.assertEqual(primera_posicio(llista, 7), 2)
        self.assertEqual(primera_posicio(llista, 15), -1)

    # =========================
    # TEST 4: diagonal_principal
    # =========================
    def test_diagonal_principal(self):
        """Comprova matriu quadrada correcta"""
        matriu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(diagonal_principal(matriu), [1, 5, 9])

    def test_diagonal_principal_invalid(self):
        """Comprova matriu no quadrada"""
        matriu = [[1, 2], [3, 4, 5]]
        self.assertEqual(diagonal_principal(matriu), [])
# =========================
# EXECUCIÓ DELS TESTS
# =========================

if __name__ == "__main__":
    unittest.main()