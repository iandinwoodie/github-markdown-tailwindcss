import os


CLASS = '.markdown'
INFILE = 'markdown.css'
OUTFILE = 'markdown-nested.css'


def reformat_lines(lines):
    class_decl = '{} '.format(CLASS)
    decl_end = len(class_decl)
    leave_open = False
    nested = False
    reformatted = []
    for line in lines:
        line = line.rstrip()
        if line[:decl_end] == class_decl:
            line = line.rstrip()
            pos = line.index('{')
            rule = line[decl_end:pos].rstrip()
            if not rule:
                leave_open = True
            else:
                line = '& {} {{'.format(rule)
        if leave_open and line == '}':
            nested = True
            leave_open = False
        else:
            if line and nested:
                line = '  {}'.format(line)
            reformatted.append(line)
    reformatted.append('}')
    return reformatted


def main():
    with open(INFILE, 'r') as f:
        lines = f.readlines()
    lines = reformat_lines(lines)
    with open(OUTFILE, 'w') as f:
        for line in lines:
            f.write('{}\n'.format(line))


if __name__ == '__main__':
    main()
