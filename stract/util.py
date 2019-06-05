from settheory import intersection, compliment, union, difference
from configparser import ConfigParser
from copy import copy
import inspect
import parser

def get_attributes(A):
	try:return vars(A)
	except TypeError:
		attrs={}
		members=inspect.getmembers(A)
		for member in members:
			key,value=member
			if not callable(value):
				attrs[key]=value
		return attrs

def get_attribute_keys(A):
	return list(get_attributes(A).keys())

def get_value_from_string(string):
	try:return eval(parser.expr(string).compile())
	except:return string

def jaccard_similarity(A,B):
	return len(intersection(A,B))/len(union(A,B))