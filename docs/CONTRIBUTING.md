# Contributing Guide

Thank you for contributing to the Developer Console project.

This project prioritizes readability, maintainability, consistency, and safety over clever code.

Before contributing, please read this document and the Architecture documentation.

---

# Guiding Principles

Every contribution should follow these principles.

1. Readability over brevity.
2. Explicit is better than implicit.
3. Validate early.
4. Fail with meaningful errors.
5. Keep responsibilities separated.
6. Every public feature should be testable.
7. Every layer has one responsibility.
8. Code should be easy to understand six months from now.

If a design decision violates one of these principles, reconsider the implementation.

---

# Project Architecture

The project follows a layered architecture.

```
UI
 ↓
Services
 ↓
Wrappers
 ↓
External Tools
```

Supporting layers:

```
Validators
Models
Interfaces
Caches
Exceptions
Enums
```

Each layer has a single responsibility.

---

# Layer Responsibilities

## Validators

Responsible for validating all user input.

Validators MUST NOT:

- execute commands
- access GitHub
- access the file system

Validators ONLY validate.

---

## Services

Services contain business logic.

Services:

- validate workflow
- coordinate operations
- call wrappers

Services MUST NOT execute shell commands directly.

---

## Wrappers

Wrappers communicate with external tools.

Examples:

- Git
- GitHub CLI
- Docker
- Terraform

Wrappers should contain minimal logic.

Their job is translating Python calls into external commands.

---

## Models

Models represent project data.

Models should not contain business logic.

---

## Interfaces

Interfaces define contracts between implementations.

Services should depend on interfaces whenever practical.

---

## Caches

Caches store temporary information that reduces unnecessary external calls.

Caches must never become the source of truth.

---

## Exceptions

Use project-specific exceptions whenever possible.

Avoid raising generic Exception.

---

# Naming Conventions

Classes

Use PascalCase.

Example:

```
GitHubService
RepositoryModel
```

Functions

Use snake_case.

```
create_repository()
delete_repository()
```

Variables

Use descriptive names.

Good:

```
repository_name
workflow_identifier
```

Bad:

```
r
x
tmp
```

---

# Validation Rules

Validation always happens before execution.

Every public entry point should validate inputs.

Validation belongs inside Validators whenever possible.

---

# Error Handling

Raise the most specific exception available.

Good:

```
RepositoryNotFoundError
```

Avoid:

```
Exception
```

Error messages should explain:

- what failed
- why it failed
- how to fix it

---

# Testing

Every feature requires tests.

Mirror the project structure.

Example:

```
core/services/github.py

↓

tests/test_services/github.py
```

Tests should be:

- isolated
- deterministic
- repeatable

Never depend on network availability unless explicitly testing integration behavior.

---

# Documentation

Public classes should include docstrings.

Complex algorithms should include comments explaining why, not what.

Keep Architecture.md updated when introducing new architectural concepts.

---

# Code Style

Follow PEP 8.

Maximum line length: 88 characters.

Prefer explicit code over clever one-liners.

Avoid deeply nested logic.

Use early returns whenever possible.

---

# Imports

Standard library

↓

Third-party libraries

↓

Project imports

Separate groups with one blank line.

---

# Commits

Write clear commit messages.

Examples:

```
Add GitHub repository validator

Implement workflow validation

Refactor GitHub wrapper architecture

Add unit tests for repository service
```

Avoid:

```
stuff

fix

changes

update
```

---

# Pull Requests

Each pull request should:

- have a single purpose
- include tests
- update documentation if needed
- pass all existing tests

---

# Future Integrations

Every new integration should follow the existing architecture.

Example:

```
validators/docker.py

services/docker.py

wrappers/docker.py

tests/test_wrappers/docker.py
```

Avoid creating special cases.

Consistency is more valuable than convenience.

---

# Philosophy

This project is designed to grow.

Small improvements made consistently are better than large rewrites.

Favor clean architecture over quick solutions.

Write code that future contributors will enjoy maintaining.

---

# The Broken Window Rule

Leave the codebase better than you found it.

If you notice:

- confusing names
- missing documentation
- outdated comments
- duplicated logic
- inconsistent formatting

take a few minutes to improve it while you're 
already working in that area.

Small improvements accumulate into a codebase 
that remains clean and maintainable over time.
