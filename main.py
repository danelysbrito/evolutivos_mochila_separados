import os
import time
import timeit
from knapsack.instance import KnapsackInstance
from knapsack.simulated_annealing import SimulatedAnnealingSolver
from knapsack.greedy_solution import GreedySolver
from knapsack.hill_climbing import HillClimbingSolver
from knapsack.tabu_search import TabuSearchSolver
from knapsack.genetico import GeneticSolver
from knapsack.instance import State
#from utils.file_utils import list_and_sort_files
from colorama import init, Fore, Back

if __name__ == "__main__":
    init()
    data_path = "data/instances_01_KP/low-dimensional/"
    items_list = []
    files = os.listdir(data_path)
    sorted_files = sorted(files, key=lambda x: int(x[1:].split("_")[0]))

    print(Fore.YELLOW + f"Contenido de la carpeta {data_path}, ordenado por nombre:")
    print()
    for file in sorted_files:
        print(file)
        print()
    print("------------------------------------------")    

    for entry in sorted_files:
        file_path = os.path.join(data_path, entry)
        if os.path.isfile(file_path):
            knapsack_instance = KnapsackInstance()
            knapsack_instance.load_instance(file_path)
            items_list.append(knapsack_instance)

     
    for i, knapsack_instance in enumerate(items_list, start=1):
            #knapsack_instance = KnapsackInstance()  # Crear una nueva instancia para cada iteración
            #knapsack_instance.load_instance(file_path)
            print(Fore.YELLOW + Back.WHITE + f"INSTANCIA {i}: NUMERO DE ITEMS={knapsack_instance.NUMBER_OF_ITEMS}, PESO MAXIMO={knapsack_instance.MAX_WEIGHT}")
            print()

            # Simulated Annealing
            solver = SimulatedAnnealingSolver()
            initial_temperature = 1000
            cooling_rate = 0.03
            max_iterations = 1000
            start_time = time.time()
            start_time_ok = timeit.default_timer()
            best_solution, best_value, final_weight = solver.solve(knapsack_instance, initial_temperature, cooling_rate, max_iterations)
            print(Fore.BLUE + Back.BLACK + f"*** SIMULATED ANNEALING ***")
            print(Fore.BLUE + Back.BLACK + f"Mejor Solución: {best_solution}")
            print(Fore.BLUE + Back.BLACK + f"Mejor Valor: {best_value}")
            print(Fore.BLUE + Back.BLACK + f"Peso Final: {final_weight}")
            execution_time = time.time() - start_time
            execution_time_ok = timeit.default_timer() - start_time_ok
            print(Fore.BLUE + Back.BLACK + f"Tiempo total de ejecución   : {execution_time} segundos")
            print(Fore.BLUE + Back.BLACK + f"Tiempo total de ejecución ok: {execution_time_ok} segundos")
            print()

            # Greedy 
            greedy_solver = GreedySolver(knapsack_instance)
            start_timeg = time.time()
            start_timeg_ok = timeit.default_timer()
            best_solutiong, best_valueg, final_weightg = greedy_solver.solve()
            print(Fore.MAGENTA + Back.BLACK + f"*** GREEDY ***")
            print(Fore.MAGENTA + Back.BLACK + f"Mejor Solución: {best_solutiong}")
            print(Fore.MAGENTA + Back.BLACK + f"Mejor Valor: {best_valueg}")
            print(Fore.MAGENTA + Back.BLACK + f"Peso Final: {final_weightg}")
            execution_timeg = time.time() - start_timeg
            execution_timeg_ok = timeit.default_timer() - start_timeg_ok
            print(Fore.MAGENTA + Back.BLACK + f"Tiempo total de ejecución   : {execution_timeg} seconds")
            print(Fore.MAGENTA + Back.BLACK + f"Tiempo total de ejecución ok: {execution_timeg_ok} segundos")
            print()
            

            # Hill Climbing BI
            solverbest = HillClimbingSolver(knapsack_instance) 
            start_timehbi = time.time()
            start_timehbi_ok = timeit.default_timer()
            best_valuehbi, final_weighthbi, best_solutionhbi = solverbest.solve("Mejor-Mejora")
            print(Fore.GREEN + Back.BLACK + f"*** HILL CLINBING - MEJOR MEJORA ***")
            print(Fore.GREEN + Back.BLACK + f"Mejor Solución: {best_solutionhbi}")
            print(Fore.GREEN + Back.BLACK + f"Mejor Valor: {best_valuehbi}")
            print(Fore.GREEN + Back.BLACK + f"Peso Final: {final_weighthbi}")
            execution_timehbi = time.time() - start_timehbi
            execution_timehbi_ok = timeit.default_timer() - start_timehbi_ok
            print(Fore.GREEN + Back.BLACK + f"Tiempo total de ejecución   : {execution_timehbi} seconds")
            print(Fore.GREEN + Back.BLACK + f"Tiempo total de ejecución ok: {execution_timehbi_ok} segundos")
            print()

            # Hill Climbing FI
            solverfirst = HillClimbingSolver(knapsack_instance) 
            start_timehfi = time.time()
            start_timehfi_ok = timeit.default_timer()
            best_valuehfi, final_weighthfi, best_solutionhfi = solverfirst.solve("Primera-Mejora")
            print(Fore.GREEN + Back.BLACK + f"*** HILL CLINBING - PRIMERA MEJORA ***")
            print(Fore.GREEN + Back.BLACK + f"Mejor Solución: {best_solutionhfi}")
            print(Fore.GREEN + Back.BLACK + f"Mejor Valor: {best_valuehfi}")
            print(Fore.GREEN + Back.BLACK + f"Peso Final: {final_weighthfi}")
            execution_timehfi = time.time() - start_timehfi
            execution_timehfi_ok = timeit.default_timer() - start_timehfi_ok
            print(Fore.GREEN + Back.BLACK + f"Tiempo total de ejecución   : {execution_timehfi} seconds")
            print(Fore.GREEN + Back.BLACK + f"Tiempo total de ejecución ok: {execution_timehfi_ok} segundos")
            print()

            # Tabu Search
            solvertabu= TabuSearchSolver(knapsack_instance, number_of_steps=100, tabu_list_length=10) 
            start_timet = time.time()
            start_timet_ok = timeit.default_timer()
            best_valueT, final_weightT, best_solutionT = solvertabu.solve()
            print(Fore.RED + Back.BLACK + f"*** TABU SEARCH ***")
            print(Fore.RED + Back.BLACK + f"Mejor Solución: {best_solutionT}")
            print(Fore.RED + Back.BLACK + f"Mejor Valor: {best_valueT}")
            print(Fore.RED + Back.BLACK + f"Peso Final: {final_weightT}")
            execution_timet = time.time() - start_timet
            execution_timet_ok = timeit.default_timer() - start_timet_ok
            print(Fore.RED + Back.BLACK + f"Tiempo total de ejecución   : {execution_timet} seconds")
            print(Fore.RED + Back.BLACK + f"Tiempo total de ejecución ok: {execution_timet_ok} segundos")
            print()

            # Genetico
            print(Fore.CYAN + f"*** GENETICO ***")
            genetic_solver = GeneticSolver(knapsack_instance, population_size=20, maximum_generations=30, crossover_probability=0.8, mutation_probability=0.05)
            start_timegene = time.time()
            start_timegene_ok = timeit.default_timer()
            best_valueGe, final_weightGe, best_solutionGe = genetic_solver.solve()
            
            print(Fore.CYAN + Back.BLACK + f"Mejor Solución: {best_solutionGe}")
            print(Fore.CYAN + Back.BLACK + f"Mejor Valor: {best_valueGe}")
            print(Fore.CYAN + Back.BLACK + f"Peso Final: {final_weightGe}")
            execution_timegene = time.time() - start_timegene
            execution_timegene_ok = timeit.default_timer() - start_timegene_ok
            print(Fore.CYAN + Back.BLACK + f"Tiempo total de ejecución   : {execution_timegene} seconds")
            print(Fore.CYAN + Back.BLACK + f"Tiempo total de ejecución ok: {execution_timegene_ok} segundos")
            print()

            print("------------------------------------------") 
    

        
        
