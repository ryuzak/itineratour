class UserForm(ModelForm):
    
    first_name = forms.CharField(
        label = 'Nombre',
        #error_messages = {'required':'cmapo no valido'},
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )
    last_name = forms.CharField(
        label = 'Apellidos', 
        #error_messages = {'required':'Enter a valid phone number'},
        widget = forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    email = forms.EmailField(
        label = 'Correo',
        #error_messages = {'required':'Este campo es requerido', 'invalid':'correo mal'},
        widget = forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    picture = forms.ImageField(
        label = 'Foto',
        required = False,
        error_messages = {'invalid': "Solo archivos de imagen"},
        widget = forms.FileInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )
    
    phone = forms.CharField(
        label = 'Teléfono', 
        #error_messages = {'required':'Enter a valid phone number'},
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'id' : 'mask_phone'
            }
        )
    )
    
    status = forms.MultipleChoiceField(
        label = 'Status',
        required = False,
        widget = forms.CheckboxSelectMultiple(
            choices=ut.STATUS_CHOICES,
            attrs={
                'class': 'make-switch',
                'checked' : 'true',
                'data-size' : 'small'
            }
        )
    )
    
    #-- 
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(UserForm, self).__init__(*args, **kwargs)
                                       
    def clean_email(self):
        email = self.cleaned_data['email']
        #print email

        #usermail = User.objects.filter(email__iexact=email).exclude(email__iexact=email)
        try:
            usermail = User.objects.get(email=email, status=1)
            raise forms.ValidationError('Este correo ya está registrado')
        except Exception as e:
            pass
            
        return email
        
    class Meta:
        model = User
        fields = ('first_name','last_name','email', 'phone', 'picture', 'status')
 