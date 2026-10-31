# ShowVilla: Storytelling Skill Specification

Status: Draft, based on the discussion and the current files.

## Problem Statement

People want an AI assistant to turn a show episode or their own story idea into a short manga-style story. Repeating detailed writing rules in every chat is inconvenient, and different AI apps load reusable instructions in different ways.

When someone gives only a show and episode, the assistant also needs to find reliable story facts, avoid later events and hide the ending unless asked to reveal it.

## Solution

ShowVilla is a shareable collection of story guides. A main guide directs the assistant to smaller guides for show research, spoiler limits, comic formatting and checking the finished story.

The same story rules are maintained once and packaged for the apps that support them. Each app supplies its own AI and, when needed, web access. ShowVilla does not need the old SHOW-MCP server or a separate model API key.

## User Stories

1. As a viewer, I want to name a show and episode so that I can receive a story about that episode.
2. As a viewer, I want to name a show without an episode so that the story starts with episode 1 by default.
3. As a viewer, I want the assistant to identify the right version and episode so that it does not mix different adaptations.
4. As a viewer, I want a short question when the show cannot be identified reliably so that the assistant uses the right story.
5. As a viewer, I want the assistant to look up the episode online so that I do not have to supply a summary.
6. As a viewer, I want the assistant to read actual episode sources so that its facts are better supported.
7. As a viewer, I want it to favor official or licensed sources when useful so that the research starts with reliable material.
8. As a viewer, I want conflicting facts left out unless resolved so that doubtful details do not enter the story.
9. As a viewer, I want to be told when the assistant cannot browse so that I can provide a summary or source.
10. As a viewer, I want the assistant to avoid inventing missing plot when sources are thin so that the story remains trustworthy.
11. As a viewer, I want the ending and major twists hidden by default so that the story leaves surprises intact.
12. As a viewer, I want events after my selected episode excluded so that later episodes are not spoiled.
13. As a viewer, I want to request the ending or a full recap so that I can choose to see supported outcomes within my chosen episode.
14. As a viewer, I want to request the sources separately so that I can check the facts.
15. As a writer, I want to provide a story brief, scene or idea so that my own material can become a comic story.
16. As a writer, I want the assistant to use the facts in my story brief so that it respects my original plot.
17. As a writer, I want the assistant to avoid web research for my supplied brief unless I request it so that my input remains the source of the story.
18. As a writer, I want thin input handled lightly so that missing details do not become made-up plot.
19. As a reader, I want the story rewritten in fresh, simple words so that it feels lively and is easy to understand.
20. As a reader, I want exactly five panels so that every story follows my chosen format.
21. As a reader, I want a clear title, short panel headings and separators so that the story is easy to scan.
22. As a reader, I want short lines, emojis, feelings, bold text and italics so that the story feels like a comic.
23. As a reader, I want short imagined dialogue and small decorative details when they fit so that the retelling feels natural without changing the facts.
24. As a reader, I want invented dialogue kept distinct from real quotations so that I am not misled about what was actually said.
25. As a reader, I want the fifth panel to end with two bold questions so that the story ends on a cliffhanger.
26. As a reader, I want a short TLDR with no new facts so that I can quickly recall the story.
27. As a reader, I want the answer to contain the story alone so that I do not get an unnecessary introduction or extra notes.
28. As a user of ChatGPT or Codex, I want an installable local plugin package so that I can use ShowVilla in supported setups.
29. As a user of Claude Code, I want a compatible plugin package so that I can load ShowVilla in my coding assistant.
30. As a Claude user, I want an uploadable skill archive so that I can add the story guide to Claude.
31. As a Gemini user, I want an uploadable skill folder or archive so that I can use the same story guide there.
32. As a DeepSeek Harness user, I want to place the shared skill in a supported skills folder so that the assistant can discover it.
33. As a user of another AI app, I want a manual fallback when it cannot load the skill so that I can still provide the instructions.
34. As the owner, I want the shared guides kept in one place so that updates do not drift between apps.
35. As the owner, I want upload packages rebuilt from the shared guide so that each app receives the same rules.
36. As the owner, I want the earlier project and its unfinished work preserved so that a new workspace does not destroy them.
37. As a user, I want the assistant to check the complete story before answering so that formatting and factual mistakes can be corrected.

## Implementation Decisions

