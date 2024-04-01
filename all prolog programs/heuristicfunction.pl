% Heuristic function (replace with your own heuristic)
heuristic(start, 5).
heuristic(a, 4).
heuristic(b, 2).
heuristic(c, 3).
heuristic(d, 1).
heuristic(goal, 0).

% Define the transition rules (replace with your own problem)
transition(start, a, 1).
transition(start, b, 2).
transition(a, c, 3).
transition(a, d, 2).
transition(b, d, 4).
transition(c, goal, 2).
transition(d, goal, 3).

% Best-First Search
best_first_search(Start, Path) :-
    best_first_search_internal([node(Start, 0, 0, [])], [], Path).

best_first_search_internal([node(State, _, _, Path) | _], _, Path) :-
    goal(State).

best_first_search_internal([node(State, G, _, Path) | Rest], Visited, FinalPath) :-
    findall(
        node(Child, NewG, H, [State | Path]),
        (transition(State, Child, Cost),
         \+ member(Child, Visited),
         NewG is G + Cost,
         heuristic(Child, H)),
        Children
    ),
    append(Children, Rest, UpdatedQueue),
    sort_queue(UpdatedQueue, SortedQueue),
    best_first_search_internal(SortedQueue, [State | Visited], FinalPath).

% Helper predicate to sort the queue based on heuristic values
sort_queue(Queue, SortedQueue) :-
    predsort(compare_nodes, Queue, SortedQueue).

compare_nodes(Order, node(, _, H1, _), node(, _, H2, _)) :-
    compare(Order, H1, H2).
