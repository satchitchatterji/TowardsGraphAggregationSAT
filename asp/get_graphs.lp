% define number of nodes per profile
#const num_nodes=3.
node(1..num_nodes).

% define edges in profiles
possible_edge(1..num_nodes,1..num_nodes).

% define edges per profile
% each graph can have any number of edges
{edge(X,Y): possible_edge(X,Y)}.

%reflexivity
:- node(X), not edge(X,X).

% transitivity
edge(X,Z) :- edge(X,Y), edge(Y,Z).

% completeness
:- node(X), node(Y), not edge(X,Y), not edge(Y,X), X != Y.


#show edge/2.
