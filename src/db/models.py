from datetime import datetime

from sqlalchemy import Column, Integer, String, func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql.sqltypes import DateTime, Date


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"

    def __repr__(self):
        return f"#Contact(id={self.id}, name={self.first_name} {self.last_name}, email={self.email})"

    def __str__(self):
        return f"#Contact(id={self.id}, name={self.first_name} {self.last_name}, email={self.email})"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False)
    phone_number = Column(String(15), nullable=False)
    birthday = Column(Date)

    # id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # title: Mapped[str] = mapped_column(String(50), nullable=False)
    # created_at: Mapped[datetime] = mapped_column(
    #     "created_at", DateTime, default=func.now()
    # )
    # updated_at: Mapped[datetime] = mapped_column(
    #     "updated_at", DateTime, default=func.now(), onupdate=func.now()
    # )
    # description: Mapped[str] = mapped_column(String(150), nullable=False)
    # done: Mapped[bool] = mapped_column(Boolean, default=False)
    # tags: Mapped[list["Tag"]] = relationship(
    #     "Tag", secondary=note_m2m_tag, backref="notes"
    # )
