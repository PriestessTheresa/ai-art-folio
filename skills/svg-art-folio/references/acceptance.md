# Acceptance checklist

- Static full view and representative detail views match the reference composition and palette.
- SVG uses native paths/groups and has unique IDs with valid references.
- No Canvas, raster image, Base64 data, external URL, external font, or framework is required.
- Drawing actions are ordered and intentional; line, fill, erase, and revision timing is explainable.
- Seeking and playing the same timestamp produce the same state; pause is stable; replay creates one frame chain.
- Every speed works; menu focus, Escape, outside dismissal, and selected contrast work.
- Buttons have hover, pressed, focus, and touch states; stage text is readable; no canvas text appears.
- The menu does not overlap following content; mobile widths have no horizontal overflow.
- Hidden tabs pause; reduced-motion removes transitions/animation; Space does not toggle on key repeat.
- ZIP extraction yields the exact tested entry and opens with the browser offline without errors or network requests.
