import typing
from typing import Any, Dict, Optional

class MBTATrip:
    """A trip object to hold information about a trip."""
    
    def __init__(self, trip: Dict[str, Any]) -> None:
        attributes = trip.get('attributes', {})
        
        self.trip_id: str = trip.get('id', '')
        self.name: str = attributes.get('name', '')
        self.headsign: str = attributes.get('headsign', '')
        self.direction_id: int = attributes.get('direction_id', 0)
        self.block_id: str = attributes.get('block_id', '')
        self.shape_id: str = attributes.get('shape_id', '')
        self.wheelchair_accessible: Optional[bool] = attributes.get('wheelchair_accessible')
        self.bikes_allowed: Optional[bool] = attributes.get('bikes_allowed')
        self.schedule_relationship: str = attributes.get('schedule_relationship', '')

        self.route_id: str = trip.get('relationships', {}).get('route', {}).get('data', {}).get('id', '')
        
        service_data = trip.get('relationships', {}).get('service', {}).get('data', {})
        self.service_id: str = service_data.get('id', '') if service_data else ''

    
    def __repr__(self) -> str:
        return (f"MBTAtrip(id={self.trip_id}, name={self.trip_name}, headsign={self.trip_headsign}, "
                f"direction_id={self.trip_direction_id}, block_id={self.trip_block_id}, shape_id={self.trip_shape_id}, "
                f"wheelchair_accessible={self.trip_wheelchair_accessible}, bikes_allowed={self.trip_bikes_allowed}, "
                f"schedule_relationship={self.trip_schedule_relationship}, route_id={self.route_id}, service_id={self.service_id})")

    def __str__(self) -> str:
        return f"Trip {self.trip_id} on route {self.route_id}"
