# Project coding conventions

Apply these conventions throughout implementation, deployment, and maintenance work in this repository:

- Use clear, simple English names for variables, functions, classes, modules, files, and URLs.
- When a domain-specific name would otherwise be unclear, Vietnamese names without diacritics may be used for difficult variable names, database fields, JSON keys, and test names. Keep ordinary identifiers in English; do not translate names just for the sake of translating them.
- Write Vietnamese comments that explain the purpose of functions and non-obvious logic, including important loops and conditions. Comments should help a Vietnamese-speaking maintainer understand why the code is there.
- Keep names consistent across API contracts, database models, serializers, and frontend integrations. If a Vietnamese no-diacritic field or key is needed, document its meaning in a nearby Vietnamese comment or API/schema documentation.

These conventions apply to new code and to code changed as part of this project. Do not rename existing public interfaces solely for style unless the task requires it.
