# YouTube Telegram Bot

This project is a Telegram bot that allows users to download videos from YouTube directly through the Telegram interface. It utilizes the `python-telegram-bot` library for bot functionality and `pytube` for downloading videos.

## Features

- Download videos from YouTube by sending a video URL.
- Simple and user-friendly interface.
- Built with Python and designed for easy deployment.

## Project Structure

```
youtube-telegram-bot
├── src
│   ├── bot.py                # Entry point of the Telegram bot
│   ├── handlers
│   │   └── __init__.py       # Command handlers for the bot
│   ├── utils
│   │   └── youtube_downloader.py # Logic for downloading YouTube videos
│   └── config.py             # Configuration settings for the bot
├── requirements.txt           # Project dependencies
├── render.yaml                # Deployment configuration for Render
└── README.md                  # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/youtube-telegram-bot.git
   cd youtube-telegram-bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Telegram bot token in `src/config.py`.

## Usage

1. Run the bot:
   ```
   python src/bot.py
   ```

2. In Telegram, search for your bot and start a chat.

3. Send a YouTube video URL to download the video.

## Deployment

This project is configured for deployment on Render. Ensure that you have set up your Render account and linked it to this repository. The `render.yaml` file contains the necessary configuration for deployment.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.