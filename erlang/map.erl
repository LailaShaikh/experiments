-module(map).
-export([new/4]).

%macro experment
-define(is_channel(V), (is_float(V) andalso V > 0.0 andalso V < 1.0)).

new(R, G, B, A) when ?is_channel(R), ?is_channel(G), 
       	     	     ?is_channel(B), ?is_channel(A) ->
       io:format("Macro side calling..~n"),
       io:format("~-15w ~-15w ~-15w ~-15w ~n",[R, G, B, A]);

new(_, _, _, _) ->
       io:format("Non macro side is executing..").

% we will experiment map in erl