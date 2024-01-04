# +, -, *, /, (, ), ^

"""
- can't have double parentheses
"""

parentheses = ["(", ")"]
operations = ["+", "-", "/", "*", "^"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def add(a, b):
  return a + b

def multiply(a, b):
  return a * b

def subtract(a, b):
  return a - b

def divide(a, b):
  return a/b

def power(a, b):
  return a**b

def toOperator(operator):
  if operator == "+":
    return add
  elif operator == "*":
    return multiply
  elif operator == "-":
    return subtract
  elif operator == "/":
    return divide
  elif operator == "^":
    return power
  else:
    raise Exception("this shouldn't happen")

def tokenize(exp_whitespace):
  exp = exp_whitespace.replace(" ", "")
  arr_exp = []
  for token in exp:
    if token in operations or token in parentheses:
      arr_exp.append(token)
    elif token in numbers:
      if len(arr_exp) == 0:
        arr_exp.append(token)
      elif arr_exp[-1][-1] in numbers:
        arr_exp[-1] += token
      else:
        arr_exp.append(token)
    else:
      raise Exception("Input error, not valid input, all characters must be parentheses, operations, or numbers")
  
  for index, item in enumerate(arr_exp):
    if item in parentheses or item in operations:
      continue
    else:
      arr_exp[index] = int(item)

  return arr_exp

def is_valid(exp):
  left_counter = 0
  right_counter = 0

  if exp[0] in operations:
    raise Exception("Input error, cannot start on operation")

  for index, token in enumerate(exp):
    if index < len(exp) - 1:
      if token in operations and exp[index+1] in operations:
        raise Exception("Input error, consecutive operations")
      elif token in parentheses and exp[index+1] != token and exp[index+1] in parentheses:
        raise Exception("Input error, () cannot be parsed")
      elif index > 0 and token in parentheses and type(exp[index+1]) == int and type(exp[index-1]) == int:
        raise Exception("Input error, not valid expression, cannot have number(number, need an operation")
      elif index > 0 and token in operations and token != "-" and exp[index-1] == "(":
        raise Exception("Input error, cannot have (operation sequence")
    
    if index > 0 and token == ")" and exp[index-1] in operations:
        raise Exception("Input error, can't have operation before end of parentheses")

    if token == "(":
      left_counter += 1
    elif token == ")":
      right_counter += 1
      if right_counter > left_counter:
        raise Exception("Input error, ) came before (")
  
  if left_counter != right_counter:
    raise Exception("Input error, incorrect number of parentheses, ( don't match )")
  
  if exp[-1] in operations:
    raise Exception("Input error, can't end on an operation")

def find_matching_parentheses(exp):
  left_counter = 0
  right_counter = 0
  for index, token in enumerate(exp):
    if token == "(":
      left_counter += 1
    elif token == ")":
      right_counter += 1
    if left_counter == right_counter:
      return index
  
  raise Exception("This shouldn't happen")

def evaluate(exp):
  if len(exp) == 0:
    return None
  elif len(exp) == 1 and type(exp[0]) == int:
    return exp[0]
  elif exp[0] == "(":
    matching_index = find_matching_parentheses(exp)
    inside = evaluate(exp[1:matching_index])
    outside = evaluate(exp[matching_index+2:])
    if outside == None:
      return inside
    else:
      return evaluate([inside, exp[matching_index+1], outside])
  elif exp[0] == "-":
    return exp[1]*-1
  elif type(exp[0]) == int:
    func = toOperator(exp[1])
    if func != sum and func != subtract:
      if type(exp[2]) == int:
        return evaluate([func(exp[0], exp[2])] + exp[3:])
      else:
        index = find_matching_parentheses(exp[2:])
        paren = evaluate(exp[2:2+index+1])
        return evaluate([func(exp[0], paren)] + exp[2+index+1:])
    else:
      return func(exp[0], evaluate(exp[2:]))

expression = input("Enter in expression wih negative numbers in parentheses, i.e. 3*(-4): \n")

exp_tokenized = tokenize(expression)
is_valid(exp_tokenized)

print(evaluate(exp_tokenized))