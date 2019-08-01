import cv2


class WindowManager(object):

    def __init__(self, windowName, keypressCallback=None):
        self.keypressCallback = keypressCallback
        self._windowName = windowName
        self._isWindowCreadted = False

    @property
    def isWindowCreated(self):
        return self._isWindowCreadted

    def createWindow(self):
        cv2.namedWindow(self._windowName)
        self._isWindowCreadted = True

    def show(self, frame):
        cv2.imshow(self._windowName, frame)

    def destroyWindow(self):
        cv2.destroyWindow(self._windowName)
        self._isWindowCreadted = False

    def processEvents(self):
        keycode = cv2.waitKey(1)
        if self.keypressCallback is not None and keycode != -1:
            # Discard any non-ASCII ifo encoded by GTK
            keycode &= 0xFF
            self.keypressCallback(keycode)
