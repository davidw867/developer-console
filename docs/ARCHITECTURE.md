# Developer Console Architecture

Version: 2.0
Status: Active
Last Updated: July 2026

---

# Overview

Developer Console is a lightweight, extensible developer toolkit designed to provide a consistent interface over multiple development tools, services, and APIs.

The project follows a domain-driven architecture emphasizing:

- Simplicity
- Readability
- Testability
- Maintainability
- Extensibility
- Low resource usage

The initial target platform is **Termux**. Once stable, support will expand to Linux, macOS, and Windows.

---

# Guiding Philosophy

Developer Console exists to hide the complexity of external tooling while exposing a clean, consistent Python API.

External tools should feel interchangeable.

Examples:

- Git
- GitHub CLI
- Docker
- Kubernetes
- Terraform
- SSH
- Local Filesystem

Every integration follows the same architectural rules.

---

# Architectural Laws

## Law 1 — Single Responsibility

Every module, class, and function has one clearly defined responsibility.

If a component performs multiple unrelated tasks, it should be split.

---

## Law 2 — Domain First

The project is organized around domains, not file types.

Example:

core/
    services/
        github/
        git/

instead of

core/
    github_services.py

---

## Law 3 — Separation of Concerns

Responsibilities are separated into dedicated layers.

Commands

↓

Validators

↓

Services

↓

Wrappers

↓

External Tool

No layer should bypass another without a documented reason.

---

## Law 4 — Wrappers Never Contain Business Logic

Wrappers only communicate with external systems.

Wrappers:

✓ Execute commands

✓ Parse responses

✓ Translate errors

Wrappers do NOT:

✗ Make business decisions

✗ Validate user input

✗ Implement workflows

---

## Law 5 — Services Own Business Logic

Business decisions belong inside Services.

Examples:

✓ deciding execution order

✓ coordinating wrappers

✓ caching

✓ retry policies

✓ orchestration

---

## Law 6 — Validation Happens Before Execution

Validation always occurs before commands are executed.

Invalid input should never reach wrappers.

---

## Law 7 — Models Belong to Developer Console

External APIs never leak into the rest of the application.

Wrappers convert external data into Developer Console models.

Example:

Git CLI Output

↓

GitRepositoryModel

↓

Service

↓

Command

---

## Law 8 — Commands Represent User Actions

Commands are the public entry point.

Commands should remain thin.

Commands delegate work to Services.

---

## Law 9 — Dependencies Point Downward

Allowed:

Commands

↓

Services

↓

Wrappers

↓

External APIs

Forbidden:

Wrappers importing Commands

Models importing Services

Enums importing Wrappers

---

## Law 10 — Consistency Over Cleverness

A predictable codebase is better than a clever one.

Follow established conventions unless there is a compelling reason not to.

---

## Law 11 — Test Everything Public

Every public component should have tests.

Production structure should be mirrored inside tests.

---

## Law 12 — Standard Library First

Prefer Python's standard library.

Third-party dependencies should only be introduced when they provide clear long-term value.

---

# High Level Architecture

Commands
    │
    ▼
Validators
    │
    ▼
Services
    │
    ▼
Wrappers
    │
    ▼
External Tools

---

# Core Components

## Commands

Represent user actions.

Examples:

- Clone Repository
- Push
- Doctor
- Status

Commands never contain business logic.

---

## Validators

Responsible for verifying input.

Examples:

- Path validation
- URL validation
- Configuration validation

---

## Services

Coordinate workflows.

Examples:

- Repository initialization
- Retry logic
- Multi-step operations
- Cache management

---

## Wrappers

Low-level communication layer.

Examples:

- Git CLI
- GitHub CLI
- Filesystem
- Terminal

Wrappers should be easily replaceable.

---

## Interfaces

Define contracts.

Interfaces make implementations interchangeable.

---

## Models

Represent Developer Console's domain objects.

Examples:

GitRepositoryModel

GitStatusModel

GitHubRepositoryModel

IssueModel

---

## Enums

Represent fixed sets of values.

Enums are grouped by domain.

---

## Exceptions

Provide meaningful, typed errors.

Never raise generic Exception when a domain-specific exception exists.

---

# Command Organization Principle

Commands are organized by the external tool they wrap.

Example:

commands/git/

wraps Git CLI

commands/github/

wraps GitHub CLI

Even if both perform similar operations, they remain separate because they represent different tools.

---

# Directory Organization Principle

Every major component follows the same domain structure.

Example:

services/
    github/

validators/
    github/

wrappers/
    github/

models/
    github/

interfaces/
    github/

This consistency reduces cognitive load.

---

# Naming Conventions

Packages

snake_case

Modules

snake_case

Classes

PascalCase

Functions

snake_case

Constants

UPPER_CASE

Enums

PascalCase

Exceptions

End with Exception

Wrappers

End with Wrapper

Validators

End with Validator

Services

End with Service

Models

End with Model

Providers

End with Provider

---

# Testing Philosophy

Tests mirror production.

Example:

core/services/github/

↓

tests/test_services/github/

Tests should verify:

- success paths
- failure paths
- edge cases
- invalid input

---

# Future Expansion

Developer Console is designed to support additional providers without architectural changes.

Examples:

Docker

Kubernetes

Terraform

AWS

Azure

GitLab

Bitbucket

SSH

SQLite

PostgreSQL

REST APIs

Each provider should follow the same architectural principles.

---

# Final Principle

Architecture exists to make future development easier.

If a design decision makes future contributors more productive while preserving simplicity, it is likely the correct decision.
