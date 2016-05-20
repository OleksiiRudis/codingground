# Hello World program in Python

def sklonenie(n, args):
    if args is None:
        return False
    arg_list = [arg.strip() for arg in args.split(',')]
    if n%10 == 1 and n%100 != 11:
        str = arg_list[0]
    elif n%10 >= 2 and n%10 <= 4 and (n%100 < 10 or n%100 >= 20):
        str = arg_list[1]
    else:
        str = arg_list[2]
    return str

for num in range(1,150): 
    print num, " ", sklonenie(num, "tovar,tovara,tovarov")
    
