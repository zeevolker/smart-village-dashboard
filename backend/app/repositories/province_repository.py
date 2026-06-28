from app.models.province import Province
from app.repositories.base_repository import BaseRepository


class ProvinceRepository(
    BaseRepository[Province]
):
    model = Province