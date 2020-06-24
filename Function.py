from FunctionCallParser import FunctionCallParser

class ValuePlaceholder:
    def __init__(self, depth, index):
        self.depth = depth
        self.index = index

class Value:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f'Value({self.value})'

class Statement:
    def __init__(self, operator):
        self.operator = operator
        self.args = []

class Function:
    def __init__(self, function):
        self.function = function
    
    def probe_depth(self, function, depth=1):
        max_depth = depth

        for child in function.getChildren():
            if (type(child) is FunctionCallParser.FunctionContext):
                new_depth = depth + self.probe_depth(child, depth)
                max_depth = max(max_depth, new_depth)

        return max_depth
    
    def process_statement_tree(self):
        self.tree_depth = self.probe_depth(self.function)
        self.statements = [[] for _ in range(self.tree_depth)]
        self._process_statement_tree(self.function)
        return self.statements

    def _process_statement_tree(self, function, depth=0):
        operator = function.operator().getText()

        new_statement = Statement(operator)

        for child in function.getChildren():
            if (type(child) is FunctionCallParser.FunctionContext):
                new_statement.args.append(ValuePlaceholder(depth + 1, len(self.statements[depth + 1])))
                self._process_statement_tree(child, depth + 1)
            elif (type(child) is FunctionCallParser.ArgumentContext):
                new_statement.args.append(Value(child.getText()))
        
        self.statements[depth].append(new_statement)