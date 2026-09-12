---
name: svg-art-folio
description: Turn a supplied reference image into a self-contained SVG drawing folio with a human-readable process timeline, themed interface, browser verification, and offline ZIP delivery. Use when the user asks to recreate artwork as SVG/HTML and animate the drawing process from an image.
metadata:
  short-description: Generate a self-contained SVG drawing process from one reference image
---

# SVG Art Folio

Use the supplied image as the sole visual source for the artwork. Produce a polished HTML folio with native SVG, a deterministic drawing timeline, themed surrounding UI, and a ZIP whose extracted `index.html` opens offline.

## Workflow

1. Inspect the image: aspect ratio, composition, layers, palette, line quality, material cues, and any known character or setting. Ask only for information that cannot be inferred.
2. Plan the art and interface separately. Keep image content inside the canvas; use the surrounding page for title, quotations, stage labels, controls, seasonal or editorial motifs, and credits. Choose copy and palette that belong together. Do not reuse a character-specific theme for another subject.
3. Build semantic SVG groups and paths. Preserve proportion, occlusion, colors, stroke widths, and viewBox. Do not use Canvas, raster `<image>`, Base64, remote image links, external fonts, frameworks, or runtime network requests.
4. Build an ordered timeline that follows a plausible human process: construction, structure, clean lines, flats, shadow/material, light/detail, and close. Split disconnected lines into separate actions. Make erasing, revision, flip, pan, zoom, and inspection actions correspond to visible drawing decisions.
5. Add controls for play/pause, restart, speed, stage seeking, final view, and detail view. Keep one animation-frame chain, cache high-frequency nodes, update only changed attributes, pause when the tab is hidden, preserve focus and reduced-motion behavior, and prevent speed menus from covering following content.
6. Validate before delivery: compare full and detail views; check SVG IDs/references, action ordering, no unintended simultaneous strokes, timeline seek/play equivalence, all controls, keyboard use, mobile overflow, and no script errors. Test the extracted ZIP offline, not just the working directory.
7. Clean the output. Include only the deliverable and required files in the ZIP. Never include caches, logs, screenshots, source references, credentials, personal paths, or experimental pages.

## Content and fidelity

Keep canvas fidelity stricter than decorative UI. Character dialogue or official material may be used only when the identity is reliable and the wording is verified; otherwise write original, clearly themed copy. Do not add text, debugging labels, or explanatory UI inside the drawing canvas. Do not claim pixel-perfect identity without evidence. Report limitations and distinguish local tests from hosted tests.

## Default deliverable

Name the archive after the work. The default is a single self-contained `index.html` in the ZIP. A split asset build is an optional hosting experiment only when requested; it must never replace the reliable offline package without verification.

Read [references/visual-and-copy.md](references/visual-and-copy.md) while designing the folio, [references/drawing-process.md](references/drawing-process.md) while building the timeline, and [references/acceptance.md](references/acceptance.md) before final packaging. Read [references/publishing.md](references/publishing.md) only when the user asks to publish.
