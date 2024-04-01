dob(john, '1990-05-15').
dob(amy, '1985-09-28').
dob(mike, '1995-02-10').
dob(lisa, '1980-12-03').

get_dob(Person, DateOfBirth ) :-
    dob(Person, DateOfBirth).
