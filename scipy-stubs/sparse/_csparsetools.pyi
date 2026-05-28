from collections.abc import Iterable
from typing import TypeAlias

import numpy as np
import optype.numpy as onp
import optype.numpy.compat as npc

_Index: TypeAlias = int | np.intp
_Scalar: TypeAlias = npc.number | np.bool

###

#
def lil_get1[
    FusedScalarT: (
        np.bool,
        np.uint8,
        np.int8,
        np.uint16,
        np.int16,
        np.uint32,
        np.int32,
        np.uint64,
        np.int64,
        np.float32,
        np.float64,
        npc.floating80,
        np.complex64,
        np.complex128,
        npc.complexfloating160,
    )
](M: _Index, N: _Index, rows: list[list[FusedScalarT]], datas: list[list[FusedScalarT]], i: int, j: int) -> FusedScalarT: ...
def lil_insert[
    FusedScalarT: (
        np.bool,
        np.uint8,
        np.int8,
        np.uint16,
        np.int16,
        np.uint32,
        np.int32,
        np.uint64,
        np.int64,
        np.float32,
        np.float64,
        npc.floating80,
        np.complex64,
        np.complex128,
        npc.complexfloating160,
    )
](
    M: _Index, N: _Index, rows: list[list[FusedScalarT]], datas: list[list[FusedScalarT]], i: int, j: int, x: FusedScalarT
) -> None: ...
def lil_get_lengths[
    FusedScalarT: (
        np.bool,
        np.uint8,
        np.int8,
        np.uint16,
        np.int16,
        np.uint32,
        np.int32,
        np.uint64,
        np.int64,
        np.float32,
        np.float64,
        npc.floating80,
        np.complex64,
        np.complex128,
        npc.complexfloating160,
    )
](input: list[list[FusedScalarT]], output: onp.Array1D[npc.integer]) -> None: ...
def lil_flatten_to_array(input: onp.Array1D[np.object_ | np.float64], output: onp.Array1D[_Scalar]) -> None: ...
def lil_fancy_get[
    FusedScalarT: (
        np.bool,
        np.uint8,
        np.int8,
        np.uint16,
        np.int16,
        np.uint32,
        np.int32,
        np.uint64,
        np.int64,
        np.float32,
        np.float64,
        npc.floating80,
        np.complex64,
        np.complex128,
        npc.complexfloating160,
    )
](
    M: _Index,
    N: _Index,
    rows: list[list[FusedScalarT]],
    datas: list[list[FusedScalarT]],
    new_rows: list[list[FusedScalarT]],
    new_datas: list[list[FusedScalarT]],
    i_idx: onp.Array1D[np.intp],
    j_idx: onp.Array1D[np.intp],
) -> None: ...
def lil_fancy_set[
    FusedScalarT: (
        np.bool,
        np.uint8,
        np.int8,
        np.uint16,
        np.int16,
        np.uint32,
        np.int32,
        np.uint64,
        np.int64,
        np.float32,
        np.float64,
        npc.floating80,
        np.complex64,
        np.complex128,
        npc.complexfloating160,
    )
](
    M: _Index,
    N: _Index,
    rows: list[list[FusedScalarT]],
    data: list[list[FusedScalarT]],
    i_idx: onp.Array1D[np.intp],
    j_idx: onp.Array1D[np.intp],
    values: onp.Array2D[_Scalar],
) -> None: ...
def lil_get_row_ranges[
    FusedScalarT: (
        np.bool,
        np.uint8,
        np.int8,
        np.uint16,
        np.int16,
        np.uint32,
        np.int32,
        np.uint64,
        np.int64,
        np.float32,
        np.float64,
        npc.floating80,
        np.complex64,
        np.complex128,
        npc.complexfloating160,
    )
](
    M: _Index,
    N: _Index,
    rows: list[list[FusedScalarT]],
    datas: list[list[FusedScalarT]],
    new_rows: list[list[FusedScalarT]],
    new_datas: list[list[FusedScalarT]],
    irows: Iterable[_Index],
    j_start: _Index,
    j_stop: _Index,
    j_stride: _Index,
    nj: _Index,
) -> None: ...
