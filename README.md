# ShowMeStory (ShowVilla)

[![Tests](https://github.com/Clean8876/ShowMeStory/actions/workflows/ci.yml/badge.svg)](https://github.com/Clean8876/ShowMeStory/actions/workflows/ci.yml) [![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

ShowVilla turns a show episode or your own summary into a short, five-panel comic. For a named show it uses the AI app's own web tools to look up the episode. It hides the ending by default.

The files live in [plugins/showvilla/skills/tell-story](plugins/showvilla/skills/tell-story). The main guide opens separate guides for research, spoilers, format and checking. The story-format guide contains the format and examples requested by the creator. ShowVilla has no MCP server or separate API key.

## Install or use

### ChatGPT and Codex

1. Add this folder as a local marketplace. In a terminal:
   ```powershell
   codex plugin marketplace add "."
   ```
   On another computer, use that computer's path to the ShowVilla folder instead.
2. Restart the ChatGPT desktop app. In the Plugins Directory, choose **ShowVilla** and install **showvilla**. Start a new chat and choose the plugin.
3. Local marketplace availability varies by app and account. This package has not been published to the public directory. See [OpenAI's local marketplace guide](https://developers.openai.com/plugins/build/plugins).

### Claude Code

Run these in a terminal after opening this folder:
```powershell
claude plugin marketplace add .
claude plugin install showvilla@showvilla-local
```
Start a new Claude Code session and use `/showvilla:tell-story`. To try it for one session without installing, run `claude --plugin-dir ./plugins/showvilla`. See [Claude Code's marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces).

### Claude

In Claude, open **Customize > Skills > Create skill > Upload a skill** and upload [dist/showvilla-claude-skill.zip](dist/showvilla-claude-skill.zip). Enable it, then start a chat. Availability and required settings depend on your account; see [Claude's instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

### Gemini

Open **Customize > Skills > Create > Upload** and upload [dist/showvilla-gemini-skill.zip](dist/showvilla-gemini-skill.zip), or select the `plugins/showvilla/skills/tell-story` folder including its references. See [Gemini's instructions and account requirements](https://support.google.com/gemini/answer/17094296).

### DeepSeek

DeepSeek Harness can discover the shared skill. Copy the entire `plugins/showvilla/skills/tell-story` folder to `<your-project>/.agents/skills/tell-story` or to your user skills folder `~/.agents/skills/tell-story`, and start a new session. The local skill provider and skill tool must be enabled. See the [DeepSeek Harness guide](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.md).

DeepSeek's regular chat app may not provide the same skill installation or file access. If it cannot load the folder, paste the main guide and relevant reference text into the chat. Do not assume all DeepSeek apps install Harness plugins.

## What has been checked

The skill metadata, linked files, local manifests and both upload ZIPs passed local checks. Claude Code's validator reported optional marketplace-description and author warnings. The apps have not yet been tested with the installed skill; see [host checks](docs/host-checks.md) for the current results and limits.

## Using it

- Give it a show name and episode, such as `Mob Psycho 100 season 1 episode 10`.
- Give it your own summary, scene or idea instead.
- Ask for the episode ending if you want a full recap.
- Ask for sources separately if you want the research links.

The AI app must have working web search and page access to research a title. If it cannot browse, provide a summary. Uploaded skills and AI self-checks do not guarantee perfect adherence; review the output.

## Update the upload files

Edit the maintained guides under plugins/showvilla/skills/tell-story, then run from the ShowVilla folder:

    python scripts/build_packages.py

Both uploads are rebuilt from the same source snapshot. Python is needed only to rebuild packages, not to use an uploaded skill.

Check archive building with:

    python -m unittest discover -s tests -p "test_packages.py" -v

See [behavior checks](docs/behavior-checks.md) and [host checks](docs/host-checks.md) for verification details.
