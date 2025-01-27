current_var = input()

simple_paths = "folder1/file1.txt " \
               "folder2/file2.txt " \
               "folder3/file3.txt"

tabbed_paths = "folder1/file1.txt\t" \
               "folder2/file2.txt\t" \
               "folder3/file3.txt"
single_line = "this_is_single_line"
another_single = "another_single_line"

spaced_paths = "    path1/to/resource   " \
               "    path2/to/another/resource   " \
               "    path3/to/final/resource   "

quoted_paths = "path1/to/resource 'quoted'" \
               "path2/to/another/resource \"double-quoted\" " \
               "path3/to/final/resource"

unicode_paths = "путь1/ресурс " \
                "путь2/другой_ресурс " \
                "путь3/финальный_ресурс"

nested_paths = "path1/to/resource \\\n" \
               "path2/to/another/resource \\\n" \
               "path3/to/final/resource"

empty_line_paths = "path1/to/resource " \
                   f"{current_var}" \
                   "path2/to/another/resource " \
                   "path3/to/final/resource"

# ======================================================================================================================

# Простая строка с обратным слешем
multi_line_var1 = "This is part 1 of the line " \
                  "and here is part 2 with " \
                  f"{current_var} inside it."

# Форматирование через %
multi_line_var2 = "First line: %s " \
                  "Second line: %s" % (current_var, "constant_value")

# Комбинация % и конкатенации через обратный слеш
multi_line_var3 = "User input: %s " % current_var + \
                  "and more content follows here."

# f-строки с переносом
multi_line_var4 = f"Path: /usr/local/bin/{current_var} " \
                  f"and another path /var/log/{current_var}/log.txt"

# Конкатенация строк
multi_line_var5 = "Header: " + current_var + \
                  " Footer: " + "fixed_value"

# Вложенное форматирование через %
multi_line_var6 = ("Formatted value: %s " % current_var +
                   "Another formatted: %s" % "constant_value")

# Конкатенация строк с вызовами методов
multi_line_var7 = ("First part: " + current_var.strip() +
                   " Second part: " + current_var.upper())

# Смешанный случай: обратный слеш + форматирование через f-строки
multi_line_var8 = "Some data: " + \
                  f"{current_var} appended here."

# Форматирование через .format() с переносом
multi_line_var9 = ("Value 1: {}".format(current_var) +
                   " Value 2: {}".format("constant_value"))

# Сложный случай: разные переносы
multi_line_var10 = (
    f"First f-string: {current_var} " +
    "Concatenated: {}".format(current_var.upper()) +
    " Another: %s" % "hardcoded_value"
)

print(
    multi_line_var1, multi_line_var2, multi_line_var3,
    multi_line_var4, multi_line_var5, multi_line_var6,
    multi_line_var7, multi_line_var8, multi_line_var9,
    multi_line_var10, sep="\n\n"
)
