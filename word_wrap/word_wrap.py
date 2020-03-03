example_string = "hello there luna, you are sitting on my table. Isn't that nice?"


def max_line_len(input_string: str, max_len: int) -> str:
    """
    splits the string into lines no longer than the max line length set
    :param input_string: str
    :param max_len: int
    :return: str
    """
    word_list = input_string.split(" ")
    return_list = []
    return_string = ""

    for index, word in enumerate(word_list):
        print(f"rs: {return_string}")
        update_word = f"{word}" if index == 0 else f" {word}"
        # line is max len
        if len(return_string) == max_len:
            return_list.append(return_string + "\n")
            return_string = update_word  # current word will be reviewed next cycle
        # line plus new word is less than max len
        elif len(f"{return_string}{update_word}") < max_len:
            return_string += update_word
            if index == len(word_list) - 1:  # we are at the end of the list
                return_list.append(return_string)
        # line plus new word is greater than max len
        elif len(f"{return_string}{update_word}") > max_len:
            return_list.append(return_string + "\n")
            return_string = update_word

    return f"{''.join(return_list)}"


