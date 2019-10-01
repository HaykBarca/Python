# Global scoped variables
glob_var = "Global"
def func():
  print(glob_var)
func()

# Function scoped variables(Only can be seen isnide that functions or nested functions)
def scoped():
  scoped_var = "Scoped"
  print(scoped_var)
scoped()

# If you want to change global variable you should pass 'global' keyword before
def change_global():
  global glob_var
  glob_var = "Changed Global!"
change_global()
func()