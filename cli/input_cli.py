import sys
import msvcrt
from colorama import init, Fore, Back, Style


# Initialize colorama
init()

def move_cursor_up(n):
    sys.stdout.write(f"\033[{n}A")
    sys.stdout.flush()

def draw_list(menu, selected_idx):
    if len(menu) == 0:
        return
    move_cursor_up(len(menu))  # Move cursor up to account for menu items
    max_length = max(len(item) for item in menu)
    for idx, item in enumerate(menu):
        if idx == selected_idx:
            print("\033[2K", end='\r', flush=True)
            print(f"{Back.WHITE + Fore.LIGHTCYAN_EX + item.ljust(max_length) + Style.RESET_ALL}")
        else:
            print("\033[2K", end='\r', flush=True)
            print(f"{item.ljust(max_length + 2)}")


def handle_enter(input_str, _, __):
    return input_str, True

def handle_backspace(input_str, _, __):
    if len(input_str) > 0:
        input_str = input_str[:-1]
        print('\b \b', end='', flush=True)
    return input_str, False

def handle_arrow_or_null(input_str, _, __):
    msvcrt.getch()  # Skip the next character
    return input_str, False

def handle_printable(input_str, char, limit):
    try:
        decoded_char = char.decode('utf-8')
        if decoded_char.isprintable() and len(input_str) < limit:
            input_str += decoded_char
            print(decoded_char, end='', flush=True)
    except UnicodeDecodeError:
        pass
    return input_str, False

def get_limited_input(prompt, limit, input_str = ''):
    enter_key = b'\r'
    backspace_key = b'\x08'
    arrow_key = b'\xe0'
    null_key = b'\x00'
    print(prompt, end='', flush=True)
    print(input_str, end='', flush=True)
    handlers = {
        enter_key: handle_enter,
        backspace_key: handle_backspace,
        arrow_key: handle_arrow_or_null,
        null_key: handle_arrow_or_null
    }
    while True:
        char = msvcrt.getch()
        handler = handlers.get(char, handle_printable)
        input_str, should_break = handler(input_str, char, limit)
        if should_break:
            break
    print("\r\033[2K", end='\r', flush=True)
    return input_str

def input_cli():
    equations = list()
    selected_idx = 0
    print("\033[1mEquations\033[0m")
    print("Example: 1*a + 2*b + 3*c = 4")
    while True:
        draw_list(equations, selected_idx)
        print("\n\033[2K", end='\r', flush=True)
        print("Up and down arrow keys to navigate, Enter to Edit, Press n to add new equation, Press d to delete equation, Press s to submit , Press q to quit", end='\r', flush=True)
        move_cursor_up(1)
        key = b'n'
        if len(equations) > 0:
            key = msvcrt.getch()
        if key == b'\xe0':
            key = msvcrt.getch()
            if key == b'H':  # Up arrow
                selected_idx = (selected_idx - 1) % len(equations)
            elif key == b'P':  # Down arrow
                selected_idx = (selected_idx + 1) % len(equations)
        elif key == b'\r':
            move_cursor_up(len(equations) - selected_idx)
            print("\033[2K", end='\r', flush=True)
            def edit_input():
                edited = get_limited_input("Edit the equation: ", 100, equations[selected_idx])
                if edited == '':
                    edit_input()
                else:
                    equations[selected_idx] = edited
                    [print() for _ in range(len(equations) - selected_idx)]
                return edited
            edit_input()

        elif key == b'n':
            equation = get_limited_input("Enter the equation: ", 100)
            if equation == '':
                pass
            else:
                print()
                equations.append(equation)
        elif key == b'd':
            if len(equations) > 0:
                del equations[selected_idx]
                if len(equations) == 0:
                    selected_idx = 0
                else:
                    selected_idx = (selected_idx - 1) % len(equations)
                print("\n\033[2K", end='\r', flush=True)
                move_cursor_up(2)
                draw_list(equations, selected_idx)
        elif key == b's':
            draw_list(equations, len(equations)+1)
            print("\n\033[2K", end='\r', flush=True)
            return equations
        elif key == b'q':
            print("\n\033[2K", end='\r', flush=True)
            return exit()
        print("\033[2K", end='\r', flush=True)