/* Facts */
parent(john, jim).
parent(john, ann).
parent(jane, jim).
parent(jane, ann).
parent(jim, jill).
parent(ann, jill).

/* Rules */
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
grandfather(X, Z) :- father(X, Y), parent(Y, Z).

/* Predicates to check for male and female */
male(john).
male(jim).
female(jane).
female(ann).
female(jill).

/* Backward Chaining Rule */
is_grandfather(X) :- grandfather(X, _).

/* New Rule to find and print grandparents */
print_grandparents(X) :-
    grandparents(X, GP),
    write('The grandparents of '), write(X), write(' are: '), write(GP), nl.

/* Rule to find grandparents */
grandparents(X, GP) :- father(X, P), parent(P, GP).
