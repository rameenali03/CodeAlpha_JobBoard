from rest_framework import serializers
from .models import Application
from notifications.models import Notification


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            "id",
            "candidate",
            "job",
            "resume",
            "status",
            "applied_at",
        ]
        read_only_fields = ["applied_at"]

    def update(self, instance, validated_data):
        old_status = instance.status
        new_status = validated_data.get("status", old_status)

        instance = super().update(instance, validated_data)

        if old_status != new_status:
            Notification.objects.create(
                user=instance.candidate.user,
                message=(
                    f"Your application for '{instance.job.title}' "
                    f"has been updated to '{new_status}'."
                ),
            )

        return instance