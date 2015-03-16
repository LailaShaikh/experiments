-module(macro_example).
-export([new_fun/4, blend/2, update_dict/1]).

-define(is_channel(V), (is_float(V) andalso V>0.0 andalso V =< 1.0)).

new_fun(A, B, C, D) when ?is_channel(A) -> io:format("hello world~n~w~n", [A]).
blend(A, B)-> #{name => A, age=>B}.
update_dict(#{name := Name, age := Age}) -> 
		   io:format("~-15w ~w ~n ",[Name, Age]).