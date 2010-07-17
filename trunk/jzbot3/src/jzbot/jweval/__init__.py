
from pyparsing import Literal, Word, Group, ZeroOrMore, Regex, Forward
from jzbot.utils.coreutils import DynamicList

PREFIX = 1
POSTFIX = 2
INFIX = 3

# This maps operation names ("+", "*", etc) to functions that accept
# two arguments that perform the specified operation.
operation_map = {}

# Numbers. Kinda an important thing for an equation parser.
number_regex = r"([0-9]+(\.[0-9]+)?)|(\.[0-9]+)"
number = Regex(number_regex)

# We'll define equations later.
equation = Forward()

# Now we group stuff by precedence.
precedence_list = DynamicList()

def new_operation(precedence, name, function):
    precedence_list[precedence].append(name)
    operation_map[name] = function

new_operation(1, "^", INFIX, lambda x, y: x ** y)
new_operation(2, "*", INFIX, lambda x, y: x * y)
new_operation(2, "/", INFIX, lambda x, y: x / y)
new_operation(3, "+", INFIX, lambda x, y: x + y)













