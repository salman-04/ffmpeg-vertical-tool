import argparse
import subprocess
import os
import sys

#check file if not exist then give msg (file not exist) and stop the process 
def check_file(path):
    if not os.path.join(path):
        print(f"File doesn't found")
        sys.exit(1)

#using filter on our video , ffmpeg command , run it 
def vertical_clips(input_video, output_video):

    #use filter_complex command with instruction for to set blur background and convert to 9:16 etc
    filter_apply = (
        "[0:v]split=2[bg][fg];"
        "[bg]scale=1080:1920:force_original_aspect_ratio=increase,"
        "crop=1080:1920, gblur=sigma=50[bgblur];"
        "[fg]scale=1080:-1[fgscaled];"
        "[bgblur][fgscaled]overlay=(W-w)/2:(H-h)/2[out]"
    )

    #ffmpeg command list to use in subprocess.run()
    running_command = [
        "ffmpeg",
        "-i", input_video,
        "-filter_complex", filter_apply,
        "-map", "[out]",
        "-c:v", "libx264",
        "-crf", "23",
        "-c:a", "aac",
        output_video

    ]

    #try to check if no error then run 
    try:
        subprocess.run(running_command, check=True, capture_output=True, text=True)

    #if it having some errors process stop and give error msg
    except subprocess.CalledProcessError as e:
        print("Something went wrong!")
        print(e)
        sys.exit(1)

    print("Done ->", output_video)

if __name__ == "__main__":

    #take CLI from user like> python video_utils.py input.mp4 output.mp4
    parser = argparse.ArgumentParser(description="This CLI module is use to convert 16:9 video into 9:16")
    parser.add_argument("input", help="input video file")
    parser.add_argument("output", help="output video file")
    args = parser.parse_args()
    check_file(args.input)
    vertical_clips(args.input, args.output)