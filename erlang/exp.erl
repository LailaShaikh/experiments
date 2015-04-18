-module(exp).
-compile(export_all).

one() -> 1.
two() -> 2.

add(X, Y) -> X() + Y().

increment([]) -> [];
increment([H|T]) -> [H+1 | increment(T)].

decrement([]) -> [];
decrement([H|T]) -> [H-1 | decrement(T)].

%%using map utility
incr(X) -> X + 1.
decr(X) -> X - 1.

map(_, []) -> [];
map(F, [X|T]) -> [F(X)|map(F, T)].


base(A) ->
    B = A + 1,
    F = fun() -> C = A * B,C end,
    F().


%AlarmFunction = fun(Where) ->
%	       		  io:format("Alarm is raised at ~s.~n",[Where]),
%			  fun() ->
%			  	io:format("Batman is arrived for stopping alarm% in ~s.~n",[Where])
%			  end
%		end.
