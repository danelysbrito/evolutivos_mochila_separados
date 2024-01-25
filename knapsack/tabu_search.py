import random
import math
from knapsack.random_num import random_num
from knapsack.instance import StateT

class TabuList:
    def __init__(self, tabu_list_length):
        self.tabu_list = [None] * tabu_list_length

    def is_in(self, state):
        return state in self.tabu_list

    def push_front(self, state):
        self.tabu_list.insert(0, state)

class TabuSearchSolver:
    def __init__(self, knapsack_instance, number_of_steps, tabu_list_length):
        self.knapsack_instance = knapsack_instance
        self.state = StateT(knapsack_instance)
        self.tabu_list = TabuList(tabu_list_length)
        self.rng = random.Random() #self.rng = random.Random(knapsack_instance.SEED)
        self.number_of_steps = number_of_steps

    def TabuSearch(self):
        self.state.generate_random_state(self.rng)
    
        best_state = self.state.clone()  # Almacena la mejor solución encontrada
        best_candidate = self.state.clone()

        for i in range(self.number_of_steps):
            neighbours = best_candidate.get_neighbours(self.rng)  # Pasa rng aquí
            best_candidate_evaluation = -1

            for neighbour in neighbours:
                # Verificar si el vecino cumple con las restricciones de peso antes de evaluar
                neighbour_value, neighbour_weight = neighbour.evaluate_state()

                if neighbour_weight <= self.knapsack_instance.MAX_WEIGHT:
                    # Evaluar el vecino y actualizar si es mejor que el mejor candidato actual
                    if (
                        neighbour_value > best_candidate_evaluation
                        and not self.tabu_list.is_in(neighbour.state)
                    ):
                        best_candidate = neighbour.clone()
                        best_candidate_evaluation = neighbour_value

            if best_candidate_evaluation == -1:
                break

            # Verificar si el peso acumulado no excede el límite antes de actualizar la mejor solución
            _, best_candidate_weight = best_candidate.evaluate_state()

            if best_candidate_weight <= self.knapsack_instance.MAX_WEIGHT:
                if best_candidate_evaluation > best_state.evaluate_state()[0]:
                    best_state = best_candidate

                self.tabu_list.push_front(best_candidate.state)

            self.state = best_state  # Actualiza el estado actual al mejor vecino encontrado
            best_value, best_weight = self.state.evaluate_state()
            best_solution = self.state.state

        return best_value, best_weight, best_solution

        
    def solve(self):
        best_value, best_weight, best_solution= self.TabuSearch()
        return best_value, best_weight, best_solution
