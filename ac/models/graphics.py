from ctypes import (
    LittleEndianStructure,
    sizeof,
    c_float,
    c_int32,
    c_wchar,
)
from collections.abc import Sequence


FloatArray = Sequence[float]


class GraphicsPage(LittleEndianStructure):
    _layout_ = "ms"
    _pack_ = 4

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
    car_coordinates: FloatArray
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

    _fields_ = [
        ("packet_id", c_int32),
        ("status", c_int32),
        ("session", c_int32),
        ("current_time", (c_wchar * 15)),
        ("last_time", (c_wchar * 15)),
        ("best_time", (c_wchar * 15)),
        ("split", (c_wchar * 15)),
        ("completed_laps", c_int32),
        ("position", c_int32),
        ("i_current_time", c_int32),
        ("i_last_time", c_int32),
        ("i_best_time", c_int32),
        ("session_time_left", c_float),
        ("distance_traveled", c_float),
        ("is_in_pit", c_int32),
        ("current_sector_index", c_int32),
        ("last_sector_time", c_int32),
        ("number_of_laps", c_int32),
        ("tyre_compound", (c_wchar * 33)),
        ("replay_time_multiplier", c_float),
        ("normalized_car_position", c_float),
        ("car_coordinates", (c_float * 3)),
        ("penalty_time", c_float),
        ("flag", c_int32),
        ("ideal_line_on", c_int32),
        ("is_in_pit_lane", c_int32),
        ("surface_grip", c_float),
        ("mandatory_pit_done", c_int32),
        ("wind_speed", c_float),
        ("wind_direction", c_float),
        ("is_setup_menu_visible", c_int32),
        ("main_display_index", c_int32),
    ]


assert sizeof(GraphicsPage) == 304, "GraphicsPage differs from the AC ABI"
