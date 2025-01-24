#Importamos biblioteca
from pyswip import Prolog

# Inicializamos una instancia de prolog
prolog = Prolog()

#añadimos las relaciones
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

# Hacer una consulta logica para obtener los hermanos de Mary
siblings = list(prolog.query("sibling(mary, X)"))

# Crear un conjunto para eliminar duplicados en los resultados de consulta
unique_siblings = {result["X"] for result in siblings}

#Imprimir resultados unicos
print("Sibling of Mary:", list(unique_siblings))