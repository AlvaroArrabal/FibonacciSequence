from modules import generate_sequence, validate_iterations, validate_sequence_position


class Fibonacci:
    def __init__(self, iterations=0):
        self.iterations = iterations
        self.sequence = []

    def get_iterations(self):
        return self.iterations

    def get_sequence(self):
        return self.sequence

    def get_sequence_position(self, position):
        if validate_sequence_position(position, self.sequence):
            return self.sequence[position]

    def set_iterations(self, new_iterations):
        if validate_iterations(new_iterations):
            self.iterations = new_iterations

    def set_sequence(self):
        self.sequence = generate_sequence(self.get_iterations())
