from ctypes import LittleEndianStructure
from typing import Sequence


class StaticPage(LittleEndianStructure):
    sm_version: str
    ac_version: str
    number_of_sessions: int
    num_cars: int
    car_model: str
    track: str
    player_name: str
    player_surname: str
    player_nick: str
    sector_count: int
    max_torque: float
    max_power: float
    max_rpm: int
    max_fuel: float
    suspension_max_travel: Sequence[float]
    tyre_radius: Sequence[float]
    max_turbo_boost: float
    deprecated_1: float
    deprecated_2: float
    penalties_enabled: int
    aid_fuel_rate: float
    aid_tire_rate: float
    aid_mechanical_damage: float
    aid_allow_tyre_blankets: int
    aid_stability: float
    aid_auto_clutch: int
    aid_auto_blip: int
    has_drs: int
    has_ers: int
    has_kers: int
    kers_max_j: float
    engine_brake_settings_count: int
    ers_power_controller_count: int
    track_spline_length: float
    track_configuration: str
    ers_max_j: float
    is_timed_race: int
    has_extra_lap: int
    car_skin: str
    reversed_grid_positions: int
    pit_window_start: int
    pit_window_end: int
    is_online: int
