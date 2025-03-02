from os import environ

if "DISABLE_GEVENT_FIX" not in environ:
    # Fix gevent
    try:
        from gevent import monkey
        monkey.patch_all(thread=False, socket=False)
    except ImportError:
        pass

    import ssl
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context

# Mlchain Context
from contextvars import ContextVar
from typing import Any, Dict

_request_scope_context_storage: ContextVar[Dict[Any, Any]] = ContextVar(
    "mlchain_context"
)

# Parameters of MLchain
__version__ = "0.3.1"

HOST = "https://www.api.mlchain.ml"
WEB_HOST = HOST
API_ADDRESS = HOST
MODEL_ID = None
    
from os import environ

environ['OBJC_DISABLE_INITIALIZE_FORK_SAFETY'] = 'YES'

from mlchain.base.log import logger
from .context import mlchain_context

from .base.exceptions import *
from .config import mlconfig
from .client import Client