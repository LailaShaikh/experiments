-module(switch_case).
-compile(export_all).

function(Operation, Values) ->
		    case Operation of
		    	 null ->
			      null;
			 multiple ->
			 	  case Values of
				       [A, B] when integer(A), integer(B) ->
				       	   io:format("The integers are ~w ~-15w",[A, B]),
				       	   {ok, A*B}
				end;
			divide	->
				case Values of
				     [A, B] when float(A), float(B) ->
				     	 io:format("float numbers are divided: ~w ~w",[A, B]),
					 {ok, A/B}
				end;
			_ ->
			  {undefined, nil}
		end.