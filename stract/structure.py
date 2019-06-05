from .util import *
from .metadata import Metadata

class Structure:

	def __init__(self):
		self.metadata=Metadata()
		self.set_private('metadata')

	def set_name(self, name):
		self.metadata.name=name

	def set_description(self, description):
		self.metadata.description=description

	def get_name(self):
		return self.metadata.name

	def get_description(self):
		return self.metadata.description

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
	
	def transfer_metadata(self, other):
		for key in self.metadata.constants:
			if key in other.keys():
				other.set_constant(key)
		for key in self.metadata.private:
			if key in other.keys():
				other.set_private(key)
		for key in self.metadata.protected:
			if key in other.keys():
				other.set_protected(key)
