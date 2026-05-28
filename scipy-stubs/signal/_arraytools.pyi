from typing import Literal, SupportsIndex, overload

import numpy as np
import optype.numpy as onp

###

def axis_slice[SCT: np.generic](
    a: onp.ArrayND[SCT],
    start: SupportsIndex | None = None,
    stop: SupportsIndex | None = None,
    step: SupportsIndex | None = None,
    axis: SupportsIndex = -1,
) -> onp.ArrayND[SCT]: ...
def axis_reverse[SCT: np.generic](a: onp.ArrayND[SCT], axis: SupportsIndex = -1) -> onp.ArrayND[SCT]: ...

#
def odd_ext[SCT: np.generic](x: onp.ArrayND[SCT], n: onp.ToInt, axis: SupportsIndex = -1) -> onp.ArrayND[SCT]: ...
def even_ext[SCT: np.generic](x: onp.ArrayND[SCT], n: onp.ToInt, axis: SupportsIndex = -1) -> onp.ArrayND[SCT]: ...
def const_ext[SCT: np.generic](x: onp.ArrayND[SCT], n: onp.ToInt, axis: SupportsIndex = -1) -> onp.ArrayND[SCT]: ...
def zero_ext[SCT: np.generic](x: onp.ArrayND[SCT], n: onp.ToInt, axis: SupportsIndex = -1) -> onp.ArrayND[SCT]: ...

#
@overload
def _validate_fs(fs: None, allow_none: Literal[True] = True) -> None: ...
@overload
def _validate_fs(fs: onp.ToFloat, allow_none: bool = True) -> float: ...
