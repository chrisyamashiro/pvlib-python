#!/bin/bash
pip install -e pvlib-python
python -c "
try:
    from pvlib.forecast import DarkSky
    print('INSTALLATION SUCCESFUL')
except ImportError:
    print('INSTALLATION FAILED')
"

