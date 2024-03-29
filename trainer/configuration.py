from typing import Callable, Iterable
from dataclasses import dataclass

from torchvision.transforms import ToTensor


@dataclass
class SystemConfig:
    seed: int = 42
    cudnn_benchmark_enabled: bool = False
    cudnn_deterministic: bool = True


@dataclass
class DatasetConfig:
    root_dir: str = "data"
    train_transforms: Iterable[Callable] = (ToTensor(),)
    test_transforms: Iterable[Callable] = (ToTensor(),)


@dataclass
class DataloaderConfig:
    batch_size: int = 250
    num_workers: int = 5


@dataclass
class OptimizerConfig:
    learning_rate: float = 0.001
    momentum: float = 0.9
    weight_decay: float = 0.0001
    lr_step_milestones: Iterable = (30, 40)
    lr_gamma: float = 0.1


@dataclass
class TrainerConfig:
    model_dir: str = "checkpoints"
    model_save_best: bool = True
    model_saving_frequency: int = 1
    device: str = "cpu"
    epoch_num: int = 50
    progress_bar: bool = False
