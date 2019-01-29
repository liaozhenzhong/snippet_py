from snippet.graph import *



def test_flight_itinerary():
    E = {
            'HNL':['AKL'],
            'YUL':['ORD'],
            'ORD':['SFO'],
            'SFO':['HNL'],
            'AKL':[]
            }
    V = {k:Node(k) for k in E}

    g = Graph(E, V)
    assert(['AKL', 'HNL', 'SFO', 'ORD', 'YUL'] == g.longest_path_in_graph())

