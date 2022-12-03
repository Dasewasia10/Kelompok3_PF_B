from abc import ABCMeta, abstractstaticmethod

# Reciever
class Light:
    
    def Switch_On(self):
        print("The Light is ON.")
    
    def Switch_Off(self):
        print("The Light is OFF.")


# Command Interface
class ICommand(metaclass=ABCMeta):

    @abstractstaticmethod
    def execute():
        """a static interface method"""

class SwitchOnCommand(ICommand):
    def __init__(self, light):
        self._light = light
    
    def execute(self):
        self._light.Switch_On()

class SwitchOffCommand(ICommand):
    def __init__(self, light):
        self._light = light
    
    def execute(self):
        self._light.Switch_Off()

# Invoker
class Switch:
    """The Invoker Class"""

    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands:
            self._commands[command_name].execute()
        else:
            print("command not found.")

# Client 
if __name__ == "__main__":
    #Reciever
    LIGHT = Light()

    # Commands
    SWITCH_ON = SwitchOnCommand(LIGHT)
    SWITCH_OFF = SwitchOffCommand(LIGHT)

    # Invoker
    SWITCH = Switch()

    # Register commands in the invoker
    SWITCH.register("ON", SWITCH_ON)
    SWITCH.register("OFF", SWITCH_OFF)

    SWITCH.execute("ON")
    SWITCH.execute("OFF")