# Тестовый файл для многострочных переменных с тройными кавычками и другими форматами
current_var = input()
# Многострочные переменные с тройными кавычками
var1 = f"""This is a simple
multiline variable
example using {current_var}."""

var2 = f'''Another
example of a variable
with {current_var}.'''

var3 = f"""Multiline variable
that ends with some spaces and uses {current_var}   
   """

var4 = f"""Variable with
# embedded comment inside and {current_var}
text."""

var5 = f"""Formatted string with a value: {42}
and multiline content using {current_var}."""

var6 = f'''Variable with
an "escaped" character
inside the text and {current_var}.'''

var7 = f"""Unclosed multiline
variable starts here...
and references {current_var}
"""
var8 = f'''Another unclosed
formatted multiline
variable starts here...
and uses {current_var}
'''

var9 = """Multiline with
nested triple-quotes: '''inside''' here and {current_var}."""

var10 = f"""Formatted multiline with
multiple values: {10}, {20}, and {30}, including {current_var}."""

var11 = f"""A single-line variable with triple quotes and {current_var}."""

var12 = f'''A variable with
a mix of "quotes" and ''''''triple quotes''.'''

var13 = f"""Variable with backslash continuation \
and more text on the next line using {current_var}."""

var14 = f"""Variable with no content but mentions {current_var}:"""

var15 = f'''Last example
of a properly closed
multiline variable with {current_var}.'''

# Многострочные переменные с конкатенацией
var16 = f"Hello, " + "world " + f"and {current_var}!"

var17 = f"""This is a """ + f"test with {current_var} " + "of concatenated " + "strings." ""

# Многострочные переменные с круглыми скобками
var18 = (
    "This is a multiline "
    f"string using parentheses and {current_var}."
)

var19 = (
    f"This is a multiline formatted string with value {100} "
    f"and more text including {current_var}."
)

# Многострочные переменные с процентным форматированием
var20 = "Hello, %s" % "world"

var21 = (
    "This is a %s "
    "example of %s formatting with %s" % ("test", "percent", current_var)
)
value = ""
# Многострочные переменные с f-строками
var22 = f"Hello, {current_var}"

var23 = (
    f"This is a multiline f-string "
    f"with a value: {value} and uses {current_var}."
)
