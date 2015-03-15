-module(add).
-export([double/1]).

%My first program

double(Value) ->
	      times(Value, 2).
times(X, Y) ->
	 X * Y.

