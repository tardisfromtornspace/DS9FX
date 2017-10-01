# Monitors the state of a dock button and disables it in DS9FX systems since DS9FX has its own dock mechanism

import App
import DS9FXMenuLib
import DS9FXSets

timer = None


def Initialize():
    global timer

    if not timer:
        timer = ButtonMonitor()
    else:
        return


class ButtonMonitor:
    def __init__(self):
        self.timer = None
        self.__countdown()

    def __countdown(self):
        if not self.timer:
            self.timer = App.PythonMethodProcess()
            self.timer.SetInstance(self)
            self.timer.SetFunction("monitor")
            self.timer.SetDelay(15)
            self.timer.SetPriority(App.TimeSliceProcess.LOW)
            self.timer.SetDelayUsesGameTime(1)

    def monitor(self, time):
        if DS9FXSets.IsInSet():
            button = DS9FXMenuLib.GetDockButton()
            if not button:
                return
            if button.IsEnabled():
                button.SetDisabled()
