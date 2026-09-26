<title>Igor Furlan Marks</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Sora:wght@400;500&family=Shippori+Mincho:wght@500&family=Albert+Sans:wght@300;400&display=swap">
<style>
:root{
  --bg:#f3f4f6; --surface:#ffffff; --ink:#15181e; --muted:#5b6270; --line:#dde0e6;
  --a1:#2f63d8; --a2:#c2352b; --a3:#d9921a; --a4:#0f8a78;
  --tile-l:#f7f8fa; --tile-d:#0d1117; --ink-l:#15181e; --ink-d:#e8eaee;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#0f1115; --surface:#171a20; --ink:#e7e9ee; --muted:#9aa1ae; --line:#2a2e37; color-scheme:dark;}}
:root[data-theme="dark"]{--bg:#0f1115; --surface:#171a20; --ink:#e7e9ee; --muted:#9aa1ae; --line:#2a2e37; color-scheme:dark;}
body{background:var(--bg); color:var(--ink); font:16px/1.6 "Hanken Grotesk",system-ui,sans-serif; padding-inline:20px; padding-block:48px 72px}
.wrap{max-width:1040px; margin:0 auto; display:grid; gap:56px}
header{max-width:62ch}
.eyebrow{font:500 12px/1 "JetBrains Mono",ui-monospace,monospace; letter-spacing:.08em; text-transform:uppercase; color:var(--muted)}
h1{font-weight:600; font-size:clamp(28px,4vw,40px); line-height:1.15; margin:.4em 0 .5em; text-wrap:balance; letter-spacing:-.01em}
header p{color:var(--muted); margin:0}
.concept{display:grid; gap:20px; border-top:1px solid var(--line); padding-top:32px}
.chead{display:flex; flex-wrap:wrap; align-items:baseline; gap:6px 16px}
.chead h2{margin:0; font-size:24px; font-weight:600}
.tiles{display:grid; grid-template-columns:1fr 1fr; gap:12px}
.tile{border-radius:10px; min-height:200px; display:flex; align-items:center; justify-content:center; padding:28px 20px}
.tile.l{background:var(--tile-l); color:var(--ink-l); box-shadow:inset 0 0 0 1px #e3e6eb}
.tile.d{background:var(--tile-d); color:var(--ink-d)}
.lockup{display:flex; align-items:center; gap:18px}
.lockup .mark{width:84px; height:84px; flex:none}
.lockup .word{width:min(300px,100%); height:auto}
.name{white-space:nowrap}
.n-hept{font:500 30px/1 "Sora",sans-serif; letter-spacing:-.01em}
.n-enso{font:500 30px/1 "Shippori Mincho",serif; letter-spacing:.02em}
.n-cons{font:300 22px/1 "Albert Sans",sans-serif; letter-spacing:.32em; text-transform:uppercase}
.rmono{font-family:"JetBrains Mono",ui-monospace,monospace; font-weight:500}
.below{display:grid; grid-template-columns:minmax(0,1.3fr) minmax(0,1fr); gap:24px; align-items:start}
.below p{margin:0 0 .6em; max-width:60ch}
.below .trade{color:var(--muted); font-size:15px}
.sizes{display:flex; gap:14px; align-items:center; flex-wrap:wrap; justify-content:flex-end}
.av{border-radius:50%; display:flex; align-items:center; justify-content:center; overflow:hidden}
.av svg{width:72%; height:72%}
.av.l{background:var(--tile-l); color:var(--ink-l); box-shadow:inset 0 0 0 1px #e3e6eb}
.av.d{background:var(--tile-d); color:var(--ink-d)}
.s96{width:96px;height:96px}.s40{width:40px;height:40px}.s20{width:20px;height:20px}
.cap{font:12px/1.4 "JetBrains Mono",monospace; color:var(--muted); width:100%; text-align:right}
footer{color:var(--muted); font-size:15px; max-width:66ch; border-top:1px solid var(--line); padding-top:24px}
footer code{font-family:"JetBrains Mono",monospace; font-size:.9em}
@media (max-width:720px){
  .tiles{grid-template-columns:1fr}
  .below{grid-template-columns:1fr}
  .sizes{justify-content:flex-start}.cap{text-align:left}
  .lockup .mark{width:64px;height:64px}
  .n-hept,.n-enso{font-size:24px}.n-cons{font-size:17px}
}
</style>
<div class="wrap">
<header>
  <div class="eyebrow">Profile mark · four directions</div>
  <h1>A mark for Igor Furlan</h1>
  <p>Each option is shown as a lockup on light and dark (GitHub has both), then at avatar and favicon sizes, because a mark that falls apart at 20&nbsp;px doesn't work as an avatar. The colour accent is one dot or line, never a gradient.</p>
</header>

<section class="concept">
  <div class="chead"><span class="eyebrow">Option A</span><h2>Heptagon monogram</h2></div>
  <div class="tiles">
    <div class="tile l"><div class="lockup">{{heptagon}}<span class="name n-hept">igor furlan</span></div></div>
    <div class="tile d"><div class="lockup">{{heptagon}}<span class="name n-hept">igor furlan</span></div></div>
  </div>
  <div class="below">
    <div><p>An I and F set inside a seven-sided frame, the shape of the Kubernetes wheel, without using the wheel itself. The single blue dot on the top vertex keeps it from looking like a badge.</p>
    <p class="trade">Safest and most "platform engineer". Also the closest to looking like a company logo.</p></div>
    <div class="sizes"><div class="av l s96">{{heptagon}}</div><div class="av d s40">{{heptagon}}</div><div class="av l s20">{{heptagon}}</div><div class="cap">96 · 40 · 20 px</div></div>
  </div>
</section>

<section class="concept">
  <div class="chead"><span class="eyebrow">Option B</span><h2>Ensō and seal</h2></div>
  <div class="tiles">
    <div class="tile l"><div class="lockup">{{enso}}<span class="name n-enso">Igor Furlan</span></div></div>
    <div class="tile d"><div class="lockup">{{enso}}<span class="name n-enso">Igor Furlan</span></div></div>
  </div>
  <div class="below">
    <div><p>A single-stroke Zen circle, left open, with a small red seal carrying the IF. It ties to <em>musashi</em>, your homelab, named after the swordsman who was also an ink painter and wrote about "the Void", and to a bio you describe as a bit philosophical.</p>
    <p class="trade">The most personal and least technical option. Works best when the rest of the profile stays quiet.</p></div>
    <div class="sizes"><div class="av l s96">{{enso}}</div><div class="av d s40">{{enso}}</div><div class="av l s20">{{enso}}</div><div class="cap">96 · 40 · 20 px</div></div>
  </div>
</section>

<section class="concept">
  <div class="chead"><span class="eyebrow">Option C</span><h2>Constellation</h2></div>
  <div class="tiles">
    <div class="tile l"><div class="lockup">{{constellation}}<span class="name n-cons">Igor Furlan</span></div></div>
    <div class="tile d"><div class="lockup">{{constellation}}<span class="name n-cons">Igor Furlan</span></div></div>
  </div>
  <div class="below">
    <div><p>I and F drawn as nodes and edges, reading both as a cluster topology and as a star chart. The amber node is the star, for Kubestronaut. The dotted edge links the two letters the way a service links two workloads.</p>
    <p class="trade">Most distinctive at large sizes. At 20&nbsp;px the nodes merge, so the avatar would need a simplified version.</p></div>
    <div class="sizes"><div class="av l s96">{{constellation}}</div><div class="av d s40">{{constellation}}</div><div class="av l s20">{{constellation}}</div><div class="cap">96 · 40 · 20 px</div></div>
  </div>
</section>

<section class="concept">
  <div class="chead"><span class="eyebrow">Option D</span><h2>Error budget</h2></div>
  <div class="tiles">
    <div class="tile l">{{ruler_word}}</div>
    <div class="tile d">{{ruler_word}}</div>
  </div>
  <div class="below">
    <div><p>A monospace wordmark over a measuring scale, with one tick marked at 99.9, the classic three-nines SLO. It's a nod to the line on your portfolio: "platform engineering, measured".</p>
    <p class="trade">The most SRE-specific option, and the only one that's mainly a wordmark. It suits a README banner better than an avatar.</p></div>
    <div class="sizes"><div class="av l s96">{{ruler}}</div><div class="av d s40">{{ruler}}</div><div class="av l s20">{{ruler}}</div><div class="cap">96 · 40 · 20 px</div></div>
  </div>
</section>

<footer>
  These are first drafts. Once you pick one, I'll refine it and export it as SVG with the text converted to outlines, so it renders the same on GitHub without web fonts. It will switch between light and dark versions through a <code>&lt;picture&gt;</code> tag in your profile README. Mixing is fine too, for example the ensō as your avatar and the error-budget wordmark as the README banner.
</footer>
</div>
