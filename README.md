# Audio-Extractor
This Python script allows you to download the audio from a YouTube video and save it as an MP3 file. It uses the pytube library to interact with YouTube and download the desired content.

## Prerequisites
Before running the script, make sure you have the following:

Python 3.x installed on your system.
The pytube library installed. You can install it using the following command:
pip install pytube

## Usage
1. Run the script by executing the following command in your terminal or command prompt:
python youtube_audio_downloader.py
2. When prompted, paste the YouTube link of the video from which you want to download the audio.

3. Specify the destination folder where you want to save the downloaded MP3 file. Update the destination variable in the script with the desired path. For example:
destination = "/path/to/your/folder"

4. After running the script, it will retrieve the audio stream from the YouTube video and convert it to an MP3 file.

5. The downloaded MP3 file will be saved in the specified destination folder with the same name as the YouTube video's title.

## Disclaimer
Please note that downloading copyrighted content from YouTube without proper authorization may violate YouTube's terms of service and copyright laws in your jurisdiction. This script is intended for educational and personal use with content that you have the legal right to download. Use it responsibly and respect the content creators' rights.

## Note
This script is provided as-is and may not handle all possible scenarios or YouTube video formats. It's recommended to test the script with different videos and formats to ensure its functionality meets your needs.
