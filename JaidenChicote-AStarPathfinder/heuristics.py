
def distance(a, b):
    """The distance between two (x, y) points."""
    xA, yA = a
    xB, yB = b
    return np.hypot((xA - xB), (yA - yB))
    #return np.sqrt((xA - xB)**2+(yA - yB)**2)
    
def heuristic_fun(x, mesh_nav_problem):
        locs = getattr(mesh_nav_problem.graph, 'locations', None)
        if locs:
            if type(mesh_nav_problem) is str:
                return int(distance(locs[x], locs[mesh_nav_problem.goal]))

            return int(distance(locs[x.state], locs[mesh_nav_problem.goal]))
        else:
            return np.inf

def euclidean_distance(x, y):
    return np.sqrt(sum((_x - _y) ** 2 for _x, _y in zip(x, y)))

        
def heuristic_fun_euclidean(x):
    locs = getattr(mesh_nav_problem.graph, 'locations', None)
    if locs:
        if type(mesh_nav_problem) is str:
            return int(euclidean_distance(locs[x], locs[mesh_nav_problem.goal]))

        return int(euclidean_distance(locs[x.state], locs[mesh_nav_problem.goal]))
    else:
        return np.inf