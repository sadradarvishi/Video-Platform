import subprocess
from celery import shared_task
from django.core.mail import send_mail

from VideoProcessing.entity.video_entity import VideoEntity  # import your video model

@shared_task
def process_video(video_id):
    try:
        video = VideoEntity.objects.get(id=video_id)
        video.status = 'processing'
        video.save()

        # Paths (MEDIA_ROOT + upload path)
        input_path = video.file.path
        output_path = input_path.replace('videos/', 'processed/') + '.mp4'
        thumbnail_path = input_path.replace('videos/', 'thumbnail/') + '.jpg'

        # Transcode with FFmpeg
        subprocess.run(['ffmpeg', '-i', input_path, '-c:v', 'libx264', output_path], check=True)

        # Generate thumbnail
        subprocess.run(['ffmpeg', '-i', input_path, '-ss', '00:00:01', '-vframes', '1', thumbnail_path], check=True)

        # Save results
        video.processed_file.name = output_path.replace('media/', '')
        video.thumbnail.name = thumbnail_path.replace('media/', '')
        video.status = 'completed'
        video.save()

        send_video_status_email.delay(video.creator.email, video.id, 'completed')

    except Exception as e:
        video.status = 'failed'
        video.save()

        send_video_status_email.delay(video.creator.email, video.id, 'failed')

        raise e

@shared_task
def send_video_status_email(user_email, video_id, status):
    subject = f"Your video #{video_id} has been {status}"
    message = f"Hello,\n\nYour video with ID {video_id} has been {status}.\n\nThanks!"
    send_mail(
        subject,
        message,
        'sadsaddardar@gmail.com',
        [user_email],
        fail_silently=False
    )