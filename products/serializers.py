from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "shop",
            "price",
            "sku",
            "description",
            "location",
            "discount",
            "category",
            "stock",
            "is_available",
            "picture",
              "is_delete",
            "_links"
        ]

    def get__links(self, obj):
        request = self.context.get("request")

        return [
            {
                "rel": "self",
                "href": reverse(
                    "product-list",
                    request=request
                ),
                "action": "POST",
                "types": [
                    "application/json"
                ]
            },
            {
                "rel": "self",
                "href": reverse(
                    "product-detail",
                    kwargs={"pk": obj.pk},
                    request=request
                ),
                "action": "GET",
                "types": [
                    "application/json"
                ]
            },
            {
                "rel": "self",
                "href": reverse(
                    "product-detail",
                    kwargs={"pk": obj.pk},
                    request=request
                ),
                "action": "PUT",
                "types": [
                    "application/json"
                ]
            },
            {
                "rel": "self",
                "href": reverse(
                    "product-detail",
                    kwargs={"pk": obj.pk},
                    request=request
                ),
                "action": "DELETE",
                "types": [
                    "application/json"
                ]
            }
        ]

    def validate_discount(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Discount cannot be negative."
            )
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Price cannot be negative."
            )
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Stock cannot be negative."
            )
        return value

    def validate_picture(self, value):
        if not value.startswith(("http://", "https://")):
            raise serializers.ValidationError(
                "Picture must be a valid URL."
            )
        return value

    def validate_category(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Category cannot be empty."
            )
        return value

    def validate_shop(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Shop cannot be empty."
            )
        return value

    def validate_location(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Location cannot be empty."
            )
        return value