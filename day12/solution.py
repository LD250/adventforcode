def main():
    f = open('input.txt')
    content = f.read()
    numbers = set([str(d) for d in range(10)])

    def calculate_total(content):
        number = ""
        minus_sign = False
        total = 0
        for symbol in content:
            if symbol in numbers:
                number += symbol
            elif symbol == '-' and not number:
                minus_sign = True
            elif number:
                if minus_sign:
                    total -= int(number)
                else:
                    total += int(number)
                number = ""
                minus_sign = False
        return total
    print calculate_total(content)

if __name__ == "__main__":
    main()
