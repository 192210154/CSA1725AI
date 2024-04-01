planet(mercury, rocky, small, hot, no_moons).
planet(venus, rocky, medium, very_hot, no_moons).
planet(earth, rocky, medium, moderate, one_moon).
planet(mars, rocky, small, cold, two_moons).
planet(jupiter, gas_giant, large, very_cold, '79_moons').
planet(saturn, gas_giant, large, very_cold, '82_moons').
planet(uranus, ice_giant, medium, extremely_cold, '27_moons').
planet(neptune, ice_giant, medium, extremely_cold, '14_moons').

planet_characteristics(Name, Type, Size, Temperature, Moons) :-
    planet(Name, Type, Size, Temperature, Moons).
