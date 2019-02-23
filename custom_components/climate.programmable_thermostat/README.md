# PROGRAMMABLE THERMOSTAT
This component is a revision of the official Home Assistant component 'Generic Thermostat' in order to have possibility to have target temperature variable according to a sensor state value.

## EXAMPLE OF SETUP
```yaml
climate:
  - platfrom: programmable_thermostat
    name: Termostato
    heat_switch: switch.riscaldamento
    actual_temp_sensor: sensor.temperatura_reale
    min_temp: 5
    max_temp: 30
    target_temp_sensor: sensor.temperatura_desiderata
    cold_tolerance: 0.3
    hot_tolerance: 0.3
    initial_operation_mode: heat
    
```

Field | Value | Necessity | Comments
--- | --- | --- | ---
platform | `file_restore` | *Required* |
unit_of_measurement |  | Optional |
file_path |  | *Required* | path of the file. Be sure that the URL is whitelisted, if needed.
name| File_restore | Optional |

## SPECIFICITIES
### DATA FILE
File defined in `file_path` must have the structure of a CSV file with value separated by a comma. The list of data is composed by 168 elements, one per each hour in a week and ordered within the week.

NOTE:
- Week is counted from Monday to Sunday (ISO week).
- Only last line of file will be read.

To give you an example:
```csv
10.0, 10.5, ...(165 other values)..., 11.0
```
### ATTRIBUTE AND STATE
Attribute `temperature_program` that include all 168 values read from the file.
State of the the sensor will change automatically according the the data read from file.

## NOTE
This component has been developed for the bigger project of building a smart thermostat using Home Assistant and way cheeper then the commercial ones.

***
Due to how `custom_components` are loaded, it could be possible to have a `ModuleNotFoundError` error on first boot after adding this; to resolve it, restart Home-Assistant.

***
