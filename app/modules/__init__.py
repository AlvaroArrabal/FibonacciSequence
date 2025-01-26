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


def validate_iterations(iterations):
    if iterations >= 0:
        return True
    else:
        print("ERROR: Wrong number of iterations. Must be >= 0")
        return False


def validate_sequence_position(position, sequence):
    if position >= 0 and position <= len(sequence):
        return True
    else:
        print(
            "ERROR: Wrong position number. This position does not exist in the sequence"
        )
        return False
