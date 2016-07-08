from django import forms


class ChoiceGenericForeignKey(forms.NumberInput):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Media:
        js = ('js/generic_choice.js',)