from collections import defaultdict, deque
from itertools import combinations
import networkx as nx
import time

def parse_input(filename="day_23.txt"):
    '''
    split input file by lines and then create pair based on - seperation
    '''
    graph = defaultdict(list)
    with open(filename) as f:
        lines = f.read().splitlines()
        for pair in lines:
            node1, node2 = pair.split("-")
            graph[node1].append(node2)
            graph[node2].append(node1)
    
    return graph

def parse_input_edges(filename="day_23.txt"):
    '''
    split input file by lines and then create pair based on - seperation
    '''
    edges = set()
    with open(filename) as f:
        lines = f.read().splitlines()
        for pair in lines:
            node1, node2 = pair.split("-")
            edges.add((node1, node2))
    
    return list(edges)


def largest_clique_original(edges):
    '''
    iterate over a list of edges and generate the largest complete graph possible
    and return that graph as a list of edges
    '''
    # Build the adjacency list from the list of edges
    graph = defaultdict(list)
    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)

    # Check if a set of nodes forms a clique
    def is_clique(nodes):
        for u, v in combinations(nodes, 2):
            if v not in graph[u]:
                return False
        return True

    # Find all connected components
    def find_connected_components():
        visited = set()
        components = []

        def dfs(node, component):
            visited.add(node)
            component.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for node in graph:
            if node not in visited:
                component = []
                dfs(node, component)
                components.append(component)

        return components

    # Find the largest clique in each connected component
    components = find_connected_components()
    largest_clique = []

    for component in components:
        n = len(component)
        for size in range(n, 0, -1):
            # Generate subsets of the current size
            for subset in combinations(component, size):
                if is_clique(subset):
                    if len(subset) > len(largest_clique):
                        largest_clique = list(subset)
                    break  # Stop searching once a clique of this size is found
            if len(largest_clique) == size:
                break  # Stop checking smaller sizes

    return largest_clique


def search_connected(graph):
    '''
    iterate through all the nodes and check if it contains a t in the name,
    if it does check if it has 2 neighbours, all 3 nodes must be 
    connected to each other, if they are and they are not in our result set add them to 
    result set as a tuple
    return result set
    '''
    res = set()
    for node, neighbors in graph.items():
        if node[0] == "t":
            for i in range(len(neighbors)):
                for j in range(i + 1, len(neighbors)):
                    n1, n2 = neighbors[i], neighbors[j]
                    if n1 in graph[n2] and n2 in graph[n1]:
                        res.add(tuple(sorted([node, n1, n2])))
    return res


def largest_clique(edges):
    # Create a graph from the list of edges
    G = nx.Graph()
    G.add_edges_from(edges)

    # Find all maximal cliques
    cliques = list(nx.find_cliques(G))

    # Identify the largest clique
    largest_clique = max(cliques, key=len)

    return largest_clique

'''
return edges sorted alphabetically and return them comma seperated
'''
def sorted_graph_nodes(edges):
    return ",".join(sorted(edges))


def question1():
    start_time = time.time()
    input_graph = parse_input()
    res1 = search_connected(input_graph)
    print(len(res1))
    end_time = time.time()
    print(f"Question 1 executed in {end_time - start_time:.4f} seconds")

def question2():
    start_time = time.time()
    edges = parse_input_edges()
    out_edges = largest_clique(edges)
    print(sorted_graph_nodes(out_edges))
    end_time = time.time()
    print(f"Question 2 executed in {end_time - start_time:.4f} seconds")

question1()
question2()