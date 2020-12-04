from rest_framework import serializers
from sample.models import Samplepeople

class SamplepeopleSerializers(serializers.ModelSerializer):

    class Meta:
        model = Samplepeople
        fields = ['id', 'name', 'kana', 'date_of_birth',]
