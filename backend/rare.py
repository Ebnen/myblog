from routes import session
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String,ForeignKey,Text,func,DateTime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.declarative import declarative_base
from data import session
from routes import log_direct, UserMixin




base = declarative_base()



@log_direct.user_loader
def loadUser(Id):
    return session.query(User).get(int(Id))
 
class User(base, UserMixin):
    __tablename__ = "user"
    id = Column(Integer, nullable=False, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    username = Column(String(20), nullable=False, unique=True )
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    image= Column(String(200),nullable=False, default= "default.jpg")
    
    
    posts = relationship("Post", back_populates='user')
    
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)

    
    
class Post(base):
    __tablename__ = "post"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id') ,nullable=False)
    
    user = relationship("User", back_populates='posts')
    
    
    
    




