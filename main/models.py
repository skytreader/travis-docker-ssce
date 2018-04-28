from flask.ext.login import current_user, UserMixin
from main import db, main
from sqlalchemy.ext.declarative import declared_attr

def get_or_create(model, will_commit=False, **kwargs):
    """
    Get the record from the table represented by the given model which
    corresponds to **kwargs.

    In **kwargs, there is no need to specify the creator of the record; it
    does not make sense to ask for it given that it might've been created by
    another user. If it is given as a parameter, it will be ignored in the
    "get" part of this method.

    If the logic falls to the creation of a new record, the creator will be set
    as the current user. If no user is logged-in when this is called, the admin
    user is used.
    """
    given_creator = kwargs.pop("creator_id", None)
    instance = db.session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        if given_creator:
            kwargs["creator_id"] = given_creator
        else:
            admin = (db.session.query(User)
              .filter(User.username=='admin').first())
            kwargs["creator_id"] = admin

        instance = model(**kwargs)
        if will_commit:
            db.session.add(instance)
            db.session.commit()
        return instance


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp(),
      server_default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
      server_default=db.func.current_timestamp(),
      onupdate=db.func.current_timestamp())

class User(Base, UserMixin):
    __tablename__ = "users"
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    can_read = db.Column(db.Boolean, nullable=False, default=False,
      server_default=db.false())
    can_write = db.Column(db.Boolean, nullable=False, default=False,
      server_default=db.false())
    can_exec = db.Column(db.Boolean, nullable=False, default=False,
      server_default=db.false())
    is_user_active = db.Column(db.Boolean, nullable=False, default=True,
      server_default=db.true())

    def __init__(self, **kwargs):
        self.username = kwargs["username"]
        self.password = kwargs["password"]
        self.can_read = kwargs.get("can_read", False)
        self.can_write = kwargs.get("can_write", False)
        self.can_exec = kwargs.get("can_exec", False)
        self.is_user_active = kwargs.get("is_user_active", True)

    def __repr__(self):
        return self.username
    
    def get_id(self):
        return self.id


class UserTaggedBase(Base):
    """
    Those that will extend this class may take the convention that, upon creation,
    the last_modifier is the same as the creator.
    """
    __abstract__ = True

    @declared_attr
    def creator_id(self):
        return db.Column(db.Integer, db.ForeignKey("users.id"))

    @declared_attr
    def last_modifier_id(self):
        return db.Column(db.Integer, db.ForeignKey("users.id"))
