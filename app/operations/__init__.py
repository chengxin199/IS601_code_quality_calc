"""Package shim for operations.

Re-export Operations from `app.operations_impl` so code importing `app.operations` keeps
working while we keep the implementation in a separate module.
"""

from app.operations_impl import Operations

__all__ = ["Operations"]
