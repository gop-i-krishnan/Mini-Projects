
## ⏰ Python Alarm Clock with Music

This is a simple Python script that allows you to set an alarm for a specific time. When the alarm time is reached, it plays an MP3 sound file using `pygame`.

## 📦 Requirements

- Python 3.x
- `pygame` library

You can install `pygame` using pip:

```bash
pip install pygame
````

## 🎵 Sound File

The script expects an MP3 file named:

```
Dopamina - Inaban.mp3
```

Place this file in the **same directory** as the script. If the file is not found, an error will be displayed.

## 🧠 How It Works

1. You run the script.
2. You enter an alarm time in the format `HH:MM:SS` (24-hour format).
3. The script continuously checks the current time.
4. When the time matches, it plays the MP3 file in a loop for 60 seconds.

## ▶️ Usage

Run the script:

```bash
python alarm_clock.py
```

Then enter the alarm time, like:

```
Enter the alarm time (HH:MM:SS): 07:30:00
```

## ⚠️ Notes

* Make sure your system audio is enabled.
* The alarm will only go off if the script is running and the computer is awake.
* Time must be entered in **24-hour format** (`13:00:00` for 1 PM).

## 📁 File Structure

```
alarm_clock.py
Dopamina - Inaban.mp3
README.md
```

## 📜 License

This project is open source and free to use for personal projects.

```
