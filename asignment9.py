class user_defined_exception(Exception):
    def __init__(self,arg):
        self.arg = arg

import mathoperation as c

try:
    raise user_defined_exception("User defined exception")
except user_defined_exception as u:
    print(u.arg)
obj = c.math_operations(10,40)
obj.power()
obj.trigno()
obj.basic()
obj.rest()