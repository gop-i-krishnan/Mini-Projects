import datetime
import time
import pygame
import os

def set_alarm(alarm_time):
    print(f'Alarm set for {alarm_time}')
    sound_file = "Dopamina - Inaban.mp3"

    # Check if the sound file exists
    if not os.path.exists(sound_file):
        print(f"Error: Sound file '{sound_file}' not found.")
        return

    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(f"Current time: {current_time}", end="\r")  # Updates the line in terminal

        if current_time == alarm_time:
            print("\nWAKE UP ⏰")

            # Initialize the mixer
            pygame.mixer.init()
            try:
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play(-1)  # Loop indefinitely

                # Play sound for a specified duration or until interrupted
                play_duration = 60  # Play for 60 seconds
                start_time = time.time()

                while time.time() - start_time < play_duration:
                    time.sleep(1)
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.play(-1)  # Ensure continuous looping

                pygame.mixer.music.stop()
                is_running = False
            except pygame.error as e:
                print(f"Error: {e}")
                is_running = False

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")

    # Validate the time format
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
        set_alarm(alarm_time)
    except ValueError:
        print("Invalid time format. Please enter the time in HH:MM:SS format.")
