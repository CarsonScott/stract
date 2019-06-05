from .util import *
from .model import Model
from .structure import Structure

class Template(Structure):

	def __init__(self, *data):
		super().__init__()
		self.attrs={}
		self.setup(*data)
	
	def __call__(self, **kwargs):
		data={}
		for key in self.attrs:
			if key in kwargs:
				value=kwargs[key]
			else:value=self.attrs[key]
			data[key]=value
		output=Model()
		output.setup(data)
		self.transfer_metadata(output)
		return output

	def setup(self, *data):
		for attrs in data:
			for key in attrs:
				self.attrs[key]=attrs[key]

	def keys(self):
		return list(self.attrs.keys())

	def attributes(self):
		return self.attrs

	def set_constant(self, key, state=True):
		if state==True and key not in self.metadata.constants:
			self.metadata.constants.append(key)
		elif state==False and key in self.metadata.constants:
			del self.metadata.constants[self.metadata.constants.index(key)]
	
	def set_private(self, key, state=True):
		if state==True and key not in self.metadata.private:
			self.metadata.private.append(key)
		elif state==False and key in self.metadata.private:
			del self.metadata.private[self.metadata.private.index(key)]
	
	def set_protected(self, key, state=True):
		if state==True and key not in self.metadata.protected:
			self.metadata.protected.append(key)
		elif state==False and key in self.metadata.protected:
			del self.metadata.protected[self.metadata.protected.index(key)]

	def extend(self, *data):
		output=Template(self.attrs, *data)
		self.transfer_metadata(output)
		return output

	def load(self, filename):
		config=ConfigParser()
		config.read(filename)
		sections=config.sections()
		if 'Template' in sections:
			template=config['Template']
			name=template['name']
			description=template['description']
			self.set_name(name)
			self.set_description(description)
		if 'Attributes' in sections:
			attributes=dict(config['Attributes'])
			for key in attributes:
				attributes[key]=get_value_from_string(attributes[key])
			self.setup(attributes)
		if 'Constants' in sections:
			constants=config['Constants']
			for key in constants:
				state=get_value_from_string(constants[key])
				if state==1:self.set_constant(key)
		if 'Private' in sections:
			private=config['Private']
			for key in private:
				state=get_value_from_string(private[key])
				if state==1:self.set_private(key)
		if 'Protected' in sections:
			protected=config['Protected']
			for key in protected:
				state=get_value_from_string(protected[key])
				if state==1:self.set_protected(key)
		return self

	def save(self, filename):
		config=ConfigParser()
		config['Template']={'name':str(self.get_name()), 'description':str(self.get_description())}
		config['Attributes']={}
		config['Constants']={}
		config['Private']={}
		config['Protected']={}
		for key in self.keys():
			config['Attributes'][key]=str(self.attrs[key])
			config['Constants'][key]=str(int(key in self.metadata.constants))
			config['Private'][key]=str(int(key in self.metadata.private))
			config['Protected'][key]=str(int(key in self.metadata.protected))
		config.write(open(filename, 'w'))