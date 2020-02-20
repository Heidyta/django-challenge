from rest_framework import mixins, viewsets
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer


from . import models
from . import serializers


class AccountViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    """
        API endpoint that allows accounts to be viewed.

        list:
        Return all the accounts available.

        create:
        Create an account.

        retrieve:
        Return a given account.
    """
    model = models.Account
    serializer_class = serializers.AccountSerializer
    queryset = models.Account.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'update':
            return serializers.AccountUpdateSerializer
        return serializers.AccountSerializer

class FuzzyView():
    def _fuzzy_filter_x(self, x):
        if x%15==0:
            return "FizzBuzz"
        elif x%3==0:
            return "Fizz"
        elif x%5==0:
            return "Buzz"
        return x
    
    def fuzzy(self, request):
        x = int(request.GET.get('x', 100))
        return HttpResponse(JSONRenderer().render(
                           {'x':x, 'fizzbuzz':[self._fuzzy_filter_x(i) for i in range(1, x + 1)]}))

