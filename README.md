# django-challenge-solution
This repository contains a solution of a challenge for a Django backend developer position. You can found the challenge [here](https://github.com/swagup-com/django-challenge)

There are the challenge tasks and basic ideas to solve it:

>1- A way to filter accounts by `shipping_country` in the admin interface

To complete this task I added to `AccountAdmin` class the follow line

python
list_filter = ['shipping_country']


This is a `Django-Admin` feature that allow make filters in a specific model by some of their fields(in this case only `shipping_country`).

In the admin interface of the model(`Account`) you will see the filter:
`http://localhost:8000/admin/accounts/account/`

>2- Introduce a new `PUT` endpoint at `/api/v1/accounts/{id}/` that receives a JSON body containing `phone`, `shipping_address1`, `shipping_address2`, `shipping_city`, `shipping_state`, `shipping_zip`,
`shipping_country`. The feature should update the existing record and return a JSON body representing the new state of the account item.

To solve this issue, firstly, a new `Serializer` class was created to update methods in `Account`. This new serializer needs to make the `name` field `ReadOnly` to don't check the validation in the `request` body. Also, I overried the `update` method in the new `Serializer` just to update the specified fields in the challenge. Finally, in the `AccountViewSet`, was added `mixins.UpdateModelMixin` based-class to allow to make updates in the entity. Moreover, `get_serializer_class` method was overwritten to use the new `Serializer` if the action is a `update` one.


>3-write a view responding to a `GET` to path `/api/v1/fizz-buzz/?x=25` that will write the results of running FizzBuzz program for numbers from 1 to x.

In this case, a new `View` was implemented with a simple algorithm to get the challenge request. The view is very simple, just take the `querystring` param and execute the `fuzzy` algorithm. Also the urls was changes (adding a new one) to allow make this request.

You can see the action to solve this issue below. For more details, see the code.
python
def fuzzy(self, request):
    x = int(request.GET.get('x', 100))
    return HttpResponse(JSONRenderer().render({
        'x': x,
        'fizzbuzz': [self._fuzzy_filter_x(number) for number in range(1, x+1)]
    }))


In the lacks of tests, some tests were added to `tests.py` file in `accounts`. Firstly, in the `setUp` method you will see the creations of two simple accounts to make the correspond test.

The first test check the `endpoint` to get all accounts created. Also, a update test was implemented to test the put feature with the first account storage. Finally, two very similar tests were implemented to test `fizz-buzz`, the main diference is, one of them make the test with a querystring param and the other one without it. All tests ran successfully.

Solve the challenge was a very good and enjoable experience and I really spect good news.

Thanks you.