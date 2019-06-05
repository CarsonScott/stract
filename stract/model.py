from .util import *
from .structure import Structure

class Model(Structure):

	def __init__(self, **kwargs):
		super().__init__()
		self.setup(kwargs)

	def union(self, other):
		if isinstance(other, Model):
			attributes=other.attributes()
		else:attributes=get_attributes(other)
		return union(self.attributes(), attributes)

	def intersection(self, other):
		if isinstance(other, Model):
			attributes=other.attributes()
		else:attributes=get_attributes(other)
		return intersection(self.attributes(), attributes)

	def compliment(self, other):
		if isinstance(other, Model):
			attributes=other.attributes()
		else:attributes=get_attributes(other)
		return compliment(self.attributes(), attributes)

	def difference(self, other):
		if isinstance(other, Model):
			attributes=other.attributes()
		else:attributes=get_attributes(other)
		return difference(self.attributes(), attributes)
	
	def similarity(self, other):
		if isinstance(other, Model):
			keys=other.keys()
		else:keys=get_attribute_keys()
		return jaccard_similarity(self.keys(), keys)
	
	def keys(self):
		keys=[]
		for key in list(vars(self).keys()): 
			if key not in self.metadata.private:
				keys.append(key)
		return keys

	def attributes(self):
		attrs={}
		for key in self.keys():
			attrs[key]=self.get(key)
		return attrs

	def get(self, key):
		if key in self.metadata.private:
			raise Warning('attribute \''+str(key)+'\' couldn\'t be retrieved because it is set to private.\n')
		elif key in self.metadata.protected:
			raise Warning('attribute \''+str(key)+'\' couldn\'t be retrieved because it is set to protected.\n')
		else:return getattr(self, key)
	
	def set(self, key, value):
		if key in self.metadata.constants:
			raise Warning('attribute \''+str(key)+'\' couldn\'t be reassigned because it is set to constant.\n')
		else:setattr(self, key, value)

	def copy(self):
		return copy(self)

	def setup(self, kwargs):
		for key in kwargs:
			self.set(key, kwargs[key])
		return self

	def merge(self, source):
		output=self.copy()
		attr=get_attributes(source)
		keys=get_attribute_keys(source)
		conflicts=self.intersection(source)
		for key in compliment(conflicts, keys):
			output.set(key, attr[key])
		return output
	
	def extract(self, keys):
		output=Model()
		for key in keys:
			if key not in self.metadata.private:
				output.set(key, self.get(key))
		self.transfer_metadata(output)
		return output

	def compare(self, other):
		output={}
		keys=self.intersection(other)
		for key in keys:
			if isinstance(other, Model):
				value=other.get(key)
			else:value=getattr(other,key)
			values=(self.get(key), value)
			output[key]=values
		return output