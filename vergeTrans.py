from pycparser import c_paresr, c_ast
ast = pycparser.parse_file('switchStatements.vc', use_cpp=True)

class FuncCallVisitor(c_ast.NodeVisitor):
	    def __init__(self, funcname='uaoeu'):
		self.stat = {}
		self.statobject = {}
	    def visit_FuncDef(self, node):
		stat = node.decl.name

		from StringIO import StringIO
		mys = StringIO()
		import re

		switch = node.body.children()[1][1]
		cases = [(o.children()[0][1].name, o.children()[1][1].children()[1][1]) for _, o in switch.children()[1][1].children()]

		for name, case in cases:
			if name not in self.statobject:
				self.statobject[name] = {}
			statob = self.statobject[name]
			if hasattr(case, 'value'):
				statob[stat] = case.value
			else:
				parameters = [arg[1].value for arg in case.children()[1][1].children()]
				statob[stat] = case.children()[0][1].name+'('+(', '.join(parameters))+')'

				
v = FuncCallVisitor()
v.visit(ast)