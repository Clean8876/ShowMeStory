# ShowVilla host checks

"Package checked" means file checks passed. "Installed" requires observing the skill loaded in the named app. "Behavior passed" requires reviewing a real result. Public publishing is separate.

| App | Intended route | Package checks | Installed | Story behavior |
| --- | --- | --- | --- | --- |
| ChatGPT | Local marketplace where available | Checked locally | Not tested | Not tested |
| Codex | Local plugin or shared skill | Checked locally | Not tested | Not tested |
| Claude Code | Local marketplace or one-session folder | Checked locally | Not tested | Not tested |
| Claude | Skill ZIP upload | Checked locally | Not tested | Not tested |
| Gemini | Skill folder or ZIP upload | Checked locally | Not tested | Not tested |
| DeepSeek Harness | Supported skills directory | Checked locally | Not tested | Not tested |
| Other chat apps | Manually supplied guides | Not applicable | Not a plugin install | Not tested |

## Package records

Record command, date, environment, exit code, concise output and warnings. Replace pending entries with actual results only.

## Host record

Host/version:
Date:
Account or capability limits observed (no credentials):
Package version:
Install route:
Evidence the main guide and references loaded:
Behavior cases:
Actual response or transcript:
Sources used:
Outcome and limits:

A missing account or tool is blocked, not passed. A valid package alone does not prove installation or correct story behavior.
## Checks completed on 2026-11-01

- Skill metadata: local quick validator passed.
- Package behavior: three Python tests passed, including archive contents, rebuild updates and missing-file preservation.
- Plugin identity, marketplace paths, linked files and both archives: consistency check passed.
- Claude Code marketplace and plugin manifest validation: both passed with warnings. The marketplace description and plugin author are optional and were not invented.
- Old server dependency search under the new plugin: no matches.
- Claude Code sign-in: unavailable; the CLI reported not signed in. No installation or live story test was attempted.
- Codex CLI sign-in check: unavailable because its installed launcher could not find its Node package. This does not establish the state of the Codex desktop app.
- ChatGPT, Claude, Gemini and DeepSeek Harness installation and story behavior: not tested in this session. No account, browser or app availability claim is made.
- Research, spoiler, conflict, no-web and comic behavior cases remain not tested in actual host sessions. Package checks do not validate model outputs.
