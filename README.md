# Tkinter-Hot-Reload
A wrapper around tkinter module of python which provides hot reload functionality to the UI aspect.

# Note
This project is not complete and most probaby would not get complete until and unless some volenteer invests is own time and energy. The purpose of sharing the repoisorty is to provide a base for someone in the future with same goal as mine that is Hot Reload for Tkinter.

# Idea
Reimplementing the tkinter's Widget Class and using pythons `inspect` library to extract the varaible in which the widget will be stored. Add this variable and the tkinter `name` of the widget into a Database for later access. The changes in widget are tracked using thier variable names, so change in variable means new widget. The main idea is tracking changes for all those lines which are using tkinter methods and classes, if change done to a line, get its variable name, throgh varaible name get its tkinter name, analiys the change made to the line and then excute the change using `.configure` method.

With the above, once we start our application, a database would be create with each widget_name and its variable_name. Then we track the file for changes using `difflib_parser` module, analisy the changes and sort them into 3 catagories i.e new, deleted, modified. for each line validate wheader the changed line is an tkinter libary line using `ast`. if its a new tkinter line then execute it as it is. If deleted tkinter line and is a widget line then use `widget.destroy()`. if modified then `.configure()` along with the changed parameters
