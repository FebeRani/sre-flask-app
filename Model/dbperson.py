from config import db

class employee(db.Model):
    __tablename__='Employee'
    employeeno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),index=False,unique=False,nullable=False)
    city=db.Column(db.String(30),index=False,unique=False,nullable=False)
    desig=db.Column(db.String(30),index=False,unique=False,nullable=False)
    
    

    def __init__(self,employeeno,name,city,desig):
        self.employeeno=employeeno
        self.name=name
        self.city=city
        self.desig=desig
    
    def serialize(self):
        return {
            'sno':self.employeeno,
            'name':self.name,
            'city':self.city,
            'desig':self.desig,
            }
    
    def __repr__(self):
        return str(self.serialize())