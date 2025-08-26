# backend/app/models.py
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Boolean, Text, UniqueConstraint

class Base(DeclarativeBase):
    pass

class WhrEnduser(Base):
    __tablename__ = "whr_enduser"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    wp_display_name: Mapped[str] = mapped_column(String(255), default="")
    location: Mapped[str] = mapped_column(String(255), default="")
    country: Mapped[str] = mapped_column(String(255), default="")
    active: Mapped[bool] = mapped_column(Boolean, default=True)

class WhrDevice(Base):
    __tablename__ = "whr_device"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    asset_tag: Mapped[str] = mapped_column(String(120))
    asset_serial_number: Mapped[str] = mapped_column(String(255), default="")
    display_name: Mapped[str] = mapped_column(String(255), default="")
    accesorio: Mapped[str] = mapped_column(String(255), default="")
    asset_description: Mapped[str] = mapped_column(Text, default="")

    __table_args__ = (
        UniqueConstraint("asset_tag", name="uq_whr_device_asset_tag"),
    )
