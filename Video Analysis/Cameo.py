import cv2
from CaptureManager import CaptureManager
from WindowManager import WindowManager
# from Filters import ColorSpace, BGRPortraCurveFilter, strokeEdges
import Filters
import Rects
from Tracker import FaceTracker


class Cameo(object):

    def __init__(self):

        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)

        # self._colorSpace = ColorSpace()
        self._curveFilter = Filters.BGRCrossProcessCurveFilter()
        # self._blurFilter = Filters.BlurFilter()

        self._faceTracker = FaceTracker()
        self._shouldDrawDebugRects = False

    def run(self):
        self._windowManager.createWindow()

        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()

            frame = self._captureManager.frame
            # self._colorSpace.recolorRC(frame, frame)
            # self._blurFilter.apply(frame, frame)

            self._faceTracker.update(frame)
            faces = self._faceTracker.faces
            Rects.swapRects(frame, frame, [face.faceRect for face in faces])

            Filters.strokeEdges(frame, frame)
            self._curveFilter.apply(frame, frame)

            self._faceTracker.drawDebugRects(frame)

            cv2.imshow('Cameo', frame)

            # cv2.imshow('frame', frame)
        #
        #     # Filter the frame
        #
            self._captureManager.exitFrame()
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




