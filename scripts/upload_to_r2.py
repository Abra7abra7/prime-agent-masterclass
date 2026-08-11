#!/usr/bin/env python3
"""Upload course videos to Cloudflare R2."""
import os, json, mimetypes, boto3
from botocore.config import Config
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_ID = os.getenv('CLOUDFLARE_ACCOUNT_ID')
ACCESS_KEY = os.getenv('CLOUDFLARE_R2_ACCESS_KEY_ID')
SECRET_KEY = os.getenv('CLOUDFLARE_R2_SECRET_ACCESS_KEY')
BUCKET = os.getenv('CLOUDFLARE_R2_BUCKET', 'prime-agent-courses')
ENDPOINT = os.getenv('CLOUDFLARE_R2_ENDPOINT')

s3 = boto3.client('s3',
    endpoint_url=ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    config=Config(signature_version='s3v4'),
    region_name='auto'
)

video_dir = Path('video/output')
for mp4 in video_dir.rglob('*.mp4'):
    key = f"videos/{mp4.relative_to(video_dir)}"
    print(f"Uploading {mp4.name} -> {key}...")
    s3.upload_file(str(mp4), BUCKET, key, ExtraArgs={'ContentType': 'video/mp4', 'ACL': 'public-read'})
    print(f"  OK https://{BUCKET}.{ACCOUNT_ID}.r2.dev/{key}")

for html_file in video_dir.rglob('*.html'):
    key = f"videos/{html_file.relative_to(video_dir)}"
    print(f"Uploading {html_file.name} -> {key}...")
    s3.upload_file(str(html_file), BUCKET, key, ExtraArgs={'ContentType': 'text/html; charset=utf-8', 'ACL': 'public-read'})
    print(f"  OK https://{BUCKET}.{ACCOUNT_ID}.r2.dev/{key}")

print("\nAll videos uploaded to Cloudflare R2!")
