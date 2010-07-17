
from pyparsing import Literal, Word, Group, ZeroOrMore, Regex, Forward
from decimal import Decimal

# Operations
operations = {
    "+": (lambda x, y: x + y),
    "-": (lambda x, y: x - y),
    "*": (lambda x, y: x * y),
    "/": (lambda x, y: x / y),
    "^": (lambda x, y: x ** y),
}

# This is the really interesting part, the actual parser syntax

# The literal operations
add = Literal("+")
sub = Literal("-")
mul = Literal("*")
div = Literal("/")
pow = Literal("^")
lpr = Literal("(")
rpr = Literal(")")

# Numbers. Kinda an important thing for an equation parser.
number_regex = r"([0-9]+(\.[0-9]+)?)|(\.[0-9]+)"
number = Regex(number_regex)

element = Forward()

# Now the operations and their precedence.
powp = Group(element + ZeroOrMore(pow + element)) 
dimp = Group(powp + ZeroOrMore((mul | div) + powp))
adsp = Group(dimp + ZeroOrMore((add | sub) + dimp))

equation = top

element << (number | (lpar + )) 



























