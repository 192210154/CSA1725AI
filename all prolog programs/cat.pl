cat(fubby).
black_spots(fubby).
dog(figaro).
white_spots(figaro).

owns(mary,pet):-cat(pet),black_spots(pet).
loves(who,what):-owns(who,what).
