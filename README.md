# Discord.py Bot Structure

A clean and extensible Discord.py bot structure with support for slash commands, event handling, and guild sync. This template is designed to help you quickly get up and running with a fully functional Discord bot.

## Features

- **Slash Commands**: Built-in support for Slash Commands.
- **Event Handling**: Easily manage events in separate files.
- **Command Loader**: Automatically load and sync commands from the separate files.
- **Guild Sync**: Option to sync commands to a specific guild for testing.
- **Extendable**: A flexible structure you can expand with more features.

## Prerequisites

Before you start, make sure you have:

- Python 3.8+ installed
- A [Discord Developer Account](https://discord.com/developers/docs/intro)
- A Discord Bot Token (You can get one by creating an app in the [Discord Developer Portal](https://discord.com/developers/applications))

## Setup

### 1. Clone the repository

Start by cloning the repository to your computer.

### 2. Install Dependencies

Install discord.py using PyPi:

```bash
python3 -m pip install -U discord.py
```

### 3. Set up the Bot Token

Go to `src/config.json`. In this file you can edit the bot token and testing guild ID. The bot token needs to be an *integer*.

### 4. Running the Bot

Once everything is set up, you can run your bot with the following command:

```bash
python src/main.py
```

Your bot should now be running, and it will log in to Discord usign the bot token you provided.

## Folder Structure

Here is a breakdown of the folder structure:

```bash
src/
├── main.py                # Main entry point to start the bot
├── config.json            # Config for bot token and testing guild id
├── utils/
│   └── event_handler.py   # Event handler for loading events
│   └── command_loader.py  # Loads commands into the tree
├── events/
│   └── on_ready.py        # Loads and syncs commands
│   └── on_message.py      # Cdoe for on_message event (empty)
└── commands/
    ├── ping.py            # Example command (Ping command)
    └── template.txt       # Copy this when you create new command files
```

## Customizing the Bot

You can customize this bot by:
- Adding more commands in the `commands/` folder. To create a new command:
  - Copy everything in `src/commands/template.txt`
  - Create a file with the same name as the command and paste the template
  - Edit the name and description at the bottom of the file
  - Add your code under the `run()` method
- Toggling 'testing mode' in `src/events/on_ready.py`
  - True = Load commands globally, takes up to 1 hour
  - False = Load commands to testing guild only, syncs instantly. Preferred for development
- Creating more events in `src/events`
  - Copy everything in `src/events/template.txt`
  - Create a file with the same name of the event and paste the template
  - Add your code under the `run()` function
- Any way you wish 😀

## Contribution

Feel free to fork the repository and contribute. If you have any improvements, fixes, or new features, open a pull request!
