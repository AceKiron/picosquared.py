import picosquared as ps

class MyEnabler(ps.Enabler):
    def __init__(self, led, led_onboard):
        super().__init__(False, True)

        self.led = led
        self.led_onboard = led_onboard

    def OnEnable(self):
        self.led_onboard.WriteHigh()
    
    def OnDisable(self):
        self.led_onboard.WriteLow()
        self.led.WriteLow()

class MyApp(ps.Application):
    def Init(self):
        self.SleepTime = 0.1

        self.led = ps.LED(14)
        self.led_onboard = ps.LED(25)

        self.button1 = ps.Button(12)
        self.button2 = ps.Button(13)

        self.enabler = MyEnabler(False, True)

    def Update(self):
        if self.button1.Read():
            self.enabler.Enable()
        elif self.button2.Read():
            self.enabler.Disable()
        
        self.enabler.Update()
        
        if self.enabler.IsEnabled():
            self.led.Toggle()
        
MyApp().run()