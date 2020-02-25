>>> def count_words(fn):
...       import os.path
...       if os.path.isfile(fn):
...           with open(fn,'r') as fh:
...               total = 0
...               for line in fh:
...                  total +=len(line.split())
...               return total
...
>>> count_words('E:/工程科学学院/大三课程/项目实践/git_test/SES2020spring/unit2/readme.md')
273