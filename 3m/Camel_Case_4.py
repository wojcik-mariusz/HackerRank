import sys
from typing import List, NoReturn

for line in sys.stdin.readlines():
    line = line.split(";")
    operation = line[0]
    type_output = line[1]
    name = line[2]


    def create_var_name(operation: str, name: str, type_output: str) -> NoReturn:
        if operation == "C":
            name: List[str] = name.split()
            if type_output == "V":
                var_name: str = name[0] + "".join(x.title() for x in name[1:])
            elif type_output == "C":
                var_name: str = "".join(x.title() for x in name)
            else:
                var_name: str = name[0] + "".join(x.title() for x in name[1:]) + "()"



        else:
            var_name = ""
            for i in name:
                if i.isupper():
                    var_name += "*"
                    var_name += i
                else:
                    var_name += i
            var_name = var_name.replace("*", " ").lstrip().split()
            var_name = " ".join(x.lower() for x in var_name).rstrip("()")
        print(var_name)

    create_var_name(operation=operation, name=name, type_output=type_output)








# import sys
# from typing import List, NoReturn
#
# lines = [x for x in input().split("\r\n")]
#
# for line in lines:
#     line.split(";")
#     operation = line[0]
#     type_output = line[1]
#     name = line[2]
#
#
#     def create_var_name(operation: str, name: str, type_output: str) -> NoReturn:
#         if operation == "C":
#             name: List[str] = name.split()
#             if type_output == "V":
#                 var_name: str = name[0] + "".join(x.title() for x in name[1:])
#             elif type_output == "C":
#                 var_name: str = "".join(x.title() for x in name)
#             else:
#                 var_name: str = name[0] + "".join(x.title() for x in name[1:]) + "()"
#
#
#
#         else:
#             var_name = ""
#             for i in name:
#                 if i.isupper():
#                     var_name += "*"
#                     var_name += i
#                 else:
#                     var_name += i
#             var_name = var_name.replace("*", " ").lstrip().split()
#             var_name = " ".join(x.lower() for x in var_name).rstrip("()")
#             print(var_name)
#
#     create_var_name(operation=operation, name=name, type_output=type_output)
