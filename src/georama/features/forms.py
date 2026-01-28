from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.models import Group, User

from georama.features.models import PublishedAsOgcApiFeatures


class PublishedAsOgcApiFeaturesAdminForm(forms.ModelForm):
    class Meta:
        model = PublishedAsOgcApiFeatures
        fields = "__all__"

    group_read_permission = forms.ModelMultipleChoiceField(
        required=False,
        queryset=None,
        widget=widgets.FilteredSelectMultiple(
            verbose_name="Group read permission", is_stacked=False
        ),
    )
    group_create_permission = forms.ModelMultipleChoiceField(
        required=False,
        queryset=None,
        widget=widgets.FilteredSelectMultiple(
            verbose_name="Group create permission", is_stacked=False
        ),
    )
    group_update_permission = forms.ModelMultipleChoiceField(
        required=False,
        queryset=None,
        widget=widgets.FilteredSelectMultiple(
            verbose_name="Group update permission", is_stacked=False
        ),
    )
    group_delete_permission = forms.ModelMultipleChoiceField(
        required=False,
        queryset=None,
        widget=widgets.FilteredSelectMultiple(
            verbose_name="Group delete permission", is_stacked=False
        ),
    )
    user_read_permission = forms.ModelMultipleChoiceField(
        required=False,
        queryset=None,
        widget=widgets.FilteredSelectMultiple(
            verbose_name="User read permission", is_stacked=False
        ),
    )
    user_create_permission = forms.ModelMultipleChoiceField(
        required=False,
        queryset=None,
        widget=widgets.FilteredSelectMultiple(
            verbose_name="User create permission", is_stacked=False
        ),
    )
    user_update_permission = forms.ModelMultipleChoiceField(
        required=False,
        queryset=None,
        widget=widgets.FilteredSelectMultiple(
            verbose_name="User update permission", is_stacked=False
        ),
    )
    user_delete_permission = forms.ModelMultipleChoiceField(
        required=False,
        queryset=None,
        widget=widgets.FilteredSelectMultiple(
            verbose_name="User delete permission", is_stacked=False
        ),
    )

    @staticmethod
    def get_first_match_partial_key(dictionary, partial_key) -> list[str]:
        matches = [k for k, v in dictionary.items() if partial_key in k]
        return matches if matches else None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # a dict to map the fields to the permissions
        perm_fields = {field: "" for field in self.fields if "permission" in field}
        if kwargs.get("instance"):

            # getting the permissions of the object
            permissions = kwargs["instance"].permissions
            permission_codenames = [p.codename for p in permissions]

            # mapping the permission to the field by part of the dict key
            # f.e. field "group_read_permission" to 'wms_read_bdb158db-3501-4563-be37-b2369ccf64e6'  # noqa: E501
            for perm in permission_codenames:
                permission_keys = (
                    PublishedAsOgcApiFeaturesAdminForm.get_first_match_partial_key(
                        perm_fields, perm.split("_")[1]
                    )
                )
                if len(permission_keys) > 0:
                    for p_key in permission_keys:
                        perm_fields[p_key] = perm

            # filling the field with the correct queryset and initialize it
            # with the data from the db
            for field, perm in perm_fields.items():
                if field == "column_permission":
                    pass
                elif perm.strip() != "":
                    if "group" in field:
                        self.fields[field].queryset = Group.objects.all()
                        self.fields[field].initial = Group.objects.filter(
                            permissions__codename=perm
                        )
                    elif "user" in field:
                        self.fields[field].queryset = User.objects.all().exclude(
                            is_superuser=True
                        )
                        self.fields[field].initial = User.objects.filter(
                            user_permissions__codename=perm
                        ).exclude(is_superuser=True)
                    else:
                        raise Exception(f"Unknown permission field: {field}")


class PublishedAsOgcApiFeaturesForm(forms.ModelForm):
    read_only_fields = []

    class Meta:
        model = PublishedAsOgcApiFeatures
        fields = [
            "name",
            "title",
            "description",
            "license",
            "fees",
            "access_constraints",
            "default_items",
            "max_items",
            "on_exceed",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Alle Felder read-only machen
        for read_only_field in self.read_only_fields:
            self.fields[read_only_field].disabled = True
