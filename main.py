def print_hexagon(rows, columns):
    hexagon_rows = []
    for i in range(rows):
        row = ""
        if i == 0:
            row += "   ___         ___         ___         ___"
        elif i == 1:
            row += " /     \\ ___ /     \\ ___ /     \\ ___ /     \\"
        elif i == 2:
            row += " \\ ___ /     \\ ___ /     \\ ___ /     \\ ___ /"
        hexagon_rows.append(row)

    hexagon_string = "\n".join(hexagon_rows)
    return hexagon_string


def print_two_hexagons_vertically(rows, columns):
    hexagon1 = print_hexagon(rows, columns)
    hexagon2 = print_hexagon(rows, columns)

    for i in range(2):
        print(hexagon1, end='')
        print(hexagon2, end='')


print_two_hexagons_vertically(4, 7)