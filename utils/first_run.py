import utilities, sqlite3, file_snaps
database_cursor = sqlite3.connect("reload.db").cursor()
FILE_SNAPS = file_snaps.FileSnapContainer("file_path")
def is_var_in_DB(var):
    var_list = database_cursor.execute("""SELECT var_name FROM widget_data""").fetchall()
    if var in var_list: return 1
    else: return 0

def is_var_an_tkinter_attr(var):
    if "." not in var: return 0

    if not is_var_in_DB(var.split(".")[0]): return 0
    else: return 1

def validate_program_on_first_run(file_path):
    file_lines = open(file_path).readline
    
    database_cursor.execute("""CREATE TABLE widget_data(var_name, widget_name, var_as_values)""")

    for line in file_lines:
        line_validate = utilities.ValidateLine(line)
        
        if not line_validate.validate():
            continue
        
        retrive_obj = utilities.RetriveArgumentData(line)

        var_name = retrive_obj.get_var_name() if line_validate.is_assigned() else None
        keywords = retrive_obj.get_keywords()
        name = keywords.get("name")
        var_as_values = retrive_obj.get_var_as_values()

        data = {"var_name": var_name, "widget_name": name, "var_as_values": var_as_values }
        database_cursor.execute("""INSERT INTO reload.db Values(:var_name, :widget_name, :var_as_values)""", data)
    

def validate_program_on_update(file_path):
    updated_lines = file_snaps.diffSnaps(FILE_SNAPS.get())
    
    for line in updated_lines:
        line_validate = utilities.ValidateLine(line)
        retrive_vals = utilities.RetriveArgumentData(line)

# import tkinter as tk

# def generic_init(self, master, /, *, name, **options): 
#     super(self.__class__, self).__init__(master, name=name, **options)

# widgets = [("Label", tk.Label), ("Button", tk.Button), ("Entry", tk.Entry)]

# root = tk.Tk()
# import sys
# current_module = module = sys.modules[__name__]
# for var, widget in widgets:
#     setattr(current_module, var, type(var, (widget, ), dict(__init__ = generic_init)))
# Label = type("Label", tk.Label, dict(__init__ = generic_init))
# Entry = type("Entry", tk.Entry, dict(__init__ = generic_init))
# Button = type("Button", tk.Button, dict(__init__ = generic_init))

# root.mainloop()