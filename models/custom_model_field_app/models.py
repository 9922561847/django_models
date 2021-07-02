import uuid

from django.db import models

from django.forms.widgets import SelectMultiple

class Books(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Select2Field(models.Field):
    description = "custom model field is for select2 "
    #select2_id = models.UUIDField(id = "id_select2")
    def __init__(self, *args, **kwargs):
        #self.choices = choices
        super(Select2Field, self).__init__(*args, **kwargs)

    def to_python(self, value):
        """
        purpose of this function is to make sure every time instance of field is assigned value, value may be assigned to the field, 
        need to ensure that it will be of the correct datatype
        """
        if not value:
            return []
        elif not isinstance(value, (list, tuple)):
            raise ValidationError(self.error_messages['invalid_list'], code='invalid_list')
        return [str(val) for val in value]
    
    def validate(self, value):
        """Validate that the input is a list or tuple."""
        if self.required and not value:
            raise ValidationError(self.error_messages['required'], code='required')
        # Validate that each value in the value list is in self.choices.
        for val in value:
            if not self.valid_value(val):
                raise ValidationError(
                    self.error_messages['invalid_choice'],
                    code='invalid_choice',
                    params={'value': val},
    
                )

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs
# In the model:

class Person(models.Model):

    my_field = Select2Field()