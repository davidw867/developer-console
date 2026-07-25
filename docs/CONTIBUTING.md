# Contributing to Developer Console

Thank you for your interest in contributing to 
Developer Console.

This project is intentionally designed to be lightweight, 
modular, and educational. Every contribution should 
improve the project without increasing unnecessary 
complexity.

---

# Project Philosophy

Developer Console follows a few guiding principles.

- Keep the project lightweight.
- Prefer readability over cleverness.
- Build for Termux first.
- Separate responsibilities.
- Write code that is easy to test.
- Document architectural decisions.
- Preserve backwards compatibility whenever practical.

---

# Before You Begin

Please read:

- README.md
- ARCHITECTURE.md
- Any relevant Architecture Decision Records (ADR)

Understanding the architecture before writing code 
prevents unnecessary redesigns later.

---

# Development Workflow

Every change should follow this process.

1. Create a feature branch.
2. Implement one focused change.
3. Write or update tests.
4. Run formatting and static analysis.
5. Run the test suite.
6. Update documentation.
7. Submit a Pull Request.

---

# Branch Naming

Examples

```
feature/github-service

feature/git-wrapper

bugfix/repository-validation

docs/update-readme

refactor/service-layer
```

---

# Commit Messages

Use descriptive commits.

Examples

```
feat(github): add repository service

fix(validators): reject empty repository names

docs: update architecture guide

test(git): improve wrapper coverage
```

---

# Coding Standards

## General

- Use Python type hints.
- Write self-documenting code.
- Keep functions small.
- Keep classes focused.
- Avoid unnecessary abstractions.
- Avoid hidden side effects.

---

## Naming

| Item      | Style            |
|---|-------|----|-------------|
| Classes   | PascalCase       |
| Functions | snake_case       |
| Variables | snake_case       |
| Constants | UPPER_SNAKE_CASE |
| Modules   | snake_case       |

---

## Documentation

Public classes and methods should include docstrings.

Document why something exists—not just what it does.

---

# Architecture Rules

Commands

- Parse user input.
- Call services.
- Display results.

Commands must never call providers directly.

---

Services

- Coordinate workflows.
- Use interfaces.
- Use wrappers.
- Return models.

Services should not know provider implementation details.

---

Wrappers

Wrappers communicate with:

- APIs
- SDKs
- Filesystems
- Git
- Docker
- Terminal commands

Wrappers normalize provider behavior.

---

Validators

Validators verify:

- User input
- Configuration
- Provider requirements
- Model state

Validators never mutate application state.

---

Models

Models represent data.

Models should remain lightweight.

---

Utilities

Utilities must remain stateless.

---

Dependency Injection

Dependencies should always be supplied externally.

Avoid constructing dependencies inside services.

---

# Testing Requirements

Every new feature should include tests.

Recommended coverage:

- Unit tests
- Integration tests
- Validator tests
- Wrapper tests
- Service tests

Provider tests requiring credentials should remain 
optional.

---

# Documentation Requirements

Documentation must be updated whenever:

- A provider changes.
- Commands change.
- Configuration changes.
- Architecture changes.
- New public APIs are introduced.

---

# Architecture Decision Records

Large structural changes require an ADR.

An ADR must explain:

- Context
- Decision
- Alternatives
- Consequences

Do not reorganize the architecture without an accepted ADR.

---

# Pull Request Checklist

Before submitting, verify:

- [ ] Tests pass.
- [ ] Documentation updated.
- [ ] No secrets committed.
- [ ] Logging reviewed.
- [ ] Exceptions handled.
- [ ] Interfaces respected.
- [ ] Architecture preserved.

---

# Security

Never commit:

- API keys
- Access tokens
- Private keys
- Passwords
- Sensitive configuration

Validate all external input.

Normalize provider exceptions.

---

# Performance

Developer Console targets lightweight environments.

When contributing:

- Avoid unnecessary dependencies.
- Prefer lazy loading.
- Minimize startup time.
- Keep memory usage reasonable.

---

# Final Principle

The best contribution is not the one with the most code.

It is the one that makes the project easier to understand, 
easier to maintain, and easier to extend while preserving 
the architecture.
