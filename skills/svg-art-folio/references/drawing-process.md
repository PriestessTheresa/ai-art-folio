# Drawing process decisions

A process should communicate dependencies a person would recognize. Begin with composition and construction, establish structure and clean lines, place flats, then add shadow, material, light, and small corrections. Adapt the stages to the supplied image; do not force a fixed number of stages.

Each action has an interval, target nodes, and an explainable brush path. Disconnected line fragments become separate actions. A fill action reveals one continuous brush trace. Erasing and revision must change a visible state. Flip, pan, zoom, and inspection actions occur when they serve a proportion or detail check.

Use a deterministic time model so direct seeking and playback produce the same state. Keep one requestAnimationFrame chain, cache high-frequency references and path lengths, avoid rewriting unchanged attributes, pause when the tab becomes hidden, and provide a manual way to resume.
