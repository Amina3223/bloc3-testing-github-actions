import pytest

# Import the module containing the solutions (excluding exercise 1)
import Prova_escrita_03 as mod


# ------------------------------
# TESTS EXERCI 2: trobar_edat_maxima
# ------------------------------

@pytest.mark.parametrize(
    "persones, expected",
    [
        # Valid list -> returns maximum age
        (
            [
                {'nom': 'Anna Garcia', 'edat': 25},
                {'nom': 'Marc Puig', 'edat': 42},
                {'nom': 'Laura Martí', 'edat': 35},
                {'nom': 'Jordi Soler', 'edat': 58},
                {'nom': 'Marta Vidal', 'edat': 29},
                {'nom': 'Pere Català', 'edat': 67}
            ],
            67
        ),

        # Empty list -> should return -1
        ([], -1),

        # Missing key -> should return -1
        (
            [
                {'nom': 'Anna Garcia', 'edat': 25},
                {'nom': 'Marc Puig'}
            ],
            -1
        ),

        # Wrong type -> should return -1
        (
            [
                {'nom': 'Anna Garcia', 'edat': 25},
                {'nom': 'Marc Puig', 'edat': '42'}
            ],
            -1
        )
    ]
)
def test_trobar_edat_maxima(persones, expected):
    """
    Test the function trobar_edat_maxima with several input cases.
    """
    assert mod.trobar_edat_maxima(persones) == expected


# ------------------------------
# TESTS EXERCI 3: trobar_producte_mes_car
# ------------------------------

@pytest.mark.parametrize(
    "productes, expected_preu",
    [
        # Valid list -> returns highest priced product
        (
            [
                {'nom': 'Portàtil Dell XPS 15', 'preu': 1299.99},
                {'nom': 'Ratolí Logitech MX Master', 'preu': 89.99},
                {'nom': 'Monitor Samsung 27"', 'preu': 349.50}
            ],
            1299.99
        ),

        # Empty list -> returns None
        ([], None)
    ]
)
def test_trobar_producte_mes_car(monkeypatch, productes, expected_preu):
    """
    Test trobar_producte_mes_car using monkeypatch to override global list.
    """
    # Replace global list with test case
    monkeypatch.setattr(mod, "productes", productes)

    result = mod.trobar_producte_mes_car()

    if expected_preu is None:
        assert result is None
    else:
        assert result["preu"] == expected_preu


# ------------------------------
# TESTS EXERCI 4: comptar_empleats_per_departament
# ------------------------------

@pytest.mark.parametrize(
    "empresa, expected",
    [
        # Full company example -> returns correct counts
        (
            {
                'nom': 'TechCorp',
                'departaments': [
                    {
                        'nom': 'Informàtica',
                        'empleats': [
                            {'nom': 'Anna', 'càrrec': 'Dev'},
                            {'nom': 'Marc', 'càrrec': 'Analista'},
                            {'nom': 'Laura', 'càrrec': 'DevOps'}
                        ]
                    },
                    {
                        'nom': 'Recursos Humans',
                        'empleats': [
                            {'nom': 'Jordi', 'càrrec': 'Director'},
                            {'nom': 'Marta', 'càrrec': 'Tècnica'}
                        ]
                    },
                    {
                        'nom': 'Vendes',
                        'empleats': [
                            {'nom': 'Pere', 'càrrec': 'Comercial'},
                            {'nom': 'Sofia', 'càrrec': 'Comercial'},
                            {'nom': 'David', 'càrrec': 'Cap'},
                            {'nom': 'Carla', 'càrrec': 'Comercial'}
                        ]
                    },
                    {
                        'nom': 'Administració',
                        'empleats': [
                            {'nom': 'Joan', 'càrrec': 'Comptable'}
                        ]
                    }
                ]
            },
            {'Informàtica': 3, 'Recursos Humans': 2, 'Vendes': 4, 'Administració': 1}
        ),

        # No departments -> returns empty dict
        (
            {'nom': 'TechCorp', 'departaments': []},
            {}
        )
    ]
)
def test_comptar_empleats_per_departament(empresa, expected):
    """
    Test comptar_empleats_per_departament with various company structures.
    """
    assert mod.comptar_empleats_per_departament(empresa) == expected
