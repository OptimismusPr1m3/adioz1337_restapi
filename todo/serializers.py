from django.contrib.auth.models import Group, User
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from todo.models import Todo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email'] # , 'user'

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    # user = CurrentUserDefault()
    # user = UserSerializer()
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Todo
        fields = ['id','title', 'description', 'created_at', 'user', 'time_passed'] #'user' # time_passed wird im todo model aufgerufen und da kann man dann iwas returnen lassen -> alles mögliche