from collections import namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def adjust_contrast(images: Any, contrast_factor: Any, min_value: Any, max_value: Any, name: Optional[Any] = ...): ...

AdjustContrast: Any

def adjust_contrast_eager_fallback(images: Any, contrast_factor: Any, min_value: Any, max_value: Any, name: Any, ctx: Any): ...
def adjust_contrastv2(images: Any, contrast_factor: Any, name: Optional[Any] = ...): ...

AdjustContrastv2: Any

def adjust_contrastv2_eager_fallback(images: Any, contrast_factor: Any, name: Any, ctx: Any): ...
def adjust_hue(images: Any, delta: Any, name: Optional[Any] = ...): ...

AdjustHue: Any

def adjust_hue_eager_fallback(images: Any, delta: Any, name: Any, ctx: Any): ...
def adjust_saturation(images: Any, scale: Any, name: Optional[Any] = ...): ...

AdjustSaturation: Any

def adjust_saturation_eager_fallback(images: Any, scale: Any, name: Any, ctx: Any): ...

_CombinedNonMaxSuppressionOutput = namedtuple('CombinedNonMaxSuppression', ['nmsed_boxes', 'nmsed_scores', 'nmsed_classes', 'valid_detections'])

def combined_non_max_suppression(boxes: Any, scores: Any, max_output_size_per_class: Any, max_total_size: Any, iou_threshold: Any, score_threshold: Any, pad_per_class: bool = ..., clip_boxes: bool = ..., name: Optional[Any] = ...): ...

CombinedNonMaxSuppression: Any

def combined_non_max_suppression_eager_fallback(boxes: Any, scores: Any, max_output_size_per_class: Any, max_total_size: Any, iou_threshold: Any, score_threshold: Any, pad_per_class: Any, clip_boxes: Any, name: Any, ctx: Any): ...
def crop_and_resize(image: Any, boxes: Any, box_ind: Any, crop_size: Any, method: str = ..., extrapolation_value: int = ..., name: Optional[Any] = ...): ...

CropAndResize: Any

def crop_and_resize_eager_fallback(image: Any, boxes: Any, box_ind: Any, crop_size: Any, method: Any, extrapolation_value: Any, name: Any, ctx: Any): ...
def crop_and_resize_grad_boxes(grads: Any, image: Any, boxes: Any, box_ind: Any, method: str = ..., name: Optional[Any] = ...): ...

CropAndResizeGradBoxes: Any

def crop_and_resize_grad_boxes_eager_fallback(grads: Any, image: Any, boxes: Any, box_ind: Any, method: Any, name: Any, ctx: Any): ...
def crop_and_resize_grad_image(grads: Any, boxes: Any, box_ind: Any, image_size: Any, T: Any, method: str = ..., name: Optional[Any] = ...): ...

CropAndResizeGradImage: Any

def crop_and_resize_grad_image_eager_fallback(grads: Any, boxes: Any, box_ind: Any, image_size: Any, T: Any, method: Any, name: Any, ctx: Any): ...
def decode_and_crop_jpeg(contents: Any, crop_window: Any, channels: int = ..., ratio: int = ..., fancy_upscaling: bool = ..., try_recover_truncated: bool = ..., acceptable_fraction: int = ..., dct_method: str = ..., name: Optional[Any] = ...): ...

DecodeAndCropJpeg: Any

def decode_and_crop_jpeg_eager_fallback(contents: Any, crop_window: Any, channels: Any, ratio: Any, fancy_upscaling: Any, try_recover_truncated: Any, acceptable_fraction: Any, dct_method: Any, name: Any, ctx: Any): ...
def decode_bmp(contents: Any, channels: int = ..., name: Optional[Any] = ...): ...

DecodeBmp: Any

def decode_bmp_eager_fallback(contents: Any, channels: Any, name: Any, ctx: Any): ...
def decode_gif(contents: Any, name: Optional[Any] = ...): ...

DecodeGif: Any

def decode_gif_eager_fallback(contents: Any, name: Any, ctx: Any): ...
def decode_jpeg(contents: Any, channels: int = ..., ratio: int = ..., fancy_upscaling: bool = ..., try_recover_truncated: bool = ..., acceptable_fraction: int = ..., dct_method: str = ..., name: Optional[Any] = ...): ...

DecodeJpeg: Any

