from django.db import transaction

from rms.apps.audit.application.events import record_event
from rms.apps.identity.models import Organization


@transaction.atomic
def create_organization(*, actor, data, request_id):
    """Tạo đơn vị và ghi audit/outbox trong cùng transaction."""
    organization = Organization.objects.create(**data)
    record_event(
        actor=actor,
        action="identity.organization.created",
        target_type="Organization",
        target_id=str(organization.pk),
        after={
            "code": organization.code,
            "name": organization.name,
            "organization_type": organization.organization_type,
            "parent_id": organization.parent_id,
        },
        request_id=request_id,
        event_type="identity.organization.created",
    )
    return organization
