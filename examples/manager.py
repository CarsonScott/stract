import stract

manager=stract.Manager()

# Templates

manager.create_template(
	key='t1', 
	template=stract.Template({'a':4, 'b':2, 'c':1}))

manager.create_template(
	key='t2', 
	template=stract.Template({'x':4, 'y':2, 'z':1}))

# Extensions

manager.extend(
	src='t1', 
	key='t3', 
	data={'d':4, 'e':35, 'f':354})

# Instances

manager.instantiate(
	src='t3', 
	key='m1')

manager.instantiate(
	src='t2', 
	key='m2')

# Merges

manager.merge(
	src=('m1','m2'),
 	key='m3')

for key in manager:
	data=manager.data(key)
	print(key)
	for key in data:
		print('\t', key, ': ', data[key], sep='')
