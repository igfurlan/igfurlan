import math
OUT = "./"
f = lambda v: f"{v:.2f}".rstrip("0").rstrip(".")

# 1 heptagon monogram
pts = [(50 + 43*math.sin(2*math.pi*k/7), 52 - 43*math.cos(2*math.pi*k/7)) for k in range(7)]
hept = " ".join(f"{f(x)},{f(y)}" for x, y in pts)
heptagon = f'''<svg viewBox="0 0 100 100" class="mark"><polygon points="{hept}" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>
<g stroke="currentColor" stroke-width="6" stroke-linecap="butt" fill="none"><path d="M39 33V71"/><path d="M52 71V33H66M52 51H62"/></g>
<circle cx="{f(pts[0][0])}" cy="{f(pts[0][1])}" r="4" fill="var(--a1)"/></svg>'''

# 2 enso with seal
N = 220; start = math.radians(-35); sweep = math.radians(332)
outer, inner = [], []
for i in range(N+1):
    s = i/N; th = start + sweep*s
    r = 36 + 1.1*math.sin(3*th+0.6) + 0.5*math.sin(7*th)
    t = 1.8 + 10*(s**0.18)*((1-s)**0.8)
    x, y = 48 + r*math.cos(th), 50 + r*math.sin(th)
    outer.append((48+(r+t/2)*math.cos(th), 50+(r+t/2)*math.sin(th)))
    inner.append((48+(r-t/2)*math.cos(th), 50+(r-t/2)*math.sin(th)))
ring = outer + inner[::-1]
d = "M" + " L".join(f"{f(x)} {f(y)}" for x, y in ring) + "Z"
enso = f'''<svg viewBox="0 0 100 100" class="mark"><path d="{d}" fill="currentColor"/>
<rect x="70" y="70" width="20" height="20" rx="2.5" fill="var(--a2)"/>
<g stroke="#fff" stroke-width="2.4" fill="none"><path d="M75.5 74.5V85.5"/><path d="M80.5 85.5V74.5H86M80.5 80H85"/></g></svg>'''

# 3 constellation
nodes = [(30,24),(30,50),(30,76),(54,24),(54,50),(54,76),(76,24),(70,50)]
edges = [(0,1),(1,2),(3,4),(4,5),(3,6),(4,7)]
e = "".join(f'<path d="M{nodes[a][0]} {nodes[a][1]}L{nodes[b][0]} {nodes[b][1]}"/>' for a, b in edges)
n = "".join(f'<circle cx="{x}" cy="{y}" r="3.6"/>' for i, (x, y) in enumerate(nodes) if i != 6)
constellation = f'''<svg viewBox="0 0 100 100" class="mark"><g stroke="currentColor" stroke-width="1.8" fill="none">{e}</g>
<path d="M30 24L54 50" stroke="currentColor" stroke-width="1" stroke-dasharray="1.5 3" opacity=".55"/>
<g fill="currentColor">{n}</g><circle cx="76" cy="24" r="8" fill="var(--a3)" opacity=".18"/><circle cx="76" cy="24" r="4.4" fill="var(--a3)"/></svg>'''

# 4 error-budget ruler (square mark + wide wordmark)
ticks = "".join(f'<path d="M{x} 70V{70-(9 if x%25==15 else 4)}"/>' for x in range(15, 86, 5))
ruler = f'''<svg viewBox="0 0 100 100" class="mark"><text x="50" y="52" text-anchor="middle" class="rmono" font-size="40" fill="currentColor">if</text>
<g stroke="currentColor" stroke-width="1.6">{ticks}<path d="M13 70H87"/></g>
<path d="M81 70V52" stroke="var(--a4)" stroke-width="3"/></svg>'''
wt = "".join(f'<path d="M{x} 64V{64-(8 if x%50==10 else 3.5)}"/>' for x in range(10, 311, 10))
ruler_word = f'''<svg viewBox="0 0 330 90" class="word"><text x="8" y="44" class="rmono" font-size="34" fill="currentColor">igor furlan</text>
<g stroke="currentColor" stroke-width="1.3">{wt}<path d="M8 64H312"/></g>
<path d="M297 64V40" stroke="var(--a4)" stroke-width="3"/><text x="297" y="82" text-anchor="middle" class="rmono" font-size="11" fill="var(--a4)">99.9</text></svg>'''

for name, svg in [("heptagon", heptagon), ("enso", enso), ("constellation", constellation), ("ruler", ruler), ("ruler_word", ruler_word)]:
    open(OUT+name+".svg", "w").write(svg)
