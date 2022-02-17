class SgfTree(object):
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True


def parse(input_string):
    """
    Parses the Smart Game Format string
    """
    # check for null string
    if len(input_string) == 0:
        raise ValueError("Length of input string should be greater than zero!")

    # check if tree exists
    if input_string[0] != "(" and input_string[-1] != ")":
        raise ValueError("No tree exists.")

    input_string = input_string.strip("(").strip(")")
    if input_string[0] != ";":
        raise ValueError("A tree should have a node inside it!")
    # input_string = input_string.replace
    return input_string


if __name__ == "__main__":
    SGF = "(;A[B](;B[C])(;C[D]))"
    RESULT = parse(input_string=SGF)
    print(RESULT)
