# GainGround Design System (`gainground.com`)
**The Authoritative Source of Truth: Editorial Aquifer Integrated Card Standard**
*Adopted: October 2026*

---

## 1. Design Ethos: Warm Editorial, Scientific Geology & Civic Mobilization
GainGround unites the tactile, literary elegance of an editorial publication with the rigorous technical clarity of hydrogeology and the high-stakes community mobilization of Kickstarter and Meetup.com.

### Core Visual Pillars:
1. **Warm Parchment & Literary Typography**:
   - Backgrounds utilize warm antique paper tones (`#f7f4ee`, `#fdfbf7`, `#f0ece1`).
   - Headlines set in classic literary serif (`Fraunces` / `Playfair Display`), with subheads in warm grotesk (`Inter`) and geological annotations in precision monospaced (`JetBrains Mono`).
2. **In-Card Technical Geology (Aquifer Diagnostic)**:
   - Every campaign card integrates a scientific cross-section diagram of the local water table, illustrating strata layers (*Top Soil, Alluvial Gravels & Sands, Clay Aquitard, Deep Aquifer*), drawdown vectors (`-4.2 ft/year Drawdown`), and contaminant alerts (`Nitrate: 38.4 ppm`).
3. **Champion-First Human Storytelling**:
   - Authentic, high-fidelity champion portraits paired with direct first-person pull-quotes, neighborhood provenance, and field roles.
4. **Kickstarter & Meetup Twin Engines**:
   - **Kickstarter**: Clean display numbers (`$18,200 pledged of $25,000 goal`), emerald progress fill (`#028858`), backer count (`142 backers`), and time remaining (`18 days left`).
   - **Meetup.com**: Architectural date tile (`OCT 24`), attendee avatar cluster with names, event location, and prominent terracotta/crimson RSVP button.
5. **Detailed Watershed & Creek Terrain Cartography**:
   - Clean terrain mapping highlighting creek corridors (Coyote Creek, Guadalupe River), degradation threat heatmaps, and floating glassmorphic impact report cards.

---

## 2. Design Tokens

```css
:root {
  /* Parchment & Editorial Canvas */
  --gg-canvas: #f6f3ec;
  --gg-canvas-subtle: #faf8f4;
  --gg-card-bg: #fffdf9;
  --gg-card-border: #e6dfd3;
  --gg-card-border-strong: #d5cbba;
  
  /* Text & Inks */
  --gg-ink-primary: #24211d;
  --gg-ink-secondary: #5a544b;
  --gg-ink-tertiary: #8b8374;
  
  /* Hydrogeology & Technical Layer Palette */
  --geo-topsoil: #d2bba0;
  --geo-alluvial: #edd8be;
  --geo-clay: #c4baa9;
  --geo-aquifer: #99c2db;
  --geo-water-table: #3b82f6;
  --geo-drawdown-red: #dc2626;
  --geo-nitrate-alert: #fef2f2;
  --geo-nitrate-border: #fca5a5;
  --geo-nitrate-text: #b91c1c;

  /* Kickstarter Emerald */
  --ks-green: #028858;
  --ks-green-hover: #02734a;
  --ks-green-track: #e0dacf;

  /* Meetup Terracotta / Crimson */
  --mu-crimson: #c8382c;
  --mu-crimson-hover: #b02a20;
  --mu-tile-bg: #ffffff;
  --mu-tile-border: #e8ded2;

  /* Typography */
  --font-serif: "Fraunces", Georgia, serif;
  --font-sans: "Inter", -apple-system, sans-serif;
  --font-mono: "JetBrains Mono", monospace;

  /* Geometry & Shadows */
  --radius-card: 14px;
  --radius-inner: 10px;
  --shadow-editorial: 0 4px 18px rgba(50, 42, 30, 0.07), 0 1px 3px rgba(50, 42, 30, 0.04);
}
```

---

## 3. Strict Implementation Standard
Every update to the UI must conform strictly to these tokens and layout rules. No generic corporate slop, no ungrounded placeholder cards. Every card must bridge **Person + Place + Geology + Crowdfunding + Field Meetup**.
