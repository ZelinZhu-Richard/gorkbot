# Assumptions and Open Questions

## Priority 0: blocks product direction

1. Which initial customer has the most urgent delegable workflow?
2. Which single workflow should define the MVP?
3. What result can be objectively verified and repeatedly demonstrated?
4. What is the founder's hard monthly prototype budget?
5. Which production model APIs and quotas are actually available?
6. Does the first product need a browser-only sandbox, a full desktop VM, or both?
7. Is a web application sufficient for the first users?
8. Which integration creates the shortest path to real use?

## Priority 1: blocks architecture

9. Persistent VM per user, persistent workspace plus ephemeral task sandboxes, or another isolation model?
10. Which durable workflow engine should be used?
11. What task state must survive worker and provider failure?
12. How will credentials be scoped and injected without entering model context?
13. How will the system distinguish agent-private files from shared project files?
14. What is the approval policy language and enforcement architecture?
15. What is the minimum external-state verification interface?
16. Should customers bring provider keys, use platform billing, or choose either?
17. What data retention and deletion guarantees are required?
18. How will browser and GUI control combine structured and visual state?

## Priority 2: blocks scale or differentiation

19. Which model-routing decisions are visible to users?
20. What portability format should be supported?
21. How are skills versioned, tested, and permissioned?
22. How are multi-agent ownership and delegation represented?
23. How is duplicate work prevented?
24. What metrics define better than the reference product?
25. What gross margin is acceptable?
26. What enterprise controls can be deferred safely?
27. What parts of agent activity should be replayable?
28. How will prompt injection tests become release gates?
29. Which capabilities should be open source, if any?
30. What company and product name avoids confusion and creates independent positioning?

## Explicit current assumptions

- Technical founders and small startup teams are a provisional beachhead.
- A persistent engineering or research workflow is likely more suitable than a broad general assistant.
- One reliable user-visible agent should precede visible agent teams.
- Internal multi-model orchestration must beat a single-model baseline to remain.
- Hard policy and sandbox boundaries are necessary.
- Verified completion is a promising differentiator.
- The first prototype can begin with a web control plane.
- Initial cloud and API cost should remain modest until key risks are tested.

None of these assumptions should silently become permanent decisions.
