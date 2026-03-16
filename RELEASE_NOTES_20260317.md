# Release Notes 2026-03-17

## Summary

This release improves NobelWriter's usability in constrained agent environments where external APIs, file writers, or helper tools may be unavailable.

It also adds clearer end-user guidance for how NobelWriter is actually used across Codex, GPT-OSS, Jules/Antigravity, and local LLM hosts such as Ollama.

## Highlights

- strengthened `novel-writing` so lightweight models can route, assume, and draft without stalling
- added no-tools fallback guidance for Jules / Antigravity
- added no-tools fallback guidance for GPT-OSS and local LLM hosts
- added a new local platform pack for Ollama
- added ready-to-paste system prompt, short policy, fallback template, Modelfile example, Open WebUI example, and model presets for local deployment
- added user-facing FAQ explaining that NobelWriter is an agent-operated workflow, not a standalone CLI

## Key Files

- `README.md`
- `USAGE_FAQ.md`
- `skills/novel-writing/SKILL.md`
- `skills/novel-writing/references/lightweight-execution-examples.md`
- `Platform/Google/Antigravity/JULES_NO_TOOLS_FALLBACK_TEMPLATE.md`
- `Platform/Google/Antigravity/SHORT_NO_TOOLS_POLICY.md`
- `Platform/OpenAI/GPT-OSS/NO_TOOLS_FALLBACK_TEMPLATE.md`
- `Platform/OpenAI/GPT-OSS/SHORT_NO_TOOLS_POLICY.md`
- `Platform/Local/Ollama/SYSTEM_PROMPT.md`
- `Platform/Local/Ollama/MODELFILE_EXAMPLE.md`
- `Platform/Local/Ollama/OPEN_WEBUI_SETUP.md`
- `Platform/Local/Ollama/MODEL_PRESETS.md`

## Operational Impact

- Korean fiction drafting should now continue even when tool access is blocked.
- File save failure should downgrade file output, not block prose generation.
- Users should be less likely to ask where the CLI is or how to invoke a chapter-writing command.

## Recommended Post-Release Check

- test one planning request
- test one prose-generation request
- test one no-tools fallback case in a constrained host
