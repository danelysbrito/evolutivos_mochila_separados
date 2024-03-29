class Item:
    def __init__(self, index, value, weight):
        self.index = index
        self.value = value
        self.weight = weight

class GreedySolver:
    def __init__(self, knapsack_instance):
        self.knapsack_instance = knapsack_instance
        self.state = [0] * knapsack_instance.NUMBER_OF_ITEMS
        self.value = 0.0
        self.weight = 0.0

    # Busca el "mejor" elemento (item) que se puede agregar a la mochila sin exceder su capacidad máxima de peso.
    def function_miope(self):
        best_item = None  # Inicializa best_item como None
        for i in range(len(self.knapsack_instance.items)):
            # Verifica si se puede agregar el elemento a la mochila y no ha sido incluido antes
            if (self.weight + self.knapsack_instance.items[i][1] <= self.knapsack_instance.MAX_WEIGHT) and (self.state[i] == 0):
                # Compara el valor del elemento con el valor de best_item actual
                if best_item is None or self.knapsack_instance.items[i][0] > best_item.value:
                    best_item = Item(i, self.knapsack_instance.items[i][0], self.knapsack_instance.items[i][1])
        return best_item  # Devuelve el elemento óptimo que cumple con las restricciones de peso y maximización del valor.

    def solve(self):
        while True: # Bucle continuo para buscar ítems
            best_item = self.function_miope() # Busca el mejor ítem
            if best_item is None:  # Si no se encuentra ningún elemento válido, termina la búsqueda         
                return self.state, self.value, self.weight
            # Si se encuentra un ítem válido, actualiza valores y estado de la mochila
            self.value += best_item.value # Actualiza el valor total
            self.weight += best_item.weight # Actualiza el peso total
            self.state[best_item.index] = 1 # Marca el ítem como incluido en la mochila