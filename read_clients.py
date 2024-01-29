def main():
    infile = open('clients.txt', 'r')

    i = 1
    for line in infile:
        print(i, '. ', line, end='', sep='')
        i += 1

main()