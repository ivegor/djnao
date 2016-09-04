from datetime import timedelta, datetime, date
from time import strptime

from django.utils.timezone import now
from rest_framework import serializers

from staff.models import Staff, AdditionalInformation


class Additional(serializers.ModelSerializer):
    cur_exp = serializers.SerializerMethodField()

    def get_cur_exp(self, obj):
        diff = date.today() - obj.cur_exp
        years = diff.days//365
        months = (diff.days - years * 365)//30
        return '%s %s' % (data_str(years, 'year'), data_str(months, 'month'))

    class Meta:
        model = AdditionalInformation
        exclude = ('id',)


class StaffSerializer(serializers.ModelSerializer):
    additionalinformation = Additional(many=False)

    class Meta:
        model = Staff


def data_str(amount, type):
    if not amount:
        return ''
    if type == 'year':
        if amount == 1:
            return '1 год'
        elif amount < 5:
            return '%s года' % amount
        else:
            return '%s лет' % amount
    elif type == 'month':
        if amount == 1:
            return '1 месяц'
        elif amount < 5:
            return '%s месяца' % amount
        else:
            return '%s месяцев' % amount