import sys
sys.argv = ["x"]
exec(open("export.py").read().split("INK = ")[0])  # reuse font loading + text_path only
TXT = "living in the terminal, troubleshooting for fun"
SIZE = 15
d, w = text_path(TXT, "mono", SIZE, 0, 15)
cw, gap = SIZE*0.6, SIZE*0.35
W, H = w + gap + cw + 2, 20
for theme, col in [("light", "#6a7180"), ("dark", "#8b93a1")]:
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.1f} {H}" width="{W:.0f}" height="{H}" role="img" aria-label="{TXT}">'
           f'<title>{TXT}</title><style>@keyframes b{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}'
           f'.c{{animation:b 1.1s steps(1) infinite}}@media (prefers-reduced-motion:reduce){{.c{{animation:none}}}}</style>'
           f'<path d="{d}" fill="{col}"/><rect class="c" x="{w+gap:.1f}" y="3" width="{cw:.1f}" height="15" fill="{col}"/></svg>\n')
    open(f"../igfurlan/assets/marks/tagline-{theme}.svg", "w").write(svg)
print(W)
