from functools import partial

def generateGet(type, name):
    return '''- (%s *)%s {\n\tif (!_%s) {\n\t\t_%s = [[%s alloc] init];\n\t}\n\treturn _%s;\n}\n'''% (type, name, name, name, type, name)

def addView(name):
    return '''[self.view addSubview:self.%s];'''%(name)

def constraint(name):
    return '''[self.%s mas_makeConstraints:^(MASConstraintMaker *make) {\n\t\n}];'''%(name)

inputContent = partial(input, '\n')
sentinel = 'end'

objectList = []

for content in iter(inputContent, sentinel):
    objectList.append(content)

getList = []
addList = []
constraintList = []

for objectStr in objectList:
    list1 = objectStr.split(') ')
    str2 = list1[1].split(';')[0]
    list2 = str2.split('*')

    # type = list2[0].lstrip().rsplit()[0]
    # name = list2[1].lstrip().rsplit()[0]
    type = list2[0].strip()
    name = list2[1].strip()

    getList.append(generateGet(type, name))
    addList.append(addView(name))
    constraintList.append(constraint(name))

for str in getList:
    print(str)

for str in addList:
    print(str)
print('')
for str in constraintList:
    print(str)