import glob
import os
# change this if needed
data_dir = "/home/orz/Projects/Datasets/dorm2/dorm2_fast"
depth_name = "filtered"
color_name = "color"
image_name = "*.png"                # Pick one of two. Generate by traversing file name
timestamp_name = "TIMESTAMP.txt"    # Pick one of two. Generate by reading timestamp.txt, see FastFusion datasets https://github.com/zhuzunjie17/FastFusion
log_name = "associations.txt"

idx=0
timestamp_path = os.path.join(data_dir, timestamp_name)
log_path = os.path.join(data_dir, log_name)
with open(log_path, 'w') as f:
    if not os.path.exists(timestamp_path):
        depth_paths = sorted(glob.glob(os.path.join(data_dir, depth_name, image_name)))
        color_paths = sorted(glob.glob(os.path.join(data_dir, color_name, image_name)))

        for i, (depth_path, color_path) in enumerate(zip(depth_paths, color_paths)):
            depth_filename = depth_path.split("/")[-1]
            color_filename = color_path.split("/")[-1]
            f.write("{} {}/{} {} {}/{}\n".format(idx, depth_name, depth_filename, idx, color_name, color_filename))
            idx += 1

    else:
        with open(timestamp_path, 'r') as ft:
            infos = ft.readlines()
            infos.pop(0)
            for info in infos:
                _, depth_filename, color_filename = info[:-1].split(',')
                f.write("{} {}/{} {} {}/{}\n".format(idx, depth_name, depth_filename, idx, color_name, color_filename))
                idx += 1
