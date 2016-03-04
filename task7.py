
def main():
    f = open('input.txt')
    lines = f.read()
    lines = lines.split('\n')
    parsed_code = {}
    init_vars = {}
    for line in lines:
        left, right = line.split('->')
        operations = left.strip().split(' ')
        right = right.strip()
        if len(operations) == 1:
            init_vars[right] = int(operations)
        elif len(operations) == 2:
            parsed_code[right] = {'vars': [operations[1]],
                                  'op': [operations[0]]}
        else:
            parsed_code[right] = {'vars': [operations[0], operations[2]],
                                  'op': [operation[1]]}

    def find_a():
        if 'a' in init_vars:
            print(a)
        else:
            for var, expression in parsed_code.iteritems():
                new_vars = []
                check_var_value = False
                for var in expression[vars]:
                    if var in init_vars:
                        new_var.append(init_vars[var])
                        check_var_value = True
                    else:
                        new_var.append(var)
                if check_new_var:
                    expression[vars] = new_vars
                    op = expression['op']
                    inited_var = None
                    try:
                        if op == 'AND':
                            pass
                        elif op == 'OR':
                            pass
                    except:
                        pass
                    if inited_var:
                        init_vars[var] = inited_var
                        del parsed_code[var]
            find_a()




if __name__ == "__main__":
    main()
