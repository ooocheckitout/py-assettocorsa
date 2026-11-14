from ctypes import (
    LittleEndianStructure,
    sizeof,
    c_float,
    c_int32,
    c_wchar,
)


class GraphicsPage(LittleEndianStructure):
    _layout_ = "ms"
    _pack_ = 4

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
