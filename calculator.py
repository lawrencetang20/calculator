# +, -, *, /, (, )

parentheses = ["(", ")"]
operations = ["+", "-", "/", "*"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

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
      raise Exception("Input error, not valid input")
  
  for index, item in enumerate(arr_exp):
    if item in parentheses or item in operations:
      continue
    else:
      arr_exp[index] = int(item)

  return arr_exp

def is_valid(exp):
  left_counter = 0
  right_counter = 0

  for index, token in enumerate(exp):
    if index < len(exp) - 1:
      if token in operations and exp[index+1] in operations:
        raise Exception("Input error, consecutive operations")
      elif token in parentheses and exp[index+1] != token and exp[index+1] in parentheses:
        raise Exception("Input error, () cannot be parsed")
      elif index > 0 and token in parentheses and type(exp[index+1]) == int and type(exp[index-1]) == int:
        raise Exception("Input error, not valid expression")
    if token == "(":
      left_counter += 1
    elif token == ")":
      right_counter += 1
      if right_counter > left_counter:
        raise Exception("Input error, ) came before (")
  
  if left_counter != right_counter:
    raise Exception("Input error, incorrect number of parent")


def evaluate(exp):
  exp_tokenized = tokenize(exp)
  is_valid(exp_tokenized)
  
  
  return exp_tokenized

expression = input("Enter in expression wih negative numbers in parentheses, i.e. 3*(-4): \n")
print(evaluate(expression))