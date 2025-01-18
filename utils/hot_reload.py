import tkinter as tk
import inspect, time, sqlite3
from utilities import getVariable, LineValidate

DB_create_table_query = '''
    CREATE TABLE IF NOT EXISTS Widget_Data(
        name TEXT PRIMARY KEY NOT NULL,
        variable TEXT NOT NULL
    );
    '''
DB_insert_query = '''
    INSERT INTO Widget_Data (name, variable) 
    VALUES (?, ?);
    '''
DB_remove_query = '''
    DELETE FROM Widget_Data WHERE name = ?
'''

DB_connection = sqlite3.connect(':memory:')
DB_cursor = DB_connection.cursor()
DB_cursor.execute(DB_create_table_query)
DB_connection.commit()

# TODO: ON DESTROY: Remove widget from the THR database = DONE

def get_widget_line():
    stack = inspect.stack()
    caller = stack[-1]
    return caller.code_context[0].strip()

class Button(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        name = self.winfo_name()

        line = get_widget_line()
        if not LineValidate(line, DB_cursor).is_assigned():
            raise SyntaxError("Widgets without variables are prohibited in Tkinter Hot Reload")

        var = getVariable(get_widget_line())

        DB_cursor.execute(DB_insert_query, (name, var))
    
    def destroy(self):
        DB_cursor.execute(DB_remove_query, (self.winfo_name(),))
        super().destroy()

class Checkbutton(tk.Checkbutton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        name = self.winfo_name()
        var = getVariable(get_widget_line())
        DB_cursor.execute(DB_insert_query, (name, var))
    
    def destroy(self):
        DB_cursor.execute(DB_remove_query, (self.winfo_name(),))
        super().destroy()

class Canvas(tk.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        name = self.winfo_name()
        var = getVariable(get_widget_line())

        DB_cursor.execute(DB_insert_query, (name, var))
    
    def destroy(self):
        DB_cursor.execute(DB_remove_query, (self.winfo_name(),))
        super().destroy()

class Entry(tk.Entry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        name = self.winfo_name()
        var = getVariable(get_widget_line())

        DB_cursor.execute(DB_insert_query, (name, var))
    
    def destroy(self):
        DB_cursor.execute(DB_remove_query, (self.winfo_name(),))
        super().destroy()

class Frame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        name = self.winfo_name()
        var = getVariable(get_widget_line())

        DB_cursor.execute(DB_insert_query, (name, var))
    
    def destroy(self):
        DB_cursor.execute(DB_remove_query, (self.winfo_name(),))
        super().destroy()

class Label(tk.Label):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        name = self.winfo_name()
        var = getVariable(get_widget_line())

        DB_cursor.execute(DB_insert_query, (name, var))
    
    def destroy(self):
        DB_cursor.execute(DB_remove_query, (self.winfo_name(),))
        super().destroy()

class LabelFrame(tk.LabelFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        name = self.winfo_name()

        line = get_widget_line()
        if not LineValidate(line, DB_cursor).is_assigned():
            raise SyntaxError("Widgets without variables are prohibited in Tkinter Hot Reload")

        var = getVariable(get_widget_line())

        DB_cursor.execute(DB_insert_query, (name, var))
    
    def destroy(self):
        DB_cursor.execute(DB_remove_query, (self.winfo_name(),))
        super().destroy()

class Listbox(tk.Listbox):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        name = self.winfo_name()

        line = get_widget_line()
        if not LineValidate(line, DB_cursor).is_assigned():
            raise SyntaxError("Widgets without variables are prohibited in Tkinter Hot Reload")

        var = getVariable(get_widget_line())

        DB_cursor.execute(DB_insert_query, (name, var))
    
    def destroy(self):
        DB_cursor.execute(DB_remove_query, (self.winfo_name(),))
        super().destroy()

class Menu(tk.Menu):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        name = self.winfo_name()

        line = get_widget_line()
        if not LineValidate(line, DB_cursor).is_assigned():
            raise SyntaxError("Widgets without variables are prohibited in Tkinter Hot Reload")

        var = getVariable(get_widget_line())

        DB_cursor.execute(DB_insert_query, (name, var))
    
    def destroy(self):
        DB_cursor.execute(DB_remove_query, (self.winfo_name(),))
        super().destroy()

class OptionMenu(tk.OptionMenu):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        name = self.winfo_name()

        line = get_widget_line()
        if not LineValidate(line, DB_cursor).is_assigned():
            raise SyntaxError("Widgets without variables are prohibited in Tkinter Hot Reload")

        var = getVariable(get_widget_line())

        DB_cursor.execute(DB_insert_query, (name, var))
    
    def destroy(self):
        DB_cursor.execute(DB_remove_query, (self.winfo_name(),))
        super().destroy()

class PanedWindow(tk.PanedWindow):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        name = self.winfo_name()

        line = get_widget_line()
        if not LineValidate(line, DB_cursor).is_assigned():
            raise SyntaxError("Widgets without variables are prohibited in Tkinter Hot Reload")

        var = getVariable(get_widget_line())

        DB_cursor.execute(DB_insert_query, (name, var))
    
    def destroy(self):
        DB_cursor.execute(DB_remove_query, (self.winfo_name(),))
        super().destroy()

class Radiobutton(tk.Radiobutton):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        name = self.winfo_name()

        line = get_widget_line()
        if not LineValidate(line, DB_cursor).is_assigned():
            raise SyntaxError("Widgets without variables are prohibited in Tkinter Hot Reload")

        var = getVariable(get_widget_line())

        DB_cursor.execute(DB_insert_query, (name, var))
    
    def destroy(self):
        DB_cursor.execute(DB_remove_query, (self.winfo_name(),))
        super().destroy()

class Scale(tk.Scale):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        name = self.winfo_name()

        line = get_widget_line()
        if not LineValidate(line, DB_cursor).is_assigned():
            raise SyntaxError("Widgets without variables are prohibited in Tkinter Hot Reload")

        var = getVariable(get_widget_line())

        DB_cursor.execute(DB_insert_query, (name, var))
    
    def destroy(self):
        DB_cursor.execute(DB_remove_query, (self.winfo_name(),))
        super().destroy()

class Scrollbar(tk.Scrollbar):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        name = self.winfo_name()

        line = get_widget_line()
        if not LineValidate(line, DB_cursor).is_assigned():
            raise SyntaxError("Widgets without variables are prohibited in Tkinter Hot Reload")

        var = getVariable(get_widget_line())

        DB_cursor.execute(DB_insert_query, (name, var))
    
    def destroy(self):
        DB_cursor.execute(DB_remove_query, (self.winfo_name(),))
        super().destroy()

class Spinbox(tk.Spinbox):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        name = self.winfo_name()

        line = get_widget_line()
        if not LineValidate(line, DB_cursor).is_assigned():
            raise SyntaxError("Widgets without variables are prohibited in Tkinter Hot Reload")

        var = getVariable(get_widget_line())

        DB_cursor.execute(DB_insert_query, (name, var))
    
    def destroy(self):
        DB_cursor.execute(DB_remove_query, (self.winfo_name(),))
        super().destroy()
        
class Text(tk.Text):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        name = self.winfo_name()

        line = get_widget_line()
        if not LineValidate(line, DB_cursor).is_assigned():
            raise SyntaxError("Widgets without variables are prohibited in Tkinter Hot Reload")

        var = getVariable(get_widget_line())

        DB_cursor.execute(DB_insert_query, (name, var))
    
    def destroy(self):
        DB_cursor.execute(DB_remove_query, (self.winfo_name(),))
        super().destroy()

class Tk(tk.Tk):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        name = self.winfo_name()

        line = get_widget_line()
        if not LineValidate(line, DB_cursor).is_assigned():
            raise SyntaxError("Widgets without variables are prohibited in Tkinter Hot Reload")

        var = getVariable(get_widget_line())

        DB_cursor.execute(DB_insert_query, (name, var))
    
    def destroy(self):
        DB_cursor.execute(DB_remove_query, (self.winfo_name(),))
        super().destroy()

class Toplevel(tk.Toplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        name = self.winfo_name()

        line = get_widget_line()
        if not LineValidate(line, DB_cursor).is_assigned():
            raise SyntaxError("Widgets without variables are prohibited in Tkinter Hot Reload")

        var = getVariable(get_widget_line())

        DB_cursor.execute(DB_insert_query, (name, var))
    
    def destroy(self):
        DB_cursor.execute(DB_remove_query, (self.winfo_name(),))
        super().destroy()

if __name__ == "__main__":
    start_time = time.time()
    root = Tk()

    a = Button()

    A= Scrollbar(root, name="gell")

    a = Button(root, text="Hello World",)
    a.pack()

    e = Toplevel(bg='red')

    e= DB_cursor.execute("SELECT * FROM Widget_Data")
    print(DB_cursor.fetchall())

    a.destroy()

    root.nametowidget("!button").destroy()

    DB_cursor.execute("SELECT * FROM Widget_Data")
    print(DB_cursor.fetchall())

    # print(e.nametowidget("."))
    # Start the Tkinter event loop
    print("--- %s seconds ---" % (time.time() - start_time))
    root.mainloop()