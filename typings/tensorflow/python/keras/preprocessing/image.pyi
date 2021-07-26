import abc
from keras_preprocessing import image
from scipy import linalg as linalg, ndimage as ndimage
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.utils import data_utils as data_utils
from tensorflow.python.util import tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

random_rotation: Any
random_shift: Any
random_shear: Any
random_zoom: Any
apply_channel_shift: Any
random_channel_shift: Any
apply_brightness_shift: Any
random_brightness: Any
apply_affine_transform: Any
load_img: Any

def array_to_img(x: Any, data_format: Optional[Any] = ..., scale: bool = ..., dtype: Optional[Any] = ...): ...
def img_to_array(img: Any, data_format: Optional[Any] = ..., dtype: Optional[Any] = ...): ...
def save_img(path: Any, x: Any, data_format: Optional[Any] = ..., file_format: Optional[Any] = ..., scale: bool = ..., **kwargs: Any) -> None: ...

class Iterator(image.Iterator, data_utils.Sequence, metaclass=abc.ABCMeta): ...

class DirectoryIterator(image.DirectoryIterator, Iterator, metaclass=abc.ABCMeta):
    def __init__(self, directory: Any, image_data_generator: Any, target_size: Any = ..., color_mode: str = ..., classes: Optional[Any] = ..., class_mode: str = ..., batch_size: int = ..., shuffle: bool = ..., seed: Optional[Any] = ..., data_format: Optional[Any] = ..., save_to_dir: Optional[Any] = ..., save_prefix: str = ..., save_format: str = ..., follow_links: bool = ..., subset: Optional[Any] = ..., interpolation: str = ..., dtype: Optional[Any] = ...) -> None: ...

class NumpyArrayIterator(image.NumpyArrayIterator, Iterator, metaclass=abc.ABCMeta):
    def __init__(self, x: Any, y: Any, image_data_generator: Any, batch_size: int = ..., shuffle: bool = ..., sample_weight: Optional[Any] = ..., seed: Optional[Any] = ..., data_format: Optional[Any] = ..., save_to_dir: Optional[Any] = ..., save_prefix: str = ..., save_format: str = ..., subset: Optional[Any] = ..., dtype: Optional[Any] = ...) -> None: ...

class ImageDataGenerator(image.ImageDataGenerator):
    def __init__(self, featurewise_center: bool = ..., samplewise_center: bool = ..., featurewise_std_normalization: bool = ..., samplewise_std_normalization: bool = ..., zca_whitening: bool = ..., zca_epsilon: float = ..., rotation_range: int = ..., width_shift_range: float = ..., height_shift_range: float = ..., brightness_range: Optional[Any] = ..., shear_range: float = ..., zoom_range: float = ..., channel_shift_range: float = ..., fill_mode: str = ..., cval: float = ..., horizontal_flip: bool = ..., vertical_flip: bool = ..., rescale: Optional[Any] = ..., preprocessing_function: Optional[Any] = ..., data_format: Optional[Any] = ..., validation_split: float = ..., dtype: Optional[Any] = ...) -> None: ...
