from rest_framework_json_api import serializers

from .models import Pulse


class PulseSerializer(serializers.ModelSerializer):
    """
    Serailiser for a Pulse.

    """
    class Meta:
        model = Pulse
        fields = '__all__'