from .caffe_descriptor import CaffeDescriptorGenerator
from .colordescriptor.colordescriptor import (
    ColorDescriptor_Image_rgbhistogram,
    ColorDescriptor_Video_rgbhistogram,
    ColorDescriptor_Image_opponenthistogram,
    ColorDescriptor_Video_opponenthistogram,
    ColorDescriptor_Image_huehistogram,
    ColorDescriptor_Video_huehistogram,
    ColorDescriptor_Image_nrghistogram,
    ColorDescriptor_Video_nrghistogram,
    ColorDescriptor_Image_transformedcolorhistogram,
    ColorDescriptor_Video_transformedcolorhistogram,
    ColorDescriptor_Image_colormoments,
    ColorDescriptor_Video_colormoments,
    ColorDescriptor_Image_colormomentinvariants,
    ColorDescriptor_Video_colormomentinvariants,
    ColorDescriptor_Image_sift,
    ColorDescriptor_Video_sift,
    ColorDescriptor_Image_huesift,
    ColorDescriptor_Video_huesift,
    ColorDescriptor_Image_hsvsift,
    ColorDescriptor_Video_hsvsift,
    ColorDescriptor_Image_opponentsift,
    ColorDescriptor_Video_opponentsift,
    ColorDescriptor_Image_rgsift,
    ColorDescriptor_Video_rgsift,
    ColorDescriptor_Image_csift,
    ColorDescriptor_Video_csift,
    ColorDescriptor_Image_rgbsift,
    ColorDescriptor_Video_rgbsift,
)
from .kwcnndescriptor import KWCNNDescriptorGenerator
