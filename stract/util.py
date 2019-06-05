from configparser import ConfigParser
from copy import copy
import inspect
import parser

def union(A, B):
    Y = []
    for x in A+B:
        if x not in Y:
            Y.append(x)
    return Y

def intersection(A, B):
    Y = []
    for a in A:
        if a in B:
            Y.append(a)
    return Y

def compliment(A, B):
    Y = []
    for b in B:
        if b not in A:
            Y.append(b)
    return Y

def difference(A, B):
    Y = []
    for a in A:
        if a not in B:
            Y.append(a)
    for b in B:
        if b not in A:
            Y.append(b)
    return Y

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