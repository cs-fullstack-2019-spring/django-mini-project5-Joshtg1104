from django import forms
from .models import RecipeModel, LoginModel
from django.contrib.auth.models import User
from datetime import date


class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        exclude = ["userForeignKey"]

        def clean_password2(self):
            password1Data = self.cleaned_data.get("password1")
            password2Data = self.cleaned_data.get("password2")
            print(password2Data)
            print(password1Data)
            if str(password1Data) != str(password2Data):
                raise forms.ValidationError("Does not Match")
            return password1Data
        # page still gets unique error and breaks if you enter a username the is already used
        # if you use an unused username then it is ok
        def clean_username(self):
            usernameData = self.cleaned_data["username"]
            if User.objects.filter(username=usernameData).exists():
                return usernameData


class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        exclude = ["recipeForeignKey"]

        def clean_recipe_name(self):
            cleanRecipeNameData = self.cleaned_data["recipe_name"]

            if cleanRecipeNameData == None:
                raise forms.ValidationError("Name the recipe")

                return cleanRecipeNameData

        def clean_date_created(self):
            cleanDateCreatedData = self.cleaned_data["date_created"]

            if cleanDateCreatedData == None:
                raise forms.ValidationError("No date was entered")

            if cleanDateCreatedData > date.today():
                raise forms.ValidationError("Future date is not valid")

                return cleanDateCreatedData

        def clean_recipe_creator(self):
            cleanRecipeCreatorData = self.cleaned_data["recipe_creator"]

            if cleanRecipeCreatorData == None:
                raise forms.ValidationError("No creator was named")

                return cleanRecipeCreatorData
