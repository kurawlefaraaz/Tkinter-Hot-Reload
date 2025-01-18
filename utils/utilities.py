import ast
from tokenize_str import stringTokenize

# TODO: File Snaps checker
DB_select_query = '''
    SELECT * FROM Widget_Data WHERE var = ?
'''

def getArguments(line):
    args_cords = (line.find("("), line.rfind(")") + 1)
    args_string = line[slice(*args_cords)]
    args = [token.string for token in stringTokenize(args_string)][1:-3] + [""]
        
    arguments, argument = [], [] 
    for token in args:
        if token not in ('',','):
            argument.append(token)
            continue

        if len(argument) == 3:
            argument.remove("=")
        arguments.append(tuple(argument))
        argument.clear()
    
    return arguments

def getVariable(line):
    variable = line[0: line.find("=")].replace(" ", "")
    return variable

class LineValidate:
    def __init__(self, line, DB_cursor):
        self.line = line
        self.node= ast.parse(line).body[0]
        self.DB_cursor = DB_cursor

        self.node_value = self.node.value 

    def is_assigned(self):
        return isinstance(self.node, ast.Assign)

    def is_assigned_constant(self):
        return self.is_assigned() and isinstance(self.node_value, ast.Constant)
    
    def is_tk_widget(self):
        if not isinstance(self.node_value, ast.Call): 
            return 0
        
        func_call_attr = self.node_value.func.value
        name_id = func_call_attr.id

        if (name_id) != ('tk'): return 0
        else: return 1 
    
    def is_present_in_database(self):
        if not self.is_assigned(): return 0
        variable = getVariable(self.line)

        self.DB_cursor.execute(DB_select_query, (variable,))
        contents = self.DB_cursor.fetchall()

        if contents is not []: return 1
        else: return 0
    
    def is_widget_attr(self):
        if not self.is_assigned(): return 0
        variable = getVariable(self.line).split(".")

        self.DB_cursor.execute(DB_select_query, (variable,))
        contents = self.DB_cursor.fetchall()

        if contents is not []: return 1
        else: return 0

if __name__ == "__main__":
    line = "a = tkinter.Label(ROOT, name='test1', text='testing')"