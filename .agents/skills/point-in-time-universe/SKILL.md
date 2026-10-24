---
name: point-in-time-universe
description: Build an auditable candidate frontier ordered by descending market-cap rank and map candidates to historical perpetual contracts and spot/index series. Use for asset discovery, rank history, listing/delisting, or mapping; never use current ranks as historical membership.
---

# Point-in-time expanding universe

1. Discover candidates from free public market-cap rankings and sort by descending rank/market cap. Save retrieval timestamp, source, raw response hash, page/cursor, candidate ID and order.
2. There is no fixed top-N cutoff. Batch size is only for checkpointing. Follow pagination, then investigate another free source before declaring the frontier exhausted.
3. Keep discovery ranking separate from historical eligibility. Historical formation dates require point-in-time cap/rank history or a clearly labelled rank-unverified status.
4. Map stable asset IDs to spot pair, index constituent, perpetual contract, venue, quote/settlement assets, listing/delisting dates, token migrations, redenominations and symbol reuse.
5. Preserve missing, delisted, renamed, illiquid and failed candidates with an explicit status and reason; never silently omit candidates.
6. Record timestamp conventions, revisions, licence, endpoint, temporal coverage, source-specific cutoff, gaps and every exclusion.
7. Never reconstruct historical rank using today's rank. If historical rank evidence is missing, keep the candidate in the discovery frontier and report the limitation rather than claiming point-in-time eligibility.
8. Prefer official public mark/index/spot, funding and open-interest histories. Respect rate limits with bounded retries, exponential backoff and caching. No paid or credential-gated endpoints.
9. Persist frontier updates atomically and validate duplicate IDs and rank ordering before advancing the cursor.
