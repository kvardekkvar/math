import wx

x=1
y=2
z=3
xx=1
yy=2
zz=3

def flip(a,b):
    return 2*b-a, b

def xy(event):
    global x
    global y
    global z
    x,y = flip(x,y)
    global xx
    global yy
    global zz
    yy,xx = flip(yy,xx)
    global text1
    global text2
    label1 = "(" + str(x) + " ; " + str(y) + " ; " + str(z) + ")"
    label2 = "(" + str(xx) + " ; " + str(yy) + " ; " + str(zz) + ")"
    text1.SetLabel(label1)
    text2.SetLabel(label2)
def yx(event):
    global x
    global y
    global z
    y,x = flip(y,x)
    global xx
    global yy
    global zz
    xx,yy = flip(xx,yy)
    global text1
    global text2
    label1 = "(" + str(x) + " ; " + str(y) + " ; " + str(z) + ")"
    label2 = "(" + str(xx) + " ; " + str(yy) + " ; " + str(zz) + ")"
    text1.SetLabel(label1)
    text2.SetLabel(label2)
def yz(event):
    global x
    global y
    global z
    y, z = flip(y, z)
    global xx
    global yy
    global zz
    zz, yy = flip(zz, yy)
    global text1
    global text2
    label1 = "(" + str(x) + " ; " + str(y) + " ; " + str(z) + ")"
    label2 = "(" + str(xx) + " ; " + str(yy) + " ; " + str(zz) + ")"
    text1.SetLabel(label1)
    text2.SetLabel(label2)
def zy(event):
    global x
    global y
    global z
    z, y = flip(z, y)
    global xx
    global yy
    global zz
    yy,zz = flip(yy,zz)
    global text1
    global text2
    label1 = "(" + str(x) + " ; " + str(y) + " ; " + str(z) + ")"
    label2 = "(" + str(xx) + " ; " + str(yy) + " ; " + str(zz) + ")"
    text1.SetLabel(label1)
    text2.SetLabel(label2)
def xz(event):
    global x
    global y
    global z
    x, z = flip(x, z)
    global xx
    global yy
    global zz
    zz, xx = flip(zz, xx)
    global text1
    global text2
    label1 = "(" + str(x) + " ; " + str(y) + " ; " + str(z) + ")"
    label2 = "(" + str(xx) + " ; " + str(yy) + " ; " + str(zz) + ")"
    text1.SetLabel(label1)
    text2.SetLabel(label2)
def zx(event):
    global x
    global y
    global z
    z,x = flip(z,x)
    global xx
    global yy
    global zz
    xx,zz = flip(xx,zz)
    global text1
    global text2
    label1 = "(" + str(x) + " ; " + str(y) + " ; " + str(z) + ")"
    label2 = "(" + str(xx) + " ; " + str(yy) + " ; " + str(zz) + ")"
    text1.SetLabel(label1)
    text2.SetLabel(label2)

app = wx.App()
frame = wx.Frame(None, -1, 'Kuznetchiks')
frame.SetDimensions(0,0,800,600)

panel = wx.Panel(frame, wx.ID_ANY)
buttonxy = wx.Button(panel, wx.ID_ANY, 'xy', (10, 10))
buttonxy.Bind(wx.EVT_BUTTON, xy)
buttonyx = wx.Button(panel, wx.ID_ANY, 'yx', (10, 40))
buttonyx.Bind(wx.EVT_BUTTON, yx)

buttonyz = wx.Button(panel, wx.ID_ANY, 'yz', (100, 10))
buttonyz.Bind(wx.EVT_BUTTON, yz)
buttonzy = wx.Button(panel, wx.ID_ANY, 'zy', (100, 40))
buttonzy.Bind(wx.EVT_BUTTON, zy)

buttonxz = wx.Button(panel, wx.ID_ANY, 'xz', (200, 10))
buttonxz.Bind(wx.EVT_BUTTON, xz)
buttonzx = wx.Button(panel, wx.ID_ANY, 'zx', (200, 40))
buttonzx.Bind(wx.EVT_BUTTON, zx)

label1 = "(" + str(x)+" ; "+str(y) + " ; " + str(z) + ")"
label2 = "(" + str(xx)+" ; "+str(yy) + " ; " + str(zz) + ")"

text1 = wx.StaticText(panel, id=wx.ID_ANY, label=label1, pos=(10,70))
text2 = wx.StaticText(panel, id=wx.ID_ANY, label=label2, pos=(10,100))


frame.Show(True)
#frame.Maximize()

app.MainLoop()

