
print(100*'\n')
import re
actions = {
  "^": lambda x, y: str(float(x)**float(y)),
  "*": lambda x, y: str(float(x) * float(y)),
  "/": lambda x, y: str(float(x) / float(y)),
  "+": lambda x, y: str(float(x) + float(y)),
  "-": lambda x, y: str(float(x) - float(y))
}
 
priority_reg_exp = r"\((.+?)\)"
action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
 
 
 
def my_eval(expresion: str) -> str:
 
    while (match := re.search(priority_reg_exp, expresion)):
        expresion: str = expresion.replace(match.group(0), my_eval(match.group(1)))
 
    for symbol, action in actions.items():
        while (match := re.search(action_reg_exp.format(symbol), expresion)):
            expresion: str = expresion.replace(match.group(0), action(*match.groups()))
 
    return expresion
 
 
exp = "(100 + 44) * (5 * (10 - 8)) / 5"
print(my_eval(exp), eval(exp))  # 40.0 40.0


'''
data = '1    -    2*   3'
temp_data = data.replace(' ', '')
temp_data = data.replace('+', ' + ').replace('-',
                                             ' - ').replace('*', ' * ').replace('/', ' / ').split()
print(temp_data)

for operation in ['*','/','-','+']:
    while operation in temp_data:
        index = temp_data.index(operation)
        if operation == '*':
            temp_data[index-1] = int(temp_data[index-1]) * int(temp_data.pop(index+1))
        elif operation == '/':
            temp_data[index-1] = int(temp_data[index-1]) / int(temp_data.pop(index+1))
        elif operation == '-':
            temp_data[index-1] = int(temp_data[index-1]) - int(temp_data.pop(index+1))
        elif operation == '+':
            temp_data[index-1] = int(temp_data[index-1]) + int(temp_data.pop(index+1))
        temp_data.pop(index)
'''