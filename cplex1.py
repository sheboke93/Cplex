#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 08:39:49 2017

@author: sheboke
"""

import cplex
problem = cplex.Cplex()
problem.objective.set_sense(problem.objective.sense.minimize)
names = ['a','b','c','d','e','f','g','h']
objective =[140.0,100.0,80.0,9.0,13.0,15.0,8.0,140.0]
lower_bounds=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
i=10
upper_bounds = [i,i,i,i,i,i,i,i]
problem.variables.add(obj = objective, 
                      lb =lower_bounds, 
                      ub = upper_bounds, 
                      names = names)
#将变量设置为整数
problem.variables.set_types([('a',problem.variables.type.integer),
                            ('b',problem.variables.type.integer),
                            ('c',problem.variables.type.integer),
                            ('d',problem.variables.type.integer),
                            ('e',problem.variables.type.integer),
                            ('f',problem.variables.type.integer),
                            ('g',problem.variables.type.integer),
                            ('h',problem.variables.type.integer)])
constraint_names=['c1','c2', 'c3', 'c4', 'c5','c6']
first_constraint = [['a','b','c','d','e','f', 'g','h'],[5.0,6.0,5.0,0.5,0.7,0.1,0.1,3.0]]
second_constraint = [[0, 1, 2, 3, 4, 5, 6, 7],[3.0,5.0,2.0,0.5,0.2,0.1,0.2,5.0]]
third_constraint = [[0, 1, 2, 3, 4, 5, 6, 7],[1.0,3.0,0.0,0.3,0.0,0.3,0.0,4.0]]
fouth_constraint = [[0, 1, 2, 3, 4, 5, 6, 7],[6.0,1.0,4.0,0.1,0.9,0.6,0.1,3.0]]
fifth_constraint = [[0, 1, 2, 3, 4, 5, 6, 7],[4.0,1.0,2.0,0.1,0.1,1.3,0.2,5.0]]
sixth_constraint =[[0, 1, 2, 3, 4, 5, 6, 7],[2.0,1.0,0.0,0.0,0.0,0.4,0.3,4.0]]
constraints = [first_constraint, second_constraint,third_constraint,fouth_constraint,fifth_constraint,sixth_constraint]
rhs = [60.0,60.0,28.0,60.0,60.0,28.0]
#L是<=，G>=
constraint_senses =['G','G','G','G','G','G']
problem.linear_constraints.add(lin_expr = constraints, 
                              senses = constraint_senses,
                              rhs = rhs,
                              names = constraint_names)
#将integer optimal设置为1%
problem.parameters.mip.tolerances.mipgap.set(0.01)
problem.solve()
print(problem.solution.get_objective_value())
print(problem.solution.get_values())