- ShowVilla is a separate workspace beside the earlier SHOW-MCP workspace. The old project is preserved; moving to ShowVilla does not by itself delete or uninstall anything.
- The main storytelling skill is the entry point. It routes the assistant to focused supporting guides when the current request needs them.
- The supporting guides cover research, spoiler limits, the user's comic format and examples, and the final review. They are instructions for the same assistant, not separate AI agents or a server.
- A user-provided story brief is the source of facts unless the user explicitly asks for research or verification. For a show title without a usable brief, the assistant uses the host's available search and page-reading tools to gather episode-specific facts.
- The assistant distinguishes the work, adaptation, season and episode where needed. A title alone defaults to episode 1. If identity is genuinely ambiguous, it asks a short question rather than guessing.
- The assistant reads fetched pages rather than relying on search snippets alone, and keeps internal source notes tied to claims. It omits unresolved conflicting facts.
- The selected episode sets the default spoiler limit. An opening teaser hides the ending and major twists by default; an explicit full recap or ending request can reveal supported outcomes through that episode.
- For a provided brief, its content sets the facts and available ending. No later ending, new character, new ability or new plot event may be added.
- The assistant may rewrite, use small decorative details and create short imagined dialogue if these do not introduce or change material facts or events. Imagined dialogue must not be presented as an authentic quotation.
- The comic uses the user's requested title and heading pattern, exactly five panels, horizontal separators, and a final TLDR. Panels 1–4 contain at most six short body lines each. Panel 5 presents a supported cliffhanger and ends in exactly two bold questions beginning “Will” and “Or will”. The TLDR has three to five very short lines, with one emoji per line and no new facts.
- Style uses simple words, short lines, feelings, emojis, italics, bold text and pauses as appropriate. If the input has no supported dark or shocking moment, the assistant emphasizes a real unresolved problem instead of inventing one.
- The provided examples show the desired style. Where an example adds a plot event or conflicts with the stated format, the no-new-plot rule and the requested format take precedence.
- A normal story response contains the story and TLDR only. Source notes remain separate and may be supplied on request; higher-priority host requirements for citations still apply.
- Missing web access or essential facts are explained before a story is produced. The assistant asks for a summary or accessible source rather than claiming it researched something it could not access.
- A single shared skill bundle is the source for host-specific packaging. Local plugin manifests support ChatGPT/Codex and Claude Code; separate upload archives support Claude and Gemini; DeepSeek Harness can discover the skill through its supported local skills folders. Other apps may require manually supplying the guides.
- Availability, upload rules, browsing and file access depend on each app and account. A model name alone does not guarantee plugin support.
- The assistant performs the research, writing and review with its own available capabilities. Self-checking and instruction files improve consistency but do not provide independent or guaranteed validation.

## Testing Decisions

- Test at the highest useful seam: give the packaged skill realistic requests in each available host and inspect the resulting story or clear explanation. Judge observable behavior rather than exact wording or internal steps.
- For a supplied brief, check that the output has five panels, follows the requested headings and line limits, ends panel 5 with the two required bold questions, and has a three-to-five-line TLDR with one emoji per line.
- Include a sparse brief and examples with tempting missing details. Check that dialogue and decorative details do not create a new character, ability, material fact, event or ending.
- For a named episode, check that the correct adaptation and episode are researched, sources support the included facts, the ending is hidden by default and later-episode facts are absent. Try an explicit full-recap request and check that its boundary is still respected.
- For missing browsing and ambiguous identity, check that the assistant states the limitation or asks a concise question instead of inventing research.
- For conflicting sources, check that an unresolved disputed detail is omitted.
- Validate skill metadata, referenced-file paths, marketplace manifests and upload archive contents. Verify that the host-specific packages include the complete shared guide.
- Test actual discovery, installation, web access and a sample story in each target app where an account and environment are available. A valid package or manifest alone does not prove successful installation or story quality.
- Prior art: the previous SHOW-MCP project included tests for its server, spoiler rules and validation, but those tests do not by themselves verify the new instruction-only skill. The new bundle currently has metadata, manifest, link and archive checks; real cross-app behavior remains to be tested.

## Out of Scope

- Running or rebuilding the old SHOW-MCP server, its programmatic approval flow or an external model-provider stage.
- Publishing ShowVilla to a public marketplace or changing an existing installation without a separate request.
- Guaranteeing that all AI apps support plugin installation, web browsing, linked files or perfect compliance.
- Automatically deleting the earlier project, its worktree or uncommitted changes.
- Adding new plot, new characters or abilities to make a story more dramatic.

## Further Notes

- ShowVilla currently exists as a separate workspace with a storytelling skill, supporting guides, local marketplace manifests and upload archives. Skill metadata and archive contents were checked; Claude Code's manifest validation passed with warnings.
- Installation and full story behavior have not yet been verified in all named apps. App availability and setup may change.
- The prior design proposed no imagined dialogue; the later discussion explicitly allowed short imagined dialogue and minor decorative details without changing the plot. The later decision applies.
- The earlier discussion asked whether a six-line limit should apply to every panel, but that specific question was not answered. This specification follows the original skeleton's explicit six-line limit for panels 1–4 and its separate cliffhanger requirements for panel 5.
- No issue tracker or project-specific triage labels were supplied for this workspace. This document is a local specification and has not been published as an issue.