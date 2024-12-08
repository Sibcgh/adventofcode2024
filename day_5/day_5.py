'''
looks like topo sort!


create a topo sort of the indices given 

after we create the graph create an array outputting the topo sort 
of the graph

put that array output into a dictionary where key=page, val=indx in array

go over each line in output,
create dict on key=page, val = indx in array

iterate over the output and make sure that array indices line up with ordering in topo sort

lets check if graph if item is out of order see if its index relative to

'''
import time
from collections import deque, defaultdict


def create_graph(rules, update):
    # Create graph and indegree dictionary for the given update
    graph = defaultdict(list)
    indegree_dict = defaultdict(int)
    update_set = set(update)

    for rule in rules:
        parent, child = map(int, rule.split('|'))
        if parent in update_set and child in update_set:
            graph[parent].append(child)
            indegree_dict[child] += 1

    return graph, indegree_dict


'''
turns out u can just have a function return multiple types so thats chill
'''
def topo_sort(update, graph, indegree_dict, return_topo_order=False):
    # Perform topological sort on the given graph
    q = deque([page for page in update if indegree_dict[page] == 0])
    res = []

    while q:
        curr_node = q.popleft()
        res.append(curr_node)

        for nei in graph[curr_node]:
            indegree_dict[nei] -= 1
            if indegree_dict[nei] == 0:
                q.append(nei)

    '''
    if no cycles and the list ordering is the same this was a true topo sort ordering
    '''
    if not return_topo_order:
        return len(res) == len(update) and res == update
    else:
        return res


def parse_file():
    # Read the input
    with open("day_5.txt") as f:
        content = f.read().strip()

    '''
    split into 2 sections
    '''
    sections = content.split('\n\n')

    rules = sections[0].strip().split('\n')

    '''
    formate the updates properly
    '''
    updates = [list(map(int, line.split(','))) for line in sections[1].strip().split('\n')]

    return rules, updates


def question_one():
    start_time = time.time()  # Start timing

    rules, updates = parse_file()

    valid_lines = []

    for update in updates:
        curr_graph, curr_indegree_dict = create_graph(rules, update)
        if topo_sort(update, curr_graph, curr_indegree_dict):
            valid_lines.append(update)

    mid_pages = [update[len(update)// 2] for update in valid_lines]

    result = sum(mid_pages)

    end_time = time.time()  # End timing
    print(f"question_one took {end_time - start_time:.6f} seconds")
    
    return result


def question_two():
    start_time = time.time()  # Start timing

    rules, updates = parse_file()

    invalid_lines = []

    for update in updates:
        curr_graph, curr_indegree_dict = create_graph(rules, update)
        if not topo_sort(update, curr_graph, curr_indegree_dict):
            invalid_lines.append(update)

    fixed_order_list = []

    for update in invalid_lines:
        curr_graph, curr_indegree_dict = create_graph(rules, update)
        fixed_order_list.append(topo_sort(update, curr_graph, curr_indegree_dict, return_topo_order=True))

    mid_pages = [update[len(update)// 2] for update in fixed_order_list]
    
    result = sum(mid_pages)

    end_time = time.time()  # End timing
    print(f"question_two took {end_time - start_time:.6f} seconds")

    return result

# Run both questions
res1 = question_one()
print(res1)

res2 = question_two()
print(res2)
