from rest_framework import serializers

from . import models


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = '__all__'

class AccountUpdateSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField()
    class Meta:
        model = models.Account
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.phone = validated_data.get('phone', instance.phone)
        instance.shipping_address1 = validated_data.get("shipping_address1" ,instance.shipping_address1)
        instance.shipping_address2 = validated_data.get("shipping_address2" ,instance.shipping_address2)
        instance.shipping_city = validated_data.get("shipping_city", instance.shipping_city)
        instance.shipping_state = validated_data.get("shipping_state", instance.shipping_state)
        instance.shipping_zip = validated_data.get("shipping_zip", instance.shipping_zip)
        instance.shipping_country = validated_data.get("shipping_country", instance.shipping_country)
        instance.save()

        return instance