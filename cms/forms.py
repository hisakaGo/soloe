from django.forms import ModelForm
from cms.models import List


class ListForm(ModelForm):
    """リストのフォーム"""
    class Meta:
        model = List
        fields = ('title', 'creatorName',)
