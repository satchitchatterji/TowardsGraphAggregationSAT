% define players
#const num_agents=3.
agent(1..num_agents).

% define number of profiles
#const num_profiles=1.
profile(1..num_profiles).

% define existing nodes per profile
#const num_nodes=3.
node(1..num_nodes).

% define edges in profiles
edge(1..num_nodes,1..num_nodes).

% each graph can have any number of edges
{has(P,edge(X,Y)): edge(X,Y)} :- profile(P).

%irreflexivity
%:- has(_,edge(X,X)).

%reflexivity
:- node(X), profile(P), not has(P,edge(X,X)).

% transitivity
has(P,edge(X,Z)) :- has(P,edge(X,Y)), has(P,edge(Y,Z)).

% completeness
:- node(X), node(Y), profile(P), not has(P,edge(X,Y)), not has(P,edge(Y,X)), X != Y.

% set all profiles - maybe using modulos?
% IMPLEMENT

profile(A, has(P, edge(X,Y))) :- 

% generate agent graphs per profile
% prefer/2 : prefers(A, has(P,edge(X,Y))). A - Agent, P - Profile. Agent A prefers edge(X,Y) in profile P.

#show has/2.


% encode graphs
graph(gID, )