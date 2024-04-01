% Facts
has_disease(john, diabetes).
has_disease(mary, hypertension).
has_disease(susan, celiac_disease).
has_disease(jim, obesity).

% Rules
diet_recommendation(Person, Recommendation) :-
    (   has_disease(Person, Disease) ->
        (   Disease = diabetes ->
            Recommendation = 'Follow a balanced diet with controlled carbohydrates.'
        ;   Disease = hypertension ->
            Recommendation = 'Limit sodium intake and focus on fruits, vegetables, and lean proteins.'
        ;   Disease = celiac_disease ->
            Recommendation = 'Avoid gluten-containing foods like wheat, barley, and rye.'
        ;   Disease = obesity ->
            Recommendation = 'Adopt a calorie-controlled diet with regular exercise.'
        ;   Recommendation = 'No specific diet recommendation available for this disease.'
        )
    ;   has_disease(Name, Disease) ->
        (   Name = john ->
            Recommendation = 'John has diabetes.'
        ;   Name = mary ->
            Recommendation = 'Mary has hypertension.'
        ;   Name = susan ->
            Recommendation = 'Susan has celiac disease.'
        ;   Name = jim ->
            Recommendation = 'Jim has obesity.'
        ;   Recommendation = 'No information available for this person.'
        )
    ;   Recommendation = 'Person or disease not found.'
    ).
