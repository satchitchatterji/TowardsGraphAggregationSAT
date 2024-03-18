% used to represent a possible graph in a way that can be meshed with other answer sets.

% assume some const indicating the graph_num
% #const graph_num=1.

% assume a set of edge/2 (Y,X), where Y,X are nodes

%just translate everything into graph/2 (G,edge(X,Y))

graph(graph_num, edge(X,Y)) :- edge(X,Y).

#show graph/2.