from graphProblem import *

class DFS_tree_algorithm:

    def __init__(self):
        self.algorithm_name = 'DFS_tree'

    def __call__(self):
        print ('Algorithm: {}'.format(self.algorithm_name))
        return self.depth_first_tree_search

    def depth_first_tree_search(self, problem):
        """
        Search the deepest nodes in the search tree first.
        Search through the successors of a problem to find a goal.
        The argument frontier should be an empty queue.
        Repeats infinitely in case of loops.
        """
        iterations = 0
        frontier = [Node(problem.initial)]  # Stack
        iterations += 1
        explored = set()
        while frontier:
            node = frontier.pop()
            iterations += 1
            if problem.goal_test(node.state):
                iterations += 1
                return (iterations, node)
            explored.add(node.state)
            frontier.extend(child for child in node.expand(problem) if child.state not in explored and
                            child not in frontier)
            for n in node.expand(problem):
                iterations += 1
            iterations += 1
        return None
