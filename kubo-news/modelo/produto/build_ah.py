from kubonews import *
import kubonews
def chat():
    S=2;w,h=1536*S//1,1024*S//1
    y,x=np.mgrid[0:h,0:w]
    g=np.dstack([10+20*(x/w),18+30*(y/h),48+60*(1-y/h)])
    im=Image.fromarray(np.clip(g,0,255).astype(np.uint8)).convert('RGBA');d=ImageDraw.Draw(im)
    px,py,pw,ph=w//2-520,170,1040,2000
    d.rounded_rectangle((px,py,px+pw,py+ph),110,fill=(18,24,40),outline=(70,80,110),width=10)
    sx,sy=px+40,py+40;d.rounded_rectangle((sx,sy,px+pw-40,py+ph-40),80,fill=(240,244,250))
    d.rounded_rectangle((sx,sy,px+pw-40,sy+200),80,fill=(22,104,240));d.rectangle((sx,sy+120,px+pw-40,sy+200),fill=(22,104,240))
    d.ellipse((sx+50,sy+50,sx+150,sy+150),fill='white');d.text((sx+82,sy+66),'L',font=f('Black',60),fill=(22,104,240))
    d.text((sx+180,sy+52),'Sua loja',font=f('Bold',56),fill='white');d.text((sx+180,sy+118),'responde em segundos',font=f('Medium',36),fill=(220,232,255))
    def bub(x0,y0,txt,me,t):
        fo=f('Medium',46);lines=wrap(d,txt,fo,640);bh=len(lines)*62+70;bw=max(d.textlength(l,font=fo) for l in lines)+80
        x1=x0 if not me else px+pw-80-bw
        d.rounded_rectangle((x1,y0,x1+bw,y0+bh),40,fill=(22,104,240) if me else 'white')
        yy=y0+30
        for l in lines: d.text((x1+40,yy),l,font=fo,fill='white' if me else (12,27,64));yy+=62
        d.text((x1+bw-110,y0+bh+8),t,font=f('Medium',30),fill=(120,130,150));return y0+bh+70
    yy=sy+280
    yy=bub(sx+40,yy,'Oi! Vocês entregam no meu bairro hoje?',False,'22:00')
    yy=bub(0,yy,'Oi! Entregamos sim. O pedido chega em até 40 minutos. Quer ver o cardápio?',True,'22:00')
    yy=bub(sx+40,yy,'Quero! Qual é o mais pedido?',False,'22:01')
    im=im.resize((1536,1024),Image.LANCZOS)
    return im.crop((0,0,1536,1024))
