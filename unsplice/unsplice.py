
def remove_unwanted_consec_chars(dirty_string: str, *args: str) -> str:
    """
    takes a string, removes the args from it if they are consecutive
    :param dirty_string: str
    :param args: str
    :return: str
    """
    consec_args = "".join(args)  # makes the args consecutive
    return dirty_string.replace(consec_args, "")  # strips them out - if present


if __name__ == "__main__":
    print(remove_unwanted_consec_chars(remove_unwanted_consec_chars("abc\\\ndef", "\\\n")))
    print(remove_unwanted_consec_chars(remove_unwanted_consec_chars("hellojim jane", "jim")))
    print(remove_unwanted_consec_chars(remove_unwanted_consec_chars("__pnice", "__p")))
    print(remove_unwanted_consec_chars(remove_unwanted_consec_chars("n o", " ")))
