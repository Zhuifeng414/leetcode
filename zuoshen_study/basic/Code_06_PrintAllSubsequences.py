class PrintAllSubsequence:
    def __init__(self):
        return

    def process(self, content, i, res):
        if i == len(content):
            print(res)
            return
        self.process(content, i+1, res)
        self.process(content, i+1, res+content[i])

    def fullstr(self, content, res_index, i):
        if i == 1:
            for index in range(len(content)):
                if index not in res_index:
                    res_index.append(index)
                    break
            res = ''
            for index in res_index:
                res += content[index]
            print(res)
        else:
            for index in range(len(content)):
                if index not in res_index:
                    self.fullstr(content, res_index+[index], i-1)

if __name__ == '__main__':
    content = 'abcd'
    #PrintAllSubsequence().process(content, 0, '')
    PrintAllSubsequence().fullstr(content, [], len(content))