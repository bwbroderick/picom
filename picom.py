""" main module for picom """
import api
import intercom


def run():
    """ sets up GPIOs and webserver """
    intercom.gpio_setup()
    api.start_webserver()