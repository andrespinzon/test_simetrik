from rest_framework import serializers


class TransactionSerializer(serializers.Serializer):
    transaction_id = serializers.CharField()
    transaction_date = serializers.DateField()
    transaction_amount = serializers.IntegerField()
    client_id = serializers.IntegerField()
    client_name = serializers.CharField()
