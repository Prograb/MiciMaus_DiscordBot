import time


def process(url):
    #-------------------download video----------------------------------------
    import pytube

    url = url

    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    video.download('./songs')



    #----------------------convert video---------------------------------------
    import moviepy.editor as mp
    import os
    clip = mp.VideoFileClip("./songs/" + youtube.streams[0].default_filename)
    clip.audio.write_audiofile("song.mp3")