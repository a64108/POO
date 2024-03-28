def print_with_frame(text):
    """
    Prints the given text surrounded by a frame of ASCII characters. The text
    is separated by horizontal lines if it contains newline characters.

    Args:
        text (str): The text to be framed.

    Example:
        >>> print_with_frame("Hello\nWorld")
        ┌───────┐
        │ Hello │
        ├───────┤
        │ World │
        └───────┘
    """
    lines = text.splitlines()
    max_line_length = max(len(line) for line in lines)
    width = max_line_length + 4

    # Function to create horizontal borders
    def create_border(left_char, middle_char, right_char):
        return left_char + middle_char * (width - 2) + right_char

    # Print the top border
    print(create_border("┌", "─", "┐"))

    # Print the text with vertical borders and horizontal lines
    for i, line in enumerate(lines):
        print(f"│ {line.ljust(max_line_length)} │")
        if i < len(lines) - 1:
            print(create_border("├", "─", "┤"))

    # Print the bottom border
    print(create_border("└", "─", "┘"))
