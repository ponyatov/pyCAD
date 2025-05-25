import syntax

class XXXLexer(syntax.Lexer):
    pass

class Highlighter(syntax.Highlighter):
    lexer = XXXLexer()
    
    # def __init__(self, document):
    #     super().__init__(document)
    #     syntax.Keyword(self.rules,['as'])
    #     syntax.Number(self.rules)
    #     syntax.String(self.rules)
    #     syntax.LineComment(self.rules, r'#[^\r\n]*')
