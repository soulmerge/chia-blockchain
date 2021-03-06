from dataclasses import dataclass
from typing import List

from src.types.condition_opcodes import ConditionOpcode
from src.util.streamable import streamable, Streamable


@dataclass(frozen=True)
@streamable
class ConditionVarPair(Streamable):
    """
    This structure is used to store parsed CLVM conditions
    Conditions in CLVM have either format of (opcode, var1) or (opcode, var1, var2)
    """

    opcode: ConditionOpcode
    vars: List[bytes]
