import cv2
from CaptureManager import CaptureManager
from WindowManager import WindowManager


class Cameo(object):

    def __init__(self):

        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)

    def run(self):
        self._windowManager.createWindow()

        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()

        #     frame = self._captureManager.frame
        #
        #     # Filter the frame
        #
        #     self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keycode):
        """
        handle a keypress
        space -> take a screen shot
        tab -> start/stop recording a screencast
        escape -> quit
        """
        # space
        if keycode == 32:
            self._captureManager.writeImage('screenshot.png')
        # tab
        elif keycode == 9:
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('screencast.avi')
            else:
                self._captureManager.stopWritingVideo()

        # escape
        elif keycode == 27:
            self._windowManager.destroyWindow()


if __name__ == "__main__":
    C = Cameo()
    C.run()

