
# intro video from https://pixabay.com/videos/button-youtube-intro-outro-84507/
# end of video from https://pixabay.com/videos/intro-outro-end-screen-youtube-94551/
# the main video from me or you if you have this script 🙃

import moviepy.editor as mp

# load videos
main_video_path = 'youtube video editor script add intro and end to your youtube videos.mp4'
main_video = mp.VideoFileClip(main_video_path) # your video here 🙂
video_width, video_height = main_video.w, main_video.h

# add start and end to main video

start_video = mp.VideoFileClip('start.mp4').resize((video_width, video_height))
end_video = mp.VideoFileClip('end.mp4').resize((video_width, video_height))

full_video = mp.concatenate_videoclips([start_video, main_video, end_video], method="compose")
full_video.write_videofile('out ' + main_video_path, verbose=False, logger=None)
print('The videos have been merged successfully ;)')
