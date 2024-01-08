from pytube import YouTube

try:
    # Ask the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")
    
    yt = YouTube(url)
    
    print("Title of youtube video :", yt.title)
    print("Views on that video :", yt.views)

    # Get the highest resolution stream
    yd = yt.streams.get_highest_resolution()
    
    # Download the video to the current directory
    yd.download()
    
    print("Download complete successfully .")
except Exception as e:
    print("An error occurred:", str(e))