-module(maps_all).
-export([test_my_map/2]).

test_my_map(K, V) ->
	       io:fwrite('~w ~w ~n done.',[K, V]),
	       MyMap = #{'1' => 1, '2' => 2,'3' =>3, '4' => 4, '5' => 5},
	       Fun = fun(K, V) ->
   	       	   V * 2.
	       io:fwrite("MyMap ~w", [MyMap]),
	       maps:fold(Fun,0,MyMap).
	       %io:fwrite("Squared maps: ~w ~n",[maps:fold(Fun,0,MyMap)]).%
	       %nested_func(#{K => V}). %
	      

	  
	      
