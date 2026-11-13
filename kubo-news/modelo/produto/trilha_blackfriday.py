import numpy as np, wave
SR=44100;BPM=122;beat=60/BPM;dur=20.0;N=int(SR*dur)
t=np.arange(N)/SR;mix=np.zeros((N,2))
def add(sig,start,pan=0.5,g=1.0):
    i=int(start*SR);j=min(N,i+len(sig))
    if i>=N:return
    s=sig[:j-i]*g;mix[i:j,0]+=s*(1-pan)*2**.5/1.414;mix[i:j,1]+=s*pan*2**.5/1.414
def env(n,a=0.005,r=0.2):
    x=np.arange(n)/SR;e=np.minimum(1,x/a)*np.exp(-x/r);return e
def kick():
    n=int(.35*SR);x=np.arange(n)/SR;f=45+120*np.exp(-x*35);ph=2*np.pi*np.cumsum(f)/SR
    return np.tanh(2*np.sin(ph)*np.exp(-x*7))
def hat(op=False):
    n=int((.18 if op else .05)*SR);rng=np.random.default_rng(1);w=rng.standard_normal(n)
    w=np.diff(np.concatenate([[0],w]));return w*env(n,.001,.06 if op else .015)*.35
def clap():
    n=int(.25*SR);rng=np.random.default_rng(2);w=rng.standard_normal(n)
    w=np.convolve(w,np.ones(6)/6,'same')-np.convolve(w,np.ones(60)/60,'same');return w*env(n,.002,.07)*.6
def saw(f,n,det=0):
    x=np.arange(n)/SR;o=0
    for d in (-det,0,det):o=o+2*((x*f*(1+d))%1)-1
    return o/3
def lp(x,a):
    y=np.zeros_like(x);s=0
    for i in range(len(x)):s+=a*(x[i]-s);y[i]=s
    return y
def mtof(m):return 440*2**((m-69)/12)
# progressao: Am F C G (vi IV I V em C) -> Lá menor, tom de negocios moderno
prog=[[57,60,64],[53,57,60],[48,52,55],[55,59,62]]
bass=[45,41,36,43]
bars=int(dur/(4*beat))+1
side=np.ones(N)
for b in range(bars):
    for k in range(4):
        st=(b*4+k)*beat
        if 1<=b: add(kick(),st,.5,.9)
        i=int(st*SR);n=int(.25*SR);j=min(N,i+n)
        if b>=1 and i<N: side[i:j]=np.minimum(side[i:j],0.25+0.75*np.linspace(0,1,j-i)**.6)
        if b>=2: add(hat(True),st+beat/2,.6,.5)
        if b>=1: [add(hat(),st+beat/4*q,.4,.35) for q in (1,3)]
        if b>=2 and k in(1,3): add(clap(),st,.5,.5)
# pads
for b in range(bars):
    ch=prog[b%4];st=b*4*beat;n=int(4*beat*SR)
    pad=sum(saw(mtof(m),n,.004) for m in ch)/3
    pad=lp(pad,.06)*np.minimum(1,np.arange(n)/(.15*SR))*np.minimum(1,(n-np.arange(n))/(.1*SR))
    add(pad,st,.35,.22);add(pad,st+.012,.65,.22)
# baixo em colcheias fora do tempo
for b in range(1,bars):
    r=bass[b%4]
    for k in range(8):
        if k%2==0:continue
        st=b*4*beat+k*beat/2;n=int(beat/2*.9*SR)
        s=lp(saw(mtof(r),n),.12)*env(n,.003,.15);add(s,st,.5,.45)
# arpejo a partir do compasso 3
for b in range(3,bars):
    ch=prog[b%4];notas=[ch[0]+12,ch[1]+12,ch[2]+12,ch[1]+24]
    for k in range(16):
        st=b*4*beat+k*beat/4;n=int(beat/4*SR)
        x=np.arange(n)/SR;s=np.sign(np.sin(2*np.pi*mtof(notas[k%4])*x))*.5+np.sin(2*np.pi*mtof(notas[k%4])*x)*.5
        add(lp(s,.25)*env(n,.002,.06),st,.3+.4*(k%2),.12)
mix*=side[:,None]**.5 if False else 1
# aplica sidechain so nos pads/baixo e aproximado no todo (leve)
mix*= (0.55+0.45*side)[:,None]
# fades
fi=np.minimum(1,t/1.0);fo=np.minimum(1,(dur-t)/2.0);mix*= (fi*fo)[:,None]
# eco simples
d=int(beat*.75*SR);mix[d:]+=mix[:-d][:, ::-1]*.18
mix=np.tanh(mix*1.4);mix/=np.max(np.abs(mix))*1.12
w=wave.open('trilha.wav','wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR)
w.writeframes((mix*32767).astype('<i2').tobytes());w.close();print('ok')
