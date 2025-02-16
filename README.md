# Tkinter-Hot-Reload
A wrapper around tkinter module of python which provides hot reload functionality to the UI aspect.

# Note
This project is not complete and most probaby would not get complete until and unless some volenteer invests is own time and energy. The purpose of sharing the repoisorty is to provide a base for someone in the future with same goal as mine that is Hot Reload for Tkinter.

# Idea
Reimplementing the tkinter's Widget Class and using pythons `inspect` library to extract the varaible in which the widget will be stored. Add this variable and the tkinter `name` of the widget into a Database for later access. The changes in widget are tracked using thier variable names, so change in variable means new widget. The main idea is tracking changes for all those lines which are using tkinter methods and classes, if change done to a line, get its variable name, throgh varaible name get its tkinter name, analiys the change made to the line and then excute the change using `.configure` method.
