


def structure(design) -> float:


    sections = []
    for group in groups:
        sections[group] = lookup_section(design[group])
    #

    # 1)
    model = create_model(design)

    # 2)
    weight = compute_weight(model)

    # 3)
    solution = analyze(model)

    # 4) Get limits set by design code
    constraints = create_constraints(design)

    # 5) Apply penalty based on violations of design limits
    penalty = check_constraints(model, solution, constraints)


    return penalty*weight


design = spo(structure, 3)


if not s:
    print("Not safe")
