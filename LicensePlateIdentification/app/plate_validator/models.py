# app/plate_validator/models.py

from .database import redis_client

class LicensePlate:
    @staticmethod
    def exists(plate_number: str) -> bool:
        return redis_client.exists(plate_number) == 1

    @staticmethod
    def add(plate_number: str):
        redis_client.set(plate_number, "exists")

    @staticmethod
    def remove(plate_number: str):
        redis_client.delete(plate_number)
