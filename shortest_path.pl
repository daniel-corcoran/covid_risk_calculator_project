:- module(shortpath, [test/2]).

:- use_module(library(solution_sequences), [order_by/2]).
:- use_module(library(lists), [reverse/2]).

path(A, B, [B, A], C) :- node(A, B, C).
path(A, B, [B|Ps], Cost) :-
    node(C, B, Cost1),
    path(A, C, Ps, Cost0),
    Cost is Cost0 + Cost1.

test(Path, Cost) :-
    order_by([asc(Cost)],
             ( path(placeA, placeH, Path0, Cost),
               reverse(Path0, Path) )).
