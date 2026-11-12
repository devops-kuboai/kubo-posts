import sys,os;sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
from kubodark import *
from PIL import ImageFilter
import os;src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'build_ah.py')).read();exec(src[src.index('def chat():'):])
ph=chat().crop((508,85,1029,1024)).convert('RGBA')  # só o celular
_m=Image.new('L',ph.size,0);ImageDraw.Draw(_m).rounded_rectangle((0,0,ph.width-1,ph.height+80),55,fill=255);ph.putalpha(_m)
YEL=(255,214,10)
def grad(c1,c2,ang=True):
    y,x=np.mgrid[0:H,0:W];t=(x/W*0.45+y/H*0.55)
    g=np.dstack([c1[i]*(1-t)+c2[i]*t for i in range(3)])
    return Image.fromarray(g.astype(np.uint8)).convert('RGBA')
def stamp(img,t,x,y,bg,fg,size=26):
    d=ImageDraw.Draw(img);fo=f('Black',size);w=d.textlength(t,font=fo)
    d.rounded_rectangle((x,y,x+w+44,y+size+26),12,fill=bg);d.text((x+22,y+11),t,font=fo,fill=fg)
def foot(img,light=True):
    d=ImageDraw.Draw(img);img.alpha_composite(K.CUBE.resize((58,62)),(70,H-122))
    d.text((142,H-114),'KUBO AI',font=f('Bold',32),fill='white');d.text((142,H-78),'@_kuboai',font=f('Medium',23),fill=(225,232,255))
