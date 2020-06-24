from Function import Value, ValuePlaceholder

class FunctionProcessor:
    def __init__(self):
        self.function_mappings = {}
    
    def register(self, fn_name, fn):
        self.function_mappings[fn_name] = fn

    def evaluate_statement(self, operator, args):
        # TODO
        print(f'Evaluating statement with operator \'{operator}\' and arguments {args} -> ', end='')

        if operator in self.function_mappings:
            out = self.function_mappings[operator](args)
        else:
            out = 0

        print(out)
        return Value(out)

    def evaluate_statement_tree(self, tree):
        for i, level in reversed(list(enumerate(tree))):
            for j, statement in enumerate(level):
                for k, arg in enumerate(statement.args):
                    if (type(arg) is ValuePlaceholder):
                        statement.args[k] = tree[arg.depth][arg.index]
                
                tree[i][j] = self.evaluate_statement(statement.operator, statement.args)
        
        return tree[0][0]