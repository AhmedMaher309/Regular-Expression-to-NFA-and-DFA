import pydot

def draw_nfa(nfa_dictionary, start, end, filename):
    graph = pydot.Dot(graph_name='nfa', graph_type='digraph')
    nodes_set = set()
    for st, char in nfa_dictionary.keys():
        if st not in nodes_set:
            nodes_set.add(st)
            if st in end:
                graph.add_node(pydot.Node(st, shape='doublecircle'))
            else:
                graph.add_node(pydot.Node(st, shape='circle'))

    for st, char in nfa_dictionary.keys():
        for each_out in nfa_dictionary[(st,char)]:
            graph.add_edge(pydot.Edge(st, each_out, label=char))
    graph.write_png('/media/a7medmaher/DATA/college_4/Compilers/Assigment_1/Assign/'+filename)

