class reverse:
    def __init__(self,name):
	self.name=name
	fd=open('self.name','w')
	txt="""ashok kumar raju\nb.Tech\nsvec\ntirupathi"""
	fd.write(txt)
	fd.close()
class print1(reverse):
    def method(self):
	fd=open('self.name','r')
	data=fd.read()
	print data
	fd.close()
	asd=list(data)
	asd.reverse()
	str=''
	for i in asd:
	    str=str+i
	print str
a=print1('aa.txt')
a.method()