from django.core.management.base import BaseCommand, CommandError

from rms.apps.assets.models import Station
from rms.apps.identity.models import RoleGrant, UserProfile


class Command(BaseCommand):
    help = "Check that scalar Station references point to existing Station rows."

    def add_arguments(self, parser):
        parser.add_argument(
            "--database",
            default="default",
            help="Database alias to inspect.",
        )
        parser.add_argument(
            "--max-details",
            type=int,
            default=50,
            help="Maximum orphan records to display for each reference type.",
        )

    def handle(self, *args, **options):
        """Dò soát ID trạm không có bản ghi tương ứng mà không cập nhật dữ liệu."""
        database = options["database"]
        max_details = options["max_details"]
        if max_details < 0:
            raise CommandError("--max-details must be zero or a positive number.")

        station_ids = Station.objects.using(database).order_by().values("pk")
        orphan_profiles = (
            UserProfile.objects.using(database)
            .filter(home_station_id__isnull=False)
            .exclude(home_station_id__in=station_ids)
            .order_by("pk")
        )
        orphan_grants = (
            RoleGrant.objects.using(database)
            .filter(station_id__isnull=False)
            .exclude(station_id__in=station_ids)
            .order_by("pk")
        )

        profile_count = orphan_profiles.count()
        grant_count = orphan_grants.count()
        self.stdout.write(f"Database: {database}")
        self.stdout.write(f"UserProfile.home_station_id orphans: {profile_count}")
        self.stdout.write(f"RoleGrant.station_id orphans: {grant_count}")

        profile_rows = orphan_profiles.values_list(
            "pk", "user__username", "home_station_id"
        )[:max_details]
        for profile in profile_rows:
            self.stdout.write(
                f"  UserProfile pk={profile[0]} user={profile[1]} station_id={profile[2]}"
            )
        grant_rows = orphan_grants.values_list(
            "pk", "user__username", "role_code", "station_id"
        )[:max_details]
        for grant in grant_rows:
            self.stdout.write(
                f"  RoleGrant pk={grant[0]} user={grant[1]} role={grant[2]} station_id={grant[3]}"
            )

        total_orphans = profile_count + grant_count
        if total_orphans:
            raise CommandError(
                f"Found {total_orphans} stale Station reference(s). "
                "Review the listed records; no data was changed."
            )

        self.stdout.write(self.style.SUCCESS("All Station references point to existing rows."))
