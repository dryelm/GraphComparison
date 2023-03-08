import timeit
import tracemalloc

import random_graph_factory
from bfs import BFS
from dfs import DFS
import matplotlib.pyplot as plt
import multiprocessing as mp


# memprofiler
def show_results(ans: dict):
    for alg in ans.keys():
        x = list(ans[alg]["time"].keys())
        y = [ans[alg]["time"][j] for j in x]
        print()
        plt.plot(x, y, label=alg)
    plt.ylabel('Time')
    plt.xlabel('Amount of nodes')
    plt.legend(ans.keys(), loc=2)
    plt.show()

    for alg in ans.keys():
        x = list(ans[alg]["memory"].keys())
        y = [ans[alg]["memory"][j] for j in x]
        print()
        plt.plot(x, y, label=alg)
    plt.ylabel('Memory')
    plt.xlabel('Amount of nodes')
    plt.legend(ans.keys(), loc=2)
    plt.show()


def algo_start(algo, graph, results):
    for i in range(1, len(graph)):
        start = timeit.default_timer()
        t = algo.start(graph, graph[0], graph[i])
        end = timeit.default_timer()
        tracemalloc.start()
        algo.start(graph, graph[0], graph[i])
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        if t:
            print(f"{str(algo()).ljust(12)} {t[0]} {[str(i) for i in t[1]]}")
        else:
            print("no path")

        results["time"].append(end - start)
        results["memory"].append(peak)


def negative_weights_algo(algorythms: list):
    algos = algorythms
    ans = {}
    for a in algos:
        ans[str(a())] = {}
        ans[str(a())]["time"] = {}
        ans[str(a())]["memory"] = {}
    for size in range(2, 31):
        tasks = []
        results = {}
        for a in algos:
            results[str(a())] = {"memory": [], "time": []}

        for i in range(5):
            graph = random_graph_factory\
                .generate_weighted_graph(size, -1, 100)
            for a in algos:
                algo_start(a, graph, results[str(a())])
        for t in tasks:
            t.start()

        for t in tasks:
            t.join()

        for a in algos:
            # print(list(map(lambda x: str(x), results[str(a())])))
            ans[str(a())]["time"][size] = sum(results[str(a())]['time']) / len(
                results[str(a())]['time'])
            ans[str(a())]["memory"][size] = sum(
                results[str(a())]['memory']) / len(results[str(a())]['memory'])

    show_results(ans)

def weighted_matrix_algo(algorythms: list):
    algos = algorythms
    ans = {}
    mp.set_start_method('spawn')
    for a in algos:
        ans[str(a())] = {}
        ans[str(a())]["time"] = {}
        ans[str(a())]["memory"] = {}

    for size in range(2, 21):
        results = {}
        for a in algos:
            results[str(a())] = {"memory": [], "time": []}
            # results[str(a())] = []
        tasks = []
        for i in range(5):
            graph = random_graph_factory.generate_weighted_matrix_graph(size, 1, 10)
            for a in algos:
                algo_start(a, graph, results[str(a())])
                # proc = Process(target=algo_start, args=(a, graph, results[str(a())]))
                # proc.start()
                # tasks.append(proc)

        for t in tasks:
            t.join()

        for a in algos:
            # print(list(map(lambda x: str(x), results[str(a())])))
            ans[str(a())]["time"][size] = sum(results[str(a())]['time']) / len(results[str(a())]['time'])
            ans[str(a())]["memory"][size] = sum(results[str(a())]['memory']) / len(results[str(a())]['memory'])

    show_results(ans)


def oriented_graph(algorythms: list):
    algos = algorythms
    ans = {}
    for a in algos:
        ans[str(a())] = {}
        ans[str(a())]["time"] = {}
        ans[str(a())]["memory"] = {}
    for size in range(100, 201, 10):
        tasks = []
        results = {}
        for a in algos:
            results[str(a())] = {"memory": [], "time": []}

        for i in range(5):
            graph = random_graph_factory\
                .generate_oriented_graph(size, int(size * 0.1))
            for a in algos:
                algo_start(a, graph, results[str(a())])
                # tasks.append(
                #     threading.Thread(target=algo_start,
                #                      args=(a, graph, results[str(a())])))
                # multiprocessing
        for t in tasks:
            t.start()

        for t in tasks:
            t.join()

        for a in algos:
            # print(list(map(lambda x: str(x), results[str(a())])))
            ans[str(a())]["time"][size] = sum(results[str(a())]['time']) / len(
                results[str(a())]['time'])
            ans[str(a())]["memory"][size] = sum(
                results[str(a())]['memory']) / len(results[str(a())]['memory'])

    show_results(ans)


def weighted_graph_algo(algorythms: list):
    algos = algorythms
    ans = {}
    for a in algos:
        ans[str(a())] = {}
        ans[str(a())]["time"] = {}
        ans[str(a())]["memory"] = {}
    for size in range(5, 51, 5):
        tasks = []
        results = {}
        for a in algos:
            results[str(a())] = {"memory": [], "time": []}

        for i in range(1):
            graph = random_graph_factory\
                .generate_weighted_graph(size, 0, 100)
            for a in algos:
                algo_start(a, graph, results[str(a())])
        for t in tasks:
            t.start()

        for t in tasks:
            t.join()

        for a in algos:
            # print(list(map(lambda x: str(x), results[str(a())])))
            ans[str(a())]["time"][size] = sum(results[str(a())]['time']) / len(
                results[str(a())]['time'])
            ans[str(a())]["memory"][size] = sum(
                results[str(a())]['memory']) / len(results[str(a())]['memory'])

    show_results(ans)


if __name__ == "__main__":
    #weighted_matrix_algo([Dijkstra, AStar])
    #weighted_graph_algo([Dijkstra, BellmanFord])
    oriented_graph([BFS, DFS])
    #negative_weights_algo([BellmanFord, FloydWarshall])
