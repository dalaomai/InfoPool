# """
# 用于处理指定转义的工具
# """

import re

class EscapeTool():

    @staticmethod
    def replace(text,escape,replace):
        text = str(text)
        escape = str(escape)
        replace = str(replace)

        indexStart = 0
        escapeLen = len(escape)
        pattern = re.compile(escape.replace('\\','\\\\'))

        while True:
            searchResult = pattern.search(text,indexStart)
            if searchResult == None:
                break
            indexStart = searchResult.span()[1]
            if pattern.search(text,indexStart,indexStart+escapeLen) == None:
                text = text[0:searchResult.span()[0]] + replace + text[indexStart:]
            else:
                text = text[0:searchResult.span()[0]] +  text[indexStart:]

        
        return text

    @staticmethod
    def insert(text,escape):
        text = str(text)
        escape = str(escape)
        return text.replace(escape,escape+escape)

if __name__=="__main__":
    EscapeTool.replace(r'asdf\d\d\dasdfas\d',r'\d','代替')
    print(EscapeTool.insert(r'asdf\dasdf\d',r'\d'))