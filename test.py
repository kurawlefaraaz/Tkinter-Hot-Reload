# import tkinter as tk

# root = tk.Tk()
# def main():
# 	a = tk.Button(root, text = "hell0 world")
# 	a.pack()
# 	a = tk.Button(master = root, text = "hello wo1rld", name="test")
# 	print(a.winfo_name(), a)
# 	a.pack()
# 	print("hello")
# 	print("21")
# main()
# a = tk.Frame(root, name="test")
# print(a.winfo_name(), a)
# a.pack()

# b= tk.Button(a, text="test")
# b.pack()
# print(b.winfo_name())

# import tkinter as tk

# def show_widget_name(widget):
#     print("Widget Name:", widget.winfo_name())

# button1 = tk.Button(root, text="Button 1", name="shared_name")
# button1.pack()

# button2 = tk.Button(root, text="Button 2", name="shared_name")
# button2.pack()
# print(button1.cget("text"), button1.winfo_name(), "########################")
# print(button2.cget("text"), button2.winfo_name())
# # Attempting to access widgets by their name
# print(root.winfo_children())
import inspect

def my_function():
    a = 10
    b = 20
    print("Inside my_function")

def get_variable_scope(func_name):
    # Get the function object by name
    func = globals().get(func_name)
    
    if func or callable(func):
        # Create a frame for the function's execution context
        frame = inspect.currentframe()
        print(frame.__dir__())
        print(frame.f_locals)
        try:
            while frame:
                if frame.f_code == func.__code__:
                    # Return local variables in that frame
                    return frame.f_locals
                frame = frame.f_back
        finally:
            del frame  # Clean up reference to avoid circular reference
    return None

# Example usage
my_function()  # Call the function first to set its local scope
scope_vars = get_variable_scope('my_function')
print("Local variables in my_function:", scope_vars)


# root.mainloop()




