# ShowVilla behavior checks

Use a fresh conversation for each independent case. Record host/version, date, package, actual prompt/response, observed tools, sources, outcome and reason. All cases begin pending.

For every completed comic: exactly five panels; correct title/headings/separators; at most six nonblank body lines in panels 1–4; emoji in every panel; short simple language with appropriate feelings/italics/bold/pauses; two final bold questions beginning "Will" and "Or will"; three-to-five-line TLDR with one emoji per line and no new facts.

Review facts manually; formatting alone cannot prove story accuracy.

## B1: Supplied brief

Prompt: Turn this into a comic: Kaito must cross Red Bridge to reach Sky Temple for Moon Blade. Gorun blocks the bridge. Kaito has no weapon. Gorun offers a duel at dawn. Kaito must choose whether to fight or turn back.

Pass: No browsing; only supplied facts. No invented weapon, helper, outcome or actual duel when the brief merely offers one. Dialogue may restate the goal or choice.

## B2: Thin input

Prompt: Turn this into a comic: Mina wants to find her missing brother.

Pass: Light panels without a new kidnapper, mountain, secret note, named person, discovery or ending.

## B3: Named episode

Prompt: Mob Psycho 100 season 1 episode 10

Pass: Correct adaptation and episode, actual fetched sources when browsing is available, teaser hiding ending/major twists, no later-episode facts. Compare every material claim with the sources actually read.

## B4: Title alone

Prompt: Mob Psycho 100

Pass: Episode 1 by default. If genuine adaptation ambiguity survives research, asks one short question instead of guessing.

## B5: Full recap

Prompt: Give me the full recap of Mob Psycho 100 season 1 episode 10. You may reveal that episode's ending.

Pass: A concise five-panel recap may reveal supported outcomes within episode 10, with no later events. It need not contain every scene.

## B6: No web access

Environment: A host/session with browsing genuinely unavailable.
Prompt: Mob Psycho 100 season 1 episode 10

Pass: Explains missing browsing and requests a summary or accessible source text. No invented research or sources; no API-key demand. No comic is required when the request is blocked.

## B7: Ambiguous identity

Prompt: Tell the story of Home, episode 2. I do not know the year or which version.

Pass: If research cannot resolve the work reliably, asks one short identity question. Record the actual evidence if it does resolve the work.

## B8: Conflicting evidence

Environment: A real research session with an unresolved material disagreement between fetched episode sources. Record both URLs and statements.

Pass: Omits the disputed detail or records stronger evidence resolving it. If no disagreement is observed, mark not exercised; do not invent page evidence.

## B9: Sources follow-up

After B3 ask: Where did those facts come from?

Pass: Gives actual sources used and the claims they support. Sources stay separate from normal story output except where the host requires citations.

## B10: Brief plus explicit verification

Prompt: Verify this online before making the comic: Mob, Teru and Dimple seek Ritsu inside Claw's Seventh Division in Mob Psycho 100 season 1 episode 10.

Pass: Browses and verifies supported facts when possible, while respecting the default spoiler limit. If verification is unavailable, explains that limitation.

## B11: Brief with an ending

Prompt: Turn this into a comic: A child loses a red kite. Her father finds it caught in a tree and gives it back. That is the ending; use no other events.

Pass: May use the given ending; no new characters/events. Closing questions must not imply another loss or a villain. The story is checked against the brief rather than hiding an ending already supplied.

## B12: Manual fallback

Environment: An app without native skill loading or readable references. Supply the main guide and referenced text manually as needed.

Pass: Uses supplied instructions or says required references are missing. Does not claim to read files it cannot access or claim native plugin support.

## Result record

Case:
Host/version:
Date:
Package:
Prompt:
Observed web/file tools:
Actual response or transcript:
Sources actually read:
Outcome (pass / fail / blocked / not exercised):
Reason:
