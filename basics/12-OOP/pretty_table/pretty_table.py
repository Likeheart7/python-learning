from prettytable import PrettyTable

table = PrettyTable()
table.add_column("name", ["chenxing", "likeheart", "liushu", "chensheng"])
table.add_column("age", [25, 27, 19, 29])
table.add_column("grade", [60, 85, 99, 80])
print(table)


# +-----------+-----+-------+
# |    name   | age | grade |
# +-----------+-----+-------+
# |  chenxing |  25 |   60  |
# | likeheart |  27 |   85  |
# |   liushu  |  19 |   99  |
# | chensheng |  29 |   80  |
# +-----------+-----+-------+