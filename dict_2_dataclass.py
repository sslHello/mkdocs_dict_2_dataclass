from typing import Any, Dict, List, Union, NewType, get_type_hints
from dataclasses import dataclass, field, asdict
from dacite import from_dict, Config, ForwardReferenceError, UnexpectedDataError, StrictUnionMatchError
import yaml
import warnings
import logging
import os
import sys

debug               = 3                                             # global variables
log                 = logging.getLogger(__name__)                   # logging
if debug > 2:
  logging.basicConfig(level=logging.DEBUG)
elif debug > 1:
  logging.basicConfig(level=logging.INFO)

@dataclass
class X:
  i: int
  j: int

@dataclass
class Y:
  children: Dict[Union[str, int], X]
  def to_dict(self) -> Dict[str, Any]:
    return asdict(self)

d = {"children": {1: {"i": 42, "j": 43}, 2: {"i": 37, "j": 38}}}  # Test Dict
result = from_dict(Y, d)
print ("Dict d: ...............", d)
print ("Class result: .........", result)
print ("YAML result: ..........\n", yaml.dump(result.to_dict(), sort_keys=False, indent=2, default_flow_style=False), "\n")
print ("Dict result.to_dict(): ", result.to_dict())
assert result == Y(children={1: X(i=42, j=43), 2: X(i=37, j=38)})
