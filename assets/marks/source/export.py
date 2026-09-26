import re, os
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FD = "../fonts/"
def load(fn, wght=None):
    f = TTFont(FD + fn)
    if wght and "fvar" in f: f = instantiateVariableFont(f, {"wght": wght})
    return f
FONTS = {
    "sora": load("Sora%5Bwght%5D.ttf", 500),
    "mincho": load("ShipporiMincho-Medium.ttf"),
    "albert": load("AlbertSans%5Bwght%5D.ttf", 300),
    "mono": load("JetBrainsMono%5Bwght%5D.ttf", 500),
}
def text_path(txt, font, size, x, y, anchor="start", tracking=0.0):
    f = FONTS[font]; cmap = f.getBestCmap(); gs = f.getGlyphSet(); upm = f["head"].unitsPerEm
    s = size / upm; hmtx = f["hmtx"]
    names = [cmap[ord(c)] for c in txt]
    adv = [hmtx[n][0]*s + tracking*size for n in names]
    width = sum(adv) - (tracking*size if names else 0)
    cx = x - (width/2 if anchor == "middle" else width if anchor == "end" else 0)
    ds = []
    for n, a in zip(names, adv):
        pen = SVGPathPen(gs); gs[n].draw(TransformPen(pen, (s, 0, 0, -s, cx, y)))
        if pen.getCommands(): ds.append(pen.getCommands())
        cx += a
    return " ".join(ds), width

INK = {"light": "#15181e", "dark": "#e8eaee"}
ACC = {"--a1": "#2f63d8", "--a2": "#c2352b", "--a3": "#d9921a", "--a4": "#0f8a78"}

def outline_texts(svg):
    def rep(m):
        a = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        d, _ = text_path(m.group(2), "mono", float(a["font-size"]), float(a["x"]), float(a["y"]), a.get("text-anchor", "start"))
        return f'<path d="{d}" fill="{a["fill"]}"/>'
    return re.sub(r'<text ([^>]*)>([^<]*)</text>', rep, svg)

def inner(svg):
    return re.sub(r'^<svg[^>]*>|</svg>$', "", svg.strip().replace("\n", ""))

def finalize(body, w, h, theme, title):
    body = body.replace("currentColor", INK[theme])
    for k, v in ACC.items(): body = body.replace(f"var({k})", v)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" '
            f'width="{w:.0f}" height="{h:.0f}" role="img" aria-label="{title}"><title>{title}</title>{body}</svg>\n')

LOCK = {  # concept: (mark file, font, text, size, tracking, uppercase)
    "heptagon": ("heptagon", "sora", "igor furlan", 34, -0.01),
    "enso": ("enso", "mincho", "Igor Furlan", 34, 0.02),
    "constellation": ("constellation", "albert", "IGOR FURLAN", 25, 0.32),
}
out = "out/"; os.makedirs(out, exist_ok=True)
for theme in INK:
    for c in ["heptagon", "enso", "constellation", "ruler"]:
        body = inner(outline_texts(open(c + ".svg").read()))
        open(f"{out}{c}-mark-{theme}.svg", "w").write(finalize(body, 100, 100, theme, "Igor Furlan"))
    for c, (mk, font, txt, size, tr) in LOCK.items():
        mbody = inner(open(mk + ".svg").read())
        d, w = text_path(txt, font, size, 122, 50 + size*0.35, tracking=tr)
        body = mbody + f'<path d="{d}" fill="currentColor"/>'
        open(f"{out}{c}-lockup-{theme}.svg", "w").write(finalize(body, 122 + w + 6, 100, theme, "Igor Furlan"))
    body = inner(outline_texts(open("ruler_word.svg").read()))
    open(f"{out}ruler-lockup-{theme}.svg", "w").write(finalize(body, 330, 90, theme, "Igor Furlan"))
print(sorted(os.listdir(out)))
