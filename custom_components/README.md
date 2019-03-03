# INFORMATION
I have dev a bunch of custom components and you can find all of them on [custom-components repository][1] so track and update them easily.

Compontents that I have developed are the following
 - [file_restore][2]
   
   This is a sensor that reads the last row of a file (vector) and return in state a value of this row that change every hour in a week and an attribute with a vector of all values read from file.
 - [programmable_thermostat][3]
   
   This is a climate components that mange heating system (and cooling in future), according to a sensor value so to let program it during the week. Of course it will allow manage manually change temperature for just 1h or for undefined time.
 
On custom-components repository you can find all the information about them.

## NOTE
You should include the following in your `custom_updater` configuration till I figure out how to automatically do it with `customjson`.

```yaml
custom_updater:
  component_urls:
    - https://raw.githubusercontent.com/MapoDan/home-assistant/master/custom_components/custom_components.json
```

![logo][4]

[1]: https://github.com/custom-components
[2]: https://github.com/custom-components/sensor.file_restore
[3]: https://github.com/custom-components/climate.programmable_thermostat
[4]: https://github.com/MapoDan/home-assistant/blob/master/mapodanlogo.png
