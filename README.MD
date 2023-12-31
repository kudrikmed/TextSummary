# Telegram Bot for Video and Article Summarization

This Telegram bot is designed to provide summaries for both YouTube videos and text-based articles. It utilizes the Whisper model from OpenAI for speech-to-text conversion and the BERT model for summarization.

## Features

- **Summarization of YouTube Videos**: Simply send the bot a YouTube link, and it will provide a summary of the video content.
- **Summarization of Text Articles**: Share a URL to an article, and the bot will generate a summary of the article's content.
- **Text File Downloads**: Ability to download full text or summarized versions in `.txt` format for both videos and articles.

## Installation and Setup

To deploy this bot, follow these steps:

1. Clone this repository.
2. Install the required dependencies.
    ```bash
    pip install -r requirements.txt
    ```
3. Make sure, that [ffmpeg](https://www.ffmpeg.org/download.html) is installed on your machine.
4. Run the bot.
    ```bash
    python telegram_bot.py
    ```

## Usage

1. Start the bot by sending a message with the `/start` or `/help` command.
2. Share a YouTube URL or a URL to a text-based article to receive a summary.
3. For YouTube links, the bot will transcribe the video and generate a summary.
4. For articles, it will extract the text and provide a concise summary.

## Try bot
- [SummarEaseBot](https://t.me/SummarEaseBot)


![BotImage](bot_example.jpg)
## Contributors

- [Dzmitry Kudrytski](https://github.com/kudrikmed/)

## License

This project is licensed under the [MIT License](link_to_license_file).