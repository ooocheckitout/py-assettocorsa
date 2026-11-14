from ctypes import LittleEndianStructure
from typing import Sequence


class GraphicsPage(LittleEndianStructure):
    packet_id: int
    status: int
    session: int
    current_time: str
    last_time: str
    best_time: str
    split: str
    completed_laps: int
    position: int
    i_current_time: int
    i_last_time: int
    i_best_time: int
    session_time_left: float
    distance_traveled: float
    is_in_pit: int
    current_sector_index: int
    last_sector_time: int
    number_of_laps: int
    tyre_compound: str
    replay_time_multiplier: float
    normalized_car_position: float
    car_coordinates: Sequence[float]
    penalty_time: float
    flag: int
    ideal_line_on: int
    is_in_pit_lane: int
    surface_grip: float
    mandatory_pit_done: int
    wind_speed: float
    wind_direction: float
    is_setup_menu_visible: int
    main_display_index: int
