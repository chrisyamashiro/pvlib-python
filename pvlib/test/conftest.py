import os
import pytest

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


if 'DARKSKY_SECRET_KEY' in os.environ:
    has_darksky_secret_key = True
else:
    has_darksky_secret_key = False


requires_darksky = pytest.mark.skipif(not has_darksky_secret_key,
                                      reason='requires darksky_secret_key')
