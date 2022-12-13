import math

input = 'day11_input.txt'
class Monkey:
    def __init__(self,name, items,operator,factor, test, pass_true, pass_false, inspect_count):
        self.name = name
        self.items = items
        self.operator = operator
        self.factor = factor
        self.test = test
        self.pass_true = pass_true
        self.pass_false = pass_false
        self.inspect_count = inspect_count
    def show(self):
        print('---MONKEY INFO---', '\nName: ', self.name, '\nItems: ', self.items, '\nOperator: ', self.operator, '\nFactor: ', self.factor,
              '\nTest: ', self.test, '\nTrue: ', self.pass_true, '\nFalse:', self.pass_false, '\nNumItemsInspected: ', self.inspect_count)

monkeys = list()
with open(input) as lines:
    for l in lines:
        if l.strip() == "": continue
        if 'Monkey' in l:
            got_name = False
            got_items = False
            got_op = False
            got_test = False
            monkey_name = l.strip().replace(':','').split(' ')[1]
            got_name = True
        elif 'Starting' in l:
            items = l.strip().replace(',', '').split(' ')[2:len(l.strip().replace(',', '').split(' '))]
            for i in range(0, len(items)):
                items[i] = int(items[i])
            got_items = True
        elif 'Operation' in l:
            operator = l.strip().split(' ')[4]
            factor = (l.strip().split(' ')[5])
            got_op = True
        elif 'Test' in l:
            test = int(l.strip().split(' ')[3])
        elif 'true' in l:
            pass_true = int(l.strip().split(' ')[5])
        elif('false' in l):
            pass_false = int(l.strip().split(' ')[5])
            got_test = True
        if got_name and got_items and got_op and got_test:
            monkeys.append(Monkey(monkey_name, items, operator, factor, test, pass_true, pass_false,0))

def operation(number, factor, operator):
    if(factor == "old"):
        factor = number
    else:
        factor = int(factor)
    if operator == '*':
        return number * factor
    if operator == '+':
        return number + factor
    if operator == '-':
        return number - factor

for i in range(0, 20):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspect_count +=1
            new_worry = math.trunc(operation(item, monkey.factor, monkey.operator) / 3)
            if math.trunc(new_worry / monkey.test) == new_worry / monkey.test:
                monkeys[monkey.pass_true].items.append(new_worry)
            else:
                monkeys[monkey.pass_false].items.append(new_worry)
        monkey.items = []
    i +=1
for monkey in monkeys:
    monkey.show()