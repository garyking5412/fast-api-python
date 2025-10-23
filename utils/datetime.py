from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declared_attr, attributes
from sqlalchemy import event

class TimeStampUtils:
    @declared_attr
    def createddate(cls):
        return Column(DateTime, default=datetime.utcnow, nullable=False)
    
    @classmethod
    def __declare_last__(cls):
        """Register the event listener on the inheriting class."""
        event.listen(cls, 'before_insert', cls._set_created_at)

    def _set_created_at(mapper, connection, target):
        """Event listener function to explicitly set created_at on insert."""
        # Check if created_at is not already set by the application code
        if not attributes.instance_state(target).has_identity:
            target.created_at = datetime.utcnow()