Aca tenemos un sistema de logeo en donde solo tienes que ir a setting y colocar tu correo y clave y cada una de las url funcionara perfectamente.

    path('', views.Home.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/',views.LogoutView.as_view(), name='logout'),
    path('register/',views.RegisterView.as_view(), name='register'),
    path('password_change/',views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/',views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/',views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/',views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

Si por alguna razón el uso de Proxy model o la relación uno a uno no son suficientes para solventar tus necesidad, pues bien, no queda de otra que sobre escribir por completo el modelo User.

Para crear nuestro propio modelo User debemos apoyarnos de la clase AbstractUser o AbstractBaseUser.

Las principal diferencia entre estas dos clases son los atributos que poseen. Para la clase AbstractBaseUser únicamente tendremos 3 atributos:

id
password
last_login

Por otro lado, la clase AbstractUser poseerá los siguientes atributos:

username
first_name
last_name
email
password
groups
user_permissions
is_staff
is_active
is_superuser
last_login
date_joined
