import argparse
import re
import numpy as np
import imageio

def parse_hex_color(s: str):
    """Convert #RRGGBB or #RGB to (R,G,B) uint8 tuple."""
    s = s.strip()
    if not s.startswith("#"):
        s = "#" + s
    if not re.fullmatch(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})", s):
        raise ValueError(f"Invalid hex color: {s}")
    hexpart = s[1:]
    if len(hexpart) == 3:
        hexpart = "".join(ch * 2 for ch in hexpart)
    r = int(hexpart[0:2], 16)
    g = int(hexpart[2:4], 16)
    b = int(hexpart[4:6], 16)
    return r, g, b

def main():
    parser = argparse.ArgumentParser(description="Generate a solid-color video from hex code.")
    parser.add_argument("-hex", required=True, help='Hex color like "#FF0000" or "09f"')
    parser.add_argument("-q", default="1920x1080", help="Resolution, e.g. 1920x1080 (default: 1920x1080)")
    parser.add_argument("-fps", type=int, default=60, help="Frames per second (default: 60)")
    parser.add_argument("-t", type=float, default=10.0, help="Duration in seconds (default: 10)")
    parser.add_argument("-out", help="Output filename (default: <hex>.mp4)")
    args = parser.parse_args()

    # Parse resolution
    try:
        width, height = map(int, args.q.lower().split("x"))
    except Exception:
        raise ValueError("Resolution must be in WIDTHxHEIGHT format, e.g. 1920x1080")

    # Parse hex color
    r, g, b = parse_hex_color(args.hex)

    # Default output file: <hex>.mp4
    out_file = args.out if args.out else args.hex.replace("#", "") + ".mp4"

    fps = args.fps
    total_frames = int(round(args.t * fps))

    # Single frame of given color
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    frame[:, :] = [r, g, b]

    # Write video
    writer = imageio.get_writer(
        out_file,
        fps=fps,
        codec="libx264",
        format="ffmpeg",
        macro_block_size=None,
        ffmpeg_params=["-movflags", "+faststart"],
        bitrate="10M"
    )

    try:
        for _ in range(total_frames):
            writer.append_data(frame)
    finally:
        writer.close()

    print(f"✅ Done. Wrote {out_file} ({args.t}s @ {fps}fps, {width}x{height}, color #{r:02X}{g:02X}{b:02X}).")

if __name__ == "__main__":
    main()
