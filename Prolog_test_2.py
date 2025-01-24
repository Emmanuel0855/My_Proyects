# Importamos biblioteca
from pyswip import Prolog

# Inicializamos una instancia de Prolog
prolog = Prolog()

# Añadimos las relaciones
prolog.assertz("parent(john, mary)")
prolog.assertz("parent(john, michael)")
prolog.assertz("parent(susan, mary)")
prolog.assertz("parent(susan, michael)")
prolog.assertz("male(john)")
prolog.assertz("female(susan)")
prolog.assertz("female(mary)")
prolog.assertz("male(michael)")

# Definir una regla en Prolog
prolog.assertz("sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \\= Y")

# Consultar quienes son hombres
males = list(prolog.query("male(X)"))
male_names = [result["X"] for result in males]

# Consultar quienes son mujeres
females = list(prolog.query("female(X)"))
female_names = [result["X"] for result in females]

# Imprimir resultados separados
print("Hombres:", male_names)
print("Mujeres:", female_names)