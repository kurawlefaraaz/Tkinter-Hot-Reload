import sys, io
import tokenize, token
#BACKUP
def stringTokenize(string):
        string = io.StringIO(string)
        return tokenize.generate_tokens(string.readline)

if len(sys.argv)!=2: 
    string = "a= tkinter.Label(ROOT, name='test1', text='testing')"
else: string = sys.argv[1]

if __name__=="__main__":
    for token in stringTokenize(string):
        print(list(token))

    # just_len = 20
    # for toknum, tokval, start, end, line in stringTokenize(string):
    #     tokname = token.tok_name[toknum]
    #     start = str(start).ljust(just_len)
    #     tokname = str(tokname).ljust(just_len)
    #     start = str(start).ljust(just_len)
    #     print(start, tokname, repr(tokval))