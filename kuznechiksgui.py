import wx

# 3 grasshoppers and 3 anti-grasshoppers live in points 0, 1, 2 on the real line. On each move, grasshopper i jumps over grasshopper j, whereas anti-grasshopper j jumps over anti-grasshopper i. Below is GUI application to follow the history of the grasshoppers.


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

class HoppersView():
    
    
    def __init__(self):
        self.model = HoppersModel()
        
        self.app = wx.App()

        self.frame = wx.Frame(None, -1, 'Kuznetchiks')
        self.frame.SetDimensions(0, 0, 800, 600)

        panel = wx.Panel(self.frame, wx.ID_ANY)

        self.text_hoppers = wx.StaticText(panel, id=wx.ID_ANY, label="", pos=(10, 70))
        self.text_shadows = wx.StaticText(panel, id=wx.ID_ANY, label="", pos=(10, 100))
        
        self.buttonxy = wx.Button(panel, wx.ID_ANY, 'x over y', (10, 10))
        self.buttonyx = wx.Button(panel, wx.ID_ANY, 'y over x', (10, 40))
        self.buttonyz = wx.Button(panel, wx.ID_ANY, 'y over z', (100, 10))
        self.buttonzy = wx.Button(panel, wx.ID_ANY, 'z over y', (100, 40))
        self.buttonxz = wx.Button(panel, wx.ID_ANY, 'x over z', (200, 10))
        self.buttonzx = wx.Button(panel, wx.ID_ANY, 'z over x', (200, 40))

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

    def flip_hoppers(self, i: int, j: int):
        assert i != j
        
        model = self.model
        view = self.view
        
        hopper_connection_1 = model.hoppers_list[i]
        hopper_connection_2 = model.hoppers_list[j]
        
        hopper1_coordinate = hopper_connection_1.hopper.get_coordinate()
        hopper2_coordinate = hopper_connection_2.hopper.get_coordinate()
        
        hopper1_coordinate, hopper2_coordinate = HoppersModel.flip(hopper1_coordinate, hopper2_coordinate)
        
        hopper_connection_1.hopper.set_coordinate(hopper1_coordinate)
        hopper_connection_2.hopper.set_coordinate(hopper2_coordinate)

        
        shadow1_coordinate = hopper_connection_1.shadow.get_coordinate()
        shadow2_coordinate = hopper_connection_2.shadow.get_coordinate()        

        shadow2_coordinate, shadow1_coordinate = HoppersModel.flip(shadow2_coordinate, shadow1_coordinate)
        
        hopper_connection_1.shadow.set_coordinate(shadow1_coordinate)
        hopper_connection_2.shadow.set_coordinate(shadow2_coordinate)

        view.update_labels()

    def fill_hoppers_list(self):
        hoppers = self.model
        for i in range(3):
            hopper = RealHopper(i)
            shadow = ShadowHopper(i)
            pair = HopperPair(hopper, shadow)
            hoppers.hoppers_list.append(pair)


    def bind_buttons(self):
        view = self.view
        
        view.buttonxy.Bind(wx.EVT_BUTTON, lambda t: self.flip_hoppers(0,1))
        view.buttonyx.Bind(wx.EVT_BUTTON, lambda t: self.flip_hoppers(1,0))
        view.buttonzy.Bind(wx.EVT_BUTTON, lambda t: self.flip_hoppers(2,1))
        view.buttonzx.Bind(wx.EVT_BUTTON, lambda t: self.flip_hoppers(2,0))
        view.buttonyz.Bind(wx.EVT_BUTTON, lambda t: self.flip_hoppers(1,2))
        view.buttonxz.Bind(wx.EVT_BUTTON, lambda t: self.flip_hoppers(0,2))

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