
def main():
    f = open('input.txt')
    lines = f.read()
    lines = lines.split('\n')
    parsed_code = {}
    init_vars = {}
    for line in lines:
        if line:
            left, right = line.split('->')
            operations = left.strip().split(' ')
            right = right.strip()
            if len(operations) == 1:
                if operations[0].isdigit():
                    init_vars[right] = int(operations[0])
                else:
                    parsed_code[right] = {'vars': [operations[0]],
                                        'op': 'INT'}
            elif len(operations) == 2:
                parsed_code[right] = {'vars': [operations[1]],
                                    'op': [operations[0]]}
            else:
                parsed_code[right] = {'vars': [operations[0], operations[2]],
                                    'op': [operations[1]]}

    def find_a():
        if 'a' in init_vars:
            print(a)
        else:
            for var, expression in parsed_code.iteritems():
                new_vars = []
                check_var_value = False
                for var in expression['vars']:
                    if var in init_vars:
                        new_vars.append(init_vars[var])
                        check_var_value = True
                    else:
                        new_vars.append(var)
                if check_var_value:
                    expression['vars'] = new_vars
                    op = expression['op']
                    inited_var = None
                    try:
                        expression['vars'] = [int(v) for v in expression['vars']]
                        if op == 'AND':
                            inited_var = expression['vars'][0] & expression['vars'][1]
                        elif op == 'OR':
                            inited_var = expression['vars'][0] | expression['vars'][1]
                        elif op == 'NOT':
                            inited_var = ~expression['vars'][0]
                        elif op == 'INT':
                            inited_var = int(expression['vars'][0])
                        elif op == 'LSHIFT':
                            inited_var = expression['vars'][0] << expression['vars'][1]
                        elif op == 'RSHIFT':
                            inited_var = expression['vars'][0] >> expression['vars'][1]
                    except:
                        pass
                    if inited_var is not None:
                        init_vars[var] = inited_var
                        print init_vars
                        del parsed_code[var]
            find_a()

    find_a()

if __name__ == "__main__":
    main()
