### [Main PVLIB](https://github.com/pvlib/pvlib-python)

DarkSky Forecasting Model
=

### Installation
`$ pip install git+https://github.com/allenlawrence94/pvlib-python`

### Usage
```
>>> from pvlib.forecast import DarkSky
>>> forecaster = DarkSky(YOUR_DARKSKY_SECRET_KEY)  # get a secret key from https://darksky.net/dev/register
>>> forecast = forecaster.get_proccessed_data(40, -80)
```

By default, `get_processed_data` provides two days of hourly forecasts. To extend this to a week, you can use:
```
>>> forecast = forecaster.get_processed_data(40, -80, extend=True)
```

To retrieve historical forecasts, simply specify a starting datetime:
```
>>> forecast = forecaster.get_processed_data(40, -80, datetime.datetime(2018, 1, 1, 0, 0))
```
Note that __this datetime must be timezone-naive__, as the DarkSky API will infer timezone for us.


### Going forward

- This needs to be vetted as  I know nothing about irradiance models.
- This currently only supports hourly resolution, but could potentially do minutely and daily forecasts.