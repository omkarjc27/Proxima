class ProximaError(Exception):

    def __init__(self, message, line, column):
        super(ProximaError,self).__init__()
        print('{} at line {}, column {}'.format(message, line, column))


def report_syntax_error(lexer, error):
    line = error.line
    column = error.column
    source_line = lexer.source_lines[line - 1]
    print('{}\n{}^'.format(source_line, ' ' * (column - 1)))
