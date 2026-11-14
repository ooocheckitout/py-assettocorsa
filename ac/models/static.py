from ctypes import (
    LittleEndianStructure,
    sizeof,
    c_float,
    c_int32,
    c_wchar,
)


class StaticPage(LittleEndianStructure):
    _layout_ = "ms"
    _pack_ = 4

    _fields_ = [
        ("sm_version", (c_wchar * 15)),
        ("ac_version", (c_wchar * 15)),
        ("number_of_sessions", c_int32),
        ("num_cars", c_int32),
        ("car_model", (c_wchar * 33)),
        ("track", (c_wchar * 33)),
        ("player_name", (c_wchar * 33)),
        ("player_surname", (c_wchar * 33)),
        ("player_nick", (c_wchar * 33)),
        ("sector_count", c_int32),
        ("max_torque", c_float),
        ("max_power", c_float),
        ("max_rpm", c_int32),
        ("max_fuel", c_float),
        ("suspension_max_travel", (c_float * 4)),
        ("tyre_radius", (c_float * 4)),
        ("max_turbo_boost", c_float),
        ("deprecated_1", c_float),
        ("deprecated_2", c_float),
        ("penalties_enabled", c_int32),
        ("aid_fuel_rate", c_float),
        ("aid_tire_rate", c_float),
        ("aid_mechanical_damage", c_float),
        ("aid_allow_tyre_blankets", c_int32),
        ("aid_stability", c_float),
        ("aid_auto_clutch", c_int32),
        ("aid_auto_blip", c_int32),
        ("has_drs", c_int32),
        ("has_ers", c_int32),
        ("has_kers", c_int32),
        ("kers_max_j", c_float),
        ("engine_brake_settings_count", c_int32),
        ("ers_power_controller_count", c_int32),
        ("track_spline_length", c_float),
        ("track_configuration", (c_wchar * 33)),
        ("ers_max_j", c_float),
        ("is_timed_race", c_int32),
        ("has_extra_lap", c_int32),
        ("car_skin", (c_wchar * 33)),
        ("reversed_grid_positions", c_int32),
        ("pit_window_start", c_int32),
        ("pit_window_end", c_int32),
        ("is_online", c_int32),
    ]


assert sizeof(StaticPage) == 688, "StaticPage differs from the AC ABI"
