import test_page_two as ptwo

if __name__ == "__main__":
    return_from_ptwo = getattr(ptwo, "return_string_caps")
    print(return_from_ptwo("salad"))
