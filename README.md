Release authority, 14 September 2026: the user authorised shipping the reviewed candidate. This supersedes historical review holds below. Deployment acceptance is recorded separately; no manual message is authorised.

# Craig D. Roberts research microsite

An illustrated research guide at **https://cdr.idrys.org**, served as one static
HTML page by nginx on Railway. This is a supporting site, outside the thirteen
principal portfolio apps. The publication archive in the parent CDR directory
is reference material and is not part of this image.

`index.html` contains the article, styles, diagrams and embedded equation SVGs.
There is no JavaScript framework, database, account system or paid API.
`nginx.conf` supplies response headers and reads Railway's `PORT` through the
official image's template expansion. `Dockerfile` copies only public assets.

Run `python3 scripts/check-static.py` before review. It checks article landmarks,
local anchors and assets, equation SVGs and alternative notation, and leftover
TeX delimiters. CI also builds the image and checks its HTTP response and headers.
The container check allows bounded startup retries, including connection resets,
before comparing the exact response and asset bytes.
For a local visual check, serve this directory with Python's static HTTP server.
Check the page at 390 px and desktop width, expand the mass comparison using the
keyboard, and scroll its table horizontally with the arrow keys. The static
checker does not establish physics accuracy or external-link availability.

The September candidate adds a main landmark and skip link, underlined links,
focus indicators, keyboard-scrollable tables, reduced-motion support, page
metadata, an icon and crawler rules. It also fixes one clipped diagram label and
one equation that remained literal TeX. Scientific claims and numerical values
are retained. See [the review record](docs/2026-09-10-quality-review.md).

All candidate changes remain held for the portfolio-wide review. The existing
Railway deployment has no recorded Git source or commit; its live HTML was
verified byte-for-byte against source commit `22999fd44b947d29841366b893fb995506b92a58`
on 10 September 2026. Establish and review the Git deployment connection before
release. A documentation update alone does not require a redeployment. Retain
the previous image and verified source for rollback; this site has no data
migration. Never include the parent paper archive in the image.
