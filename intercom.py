from RPi import GPIO
import phone

_BUZZER_GPIO = 21


def buzzer_press_event_callback():
    ''' Callback when a buzzer edge is detected '''
    phone.notify_buzzer_pressed()


def gpio_setup():
    ''' Configure the gpio's '''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(_BUZZER_GPIO, GPIO.IN)
    GPIO.add_event_detect(_BUZZER_GPIO,
                          GPIO.RISING,
                          callback=buzzer_press_event_callback,
                          bouncetime=200)


def gpio_cleanup():
    ''' Cleanup the GPIOs '''
    GPIO.cleanup()
