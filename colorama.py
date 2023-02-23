import colorama

print(dir(colorama))


import colorama

colorama.init()
print(colorama.Fore.RED + colorama.Back.GREEN + "Hello, world!" + colorama.Style.RESET_ALL)