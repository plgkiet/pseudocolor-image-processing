 
import os
import cv2
import sys
import glob
from shutil import rmtree

def color_map():
  image_dir_path = os.path.join(os.getcwd(), "assets/img")
  out_path = os.path.join(os.getcwd(), "out/color-map")
  ext = "png"

  # find all images in the directory
  images = glob.glob(f"{image_dir_path}/*.{ext}")

  # get all colormap flags available in opencv
  colormap_flag_prefix = 'COLORMAP_'
  colormap_flags = [i for i in dir(cv2) if i.startswith(colormap_flag_prefix)]

  # assemble the dictionary of color maps
  colormaps = {}
  for colormap_flag in colormap_flags:
    colormap_key = colormap_flag[len(colormap_flag_prefix):].lower()

    colormaps[colormap_key] = getattr(cv2, colormap_flag)

  # exit immediately when there are no detected color maps
  num_colormap_flags = len(colormap_flags)
  if num_colormap_flags == 0:
    print("No color map flags present on OpenCV. This is insane! should have at least one!")
    sys.exit(1)

  # exit immediately when there are no images present on the folder
  num_images = len(images)
  if num_images == 0:
    print(f"No images present on the directory: {image_dir_path}")
    sys.exit(1)

  print(f"Reading all images from the directory: {image_dir_path}")
  print(f"Output will be saved in: {out_path}")

  # delete the folder to make sure we are create new files
  if os.path.exists(out_path):
    rmtree(out_path)

  # create the output folder if not exists
  if not os.path.exists(out_path):
    os.makedirs(out_path)

  # iterate all found images
  for image in images:
    basename = os.path.basename(image)
    filename, _ = os.path.splitext(basename)
    im_gray = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    # resolve the output folder for each image
    final_out_path = os.path.join(out_path, filename)
    if not os.path.exists(final_out_path):
      os.makedirs(final_out_path)

    # apply the colormap to the grayscaled image and write it to the filesystem
    for color_name, color_val in colormaps.items():
      im_color = cv2.applyColorMap(im_gray, color_val)

      cv2.imwrite(f"{final_out_path}/{color_name}.jpg", im_color)

  print("Done processing images.")

# execute the main function
if __name__ == "__main__":
  color_map()


