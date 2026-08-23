# Product OS Guide

Learn product management by working one real case end to end.

**The case:** Uber Eats has strong overall growth, but weekday lunchtime orders from 11:30am to 1:30pm are 30% lower than dinner orders. That observation is all you start with. Everything else you build yourself.

44 skills in six phases: Discover, Shape the value, Decide and scope, Specify, Validate, Go to market, plus a reference shelf.

Live at https://thejoseplatero.github.io/product-os-guide/

## Rebuilding

The page is generated from `src/`. One fragment per skill in `src/frags/`, the
shell in `src/home.html` and `src/site.css`, the case and sequence in
`src/CASE.md`.

```bash
python3 src/build.py
```

That writes `index.html`. Commit and push to deploy.
