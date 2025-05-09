from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import speedtest

class SpeedTestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Add a button to start the speed test
        test_button = Button(text="Test Speed")
        test_button.bind(on_press=self.check_speed)
        layout.add_widget(test_button)

        # Add a label to display the result
        self.result_label = Label(text="Click 'Test Speed' to start")
        layout.add_widget(self.result_label)

        return layout

    def check_speed(self, instance):
        test = speedtest.Speedtest()
        down_speed = test.download() / 1_000_000  # Convert from bits to Mbps
        up_speed = test.upload() / 1_000_000  # Convert from bits to Mbps
        self.result_label.text = f"Download speed: {down_speed:.2f} Mbps\nUpload speed: {up_speed:.2f} Mbps"

if __name__ == "__main__":
    SpeedTestApp().run()
