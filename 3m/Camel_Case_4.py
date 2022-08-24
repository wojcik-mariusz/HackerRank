from typing import List



params: List[str] = list(map(str, input().split(";")))

operation = params[0]
type_output = params[1]
name = params[2]


def create_var_name(operation: str, name: str, type_output: str):
    if operation == "C":
        if type_output == "V":
            name: List[str] = name.split()
            var_name: str = name[0] + "".join(x.title() for x in name[1:])

    else:
        var_name = ""
        for i in name:
            if i.isupper():
                var_name += "*"
                var_name += i
            else:
                var_name += i
        var_name = var_name.replace("*", " ").lstrip()
    print(var_name)
    return var_name

create_var_name(operation=operation, name=name, type_output=type_output)

