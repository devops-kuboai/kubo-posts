"""Agent-Hub, dia da Black Friday (27/11): mesmo visual amarelo do post de 13/11, com a mensagem do dia."""
import sys,os
AQUI=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,AQUI)
_s=open(os.path.join(AQUI,'blackfriday.py')).read();exec(_s[:_s.index("ph=celular(")])
ph=celular([('Vocês entregam em Curitiba até sexta?',False,'01:12'),
            ('Entregamos sim! Pedindo hoje, chega até quinta. Quer o link com o desconto?',True,'01:12'),
            ('Quero! Ainda tem cupom?',False,'01:13'),
            ('Tem! BLACK15 dá mais 15% no carrinho',True,'01:13')])
def hoje(out,phone_y=640):
    c=Image.new('RGBA',(W,H),YEL);d=ImageDraw.Draw(c,'RGBA')
    for r in (440,515,590): d.ellipse((1080-r,1090-r,1080+r,1090+r),outline=INK,width=3)
    stamp(c,'AGENT-HUB · BLACK FRIDAY',70,100,INK,'white')
    fo=f('Black',112);y=200
    for l in ['HOJE É','BLACK FRIDAY']: d.text((66,y),l,font=fo,fill=INK);y+=122
    y+=26;fo2=f('Black',40);t='Seu cliente não pode ficar esperando';w=d.textlength(t,font=fo2)
    d.rectangle((70,y,70+w+40,y+70),fill=INK);d.text((90,y+12),t,font=fo2,fill='white')
    para(d,70,610,'O Agent-Hub responde na hora, de madrugada também, no WhatsApp e no Instagram',f('Bold',38),INK,420,1.28)
    y=880;d.rounded_rectangle((70,y,500,y+100),50,fill=INK);fb=f('Bold',40)
    d.text((285-d.textlength('Comente BLACK',font=fb)/2,y+27),'Comente BLACK',font=fb,fill='white')
    para(d,70,1010,'e receba a demonstração no Direct',f('SemiBold',34),INK,420,1.28)
    pb=ph.resize((int(ph.width*0.78),int(ph.height*0.78)))
    sh=Image.new('RGBA',(W,H));ImageDraw.Draw(sh).rounded_rectangle((620,phone_y+40,620+pb.width,phone_y+40+pb.height),50,fill=(60,40,0,110))
    c.alpha_composite(sh.filter(ImageFilter.GaussianBlur(30)))
    c.alpha_composite(pb.rotate(-5,expand=True,resample=Image.BICUBIC),(590,phone_y))
    d=ImageDraw.Draw(c)
    c.alpha_composite(K.CUBE.resize((58,62)),(70,H-122))
    d.text((142,H-114),'KUBO AI',font=f('Bold',32),fill=INK);d.text((142,H-78),'@_kuboai',font=f('Medium',23),fill=(84,100,132))
    c.convert('RGB').save(out,quality=92)
if __name__=='__main__':
    o='/home/claude/kubo-posts/conteudo-kubo/agent-hub/2026-11-27/';os.makedirs(o,exist_ok=True);hoje(o+'hoje.jpg')
