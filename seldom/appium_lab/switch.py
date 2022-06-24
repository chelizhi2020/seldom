"""
author: zhiheng.hu
data: 2022/5/26
desc: appium 提供的 switch: 切换上下文
"""
from time import sleep as py_sleep
from seldom.logging import log


class Switch:

    def __init__(self, driver):
        self.driver = driver

    def switch_to_app(self) -> None:
        """
        Switch to native app.
        """
        current_context = self.driver.current_context
        if current_context != "NATIVE_APP":
            log.info("🔀 switch to native app.")
            self.driver.switch_to.context('NATIVE_APP')

    def switch_to_web(self, context=None) -> None:
        """
        Switch to web view.
        """
        log.info("🔀 switch to webview.")
        if context is not None:
            self.driver.switch_to.context(context)
        else:
            all_context = self.driver.contexts
            for context in all_context:
                if "WEBVIEW" in context:
                    self.driver.switch_to.context(context)
                    break
            else:
                raise NameError("No WebView found.")

    def switch_to_flutter(self) -> None:
        """
        Switch to flutter app.
        """
        current_context = self.driver.current_context
        if current_context != "FLUTTER":
            log.info("🔀 switch to flutter.")
            self.driver.switch_to.context('FLUTTER')

    @staticmethod
    def sleep(sec) -> None:
        """
        sleep(seconds)
        :param sec
        """
        py_sleep(sec)
