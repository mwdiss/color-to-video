🎥 Solid Color Video Generator

Generate solid-color videos from a hex color code.  
Two implementations are included:

- **`solid_color_video.py`** → Python (FFmpeg via `imageio`)  
- **`index.html`** → Pure client-side web version (HTML/CSS/JS, runs in the browser)  

Both allow you to specify resolution, FPS, duration, codec, and output filename.  
Useful for testing, placeholders, or demo purposes.

---

✨ Features
- Input a **hex color** (e.g. `#FF0000`, `#09f`)
- Adjustable **resolution** (e.g. `1920x1080`)
- Adjustable **FPS** (default: 60)
- Adjustable **duration** (default: 10s)
- Adjustable **bitrate** (Python only)
- Codec/engine selection:
  - **Python**: h264 / h265 (via FFmpeg)
  - **Web**: VP8, VP9, H264 (browser-supported codecs)
- Output format based on file extension (e.g. `.mp4`, `.mkv`, `.webm`, `.hevc`)
- **GPLv3 Licensed**

---

🐍 Python usage

Requires **Python 3.8+**, `imageio`, `numpy`, and FFmpeg installed.

Run:
pip install imageio numpy


Example:
python solid_color_video.py -hex "#008B8B" -q 1920x1080 -fps 60 -t 10 -bit 10m -engine h264 -out 008B8B.mp4


Arguments:
-hex (required) → Hex color (#RRGGBB or #RGB)

-q → Resolution (default: 1920x1080)

-fps → Frames per second (default: 60)

-t → Duration in seconds (default: 10)

-bit → Bitrate (10k, 500k, 2m, 0.01g; default: 10m)

-engine → Codec (h264 or h265; default: h264)

-out → Output filename (default: <hex>.mp4)


🌐 Web usage
Just open index.html in any modern browser (tested in Chrome/Edge/OperaGX/Firefox).
Runs entirely client-side — no server required.

Features:
Color input (hex field + palette picker)

Resolution, FPS, Duration

Codec selector (H264, VP8, VP9 depending on browser)

Download button when video is ready


📜 License
This project is licensed under the GNU General Public License v3.0 (GPLv3).
You are free to use, modify, and distribute it under the same license.

🙌 Credits
Python implementation: imageio + FFmpeg

Web implementation: HTML5 <canvas> + MediaRecorder API
