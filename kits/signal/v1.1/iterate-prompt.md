<!-- ByJTT prompt kit: signal v1.1 · iterate-prompt.md · kit version 1 · 2026-09-02.
     Delta prompt: use when the template is built and I want changes. Do not stack on top of
     build-prompt.md. -->

# Iterate on the Signal build (delta)

The template is built in this workspace and I want changes. Work like this:

1. Before touching code, write the change request as a short checklist and show it to me —
   confirm scope before editing (this template's design rules live in its manifest.json
   and design DNA: one accent family, generous whitespace, Fraunces/Inter, ember-line motif).
   If my request breaks a design rule, say so and offer the in-system alternative instead of
   silently breaking it.
2. Make the changes, smallest possible diff. Never delete files or sections unless I asked.
3. Re-verify after every batch: responsive at 375/768/1440, images load, no placeholder
   text, honest states kept (no fake checkout endpoints).
4. Show me the preview URL and the checklist with each item ticked. Wait for my next change
   request — or point me at `publish-prompt.md` when I say I'm done.

My changes: {{CHANGES}}
