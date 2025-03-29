from django import forms
from georama.maps.models import PublishedAsWms
from django.contrib.auth.models import Group, User
from django.contrib.admin import widgets


class PublishedAsWmsForm(forms.ModelForm):
    class Meta:
        model = PublishedAsWms
        fields = '__all__'

    group_read_permission = forms.ModelMultipleChoiceField(
        required=False,
        queryset=None,
        widget=widgets.FilteredSelectMultiple(verbose_name="Group read permission", is_stacked=False)
    )

    user_read_permission = forms.ModelMultipleChoiceField(
        required=False,
        queryset=None,
        widget=widgets.FilteredSelectMultiple(verbose_name="User read permission", is_stacked=False)
    )

    @staticmethod
    def get_first_match_partial_key(dictionary, partial_key):
        matches = [k for k, v in dictionary.items() if partial_key in k]
        return matches[0] if matches else None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # get the read permission, should get only one permission for PublishedAsWms
        permissions = self.instance.permissions
        permission_read = [p.codename for p in permissions][0]

        # filling the field with the correct queryset and initialize it with the data from the db

        self.fields['group_read_permission'].queryset = Group.objects.all()
        self.fields['group_read_permission'].initial = Group.objects.filter(permissions__codename=permission_read)

        self.fields['user_read_permission'].queryset = User.objects.all().exclude(is_superuser=True)
        self.fields['user_read_permission'].initial = User.objects.filter(
            user_permissions__codename=permission_read).exclude(is_superuser=True)
