from django import forms
from georama.maps.models import PublishedAsWms
from django.contrib.auth.models import Group, Permission
from django.contrib.admin import widgets

class GroupForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = [ ]

    groups = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=widgets.FilteredSelectMultiple(verbose_name="Groups", is_stacked=False)
    )

    def __init__(self, *args, **kwargs):
        # todo: make the permission and the form name variable, since we need it for all CRUD operations
        super().__init__(*args, **kwargs)

        permissions = kwargs["instance"].permissions
        permission_codenames = [p.codename for p in permissions]
        perm_read = permission_codenames[0]

        self.fields["groups"].queryset = Group.objects.all()
        self.fields["groups"].initial = Group.objects.filter(permissions__codename=perm_read)

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        instance.staff.set(self.cleaned_data['staff'])
        return instance