-module(index_of_list).
-export([find_index/2, find_index_by_case/2]).

find_index(1, [X|_]) ->
	      X;
find_index(N, [_|X]) when N > 0 ->
	      find_index(N-1, X).

find_index_by_case(X,Y)->
	case X of 
	     0 ->
	  
	       case Y of
	       	    [Z|_] -> Z
	       end;  
	     N when N>0 ->
	       case Y of 
	      	   [_|Zs] -> find_index_by_case(N-1, Zs)
	       end
	end.