from flask.ext.wtf import Form
from wtforms import HiddenField, PasswordField, TextField
from wtforms.validators import Length, Required


class LoginForm(Form):
    main_username = TextField("Username",
      [Required(message="Enter your username"), Length(max=50)])
    main_password = PasswordField("Password", [Required(message="Enter your password")])
    
    def __str__(self):
        return str(self.main_username.data) + " // " + str(self.main_password.data)
