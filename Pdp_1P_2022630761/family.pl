%Castillo Reyes Diego
%Escamilla Reséndiz Aldo
%Lopez Sanchez Adair
%Yañez Martinez Marthon Leobardo

% Facts: parent(Child, Parent)
parent(john, mary).
parent(john, mike).
parent(mary, alice).
parent(mary, george).
parent(mike, lisa).
parent(mike, james).
parent(susan, alice).
parent(susan, george).
parent(lisa, carol).
parent(lisa, paul).
parent(james, karen).
parent(james, daniel).
parent(karen, elizabeth).
parent(karen, jean).
parent(adair, susan).
parent(adair, jose).

% Rule: grandparent(Grandchild, Grandparent)
grandparent(Grandchild, Grandparent) :-
    parent(Grandchild, Parent),
    parent(Parent, Grandparent).

% Rule: sibling(Person1, Person2)
sibling(Person1, Person2) :-
    parent(Person1, Parent),
    parent(Person2, Parent),
    Person1 \= Person2.

% Rule: cousin(Person1, Person2)
cousin(Person1, Person2) :-
    parent(Person1, Parent1),
    parent(Person2, Parent2),
    sibling(Parent1, Parent2).

% Rule: bisabuelo(Bisnieto, Bisabuelo)
bisabuelo(Bisnieto, Bisabuelo) :-
    parent(Bisnieto, Padre),
    parent(Padre, Abuelo),
    parent(Abuelo, Bisabuelo).

% Rule: tatarabuelo(Tataranieto, Tatarabuelo)
tatarabuelo(Tataranieto, Tatarabuelo) :-
    parent(Tataranieto, Padre),
    bisabuelo(Padre, Tatarabuelo).