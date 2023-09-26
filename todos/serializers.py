from .models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'company', 'about', 'process', 'remarks', 'companyBenefits', 'questionsToAsk', 'questionsToAnswer','technicalSkills', 'softSkills', 'cultureFit', 'helpfulLinks')