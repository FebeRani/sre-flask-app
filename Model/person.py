class person:
    def __init__(self,employeeno,name,city,desig):
        self.employeeno=employeeno
        self.name=name
        self.city=city
        self.desig=desig

    def serialize(self):
        return {'sno':self.employeeno, 'name':self.name,'city':self.city,'desig':self.desig}

    def __repr__(self):
       return str(self.serialize())

