"""Reel final da pizzaria (25/11): 4 cenas, transições animadas entre telas, render contínuo."""
import sys,os,subprocess
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import reel_pizzaria as R
from loja_noite import *
from PIL import ImageFilter
FPS=30;TR=0.55
def e(x): x=max(0,min(1,x));return x*x*(3-2*x)
def push(A,B,p):  # empurra para a esquerda
    p=e(p);o=Image.new('RGB',(W,H));o.paste(A,(int(-W*p),0));o.paste(B,(int(W*(1-p)),0));return o
def zoom(A,B,p):  # A amplia e some, B surge levemente reduzido
    p=e(p);s=1+0.25*p;a=A.resize((int(W*s),int(H*s)));a=a.crop(((a.width-W)//2,(a.height-H)//2,(a.width-W)//2+W,(a.height-H)//2+H))
    if p<0.5: a=a.filter(ImageFilter.GaussianBlur(6*p*2))
    sb=0.9+0.1*p;b=B.resize((int(W*sb),int(H*sb)));bb=Image.new('RGB',(W,H),B.getpixel((5,5)));bb.paste(b,((W-b.width)//2,(H-b.height)//2))
    return Image.blend(a,bb,p)
def up(A,B,p):  # B sobe por cima de A
    p=e(p);o=A.copy();d=ImageDraw.Draw(o);o.paste(B,(0,int(H*(1-p))));return o
cenas=[('1',R.cena1),('3',R.cena3),('4',R.cena4),('5',R.cena5)];trans=[push,zoom,up]
durs={k:float(os.environ['DUR'+k]) for k,_ in cenas}
out=sys.argv[1];tmp=out+'.tmp.mp4'
p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
   '-c:v','libx264','-crf','18','-preset','veryfast','-pix_fmt','yuv420p',tmp],stdin=subprocess.PIPE)
prev_last=None
for i,(k,fn) in enumerate(cenas):
    f,_=fn();du=durs[k];n=int(round(du*FPS))
    for j in range(n):
        t=j/FPS;fr=f(t).convert('RGB')
        if i==0 and t<0.25: fr=Image.blend(Image.new('RGB',(W,H),'white'),fr,t/0.25)
        if i>0 and t<TR: fr=trans[i-1](prev_last,fr,t/TR)
        p.stdin.write(fr.tobytes())
    prev_last=f(du-1/FPS).convert('RGB')
p.stdin.close();assert p.wait()==0;os.replace(tmp,out);print('ok')
