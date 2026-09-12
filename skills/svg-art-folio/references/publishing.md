# GitHub publishing

Use one public repository for the reusable skill and multiple examples. Put the skill under `skills/svg-art-folio/`, the example under `examples/shu/`, and an optional online copy under `docs/`. Keep the release ZIP separate from repository source.

1. Create a repository such as `svg-art-folio` (Public).
2. Upload `README.md`, `LICENSE`, `THIRD_PARTY_NOTICES.md`, the skill folder, and the example. Exclude caches, credentials, and private paths.
3. Create a Release tag such as `v0.1.0`; attach the named artwork ZIP and a skill ZIP. GitHub's generated Source code ZIP is not the artwork deliverable.
4. For an optional preview, put the self-contained example at `docs/index.html`, then use Settings → Pages → Deploy from a branch → `main`/`docs`. Test the published URL separately from the offline ZIP.
5. When updating, publish a new version tag and retain old release assets.

Record third-party art, dialogue, fonts, and converted glyphs separately from the code license. Do not publish access tokens, private attachments, or temporary hosting URLs.
