from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.database.database import SessionLocal


class BaseSeeder(ABC):
    """
    Base class untuk semua seeder.
    """

    def __init__(self) -> None:
        self.db: Session = SessionLocal()

    @abstractmethod
    def run(self) -> None:
        """
        Jalankan proses seeding.
        """
        raise NotImplementedError

    def close(self) -> None:
        """
        Tutup koneksi database.
        """
        self.db.close()
