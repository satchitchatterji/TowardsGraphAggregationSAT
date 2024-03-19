% define players
%#const num_agents=3.
agent(1..num_agents).

% define number of profiles
%#const num_profiles=1.
profile(1..num_profiles).

% define existing nodes per profile
%#const num_nodes=3.
node(1..num_nodes).

% define possible edges
edge(1..num_nodes, 1..num_nodes).

% define a redundant graph/1 (there is also a graph_2)
%#const num_graphs=13.
graph(1..num_graphs).

% define edges in profiles
edge(1..num_nodes,1..num_nodes).

% find a graph that satisfies the profile - collective rationality assumed
1{select(P,G): graph(G)}1 :- profile(P).

% dictatorship: there is no agent A such that their graph always wins.
:- agent(A), select(P,G): profile(P, choose(A,G)).


% unanimity: if all agents agree on an edge, it is selected in the final graph
:- edge(X,Y), profile(P), graph(G),
   select(P,G),
   profile(P, choose(A,G)) : agent(A),
   not graph(G, edge(X,Y)). 

% grounded: if an edge is in the final graph, at least one agent must accept it
:- edge(X,Y), profile(P), graph(G),
   select(P,G),
   graph(G, edge(X,Y)),
   not graph(Gag, edge(X,Y)) : profile(P, choose(A,Gag)). 

% iie: 

%irreflexivity
%:- has(_,edge(X,X)).

%reflexivity - all nodes point to themselves
%:- node(X), profile(P), not has(P,edge(X,X)).
%:- node(X), profile(P), graph(G),
%   select(P,G),
%   not graph(G, edge(X,X)).

% transitivity - an edge from X to Y & Y to Z indicates an edge from X to Z
%:- node(X), node(Y), node(Z), profile(P), graph(G),
%   select(P,G),
%   graph(G, edge(X,Y)),
%   graph(G, edge(Y,Z)),
%   not graph(G, edge(X,Z)).

% completeness - all nodes are connected to each other
%:- node(X), node(Y), profile(P), graph(G), X != Y,
%   select(P,G),
%   not graph(G, edge(X,Y)),
%   not graph(G, edge(Y,X)).


% generate agent graphs per profile
% prefer/2 : prefers(A, has(P,edge(X,Y))). A - Agent, P - Profile. Agent A prefers edge(X,Y) in profile P.

#show has/2.


% encode graphs
graph(gID, )