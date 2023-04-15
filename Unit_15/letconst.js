/* Write an ES2015 version:
var PI =3.14;
PI = 42; //stop me from doing this!*/

const PI =3.14;
PI = 42; //Error

//What is the difference between var and let?
    //var has a scope of the function it is declared in, and let creates a variable with a scope of the code block it is in. Var can be redeclared and reassigned; let can only be reassigned.

//What is the difference between var and const?
    //Var can be reassigned or redeclared and has a function scope. Const cannot be reassigned or redeclared and has a block scope.

//What is the difference between let and const?
    //Let can be reassigned; const cannot be.

//What is hoisting?
    //Hoisting is when a variable or function declaration is initalized first, as if you had declared it at the top of the scope it was declared in.