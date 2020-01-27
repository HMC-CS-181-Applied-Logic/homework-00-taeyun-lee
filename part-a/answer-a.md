## Part a

### Describe what the code in `z3-test.py` is doing in a paragraph or two.

    The code defines some integer and boolean variables, then creates an expression that Ands together multiple conditions involving those variables. The expression is then added to a solver, printed, and then checked by the solver. Since the check determines the expression to be satisfiable, then the program prints 'sat' and prints out the model that satisfies the expression. Then, another condition y < 1 is added to the solver, the expressions are printed, and then the solver checks to see if the expressions are satisfiable. The new condition makes them unsatisfiable so the program prints 'unsat'. 


    In the output, we first see the expression to be evaluated printed. Then, the program prints 'sat', telling us that this expression is satisfiable, and then prints out a model that satisfies the expression, assigning values to each variable in the expression. We can interpret these as assignments that will make our expression evaluate to true. Then the program prints out a list of two expressions, and then 'unsat', telling us that these expressions are not satisfiable. This means that there is no way to assign values to the variables so that the expression will evaluate to true. 