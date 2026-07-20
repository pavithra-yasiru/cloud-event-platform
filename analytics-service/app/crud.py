from datetime import datetime
from sqlalchemy.orm import Session

from app.db_models import AnalyticsTable
from app.models import Analytics
from app.database import clickhouse_client


def get_analytics(db: Session):
    return db.query(AnalyticsTable).all()


def create_analytics(db: Session, analytics: Analytics):

    # Save to PostgreSQL
    db_analytics = AnalyticsTable(**analytics.model_dump())

    db.add(db_analytics)
    db.commit()
    db.refresh(db_analytics)

    # Save to ClickHouse
    try:
        clickhouse_client.insert(
            "analytics",
            [[
                db_analytics.id,
                db_analytics.event_type,
                db_analytics.page,
                datetime.fromisoformat(
                    db_analytics.event_time.replace("Z", "+00:00")
                )
            ]],
            column_names=[
                "id",
                "event_type",
                "page",
                "event_time"
            ]
        )

    except Exception as e:
        print(f"ClickHouse insert failed: {e}")

    return db_analytics
