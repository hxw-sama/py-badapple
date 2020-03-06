import subprocess
import os
import config

if __name__ == '__main__':

    if not os.path.isfile(config. video_path):
        print("[ERROR] Video {} not exist".format(config. video_path))
        exit()

    if not os.path.isdir(config. img_out_dir):
        print("[ERROR] Directory {} not exist".format(config.img_out_dir))
        exit()

    command = r"ffmpeg -i {} -r {} -s {}x{} {}/frame%04d.png".format(
        config.video_path,
        config.fps,
        config.out_width,
        config.out_height,
        config.img_out_dir)

    # print(command)
    subprocess.Popen(command)
