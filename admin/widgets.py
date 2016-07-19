from django import forms


class ChoiceGenericForeignKey(forms.NumberInput):

    class Media:
        js = ('js/generic_choice.js',)


class LeftRight(forms.Select):

    class Media:
        js = ('js/left_right.js',)