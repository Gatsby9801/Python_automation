filenames = ['a.txt', 'b.txt']
with open('out.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
