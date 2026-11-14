# py-assettocorsa

The Python library to read shared memory of Assetto Corsa.

## Install

```bash
pip install py-assettocorsa
```

## Example

```python
from ac import ACSharedMemory

try:
    with ACSharedMemory() as memory:
        static, physics, graphics = memory.read_snapshot()
        print(static.car_model, static.track)
        print(physics.speed_kmh, physics.gas, physics.brake)
        print(graphics.i_current_time, graphics.car_coordinates)
except FileNotFoundError as error:
    print("The AC shared memory is unavailable. Start a driving session.")
```

## Available Models

| Model | Description |
| --- | --- |
| [Static](https://github.com/ooocheckitout/py-assettocorsa/blob/main/ac/models/static.py) | Car, track, player, and game information. |
| [Physics](https://github.com/ooocheckitout/py-assettocorsa/blob/main/ac/models/physics.py) | Speed, controls, engine, damage, and wheel telemetry. |
| [Graphics](https://github.com/ooocheckitout/py-assettocorsa/blob/main/ac/models/graphics.py) | Session, timing, positions, tyres, and pit information. |
| [Enums](https://github.com/ooocheckitout/py-assettocorsa/blob/main/ac/models/enums.py) | Named status, session, and flag values. |
