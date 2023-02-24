from car import Car

from battery.battery_type.spindler_battery import SpindlerBattery
from battery.battery_type.nubbin_battery import NubbinBattery

from engine.engine_type.capulet_engine import CapuletEngine
from engine.engine_type.sternman_engine import SternmanEngine
from engine.engine_type.willoughby_engine import WilloughbyEngine



class ClassFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage,last_service_date)
        battery = SpindlerBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage,last_service_date)
        battery = SpindlerBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = SternmanEngine(current_mileage,last_service_date)
        battery = SpindlerBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car   
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage,last_service_date)
        battery = NubbinBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car   
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage,last_service_date)
        battery = NubbinBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car
