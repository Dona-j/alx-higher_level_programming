#!/usr/bin/python3

if __name__ == "__main__":
    """prints all the names defined by the compiled module hidden_4.pyc"""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print("{}".format(name))