class ASTNode:
    def __init__(self, data):
        self.data = data

    def typestr(self):
        return "ASTNode"

    def padding_helper(self, lines):
        piped_lines = []
        for i, line in enumerate(lines):
            if i < len(lines) - 1:
                if line[0] in ' │├└':
                    c = '│'
                else:
                    c = '├'
            else:
                c = '└'
            piped_lines.append('{} {}'.format(c, line))
        return [self.typestr()] + piped_lines

    def string_helper(self):
        # returns a list of lines
        # each one is padded with additional spacing
        lines = self.data.string_helper()
        return self.padding_helper(lines)

    def __str__(self):
        return "\n".join(self.string_helper())


class BinaryExp(ASTNode):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def typestr(self):
        return "BinaryExp"

    def string_helper(self):
        lines_left = self.left.string_helper()
        lines_right = self.right.string_helper()
        lines = lines_left + lines_right
        return self.padding_helper(lines)


class AddExp(BinaryExp):
    def typestr(self):
        return "AddExp"


class SubExp(BinaryExp):
    def typestr(self):
        return "SubExp"


class MulExp(BinaryExp):
    def typestr(self):
        return "MulExp"


class DivExp(BinaryExp):
    def typestr(self):
        return "DivExp"


class UnaryExp(ASTNode):
    def typestr(self):
        return "UnaryExp"


class NegExp(UnaryExp):
    def typestr(self):
        return "NegExp"


class Number(ASTNode):
    def typestr(self):
        return "Number"

    def string_helper(self):
        return ["{}({})".format(self.typestr(), self.data)]
