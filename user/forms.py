from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import User, Customer, Supplier

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Button
from crispy_forms.bootstrap import FormActions

class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	submit_button = Button('Sign Up', 'Sign Up', css_class='btn btn-outline-info', type='submit')
	submit_button.input_type = 'submit'

	helper = FormHelper()
	helper.form_tag = False
	helper.disable_csrf = True
	helper.layout = Layout(
		Fieldset('Account Details', 
			Field('email', wrapper_class='m-2 col-5', placeholder="Please Enter Your Email Address", autocomplete="false"),
			Field('phone', wrapper_class='m-2 col-5', placeholder='Enter Your 10 Digit Phone Number'),
			Field('password1', wrapper_class='m-2 col-5', placeholder='Enter Password'),
			Field('password2', wrapper_class='m-2 col-5', placeholder='Verify Password'),
			css_class='flex-wrap flex-row',
			style='display: flex'
		),
		Fieldset('Bank Details (Optional)', 
			Field('acct_no', wrapper_class='m-2 col-5'),
			Field('bank_name', wrapper_class='m-2 col-5'),
			Field('swift_code', wrapper_class='m-2 col-5'),
			Field('routing_no', wrapper_class='m-2 col-5'),
			css_class='flex-wrap flex-row',
			style='display: flex'
		),
		FormActions(
			submit_button
		)
	)

	class Meta:
		model = User
		fields = (
			"email",
			"phone",
			"password1",
			"password2",
			"acct_no",
			"bank_name",
			"swift_code",
			"routing_no",
			)
	
	def save(self, commit=True):
		user = super(CustomUserCreationForm, self).save(commit=False)
		user.phone = self.cleaned_data.get("phone")
		user.acct_no = self.cleaned_data.get("acct_no")
		user.bank_name = self.cleaned_data.get("bank_name")
		user.swift_code = self.cleaned_data.get("swift_code")
		user.routing_no = self.cleaned_data.get("routing_no")

		if commit:
			user.save()
		return user

class CustomerDetailsForm(forms.ModelForm):
	fname = forms.CharField(label='First Name', required=True)
	lname = forms.CharField(label='Last Name', required=True)

	helper = FormHelper()
	helper.form_tag = False
	helper.layout = Layout(
		Fieldset('Personal Details',
			Field('fname', required='true', wrapper_class='m-2 col-5', placeholder='First Name'),
			Field('lname', required='true', wrapper_class='m-2 col-5', placeholder='Last Name'),
			css_class='flex-wrap flex-row',
			style='display: flex'
		)
	)
	
	class Meta:
		model = Customer
		fields = (
			"fname",
			"lname",
		)

	def save(self, user, commit=True):
		customer = super(CustomerDetailsForm, self).save(commit=False)
		customer.userid = user
		customer.fname = self.cleaned_data.get('fname')
		customer.lname = self.cleaned_data.get('lname')

		if commit:
			customer.save()
		return customer

class SupplierDetailsForm(forms.ModelForm):
	helper = FormHelper()
	helper.form_tag = False
	
	class Meta:
		model = Supplier
		fields = tuple()
	
	def save(self, user, commit=True):
		supplier = super(SupplierDetailsForm, self).save(commit=False)
		supplier.userid = user

		if commit:
			supplier.save()
		return supplier

class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = User
		fields = ("email", "password", "phone", "acct_no", "bank_name", "swift_code", "routing_no", "is_admin")