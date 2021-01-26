from django import forms
from .models import MyUser
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    #Inherit to get password1 and password2
    class Meta:
        model = MyUser
        fields = ('first_name','last_name','email','gender','birth_date')

    def clean(self):
        data = self.data
        users = MyUser.objects.all()

        if data['email'] in [user.email for user in users]:
            self.add_error('email','Ya existe un usuario con el correo!')
        return super().clean()

    def sign_in(self, email, first_name, last_name, gender, birth_date, password):
        MyUser.objects.create_user(email,first_name,last_name,gender,birth_date,password)
        self.send_mail()
        return True
    
    def send_mail(self):
        return print("Sending email to user....")


