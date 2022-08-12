from typing import List

N = int(input())
arr: List[str] = []
for i in range(N):
    if i != "print":
        command = input().split(" ")
    else:
        command = "print(arr)"
    if len(command) == 1:
        if command == ["print"]:
            cmd = f"{command[0]}(arr)"
            eval(cmd, {"arr": arr})
        else:
            cmd = f"arr.{command[0]}()"
            eval(cmd, {"arr": arr, "command": command})
    elif len(command) == 2:
        cmd = f"arr{'.'}{command[0]}{'('}{command[1]}{')'}"
        eval(cmd, {"arr": arr, "command": command})
    else:
        cmd = f"arr.{command[0]}({command[1]}, {command[2]})"
        eval(cmd, {"arr": arr, "command": command})
