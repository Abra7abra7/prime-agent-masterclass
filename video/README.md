# Video Hosting

Video files are excluded from the git repo. They are served via CDN.

## Upload to CDN

1. Upload video/output/ to your CDN of choice (Vercel Blob, Cloudflare R2, S3)
2. Update the video URLs in the course content

## Generating videos

Run `python3 video/generate_videos.py` to regenerate all videos.
