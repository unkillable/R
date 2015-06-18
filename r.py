from threading import Thread
import time

class Container:
	def __init__(self):
		self.variables = {}
		self.dependencies = {}
	def add(self, name, variable):
		self.variables[name] = variable

C = Container()

class R:
	def __init__(self, value=0):
		self.name = str(id(self))
		C.add(self.name, value)
		self.value = C.variables[self.name]
	def __add__(self, b):
		C.variables[self.name] = self.value + b.value
		return C.variables[self.name]
	def set(self, value):
		a_ = C.variables[self.name]
		C.variables[self.name] = value
		self.value = C.variables[self.name]
		for variable, dependencies in C.dependencies.items():
			if self.name in dependencies:
				if type(a_) is str:
					C.variables[variable.name] = C.variables[variable.name].replace(a_, self.value)
				if type(a_) is int:
					C.variables[variable.name] = C.variables[variable.name] - a_ + self.value
				variable.value = C.variables[variable.name]
	def __le__(self, a):
		C.variables[self.name] = a[0].value+a[1].value
		self.value = C.variables[self.name]
		if not C.dependencies.has_key(self.name):
			C.dependencies[self] = []
		C.dependencies[self].append(a[0].name)
		C.dependencies[self].append(a[1].name)
		return self.value