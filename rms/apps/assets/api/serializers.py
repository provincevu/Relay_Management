from rest_framework import serializers

from rms.apps.assets.models import Bay, Relay, Station, VOLTAGE_LEVEL_CATALOG_CODE
from rms.apps.catalog.models import CatalogItem
from rms.apps.identity.models import Organization


class StationListParamsSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True, max_length=100)
    organization = serializers.IntegerField(required=False, min_value=1)
    voltage = serializers.IntegerField(required=False, min_value=1)

    def validate_organization(self, value):
        if not Organization.objects.filter(pk=value, is_active=True).exists():
            raise serializers.ValidationError("Organization does not exist or is inactive.")
        return value

    def validate_voltage(self, value):
        if not CatalogItem.objects.filter(
            pk=value,
            catalog_type__code=VOLTAGE_LEVEL_CATALOG_CODE,
        ).exists():
            raise serializers.ValidationError("Voltage level does not exist.")
        return value


class StationTreeParamsSerializer(serializers.Serializer):
    depth = serializers.ChoiceField(
        choices=["bays", "relays"],
        required=False,
        default="relays",
    )
    q = serializers.CharField(required=False, allow_blank=True, max_length=100)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=100)


class OrganizationSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["id", "code", "name"]


class CatalogItemSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogItem
        fields = ["id", "code", "name"]


class StationListSerializer(serializers.ModelSerializer):
    organization = OrganizationSummarySerializer(read_only=True)
    voltage_level = CatalogItemSummarySerializer(read_only=True, allow_null=True)

    class Meta:
        model = Station
        fields = [
            "id",
            "code",
            "name",
            "location",
            "organization",
            "voltage_level",
            "commissioned_at",
            "installed_at",
            "is_active",
        ]


class RelayTreeSerializer(serializers.ModelSerializer):
    manufacturer = CatalogItemSummarySerializer(read_only=True, allow_null=True)

    class Meta:
        model = Relay
        fields = ["id", "code", "name", "model_name", "manufacturer", "is_active"]


class BayTreeSerializer(serializers.ModelSerializer):
    relays = RelayTreeSerializer(source="active_relays", many=True, read_only=True)

    class Meta:
        model = Bay
        fields = [
            "id",
            "code",
            "name",
            "rated_voltage",
            "rated_current",
            "legacy_sdm",
            "is_active",
            "relays",
        ]

    def __init__(self, *args, **kwargs):
        """Ẩn danh sách Relay khi client chỉ yêu cầu độ sâu Bay."""
        super().__init__(*args, **kwargs)
        if self.context.get("depth") == "bays":
            self.fields.pop("relays")
