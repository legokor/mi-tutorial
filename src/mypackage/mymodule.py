from dataclasses import dataclass
from typing import Optional
import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import OmegaConf


@dataclass
class MySubConfig:
    sub_variable: str


@dataclass
class MyConfig:
    variable_a: int
    variable_b: str
    variable_c: bool
    variable_d: Optional[int]
    variable_e: list[str]
    variable_f: Optional[str]
    sub_config: MySubConfig


cs = ConfigStore.instance()
cs.store(name="my_config", node=MyConfig)


@hydra.main(config_path="../../config", config_name="my_basic_config")

def main(cfg: MyConfig):
    print(OmegaConf.to_yaml(cfg, resolve=True))


if __name__ == "__main__":
    main()