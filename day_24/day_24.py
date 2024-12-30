from collections import defaultdict
import os
import networkx as nx
import pygraphviz as pgv


class Node:
    def __init__(self, name=None, value=None, left=None, right=None, operator=None):
        self.name = name
        self.value = value
        self.left = left
        self.right = right
        self.operator = operator

def parse_file(filename="day_24.txt"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_dir, filename)
    # Read and parse the input file
    with open(filepath) as f:
        initials, connections = f.read().split("\n\n")

    # Parse initial values
    initials = [line.split(": ") for line in initials.splitlines()]
    wires = defaultdict(Node)

    for name, value in initials:
        wires[name] = Node(name, bool(int(value)))  # Set initial wire values

    # Parse connections
    connections = [line.split(" -> ") for line in connections.splitlines()]
    for inputs, output in connections:
        input1, operator, input2 = inputs.split()

        # If intermediate wires don't exist, create new names and nodes for them
        node_output = wires[output]
        node_input1 = wires[input1]
        node_input2 = wires[input2]

        # Set the output wire to reference this intermediate wire
        node_output.name = output
        node_output.left = node_input1
        node_output.right = node_input2
        node_output.operator = operator

    return wires

def evaluate_gate(node):
    if node.value is not None:
        return node.value

    left_value = evaluate_gate(node.left) if node.left else None
    right_value = evaluate_gate(node.right) if node.right else None

    if node.operator == "AND":
        return left_value and right_value
    elif node.operator == "OR":
        return left_value or right_value
    elif node.operator == "XOR":
        return left_value ^ right_value
    else:
        raise ValueError(f"Unknown operator: {node.operator}")


def evaluate_z_nodes(wires):
    # Evaluate and collect values of all nodes starting with "z"
    results = []
    for name, node in wires.items():
        if name.startswith("z"):
            results.append((name, evaluate_gate(node)))

    # Sort results in reverse order of wire name
    results.sort(reverse=True, key=lambda x: x[0])

    # Combine results into a binary string and convert to an integer
    binary_string = "".join(str(int(value)) for _, value in results)
    return int(binary_string, 2), binary_string


def question1():
    # Parse data and build the binary tree
    wires = parse_file()

    # Evaluate the result for "z" nodes
    res, _ = evaluate_z_nodes(wires)
    print(res)
    

def topological_sort(wires):
    visited = set()  # To keep track of visited nodes
    result = []      # To store the topological order
    
    def dfs(node):
        if node.name not in visited:
            visited.add(node.name)
            # Visit left child
            if node.left:
                dfs(node.left)
            # Visit right child
            if node.right:
                dfs(node.right)
            # After visiting children, add the node to the result
            result.append(node)
    
    # Start DFS from each wire/node in the circuit
    for node in wires.values():
        if node.name not in visited:
            dfs(node)
    
    return result

def create_dot_file(wires):
    # Create a graph using pygraphviz
    graph = pgv.AGraph(strict=True, directed=True)
    
    # Get the nodes in topological order
    topological_order = topological_sort(wires)
    
    # Add nodes and edges to the graph
    for node in topological_order:
        if node.value is not None:
            # Create a node with the name and its value
            graph.add_node(node.name, label=f'{node.name}: {int(node.value)}')
        else:
            # Create a node with the operator for non-value nodes
            graph.add_node(node.name, label=f'{node.name}: {node.operator}')
        
        # Reverse the direction of the edges to go backwards
        if node.left is not None:  # Make sure left child exists
            graph.add_edge(node.left.name, node.name, label='left')  # Reverse direction
        if node.right is not None:  # Make sure right child exists
            graph.add_edge(node.right.name, node.name, label='right')  # Reverse direction
    
    # Render the graph to a file (you can also use 'png', 'pdf', etc.)
    graph.draw("circuit.svg", prog="dot")

    print("DOT file and graph image created: circuit.svg")

def question2():
    wires = parse_file()
    create_dot_file(wires)

question1()
question2()