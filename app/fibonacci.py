from app.modules.utils import (
    generate_sequence,
    validate_iterations,
    validate_position,
)


class Fibonacci:
    def __init__(self, iterations=0):
        self.iterations = iterations
        self._sequence = None

    def get_iterations(self):
        return self.iterations

    def get_sequence(self):
        if self._sequence is None:
            self._set_sequence()
        return self._sequence

    def get_sequence_position(self, position):
        try:
            validate_position(position, self.iterations)
            self._set_sequence()
            return self._sequence[position]
        except ValueError:
            print(
                "ERROR: Wrong position number. This position does not exist in the sequence"
            )

    def set_iterations(self, new_iterations):
        try:
            validate_iterations(new_iterations)
            self.iterations = new_iterations
            self._sequence = None
        except ValueError:
            print("ERROR: Wrong number of iterations. Must be >= 0")

    def _set_sequence(self):
        self._sequence = generate_sequence(self.get_iterations())
