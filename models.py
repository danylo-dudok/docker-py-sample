from dataclasses import dataclass
from typing import List


@dataclass
class Network:
    name: str


@dataclass
class Port:
    protocol: str
    expose: List[int] or int
    internal: int


@dataclass
class Container:
    image_name: str
    name: str
    detach: bool
    ports: Port
    networks: List[str] or str
    environments: List[str]


@dataclass
class Context:
    path: str
    networks: List[Network]
    builds: List[str]
    containers: List[Container]
