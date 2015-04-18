-module(mycalc).
-compile(export_all).

rpn(L)  ->
	[Res] = lists:foldl(fun rpn/2, [], string:tokens(L, " ")),
	Res.

rpn("+", [L1, L2|S]) ->
	 [L1+L2|S];
rpn(X, Stack) ->
       io:format("inputs: ~-15w ~-15w ~n",[X, Stack]),
       [read(X)|Stack].

read(N) ->
	io:format("read N: ~w ~n",[N]),
	case string:to_float(N) of 
	     {error, no_float} -> list_to_integer(N);
	     {F, _} -> F
	end.