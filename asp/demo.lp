% graph representation

% define number of profiles
#const num_profile=3.
profile(1..num_profile).

% define existing nodes per profile
#const num_nodes=3.
node(1..num_nodes).

% define edges in profiles
# num_edges=9.
edge(1..num_nodes;1..num_nodes).

% each graph can have any number of edges
{has(P,edge(X,Y)): edge(X,Y)} :- profile(P).


%irreflexivity
:- edge(X,Y), edge(Y,X), X != Y.

% transitivity
edge(X,Z) :- edge(X,Y), edge(Y,Z).

% completeness
:- not edge(X,Y), not edge(Y,X), X!=Y.

