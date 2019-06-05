import stract

template1=stract.Template({'a':1, 'b':2, 'c':3})
template2=template1.extend({'x':8, 'y':0, 'z':5})

model=template2(a=10, y=6)
print(model.attributes())