def decode_jpeg_eager_fallback(contents: Any, channels: Any, ratio: Any, fancy_upscaling: Any, try_recover_truncated: Any, acceptable_fraction: Any, dct_method: Any, name: Any, ctx: Any): ...
def decode_png(contents: Any, channels: int = ..., dtype: Any = ..., name: Optional[Any] = ...): ...

DecodePng: Any

def decode_png_eager_fallback(contents: Any, channels: Any, dtype: Any, name: Any, ctx: Any): ...
def draw_bounding_boxes(images: Any, boxes: Any, name: Optional[Any] = ...): ...

DrawBoundingBoxes: Any

def draw_bounding_boxes_eager_fallback(images: Any, boxes: Any, name: Any, ctx: Any): ...
def draw_bounding_boxes_v2(images: Any, boxes: Any, colors: Any, name: Optional[Any] = ...): ...

DrawBoundingBoxesV2: Any

def draw_bounding_boxes_v2_eager_fallback(images: Any, boxes: Any, colors: Any, name: Any, ctx: Any): ...
def encode_jpeg(image: Any, format: str = ..., quality: int = ..., progressive: bool = ..., optimize_size: bool = ..., chroma_downsampling: bool = ..., density_unit: str = ..., x_density: int = ..., y_density: int = ..., xmp_metadata: str = ..., name: Optional[Any] = ...): ...

EncodeJpeg: Any

def encode_jpeg_eager_fallback(image: Any, format: Any, quality: Any, progressive: Any, optimize_size: Any, chroma_downsampling: Any, density_unit: Any, x_density: Any, y_density: Any, xmp_metadata: Any, name: Any, ctx: Any): ...
def encode_jpeg_variable_quality(images: Any, quality: Any, name: Optional[Any] = ...): ...

EncodeJpegVariableQuality: Any

def encode_jpeg_variable_quality_eager_fallback(images: Any, quality: Any, name: Any, ctx: Any): ...
def encode_png(image: Any, compression: int = ..., name: Optional[Any] = ...): ...

EncodePng: Any

def encode_png_eager_fallback(image: Any, compression: Any, name: Any, ctx: Any): ...
def extract_glimpse(input: Any, size: Any, offsets: Any, centered: bool = ..., normalized: bool = ..., uniform_noise: bool = ..., noise: str = ..., name: Optional[Any] = ...): ...

ExtractGlimpse: Any

def extract_glimpse_eager_fallback(input: Any, size: Any, offsets: Any, centered: Any, normalized: Any, uniform_noise: Any, noise: Any, name: Any, ctx: Any): ...
def extract_jpeg_shape(contents: Any, output_type: Any = ..., name: Optional[Any] = ...): ...

ExtractJpegShape: Any

def extract_jpeg_shape_eager_fallback(contents: Any, output_type: Any, name: Any, ctx: Any): ...

_GenerateBoundingBoxProposalsOutput = namedtuple('GenerateBoundingBoxProposals', ['rois', 'roi_probabilities'])

def generate_bounding_box_proposals(scores: Any, bbox_deltas: Any, image_info: Any, anchors: Any, nms_threshold: Any, pre_nms_topn: Any, min_size: Any, post_nms_topn: int = ..., name: Optional[Any] = ...): ...

GenerateBoundingBoxProposals: Any

def generate_bounding_box_proposals_eager_fallback(scores: Any, bbox_deltas: Any, image_info: Any, anchors: Any, nms_threshold: Any, pre_nms_topn: Any, min_size: Any, post_nms_topn: Any, name: Any, ctx: Any): ...
def hsv_to_rgb(images: Any, name: Optional[Any] = ...): ...

HSVToRGB: Any

def hsv_to_rgb_eager_fallback(images: Any, name: Any, ctx: Any): ...
def image_projective_transform_v2(images: Any, transforms: Any, output_shape: Any, interpolation: Any, fill_mode: str = ..., name: Optional[Any] = ...): ...

ImageProjectiveTransformV2: Any

def image_projective_transform_v2_eager_fallback(images: Any, transforms: Any, output_shape: Any, interpolation: Any, fill_mode: Any, name: Any, ctx: Any): ...
def non_max_suppression(boxes: Any, scores: Any, max_output_size: Any, iou_threshold: float = ..., name: Optional[Any] = ...): ...

