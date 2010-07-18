
from pyparsing import Literal, Regex, ZeroOrMore, Forward, Optional, Group
from decimal import Decimal
import math


# The next few lines define the operations we support. To add a new infix 
# operation, simply edit this list. The list is organized in terms of 
# precedence; the first dict in the list contains all operations that have the
# highest precedence, the next dict in the list contains all operations that 
# have the next-to-highest precedence, and so on. Keys in the dict are the 
# names of the operations, and values in the dict are two-argument functions 
# that compute the specified operation.
# 
# Adding a new operation is as simple as editing this list and adding a new
# entry to the dict corresponding to the desired precedence level. If you want
# to add an operator at another precedence level, you can simply add another
# dict to the list wherever you want.
# 
# Note that all of the operations use lambdas instead of functions present in
# the operations module. I did this so that it's clearer what each operation 
# does. In other words, this wasn't an oversight on my part :)
# 
# Also, operations must consist only of symbols. They can't use underscores.
# They should try not to use percent signs or braces either, since those have
# special meaning in the Fact language.
operation_list = [
    {
        "^" : lambda x, y: x ** y
    },
    {
        "*" : lambda x, y: x * y,
        "/" : lambda x, y: x / y,
        "%" : lambda x, y: x % y
    },
    {
        "+" : lambda x, y: x + y,
        "-" : lambda x, y: x - y
    },
    {
        "<<" : lambda x, y: x << y,
        ">>" : lambda x, y: x >> y
    },
    {
        ">"   : lambda x, y: x > y,
        "<"   : lambda x, y: x < y,
        ">="  : lambda x, y: x >= y,
        "<="  : lambda x, y: x <= y,
        "="   : lambda x, y: x == y,
        "!="  : lambda x, y: x != y,
        "<>"  : lambda x, y: x != y,
    },
    {
        "&" : lambda x, y: x & y,
        "|" : lambda x, y: x | y
    }
]

# Now we have a list of default variables and default functions that will be
# available to equations. To add a new variable or function, simply edit the
# following dicts. The list named copy_from_math is a list of functions that
# will be copied in from the math module. Note that variable values should
# always be instances of Decimal.
default_variables = {
    "e" :  Decimal("2.7182818284590452353602874713526624977572470936999595"
                   "749669676277240766303535475945713821785251664274274663"
                   "919320030599218174135966290435729003342952605956307381"
                   "323286279434907632338298807531952510190115738341879307"
                   "02154089149934884167509244761460668082264"),
    "pi" : Decimal("3.1415926535897932384626433832795028841971693993751058"
                   "209749445923078164062862089986280348253421170679821480"
                   "865132823066470938446095505822317253594081284811174502"
                   "841027019385211055596446229489549303819644288109756659"
                   "33446128475648233786783165271201909145649"),
    "over_nine_thousand" : Decimal("9001") # This equation parser has a sense
                                           # of humor :D --javawizard
}
default_functions = {
    "int": lambda x: x.to_integral(),
    "round": lambda x: x.to_integral()
}
copy_from_math = ("acos acosh asin asinh atan atan2 atanh ceil copysign "
                  "cos cosh degrees exp fabs factorial floor fmod frexp "
                  "fsum hypot isinf isnan ldexp log log10 log1p modf "
                  "pow radians sin sinh sqrt tan tanh trunc").split()
for function_to_copy in copy_from_math:
    default_functions[function_to_copy] = getattr(math, function_to_copy)

# Now we construct the parser grammar based on the operations specified in the
# list above
operation_names = [name for map in operation_list for name in map]
infix = Literal(operation_names[0])
for name in operation_names[1:]:
    infix = infix | name


class Function(object):
    def __init__(self, tokens):
        self.name = tokens[0]
        self.arguments = tokens[1].asList()
        
    def __repr__(self):
        return "<invoked-function: " + self.name + ", arguments: " + \
                                                   repr(self.arguments) + ">"

