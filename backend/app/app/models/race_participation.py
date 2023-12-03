from typing import Optional, TYPE_CHECKING
from datetime import datetime
from enum import Enum

from sqlmodel import SQLModel, Field, Relationship, CheckConstraint

if TYPE_CHECKING:
    from .rider import Rider
    from .race import Race
    from .bike import Bike


class RaceParticipationStatus(Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"


class RaceParticipation(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    status: RaceParticipationStatus = Field(sa_column_args=(
        CheckConstraint("status in ('pending', 'approved', 'rejected')", name="race_participation_status_enum"),
    ), index=True)
    place_generated: Optional[int] = Field(default=None, sa_column_args=(
        CheckConstraint("place_generated > 0", name="race_participation_place_generated_positive"),
    ))
    place_assigned: Optional[int] = Field(default=None, sa_column_args=(
        CheckConstraint("place_assigned > 0", name="race_participation_place_assigned_positive"),
    ))
    ride_start_timestamp: Optional[datetime] = Field(default=None)
    ride_end_timestamp: Optional[datetime] = Field(default=None, sa_column_args=(
        CheckConstraint("ride_end_timestamp > ride_start_timestamp", name="race_participation_timestamp_order"),
    ))
    ride_gpx_file: Optional[str] = Field(default=None, max_length=256, sa_column_args=(
        CheckConstraint("ride_end_timestamp IS NOT NULL", name="race_participation_gpx_requires_timestamp"),
    ))

    rider_id: int = Field(foreign_key="rider.id", index=True)
    rider: "Rider" = Relationship(back_populates="race_participations")
    race_id: int = Field(foreign_key="race.id", index=True)
    race: "Race" = Relationship(back_populates="race_participations")
    bike_id: int = Field(foreign_key="bike.id")
    bike: "Bike" = Relationship(back_populates="race_participations")