import sys,os
import numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageOps
F=os.environ.get('KUBO_FONTES','/usr/share/fonts/opentype/inter/')  # pasta com InterDisplay-*.otf
def f(w,s): return ImageFont.truetype(F+f'InterDisplay-{w}.otf',s)
W,H=1080,1350
NAVY=(12,27,64);BLUE=(22,104,240);GR=(84,100,132);BGL=(244,247,252);LINE=(214,224,240)
AQUI=os.path.dirname(os.path.abspath(__file__))
CUBE=Image.open(os.path.join(AQUI,'assets','logo_cubo.png')).convert('RGBA')
LOGO=os.environ.get('LOGO')
def wrap(d,t,fo,maxw):
    out=[];cur=''
    for w in t.split():
        n=(cur+' '+w).strip()
        if d.textlength(n,font=fo)<=maxw: cur=n
        else: out.append(cur);cur=w
    out.append(cur);return out
def para(d,x,y,t,fo,fill,maxw,lh=1.34):
    for l in wrap(d,t,fo,maxw): d.text((x,y),l,font=fo,fill=fill);y+=int(fo.size*lh)
    return y
def pill(img,x=70,y=110):
    d=ImageDraw.Draw(img);fo=f('Bold',24);t='KUBO NEWS';sp=5
    tw=sum(d.textlength(c,font=fo)+sp for c in t)-sp
    d.rounded_rectangle((x,y,x+tw+56,y+54),27,fill=(255,255,255),outline=BLUE,width=2)
    cx=x+28
    for c in t: d.text((cx,y+13),c,font=fo,fill=BLUE);cx+=d.textlength(c,font=fo)+sp
def footer(img,i,n):
    d=ImageDraw.Draw(img)
    d.line((70,H-150,W-70,H-150),fill=LINE,width=2)
    if LOGO:
        lg=Image.open(LOGO).convert('RGBA');lg.thumbnail((260,70));img.alpha_composite(lg,(70,H-118+(70-lg.height)//2-6))
    else:
        img.alpha_composite(CUBE.resize((58,62)),(70,H-122))
        d.text((142,H-114),'KUBO',font=f('Bold',32),fill=NAVY);d.text((142+d.textlength('KUBO ',font=f('Bold',32)),H-114),'AI',font=f('Bold',32),fill=BLUE)
        d.text((142,H-78),'@_kuboai',font=f('Medium',23),fill=GR)
    for k in range(n):
        cx=W-90-(n-1-k)*26;d.ellipse((cx-6,H-100,cx+6,H-88),fill=BLUE if k==i else (200,210,228))
    if i<n-1:
        fo=f('SemiBold',26);d.text((W-90-(n-1)*26-28-d.textlength('Arraste',font=fo),H-109),'Arraste',font=fo,fill=GR)
def base(): return Image.new('RGBA',(W,H),BGL)
def cover(photo,t1,t2,sub,out,n=4):
    img=base();ph=Image.open(photo).convert('RGB')
    ph=ImageOps.fit(ph,(W,690),Image.LANCZOS,centering=(0.5,0.4));img.paste(ph,(0,0))
    pill(img);d=ImageDraw.Draw(img,'RGBA')
    t='Imagem ilustrativa';fo=f('Medium',20);tw=d.textlength(t,font=fo)
    d.rounded_rectangle((W-tw-58,640,W-30,672),16,fill=(0,0,0,110));d.text((W-tw-44,644),t,font=fo,fill=(255,255,255,235))
    y=745
    for l in wrap(d,t1,f('Black',78),940): d.text((70,y),l,font=f('Black',78),fill=NAVY);y+=90
    for l in wrap(d,t2,f('Black',78),940): d.text((70,y),l,font=f('Black',78),fill=BLUE);y+=90
    para(d,70,y+18,sub,f('Medium',35),GR,930,1.38)
    footer(img,0,n);img.convert('RGB').save(out,quality=92)
def body(kicker,head,items,out,i,n=4,numbers=True):
    img=base();pill(img);d=ImageDraw.Draw(img)
    y=230;d.text((70,y),kicker,font=f('Bold',28),fill=BLUE);y+=58
    for l in wrap(d,head,f('Black',72),940): d.text((70,y),l,font=f('Black',72),fill=NAVY);y+=84
    y+=50
    for k,it in enumerate(items,1):
        if numbers:
            d.ellipse((70,y+2,124,y+56),fill=BLUE);t=str(k);fo=f('Bold',30);d.text((97-d.textlength(t,font=fo)/2,y+10),t,font=fo,fill='white')
        y=max(para(d,150,y+4,it,f('Medium',40),NAVY,860,1.34),y+60)+38
    footer(img,i,n);img.convert('RGB').save(out,quality=92)
def last(src,out,n=4):
    img=base();pill(img);d=ImageDraw.Draw(img)
    y=230;d.text((70,y),'FONTE',font=f('Bold',28),fill=BLUE);y+=56
    y=para(d,70,y,src,f('Regular',32),GR,930,1.45)+70
    d.rounded_rectangle((70,y,W-70,y+430),36,fill=(255,255,255),outline=LINE,width=2)
    yy=y+60;d.text((120,yy),'Siga a KUBO AI',font=f('Black',80),fill=NAVY);yy+=110
    yy=para(d,120,yy,'e acompanhe o que acontece no mundo da tecnologia',f('Bold',46),BLUE,800,1.28)+30
    d.text((120,yy),'@_kuboai',font=f('Bold',40),fill=NAVY)
    footer(img,n-1,n);img.convert('RGB').save(out,quality=92)
