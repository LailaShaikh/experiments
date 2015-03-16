-module(list_length).
-export([list_len/1]).

list_len([]) -> 0;

list_len([H|T]) ->
		1 + list_len(T).