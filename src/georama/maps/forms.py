from django import forms
from georama.maps.models import PublishedAsWms
from django.contrib.auth.models import Group, Permission
from django.contrib.admin import widgets

class GroupForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = [ ]

    read_permission = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=widgets.FilteredSelectMultiple(verbose_name="Read permission", is_stacked=False)
    )
    write_permission = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=widgets.FilteredSelectMultiple(verbose_name="write_permission", is_stacked=False)
    )
    update_permission = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=widgets.FilteredSelectMultiple(verbose_name="Update permission", is_stacked=False)
    )
    delete_permission = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=widgets.FilteredSelectMultiple(verbose_name="Delete permission", is_stacked=False)
    )

    @staticmethod
    def get_first_match_partial_key(dictionary, partial_key):
        matches = [k for k, v in dictionary.items() if partial_key in k]
        return matches[0] if matches else None

    def __init__(self, *args, **kwargs):
        # todo: make the permission and the form name variable, since we need it for all CRUD operations
        super().__init__(*args, **kwargs)


        # a dict to map the fields to the permissions
        perm_fields = {field: "" for field in self.fields}

        # getting the permissions of the object
        permissions = kwargs["instance"].permissions
        permission_codenames = [p.codename for p in permissions]

        # mapping the permission to the field by part of the dict key
        # f.e. field "write_permission" to 'wms_read_bdb158db-3501-4563-be37-b2369ccf64e6'
        for perm in permission_codenames:
            pf = GroupForm.get_first_match_partial_key(perm_fields, perm.split("_")[1])
            perm_fields[pf] = perm


        # filling the field with the correct queryset and initialize it with the data from the db
        for field, perm in perm_fields.items():
            if perm.strip() != "":
                self.fields[field].queryset = Group.objects.all()
                self.fields[field].initial = Group.objects.filter(permissions__codename=perm)
            else:
                # if there is no permission, we don't show the field.
                # f.e. in case of raster layer no write, delete and update permissions exist, thus we remove the fields
                self.fields.pop(field)


    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        instance.staff.set(self.cleaned_data['staff'])

        # todo: !!!!!!!!!!!!!!!!!!!!

        return instance