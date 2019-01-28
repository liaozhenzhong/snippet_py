from graph import *


def test_it():
    E = {
        's':{'t':10, 'y':5},
        't':{'x':1, 'y':2},
        'x':{'z':4},
        'y':{'t':3, 'z':2, 'x':9},
        'z':{'s':7, 'x':6},
        }

    V = {c:Node(key=c) for c in E.keys()}
    g = Graph(E, V)
    g.dijkstra_init()
    g.dijkstra('s')
    g.show()


test_it()