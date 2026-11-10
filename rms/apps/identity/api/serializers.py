from rest_framework import serializers

from rms.apps.identity.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["id", "code", "name", "organization_type", "parent", "is_active"]
        read_only_fields = ["id", "is_active"]


class RoleGrantSerializer(serializers.Serializer):
    role_code = serializers.CharField()
    scope_type = serializers.CharField()
    organization_id = serializers.IntegerField(allow_null=True)
    station_id = serializers.CharField(allow_null=True)
    starts_at = serializers.DateTimeField(allow_null=True)
    ends_at = serializers.DateTimeField(allow_null=True)


class UserProfileSerializer(serializers.Serializer):
    organization_id = serializers.IntegerField(allow_null=True)
    organization_name = serializers.CharField(allow_null=True)
    home_station_id = serializers.CharField(allow_null=True)
    phone_number = serializers.CharField()
