from machine import Pin

class Application:
    def __init__(self):
        self.SleepTime = 0

        self.Init()
    
    def Init(self):
        pass
    
    def Update(self):
        pass
    
    def Run(self):
        while True:
            self.Update()

            if self.sleepTime > 0:
                time.sleep(self.SleepTime)

class Enabler:
    def __init__(self, lastEnabled=False, enabled=True):
        self.lastEnabled = lastEnabled
        self.enabled = enabled

        self.Update()
    
    def OnEnable(self):
        pass
    
    def OnDisable(self):
        pass
    
    def Enable(self):
        self.enabled = True
    
    def Disable(self):
        self.enabled = False

    def IsEnabled(self):
        return self.enabled
    
    def Update(self):
        if self.enabled and not self.lastEnabled:
            self.OnEnable()
        elif self.lastEnabled and not self.enabled:
            self.OnDisable()

class Input:
    def __init__(self, pin):
        self.pin = Pin(pin, Pin.IN)

    def Read(self):
        return self.pin.value()
    
class Output:
    def __init__(self, pin):
        self.pin = Pin(pin, Pin.OUT)

        self.WriteLow()
    
    def Read(self):
        return self.pin.value()
    
    def Toggle(self):
        self.pin.toggle()

    def WriteHigh(self):
        self.pin.value(1)
    
    def WriteLow(self):
        self.pin.value(0)

class Button(Input):
    def __init__(self, pin):
        super().__init__(pin)

class LED(Output):
    def __init__(self, pin):
        super().__init__(pin)