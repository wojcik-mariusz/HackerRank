from typing import List



params: List[str] = list(map(str, input().split(";")))

operation = params[0]
type_output = params[1]
name = params[2]


def create_var_name(operation: str, name: str):
    if operation == "C":
        var_name = "".join(x for x in name)
    else:
        var_name = ""
        for i in name:
            if i.isupper():
                var_name += "*"
                var_name += i
            else:
                var_name += i
        var_name = var_name.replace("*", " ").lstrip()
    return var_name

