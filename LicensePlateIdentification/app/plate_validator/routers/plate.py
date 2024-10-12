# app/plate_validator/routers/plate.py

from fastapi import APIRouter, HTTPException
from app.models import LicensePlate
from app.schemas import Plate
from app.utils import send_signal_to_arduino

router = APIRouter()

@router.post("/check_plate/")
def check_plate(plate: Plate):
    if LicensePlate.exists(plate.plate_number):
        send_signal_to_arduino()
        return {"status": "exists"}
    else:
        raise HTTPException(status_code=404, detail="Plate not found")

@router.post("/add_plate/")
def add_plate(plate: Plate):
    LicensePlate.add(plate.plate_number)
    return {"status": "added"}

@router.delete("/remove_plate/")
def remove_plate(plate: Plate):
    LicensePlate.remove(plate.plate_number)
    return {"status": "removed"}
