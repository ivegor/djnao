from django import forms


class ChoiceGenericForeignKey(forms.NumberInput):
    class Media:
        css = {'generic_choice': ('generic_choice.css',)}
        js = ('js/jquery-1.9.1.min.js', 'js/generic_choice.js')