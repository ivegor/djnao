from django import forms


class ChoiceGenericForeignKey(forms.NumberInput):

    class Media:
        js = ('js/generic_choice.js',)


class LeftRight(forms.NumberInput):

    class Media:
        js = ('js/left_right.js',)