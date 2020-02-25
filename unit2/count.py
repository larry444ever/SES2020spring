>>> def count_words(fn):
...       import os.path
...       if os.path.isfile(fn):
...           with open(fn,'r') as fh:
...               total = 0
...               for line in fh:
...                  total +=len(line.split())
...               return total
...
>>> count_words('E:/���̿�ѧѧԺ/�����γ�/��Ŀʵ��/git_test/SES2020spring/unit2/readme.md')
273