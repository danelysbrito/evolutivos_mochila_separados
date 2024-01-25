import random
import math
from knapsack.random_num import random_num

class SimulatedAnnealingSolver:
    
    def solve(self, knapsack_instance, initial_temperature, cooling_rate, max_iterations):
        current_state = [0] * knapsack_instance.NUMBER_OF_ITEMS
        current_value = 0
        current_weight = 0
        best_state = current_state
        best_value = current_value
        temperature = initial_temperature
        rng_instance = random_num(seed=knapsack_instance.SEED)
        self.rng_instance = rng_instance

        for iteration in range(max_iterations):
            neighbour = knapsack_instance.get_neighbour(current_state)
            neighbour_value, neighbour_weight = knapsack_instance.evaluate_state(neighbour)

            if neighbour_weight <= knapsack_instance.MAX_WEIGHT and (neighbour_value > current_value or self.rng_instance.get_random_probability() < math.exp((neighbour_value - current_value) / temperature)):
                current_state = neighbour
                current_value = neighbour_value
                current_weight = neighbour_weight

            if current_value > best_value:
                best_state = current_state
                best_value = current_value

            temperature *= 1 - cooling_rate

        return best_state, best_value, current_weight