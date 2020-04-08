def htmlEncodeByRegExp(str):
    if len(str)==0:
        return None
    str = str.replace('&lt;', '<')
    str = str.replace('&gt;', '>')
    str = str.replace('&nbsp;', ' ')
    str = str.replace('&#39;', '\'')
    str = str.replace('&quot;', '\"')
    str = str.replace('</p>', '')
    str = str.replace('<p>', '')
    str = str.replace('&amp;', '&')
    str = str.replace('<pre>', '')
    str = str.replace('</pre>', '')
    str = str.replace('<br>', '\n')
    return str

jjj = htmlEncodeByRegExp("<p>afdasfda&nbsp; &nbsp; &nbsp;&nbsp;</p>")
print(jjj)
