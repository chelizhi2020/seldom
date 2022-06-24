"""
App keyboard operation
"""

keycodes = {
    '0': 7,
    '1': 8,
    '2': 9,
    '3': 10,
    '4': 11,
    '5': 12,
    '6': 13,
    '7': 14,
    '8': 15,
    '9': 16,
    'A': 29,
    'B': 30,
    'C': 31,
    'D': 32,
    'E': 33,
    'F': 34,
    'G': 35,
    'H': 36,
    'I': 37,
    'J': 38,
    'K': 39,
    'L': 40,
    'M': 41,
    'N': 42,
    'O': 43,
    'P': 44,
    'Q': 45,
    'R': 46,
    'S': 47,
    'T': 48,
    'U': 49,
    'V': 50,
    'W': 51,
    'X': 52,
    'Y': 53,
    'Z': 54,
    ' ': 62,
    '*': 17,
    '#': 18,
    ',': 55,
    '`': 68,
    '-': 69,
    '[': 71,
    ']': 72,
    '\\': 73,
    ';': 74,
    '/': 76,
    '@': 77,
    '=': 161,
    '.': 158,
    '+': 157,
    'NUM_LOCK': 143,
    'CAPS_LOCK': 115,
    'HOME': 4,
    'BACK': 3,
}


class KeyEvent:
    """
    KeyEvent:
    https://developer.android.com/reference/android/view/KeyEvent
    """

    def __init__(self, driver):
        self.driver = driver

    def key_text(self, text=""):
        """
        keyword input text
        """
        if text == "":
            return

        for s in text:
            keycode = keycodes.get(s.upper(), 0)
            if keycode == 0:
                raise KeyError(f"The '{s}' character is not supported")
            self.driver.keyevent(keycode)

    def press_key(self, key):
        """
        keyboard
        :param key:
        :return:
        """
        keycode = keycodes.get(key)
        self.driver.press_keycode(keycode)

    def key_text_capital(self, text=""):
        """
        appium API
        keyword input capital text
        Usage:
            self.key_text_capital("HELLO")
        """
        if text == "":
            return

        for s in text:
            keycode = keycodes.get(s.upper(), 0)
            if keycode == 0:
                raise KeyError(f"The '{s}' character is not supported")
            self.driver.press_keycode(keycode, 64, 59)

    def back(self):
        """go back"""
        self.driver.back()

    def home(self):
        """press home"""
        self.driver.home()
