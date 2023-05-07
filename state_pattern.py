class State(object):
    def __init__(self):
        self.name = None

    def wait(self):
        pass
        
    def notify(self):
        pass

class TrafficLight(object):
    def __init__(self):
        self.state = None 

    def setState(self, state: State):
        self.state = state 

    def wait(self):
        self.state.wait(self)

    def notify(self):
        self.state.notify()

class GreenState(State):
    def __init__(self):
        self.name = 'green light' 

    def wait(self, _traffic_light: TrafficLight):
        _traffic_light.setState(RedState()) 

    def notify(self):
        print(f"{self.name}")

class RedState(State):
    def __init__(self):
        self.name = 'red light'

    def wait(self, _traffic_light: TrafficLight):
        _traffic_light.setState(GreenState())

    def notify(self):
        print(f'{self.name}')
    
if __name__ == '__main__':
    traffic_light = TrafficLight()
    traffic_light.setState(GreenState())
    traffic_light.notify()
    traffic_light.wait()
    traffic_light.notify()