NonMaxSuppression: Any

def non_max_suppression_eager_fallback(boxes: Any, scores: Any, max_output_size: Any, iou_threshold: Any, name: Any, ctx: Any): ...
def non_max_suppression_v2(boxes: Any, scores: Any, max_output_size: Any, iou_threshold: Any, name: Optional[Any] = ...): ...

NonMaxSuppressionV2: Any

def non_max_suppression_v2_eager_fallback(boxes: Any, scores: Any, max_output_size: Any, iou_threshold: Any, name: Any, ctx: Any): ...
def non_max_suppression_v3(boxes: Any, scores: Any, max_output_size: Any, iou_threshold: Any, score_threshold: Any, name: Optional[Any] = ...): ...

NonMaxSuppressionV3: Any

def non_max_suppression_v3_eager_fallback(boxes: Any, scores: Any, max_output_size: Any, iou_threshold: Any, score_threshold: Any, name: Any, ctx: Any): ...

_NonMaxSuppressionV4Output = namedtuple('NonMaxSuppressionV4', ['selected_indices', 'valid_outputs'])

def non_max_suppression_v4(boxes: Any, scores: Any, max_output_size: Any, iou_threshold: Any, score_threshold: Any, pad_to_max_output_size: bool = ..., name: Optional[Any] = ...): ...

NonMaxSuppressionV4: Any

def non_max_suppression_v4_eager_fallback(boxes: Any, scores: Any, max_output_size: Any, iou_threshold: Any, score_threshold: Any, pad_to_max_output_size: Any, name: Any, ctx: Any): ...

_NonMaxSuppressionV5Output = namedtuple('NonMaxSuppressionV5', ['selected_indices', 'selected_scores', 'valid_outputs'])

def non_max_suppression_v5(boxes: Any, scores: Any, max_output_size: Any, iou_threshold: Any, score_threshold: Any, soft_nms_sigma: Any, pad_to_max_output_size: bool = ..., name: Optional[Any] = ...): ...

NonMaxSuppressionV5: Any

def non_max_suppression_v5_eager_fallback(boxes: Any, scores: Any, max_output_size: Any, iou_threshold: Any, score_threshold: Any, soft_nms_sigma: Any, pad_to_max_output_size: Any, name: Any, ctx: Any): ...
def non_max_suppression_with_overlaps(overlaps: Any, scores: Any, max_output_size: Any, overlap_threshold: Any, score_threshold: Any, name: Optional[Any] = ...): ...

NonMaxSuppressionWithOverlaps: Any

def non_max_suppression_with_overlaps_eager_fallback(overlaps: Any, scores: Any, max_output_size: Any, overlap_threshold: Any, score_threshold: Any, name: Any, ctx: Any): ...

_QuantizedResizeBilinearOutput = namedtuple('QuantizedResizeBilinear', ['resized_images', 'out_min', 'out_max'])

def quantized_resize_bilinear(images: Any, size: Any, min: Any, max: Any, align_corners: bool = ..., half_pixel_centers: bool = ..., name: Optional[Any] = ...): ...

QuantizedResizeBilinear: Any

def quantized_resize_bilinear_eager_fallback(images: Any, size: Any, min: Any, max: Any, align_corners: Any, half_pixel_centers: Any, name: Any, ctx: Any): ...
def rgb_to_hsv(images: Any, name: Optional[Any] = ...): ...

RGBToHSV: Any

