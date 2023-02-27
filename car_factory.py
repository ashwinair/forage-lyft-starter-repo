from car import Car

from battery.battery_type.spindler_battery import SpindlerBattery
from battery.battery_type.nubbin_battery import NubbinBattery

from engine.engine_type.capulet_engine import CapuletEngine
from engine.engine_type.sternman_engine import SternmanEngine
from engine.engine_type.willoughby_engine import WilloughbyEngine

from tire.tire_types.carrigan_tires import CarriganTires
from tire.tire_types.octoprime_tires import OctoprimeTires


class ClassFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage,tire_wear):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        tires = CarriganTires(tire_wear)
        car = Car(engine,battery,tires)
        return car
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage,tire_wear):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        tires = OctoprimeTires(tire_wear)
        car = Car(engine,battery,tires)
        return car
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage,tire_wear):
        engine = SternmanEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        tires = CarriganTires(tire_wear)
        car = Car(engine,battery,tires)
        return car   
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage,tire_wear):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        tires = OctoprimeTires(tire_wear)
        car = Car(engine,battery,tires)
        return car   
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage,tire_wear):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        tires = CarriganTires(tire_wear)
        car = Car(engine,battery,tires)
        return car
