# CDR quality review, 10 September 2026

The site is live and readable. Railway project/service `cdr` reports a successful
deployment from 15 April 2026. No Git source or commit is recorded there, but the
live HTML and local main at `22999fd44b947d29841366b893fb995506b92a58` share SHA-256
`0ab13a35a820d3a09623554cc287bc05d07d7beb97d0dd2ecdf18d6b08336f46`.
That establishes content identity, not an inferred deployment history.

Live checks returned HTTP 200 and the configured CSP, nosniff, frame, referrer
and permissions headers. Five representative arXiv links returned 200. The
equations load from embedded SVGs. The research narrative was not independently
revalidated as a physics review. The missing HSTS header is recorded; changing
transport policy is outside this small rendering repair.

The 390 px browser inspection found a comparison table clipped by its containing
details element, another table wider than the article, and a diagram label
outside its SVG bounds. Lighthouse reported a missing main landmark and links
distinguished only by colour. The tab icon returned 404. One table also showed
literal `$Q^2 > 6$`, while the footer incorrectly attributed its embedded SVG
equations to a live MathJax renderer. These faults are corrected in the candidate.

Local checks on the candidate:

- `python3 scripts/check-static.py`: passed, 116 embedded equation images and
  22 links. The check first failed on the literal TeX, then passed after its
  conversion to the equivalent HTML notation.
- At 390 px: document width equals viewport width, no clipped diagram labels,
  and both wide tables scroll within their labelled regions. Tab reveals the
  skip link; Enter focuses main. Enter expands the mass comparison; ArrowRight
  scrolls the focused table region, whose focus outline is visible.
- Mobile Lighthouse on the local static server: accessibility, best practices,
  SEO and agentic browsing each scored 100, with zero failed automated checks.
  This is limited automated evidence; it does not establish scientific accuracy.

The candidate was also inspected at 1280 px: no document overflow or clipped
diagram labels, and the corrected mass label is visible. The actual image build
and local HTTP checks passed in a separate Colima profile, with no host mounts
or change to the default Docker context. Exact served index/icon/robots bytes,
configured headers, hidden server version and a 404 response were checked; the
owned container was removed. The first build lacked BuildKit, so the release's
Buildx binary was installed only in the test directory and verified against the
official signed-platform checksum list before the successful run. Hosted CI
execution remains pending. Independent source review closed after nine generic equation
alternatives were replaced with the exact notation embedded in their SVG
comments. All 116 embedded SVG payloads remain byte-identical to baseline;
the other 107 alternatives are unchanged. The static gate rejects the original
generic alternatives. The qualified image ID is
`sha256:0cde57039a6fb983e93c19554b7e5202595ab82ecede30201062f008882fe33f`.
The new workflow
uses the maintainers' current checkout/setup-python v7 actions; that small
post-review workflow update has also passed independent review.
No branch push, commit, production
change or release has occurred. The portfolio-wide review remains the release
boundary.
