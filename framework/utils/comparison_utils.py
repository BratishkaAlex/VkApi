from PIL import ImageChops, Image


def compare_two_images(path_to_first_picture, path_to_second_picture):
    first_image = Image.open(path_to_first_picture)
    second_image = Image.open(path_to_second_picture)
    return ImageChops.difference(first_image, second_image).getbbox() is None
