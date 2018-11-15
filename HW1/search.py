# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    fringe_list = util.Stack();
    closed_list = [];
    st_state=problem.getStartState();
    start_node = (st_state,[],0)# (state,path,cost)
    fringe_list.push(start_node);
    """fringe_state=set();
    fringe_state.add(st_state);"""





    while not fringe_list.isEmpty():

        node = fringe_list.pop();

        if problem.isGoalState(node[0]):
            return node[1];
        if not node[0] in closed_list:
            closed_list.append(node[0]);



            for child in problem.getSuccessors(node[0]):
                new_node_cost = node[2] + child[2]
                new_node_path = node[1] + [child[1]];
                new_state = (child[0],new_node_path,new_node_cost);

                """and not new_state[0] in fringe_state:"""  # if  not new_state[0] in [nd[0] for nd in fringe_list[0:]]:
                if not new_state[0] in closed_list:
                    fringe_list.push(new_state);
                    # fringe_state.add(new_state[0]);






    util.raiseNotDefined()


def breadthFirstSearch(problem):

    """Search the shallowest nodes in the search tree first."""
    fringe_list = util.Queue();
    closed_list = [];
    st_state=problem.getStartState()
    start_node = (st_state, [], 0);
    fringe_list.push(start_node);
    fringe_state = [];
    fringe_state.append(start_node[0]);

    while not fringe_list.isEmpty():
        node = fringe_list.pop();
        if problem.isGoalState(node[0]):
            return node[1];
        if not node[0] in closed_list:
            closed_list.append(node[0]);

            for child in problem.getSuccessors(node[0]):
                new_node_cost = node[2] + child[2];
                new_node_path = node[1] + [child[1]];
                new_state = (child[0], new_node_path, new_node_cost);
                """if problem.isGoalState(child[0]):
                    return new_node_path;""" # dont let pass q2

                if not child[0] in closed_list and not child[0] in fringe_state:
                    fringe_list.push(new_state);
                    fringe_state.append(child[0]);






    util.raiseNotDefined()

















def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    fringe_list = util.PriorityQueue();

    closed_list = [];
    st_state=problem.getStartState();
    start_node = (st_state, [], 0);
    fringe_list.push(start_node, start_node[2]);


    while not fringe_list.isEmpty():
        node = fringe_list.pop();

        if problem.isGoalState(node[0]):
            return node[1];
        if not node[0] in closed_list:
            closed_list.append(node[0]);

            for child in problem.getSuccessors(node[0]):
                new_node_cost = node[2] + child[2];
                new_node_path = node[1] + [child[1]];
                new_state = (child[0],new_node_path,new_node_cost);
                if not child[0] in closed_list:
                    fringe_list.update(new_state,new_node_cost);


    util.raiseNotDefined()




def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    fringe_list = util.PriorityQueue();
    new_cost = 0;
    closed_list = set();
    start = [problem.getStartState(), [], 0];
    new_cost = heuristic(start['state'], problem);
    fringe_list.push(start, new_cost);
    fringe_node_list =set();
    fringe_node={'state':problem.getStartState(),'cost':new_cost};
    fringe_node_list.add(fringe_node);


    while not fringe_list.isEmpty():
        Node = fringe_list.pop();
        node=Node['state'];
        if problem.isGoalState(node):
            return path;
        if not node in closed_list:
            closed_list.add(node);

            for child in problem.getSuccessors(node):
                new_cost = path_cost + child[2];
                new_path = path + [child_action];
                new_state = {'state':child_node, 'path':new_path, 'cost':new_cost};
                new_cost = new_cost + heuristic(new_state['state'], problem);
                if not child_node in closed_list:
                    if child_node in fringe_node:
                        update(new_state, new_cost);
                    elif not child_node in fringe_node:
                        fringe_list.push(new_state, new_cost);
                        #fringe_node.add(child_node);

    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
