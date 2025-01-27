current_var = input()

exotic = f"""
    text text {current_var}
""" + "text" \
    "text" \
    """text text text
    text text text
    text \ text \ text
""" + (f"""
    text text {current_var}
    more text with {f"nested {current_var}"}
""") + \
    ("""text""" + '''text text''') + \
    "text" * 3 + """text""" + str(123) \
+ (
    "text"
    "text()"
    "()text"
    "text \\"
    "text \\" + "another text"
) + "text text text text" \
'''
text text text text text text
((((((( )) text text text ((text (text )) text)))))) {len(text)}
text text \\ text text\\ text, text text + text text
''', ["text text text text",
 "text", 'text', '''more text
with tricky formatting''', """final string
    """], \
    F"text text {current_var}", \
    "Example: {}".format(current_var) + \
    ''' 
    Here is a tricky usage 
    {} '''.format(current_var) + \
    "Another example %s" % current_var + \
    ''' text text with slash \\
    continuation \\''' + \
    "Last tricky %s" % current_var + \
    F"Intermediate case with {current_var}", \
    [f"nested {current_var} {x}" for x in range(3)], \
    [
        "multiline \\ text \\ here",
        "followed by \\ another \\ tricky line"
    ] + [f"current_var {x}" for x in range(5)] + [
    '''
    Example of multiline strings \
    with explicit continuation \
    using slashes \\ and more text \
    to make it complex {}!'''.format(current_var)], \
    f'''
    Final nested example:
    "complex!"
    and a list:''', ["text","text","text","text","text","text",
      "text","text","text",
      "text","text",
      "text",
      "text",
      "text","text",
      "text","text","text","text",
      "text","text",
      "text","text","text","text","text","text","text",
      "text",
      "text","text","text","text","text",
      "text","text","text","text","text","text","text","text","text","text",
      "text","text","text",
      "text",
    ] + ["text","text","text","text","text","text",
      "text","text","text",
      "text","text",
      "text",
      "text",
      "text","text","text","text","text","text","text",
      "text",
      "text","text","text","text","text",
      "text","text","text","text","text","text","text","text","text","text",
      "text","text","text",
      "text",
    ]
new_variable = "new_variable"

new_var = "111"
