def validate_iterations(iterations):
    if iterations < 0:
        raise ValueError


def validate_position(position, iterations):
    if position not in range(iterations):
        raise ValueError


def generate_sequence(iterations):
    if iterations <= 0:
        return []
    elif iterations == 1:
        return [0]
    elif iterations == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        for _ in range(2, iterations):
            sequence.append(sequence[-1] + sequence[-2])
        return sequence
