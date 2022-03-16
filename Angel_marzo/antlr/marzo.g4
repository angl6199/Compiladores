grammar marzo;

program : expression+ ;

expression:
	expression '+' expression	# suma
	| expression '=' expression	# asignacion
	| expression '<' expression	# menor
	| expression '>' expression	# mayor
	| Numero					# primaria
	| Letra						# letra;

statement:
	'if (' expression ')' statement						# ifnoelse
	| 'if (' expression ')' statement 'else' statement	# if
	| 'int' Letra										# declaracion
	| 'print(' expression ')'							# print;


Numero: [0-9]+;
Letra: [a-zA-Z];
WS: [ \t\n\r]+ -> skip;
