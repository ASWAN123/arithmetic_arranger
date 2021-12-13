def arithmetic_arranger(problems , *args):

  if len(problems) > 5:
    return "Error: Too many problems."


  data = []
  for each in problems:
    operation = each.split(" ")
    v = max(len(operation[0]), len(operation[2]))
    if v > 4:
        return "Error: Numbers cannot be more than four digits."
    if operation[1] in "+-":
        pass
    else:
        return "Error: Operator must be '+' or '-'."
    if operation[0].isnumeric() and operation[2].isnumeric():
        pass
    else:
        return "Error: Numbers must only contain digits."
    
    muk = "-" * v + "--"

    if operation[1] == "+":
      result = int(operation[0]) + int(operation[2])

    else:
      result = int(operation[0]) - int(operation[2])

    topresults = " " * (len(str(muk)) - len(str(result)))

    if len(operation[0]) <= len(operation[2]):
      c = len(operation[2]) - len(operation[0])
      s = " " * c
      p = f"{s}  {operation[0]}\n{operation[1]} {operation[2]}\n{muk}\n{topresults}{result}"

      data.append(p)
    if len(operation[0]) > len(operation[2]):
      c = len(operation[0]) - len(operation[2])
      s = " " * c + " "
      p = f"  {operation[0]}\n{operation[1]}{s}{operation[2]}\n{muk}\n{topresults}{result}"

      data.append(p)

  first = []
  second = []
  third = []
  four = []
  for each in data:
      h = each.split('\n')
      first.append(h[0])
      second.append(h[1])
      third.append(h[2])
      four.append(h[3])

  if args:
      arranged_problems = f"{'    '.join(first)}\n{'    '.join(second)}\n{'    '.join(third)}\n{'    '.join(four)}"

  else:
    arranged_problems = f"{'    '.join(first)}\n{'    '.join(second)}\n{'    '.join(third)}"
  
  

  return arranged_problems