def rgb_to_hsv_eager_fallback(images: Any, name: Any, ctx: Any): ...
def random_crop(image: Any, size: Any, seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

RandomCrop: Any

def random_crop_eager_fallback(image: Any, size: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...
def resize_area(images: Any, size: Any, align_corners: bool = ..., name: Optional[Any] = ...): ...

ResizeArea: Any

def resize_area_eager_fallback(images: Any, size: Any, align_corners: Any, name: Any, ctx: Any): ...
def resize_bicubic(images: Any, size: Any, align_corners: bool = ..., half_pixel_centers: bool = ..., name: Optional[Any] = ...): ...

ResizeBicubic: Any

def resize_bicubic_eager_fallback(images: Any, size: Any, align_corners: Any, half_pixel_centers: Any, name: Any, ctx: Any): ...
def resize_bicubic_grad(grads: Any, original_image: Any, align_corners: bool = ..., half_pixel_centers: bool = ..., name: Optional[Any] = ...): ...

ResizeBicubicGrad: Any

def resize_bicubic_grad_eager_fallback(grads: Any, original_image: Any, align_corners: Any, half_pixel_centers: Any, name: Any, ctx: Any): ...
def resize_bilinear(images: Any, size: Any, align_corners: bool = ..., half_pixel_centers: bool = ..., name: Optional[Any] = ...): ...

ResizeBilinear: Any

def resize_bilinear_eager_fallback(images: Any, size: Any, align_corners: Any, half_pixel_centers: Any, name: Any, ctx: Any): ...
def resize_bilinear_grad(grads: Any, original_image: Any, align_corners: bool = ..., half_pixel_centers: bool = ..., name: Optional[Any] = ...): ...

ResizeBilinearGrad: Any

def resize_bilinear_grad_eager_fallback(grads: Any, original_image: Any, align_corners: Any, half_pixel_centers: Any, name: Any, ctx: Any): ...
def resize_nearest_neighbor(images: Any, size: Any, align_corners: bool = ..., half_pixel_centers: bool = ..., name: Optional[Any] = ...): ...

ResizeNearestNeighbor: Any

def resize_nearest_neighbor_eager_fallback(images: Any, size: Any, align_corners: Any, half_pixel_centers: Any, name: Any, ctx: Any): ...
def resize_nearest_neighbor_grad(grads: Any, size: Any, align_corners: bool = ..., half_pixel_centers: bool = ..., name: Optional[Any] = ...): ...

ResizeNearestNeighborGrad: Any

def resize_nearest_neighbor_grad_eager_fallback(grads: Any, size: Any, align_corners: Any, half_pixel_centers: Any, name: Any, ctx: Any): ...

_SampleDistortedBoundingBoxOutput = namedtuple('SampleDistortedBoundingBox', ['begin', 'size', 'bboxes'])

def sample_distorted_bounding_box(image_size: Any, bounding_boxes: Any, seed: int = ..., seed2: int = ..., min_object_covered: float = ..., aspect_ratio_range: Any = ..., area_range: Any = ..., max_attempts: int = ..., use_image_if_no_bounding_boxes: bool = ..., name: Optional[Any] = ...): ...

SampleDistortedBoundingBox: Any

def sample_distorted_bounding_box_eager_fallback(image_size: Any, bounding_boxes: Any, seed: Any, seed2: Any, min_object_covered: Any, aspect_ratio_range: Any, area_range: Any, max_attempts: Any, use_image_if_no_bounding_boxes: Any, name: Any, ctx: Any): ...

_SampleDistortedBoundingBoxV2Output = namedtuple('SampleDistortedBoundingBoxV2', ['begin', 'size', 'bboxes'])

def sample_distorted_bounding_box_v2(image_size: Any, bounding_boxes: Any, min_object_covered: Any, seed: int = ..., seed2: int = ..., aspect_ratio_range: Any = ..., area_range: Any = ..., max_attempts: int = ..., use_image_if_no_bounding_boxes: bool = ..., name: Optional[Any] = ...): ...

SampleDistortedBoundingBoxV2: Any

def sample_distorted_bounding_box_v2_eager_fallback(image_size: Any, bounding_boxes: Any, min_object_covered: Any, seed: Any, seed2: Any, aspect_ratio_range: Any, area_range: Any, max_attempts: Any, use_image_if_no_bounding_boxes: Any, name: Any, ctx: Any): ...
def scale_and_translate(images: Any, size: Any, scale: Any, translation: Any, kernel_type: str = ..., antialias: bool = ..., name: Optional[Any] = ...): ...

ScaleAndTranslate: Any

def scale_and_translate_eager_fallback(images: Any, size: Any, scale: Any, translation: Any, kernel_type: Any, antialias: Any, name: Any, ctx: Any): ...
def scale_and_translate_grad(grads: Any, original_image: Any, scale: Any, translation: Any, kernel_type: str = ..., antialias: bool = ..., name: Optional[Any] = ...): ...

ScaleAndTranslateGrad: Any

def scale_and_translate_grad_eager_fallback(grads: Any, original_image: Any, scale: Any, translation: Any, kernel_type: Any, antialias: Any, name: Any, ctx: Any): ...
