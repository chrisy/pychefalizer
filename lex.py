# Lexer class

import ply.lex as plex

class Lex(object):
    # A string containing ignored characters (spaces and tabs)
    #t_ignore  = ' \t'
    t_ignore  = ''

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

    # Test its output
    def test(self, data):
        self.lexer.input(data)
        while True:
             tok = self.lexer.token()
             if not tok:
                 break
             print(tok)

    def translate(self, data):
        self.lexer.input(data)
        str = ""
        while True:
             tok = self.lexer.token()
             if not tok:
                 break
             str += tok.value
        return str
