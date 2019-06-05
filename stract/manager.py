from .util import *
from .properties import Properties

class Manager(dict):
	def __init__(self):
		self.models=[]
		self.templates=[]
		self.properties=Properties()

	def create_template(self, key, template, extends=None):
		self[key]=template
		self.templates.append(key)
		self.properties.extends[key]=extends
		self.properties.instances[key]=[]
		self.properties.subtypes[key]=[]

	def create_model(self, key, model, type=None):
		self[key]=model
		self.models.append(key)
		self.properties.type[key]=type
		self.properties.partof[key]=[]
		self.properties.contains[key]=[]
	
	def extend(self, src, key, data):
		template=self[src].extend(data)
		self.create_template(key, template, src)
		self.properties.subtypes[src].append(key)

	def instantiate(self, src, key, **kwargs):
		model=self[src](**kwargs)
		self.create_model(key, model, src)
		self.properties.instances[src].append(key)

	def merge(self, src, key):
		src1,src2=src
		model=self[src1].merge(self[src2])
		self.create_model(key, model)
		self.properties.contains[key].append(src1)
		self.properties.contains[key].append(src2)
		self.properties.partof[src1].append(key)
		self.properties.partof[src2].append(key)
	
	def extends(self, key):
		if key in self.templates:
			return self.properties.extends[key]

	def subtypes(self, key):
		if key in self.templates:
			return self.properties.subtypes[key]

	def type(self, key):
		if key in self.models:
			return self.properties.type[key]

	def instances(self, key):
		if key in self.templates:
			return self.properties.instances[key]

	def contains(self, key):
		if key in self.models:
			return self.properties.contains[key]

	def partof(self, key):
		if key in self.models:
			return self.properties.partof[key]

	def data(self, key):
		if key in self:
			output={'value':self[key]}
			if key in self.templates:
				output['class']='template'
				output['extends']=self.extends(key)
				output['instances']=self.instances(key)
				output['subtypes']=self.subtypes(key)
			elif key in self.models:
				output['class']='model'
				output['type']=self.type(key)
				output['contains']=self.contains(key)
				output['partof']=self.partof(key)
			return output