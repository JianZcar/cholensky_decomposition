def generate_display_matrix(matrix):
    if not matrix or not matrix[0]:
        return
    max_width = max(len(str(item)) for row in matrix for item in row)
    top_border = f"┌{'─' * (max_width + 2)}" + f"┬{'─' * (max_width + 2)}" * (len(matrix[0]) - 1) + "┐"
    middle_border = f"├{'─' * (max_width + 2)}" + f"┼{'─' * (max_width + 2)}" * (len(matrix[0]) - 1) + "┤"
    bottom_border = f"└{'─' * (max_width + 2)}" + f"┴{'─' * (max_width + 2)}" * (len(matrix[0]) - 1) + "┘"
    display = [top_border]
    for i, row in enumerate(matrix):
        row_str = "│ " + " │ ".join(str(item).ljust(max_width) for item in row) + " │"
        display.append(row_str)
        if i < len(matrix) - 1:
            display.append(middle_border)
    display.append(bottom_border)
    return display

def generate_display_list_with_border(lst):
    if not lst:
        return

    max_width = max(len(str(item)) for item in lst)
    top_border = f"┌{'─' * (max_width + 2)}┐"
    middle_border = f"├{'─' * (max_width + 2)}┤"
    bottom_border = f"└{'─' * (max_width + 2)}┘"

    display = [top_border]
    for i, item in enumerate(lst):
        row_str = f"│ {str(item).ljust(max_width)} │"
        display.append(row_str)
        if i < len(lst) - 1:
            display.append(middle_border)
    display.append(bottom_border)
    return display

def generate_display_symbol(length, symbol='='):
    display = []
    for i in range(length):
        display.append('   ')
        if i == (length//2)-1:
            display.append(f' {symbol} ')
    return display

def join_display(display, display_2):
    joined_display = []
    for i in range(len(display)):
        joined_display.append(display[i] + display_2[i])
    return joined_display

def render_grid(display):
    for line in display:
        print(line)