class Variable(object):
    def __init__(self, tokens):
        self.name = tokens[0]
    def __repr__(self):
        return "<variable " + str(self.name) + ">"


number = Regex(r"[\+\-]?(([0-9]+(\.[0-9]+)?)|(\.[0-9]+))")

comma = Literal(",")

name = Regex("[a-z][a-z0-9_]*")
var_name = Regex("[a-z][a-z0-9_]*")
var_name.setParseAction(lambda tokens: Variable(tokens))

element = Forward()
equation = Forward()
arguments = Group(equation) + ZeroOrMore(comma.suppress() + Group(equation))
function_or_element = (name + Literal("(").suppress() + Group(arguments) + 
                      Literal(")").suppress()).setParseAction(
                                 lambda tokens: Function(tokens)) | element


element << (var_name | number | (Literal("(").suppress() + Group(equation) + 
                             Literal(")").suppress()))
equation << function_or_element + ZeroOrMore(infix + function_or_element)



# Now we have the actual evaluate function.

def evaluate(text, variables={}, functions={}):
    """
    Evaluates the specified text as an arithmetic equation. The decimal module
    is used to do the actual calculations so that there's quite a bit of
    precision available. The equation can contain references to variable names.
    If it does, the variables will be looked up in the variable dict specified.
    There are some built-in variables (such as pi) that are available and do
    not need to be inserted into the dict. Variable values stored in the dict
    should be instances of decimal.Decimal.
    
    The equation can also contain function invocations, in the form
    funcname(arg1, arg2, arg3), where each of the arguments is an equation.
    Such functions should be present in the functions dict specified. Again,
    there are some default functions, mostly inherited from the math module,
    that will be present even when not provided via this dict. Function names
    must start with a letter, and they can contain letters, numbers, and
    underscores.
    """
    # First we'll actually parse the equation.
    parsed = equation.parseString(text, True).asList()
    # Now we hand the list off to the resolver.
    return resolve(parsed, variables, functions)

def resolve(items, variables, functions):
    # In order of precedence, we iterate through the operations in the
    # specified list. When we find one that matches any of the operations in
    # the precedence level we're on, we remove the operation and the two items
    # surrounding it, process them both down to numbers, perform the operation
    # on those numbers, and put them back into the list. Once we're done, we
    # should have a list with only one item in it (if we don't, we raise an
    # exception). We then process this item and return it.
    for map in operation_list:
        index = 1
        while index < len(items):
            token = items[index]
            if token in map: # We have a matching operation!
                op_function = map[token]
                first, second = items[index - 1], items[index + 1]
                first = process(first, variables, functions)
                second = process(second, variables, functions)
                result = process(op_function(first, second), variables,
                                                             functions)
                items[index - 1:index + 2] = [result]
            else: # No match, so we'll move on to the next position
                index += 2
    if len(items) != 1:
        raise Exception("Not exactly 1 item after processing (was "
                         + str(len(items)) + ")")
    return process(items[0], variables, functions)

def process(item, variables, functions):
    if isinstance(item, Decimal): # This item has already been processed
        return item
    if isinstance(item, basestring): # This is a string representing a number
        return Decimal(item)
    if isinstance(item, Variable): # This is a variable reference
        return lookup_variable(item, variables)
    if isinstance(item, Function): # This is a function invocation
        return run_function(item, variables, functions)
    if isinstance(item, list): # This is a parenthesized equation
        return resolve(item, variables, functions)
    if isinstance(item, int) or isinstance(item, long):
        return Decimal(item)
    if isinstance(item, float): # This item is a floating-point number
        return Decimal(str(item))
    raise Exception("Invalid input type " + str(type(item)))

def lookup_variable(item, variables):
    name = item.name
    if name in variables:
        return variables[name]
    return default_variables[name]

def run_function(function, variables, functions):
    name = function.name
    if name in functions:
        real_function = functions[name]
    else:
        real_function = default_functions[name]
    args = [resolve(a, variables, functions) for a in function.arguments]
    return process(real_function(*args), variables, functions)


































