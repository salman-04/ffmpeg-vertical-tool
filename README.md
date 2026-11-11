# ffmpeg-vertical-tool

A Python CLI that converts any horizontal video into a 9:16 vertical video with a blurred background — the TikTok / Reels / Shorts look.


## What it does

- Takes any `.mp4` video
- Produces a vertical (1080×1920) version
- Keeps the original video sharp and centered
- Fills the empty sides with a blurred copy of the same video
- No UI, no browser — just one command

## Requirements

- Python 3.10+
- [FFmpeg](https://ffmpeg.org/download.html) installed and available on your `PATH`

Verify FFmpeg is installed:

```bash
ffmpeg -version