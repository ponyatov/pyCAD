import syntax

class Highlighter(syntax.Highlighter):
    def __init__(self, document):
        super().__init__(document)
        syntax.Keyword(self.rules,['as'])
        syntax.Number(self.rules)
        syntax.String(self.rules)
        syntax.LineComment(self.rules, r'#[^\r\n]*')
