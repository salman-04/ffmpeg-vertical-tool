
"""Imports Modules Section"""
import argparse
import subprocess
import os
import sys

"""if not exist -> print error, sys.exit(1)"""

def check_input(path):
    if not os.path.exists(path):
        print(f"File is not found {path}")
        sys.exit(1)

""" Take the input and output data , filter_complex, use try execption , print error if exist"""

def make_vertical(input_path, output_path):

    filter_string = (
        "[0:v]split=2[bg][fg];"
        "[bg]scale=1080:1920:force_original_aspect_ratio=increase,"
        "crop=1080:1920,gblur=sigma=50[bgblur];"
        "[fg]scale=1080:-1[fgscaled];"
        "[bgblur][fgscaled]overlay=(W-w)/2:(H-h)/2[out]"
    )

    args = [
        "ffmpeg",
        "-i", input_path,
        "-filter_complex", filter_string,
        "-map", "[out]",
        "-c:v", "libx264",
        "-crf", "23",
        "-c:a", "aac",
        output_path
    ]

    try:
        subprocess.run(args, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print("FFMPEG failed, error:")
        print(e.stderr)
        sys.exit(1)

    print("Done -> ", output_path )

"""Run the project if __name__ == __main__ """

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make a virtical video with 50 percent blurred background")
    parser.add_argument("input", help="input file video")
    parser.add_argument("output", help="output file video")
    args = parser.parse_args()
    check_input(args.input)
    make_vertical(args.input, args.output)