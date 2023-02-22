import wx

# 3 grasshoppers and 3 anti-grasshoppers live in points 0, 1, 2 on the real line. On each move, grasshopper i jumps over grasshopper j, whereas anti-grasshopper j jumps over anti-grasshopper i. Below is GUI application to follow the history of the grasshoppers.
NUMBER_OF_HOPPERS = 3

class Hopper():
    def __init__(self, coordinate):
        self.coordinate = coordinate
    
    def set_coordinate(self, coordinate : float):
        self.coordinate = coordinate
    def get_coordinate(self):
        return self.coordinate
    
class RealHopper(Hopper):
    def __init__(self, x):
        super().__init__(x)

class ShadowHopper(Hopper):
    def __init__(self, x):
        super().__init__(x)
        
class HopperPair():
    def __init__(self, hopper : RealHopper, shadow : ShadowHopper):
        self.hopper : RealHopper = hopper
        self.shadow : ShadowHopper = shadow

class HoppersModel():
    def __init__(self, hoppers_list=[]):
        self.hoppers_list = hoppers_list
    
    @staticmethod
    def flip(a, b):
        return 2 * b - a, b


class FlipButton(wx.Button):
    def __init__(self, parent, source = None, destination = None, *args, **kwargs):
        self.source = source
        self.destination = destination
        super().__init__(parent, *args, **kwargs)

class HoppersView():
    
    
    def __init__(self):
        self.model = HoppersModel()
        
        self.app = wx.App()

        self.frame = wx.Frame(None, -1, 'Kuznetchiks')
        self.frame.SetDimensions(0, 0, 800, 600)

        panel = wx.Panel(self.frame, wx.ID_ANY)

        self.text_hoppers = wx.StaticText(panel, id=wx.ID_ANY, label="", pos=(10, 70))
        self.text_shadows = wx.StaticText(panel, id=wx.ID_ANY, label="", pos=(10, 100))
        
        self.buttons = []
        for destination in range(NUMBER_OF_HOPPERS):
            for source in range(NUMBER_OF_HOPPERS):
                if destination <= source:
                    continue
                else:
                    x_coordinate = 150 * (len(self.buttons) // 2) + 10
                    
                    
                    button = FlipButton(panel, id = wx.ID_ANY, label = f"{source + 1} jumps over {destination + 1}", pos = (x_coordinate, 10), source=source, destination=destination)
                    button_reverse = FlipButton(panel, id = wx.ID_ANY, label = f"{destination + 1} jumps over {source + 1}", pos = (x_coordinate, 40), source=destination, destination=source)

                    self.buttons.append(button)
                    self.buttons.append(button_reverse)
                                    
                '''
                        self.buttonxy = wx.Button(panel, wx.ID_ANY, 'x over y', (10, 10))
                        self.buttonyx = wx.Button(panel, wx.ID_ANY, 'y over x', (10, 40))
                        self.buttonyz = wx.Button(panel, wx.ID_ANY, 'y over z', (100, 10))
                        self.buttonzy = wx.Button(panel, wx.ID_ANY, 'z over y', (100, 40))
                        self.buttonxz = wx.Button(panel, wx.ID_ANY, 'x over z', (200, 10))
                        self.buttonzx = wx.Button(panel, wx.ID_ANY, 'z over x', (200, 40))
                '''

    def update_labels(self):
        hopper_pairs = self.model.hoppers_list
        
        label_hoppers = f"({hopper_pairs[0].hopper.coordinate} ; {hopper_pairs[1].hopper.coordinate} ; {hopper_pairs[2].hopper.coordinate})"
        label_shadows = f"({hopper_pairs[0].shadow.coordinate} ; {hopper_pairs[1].shadow.coordinate} ; {hopper_pairs[2].shadow.coordinate})"
        
        self.text_hoppers.SetLabel(label_hoppers)
        self.text_shadows.SetLabel(label_shadows)
class Controller():
    
    def __init__(self):
        self.view = HoppersView()
        self.model = self.view.model

    def flip_hoppers(self, hopper_pair1 : HopperPair, hopper_pair2 : HopperPair, is_shadow : bool = False):
        if not is_shadow:
            hopper1 = hopper_pair1.hopper
            hopper2 = hopper_pair2.hopper 
        else: 
            hopper1 = hopper_pair1.shadow
            hopper2 = hopper_pair2.shadow
                  
        coordinate1 = hopper1.get_coordinate()
        coordinate2 = hopper2.get_coordinate()        

        if not is_shadow:
            coordinate1, coordinate2 = HoppersModel.flip(coordinate1, coordinate2)
        else:
            coordinate2, coordinate1 = HoppersModel.flip(coordinate2, coordinate1)

        hopper1.set_coordinate(coordinate1)
        hopper2.set_coordinate(coordinate2)
            

    def flip_ij(self, i: int, j: int):
        assert i != j
        
        model = self.model
        view = self.view
        
        hopper_pair_1 = model.hoppers_list[i]
        hopper_pair_2 = model.hoppers_list[j]
        
        self.flip_hoppers(hopper_pair_1, hopper_pair_2, True)
        self.flip_hoppers(hopper_pair_1, hopper_pair_2, False)
        
        view.update_labels()

    def fill_hoppers_list(self):
        hoppers = self.model
        for i in range(NUMBER_OF_HOPPERS):
            hopper = RealHopper(i)
            shadow = ShadowHopper(i)
            pair = HopperPair(hopper, shadow)
            hoppers.hoppers_list.append(pair)


    def bind_buttons(self):
        view = self.view
        
        '''
        #Not sure why this doesn't work
        
        for button in view.buttons:
                button : wx.Button = button
                button.Bind(wx.EVT_BUTTON, lambda t: self.flip_ij(button.source, button.destination))
        '''

        view.buttons[0].Bind(wx.EVT_BUTTON, lambda t: self.flip_ij(view.buttons[0].source, view.buttons[0].destination))
        view.buttons[1].Bind(wx.EVT_BUTTON, lambda t: self.flip_ij(view.buttons[1].source, view.buttons[1].destination))
        view.buttons[2].Bind(wx.EVT_BUTTON, lambda t: self.flip_ij(view.buttons[2].source, view.buttons[2].destination))
        view.buttons[3].Bind(wx.EVT_BUTTON, lambda t: self.flip_ij(view.buttons[3].source, view.buttons[3].destination))
        view.buttons[4].Bind(wx.EVT_BUTTON, lambda t: self.flip_ij(view.buttons[4].source, view.buttons[4].destination))
        view.buttons[5].Bind(wx.EVT_BUTTON, lambda t: self.flip_ij(view.buttons[5].source, view.buttons[5].destination))

    def run(self):
        model = self.model
        view = self.view

        self.fill_hoppers_list()
        self.bind_buttons()
        
        view.update_labels()

        view.frame.Show(True)
        view.frame.Maximize()
        view.app.MainLoop()

Controller().run()