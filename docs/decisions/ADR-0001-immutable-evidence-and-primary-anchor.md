# ADR-0001: Immutable evidence and a fixed primary anchor

- **Status:** Accepted before empirical outcome analysis.
- **Decision:** Treat the grid, primary anchor, endpoint definitions, splits and inferential family as preregistration. Never edit them after outcomes are visible.
- **Primary anchor:** 1-day basis feature; 90-day trailing reference; rich-positive orientation; q95; 14-day horizon.
- **Co-primary endpoints:** 15% forward crash incidence and worst-5% expected-shortfall of forward MAE.
- **Exploratory grid:** 324 configurations × 8 endpoints = 2,592 comparisons; Holm correction across the full family.
- **Rationale:** The hypothesis concerns tail risk. Optimizing mean return or choosing a threshold after inspection changes the question and inflates false discovery.
- **Consequences:** Each cell must have a terminal status and reason for non-ok states. Any material grid or data design change requires a new experiment ID/path. Old evidence remains immutable.
