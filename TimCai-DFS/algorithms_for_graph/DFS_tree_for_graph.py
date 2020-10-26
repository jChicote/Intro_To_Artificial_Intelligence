from graphProblem import *

class DFS_tree_algorithm_for_graph:

    def __init__(self):
        self.algorithm_name = 'DFS_tree_for_graph'

    def __call__(self):
        print ('Algorithm: {}'.format(self.algorithm_name))
        return self.depth_first_tree_search_graph

    def tree_depth_search_for_vis(self, problem):
        """Search through the successors of a problem to find a goal.
        The argument frontier should be an empty queue.
        Don't worry about repeated paths to a state. [Figure 3.7]"""
        
        # we use these two variables at the time of visualisations
        iterations = 0
        all_node_colors = []
        node_colors = {k : 'white' for k in problem.graph.nodes()}
        
        #Adding first node to the stack
        frontier = [(Node(problem.initial))]
        explored = set()
        node_colors[Node(problem.initial).state] = "orange"
        iterations += 1
        all_node_colors.append(dict(node_colors))
        while frontier:
            #Popping first node of stack
            node = frontier.pop()
            # modify the currently searching node to red
            node_colors[node.state] = "red"
            iterations += 1
            all_node_colors.append(dict(node_colors))
            if problem.goal_test(node.state):
                # modify goal node to green after reaching the goal
                node_colors[node.state] = "green"
                iterations += 1
                all_node_colors.append(dict(node_colors))
                return(iterations, all_node_colors, node)
            
            explored.add(node.state)
            frontier.extend(child for child in node.expand(problem) if child.state not in explored and
                            child not in frontier)
            for n in node.expand(problem):
                node_colors[n.state] = "orange"
                iterations += 1
                all_node_colors.append(dict(node_colors))

            # modify the color of explored nodes to gray
            node_colors[node.state] = "gray"
            iterations += 1
            all_node_colors.append(dict(node_colors))
        return None

    def depth_first_tree_search_graph(self, problem):
        "Search the deepest nodes in the search tree first."
        iterations, all_node_colors, node = self.tree_depth_search_for_vis(problem)
        return(iterations, all_node_colors, node)
