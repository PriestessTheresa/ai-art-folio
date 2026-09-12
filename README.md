# AI Art Folio

`ai-art-folio` is a reusable agent skill and example collection for turning one supplied reference image into a polished SVG drawing-process folio. The repository is intended to hold multiple skills and examples over time; `Shu` is the first published example.

## Start here

- [Installable skill package](svg-art-folio.zip)
- [Skill source](skills/svg-art-folio/SKILL.md)
- [Shu offline delivery](Shu.zip)
- [Shu source](examples/shu/index.html)
- [Validation helpers](scripts/)

Attach a reference image and ask:

> Use `$svg-art-folio` to turn this image into a polished self-contained SVG drawing folio and deliver an offline ZIP.

The skill separates the reference-driven artwork from the surrounding editorial interface, creates an ordered human-readable drawing timeline, verifies controls and responsive layout, and packages the extracted `index.html` for offline use.

## Offline use

Download `Shu.zip`, extract it, and open the included `index.html` in a modern browser. The artwork ZIP is self-contained and does not require an internet connection, server, framework, external font, or runtime asset request.

## Repository layout

```text
skills/svg-art-folio/   reusable skill
examples/shu/           first example source
scripts/                repeatable validation helpers
Shu.zip                release artwork
svg-art-folio.zip       release skill package
```

## Scope and rights

The reusable skill and original code are separate from third-party character art, quotations, fonts, and reference material. The Shu example is a fan work; read [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) before redistribution. See [LICENSE](LICENSE) for the code license.

## Release

The first planned release is `v0.1.0`. The two named ZIP files are release assets; GitHub's automatically generated Source code ZIP is the repository source, not the offline artwork package.
