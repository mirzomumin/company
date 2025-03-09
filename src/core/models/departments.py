from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Department(Base):
    __tablename__ = "departments"

    name: Mapped[str] = mapped_column(unique=True)
