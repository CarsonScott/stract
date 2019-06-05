import stract

model1=stract.Model(a=1, b=4, c=2)
model2=stract.Model(x=0, y=3, z=9)

model3=model1.merge(model2)
print(model3.attributes())

model4=model3.extract(['a', 'x', 'z'])
print(model4.attributes())
