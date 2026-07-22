# Developer Console Architecture

Version: 1.0

---
Architecture Laws

1. Every class has one responsibility.

2. Business logic belongs in Services.

3. External communication belongs in Wrappers.

4. Validation happens before execution.

5. Models represent data, not behavior.

6. Every production module has corresponding tests.

7. Every integration follows the same folder structure.

8. Favor readability over cleverness.

9. Make invalid states impossible where practical.

10. If a feature doesn't fit the architecture, improve 
    the architecture before adding the feature.
---

# Purpose

The Developer Console is designed around a layered architecture.

Each layer has a single responsibility and communicates only with the
layers directly below it.

This separation keeps the code maintainable, testable, and easy to
extend.

---

# Architecture

```
Console/UI
     │
     ▼
 Services
     │
     ▼
 Wrappers
     │
     ▼
 External APIs / CLI Tools
```

Supporting Layers

```
Enums
Models
Validators
Caches
Interfaces
Exceptions
```

These layers are shared throughout the application.

---

# Layer Responsibilities

## Console

Responsible for:

- User interaction
- Displaying menus
- Reading user input
- Formatting output

The console never communicates directly with GitHub, Git, or external
services.

Instead it calls the Service Layer.

---

## Services

Responsible for business logic.

Examples:

- Authentication workflow
- Repository management
- Confirmation prompts
- Retry logic
- Permission checks
- Caching
- Rate limiting

Services coordinate multiple wrappers when necessary.

Services never build CLI commands.

---

## Wrappers

Responsible for communication with external tools.

Examples:

- GitHub CLI
- Git CLI
- Docker CLI

Wrappers should:

- Validate input
- Build commands
- Execute commands
- Return results

Wrappers contain no business logic.

---

## Validators

Responsible for validating input.

Examples:

- Repository names
- Branch names
- Issue numbers
- Workflow identifiers

Validators never execute commands.

Validators never perform business logic.

---

## Models

Represent application data.

Examples:

- Repository
- Pull Request
- Workflow
- User

Models should not perform external operations.

---

## Enums

Provide strongly typed constants.

Examples:

- GitHub resources
- Menu options
- Integration types

Enums eliminate magic strings.

---

## Interfaces

Define contracts between layers.

Interfaces allow implementations to be replaced without changing
dependent code.

---

## Caches

Store temporary application state.

Examples:

- Authentication tokens
- Current user
- Repository metadata
- Rate limit information

Caches never become the source of truth.

---

## Exceptions

Contain application-specific exception classes.

Examples:

- AuthenticationError
- RepositoryNotFound
- InvalidWorkflowIdentifier

This provides consistent error handling throughout the application.

---

# Dependency Rules

Allowed

Console
↓

Services
↓

Wrappers
↓

External Tools

Shared layers

Validators
Models
Enums
Caches
Interfaces
Exceptions

may be referenced where appropriate.

---

Forbidden

Console → Wrappers

Console → GitHub CLI

Wrappers → Services

Validators → Wrappers

Validators → Services

Models → Wrappers

Business logic inside wrappers.

---

# Folder Structure

```
core/
    caches/
    enums/
    exceptions/
    interfaces/
    models/
    services/
    validators/

wrappers/

tests/

docs/
```

Each integration should follow the same structure.

Example

```
GitHub

github.py
validators/github.py
services/github.py
wrappers/github.py
models/github.py
caches/github.py
interfaces/igithub.py
exceptions/github.py
tests/.../github.py
```

Future integrations should mirror this layout.

Examples

- Git
- Docker
- Kubernetes
- AWS
- Azure
- Terraform

---

# Testing Strategy

Every production module should have a corresponding test module.

Example

```
services/github.py
↓

tests/test_services/github.py
```

This mirrored structure keeps tests easy to locate.

---

# Design Principles

The Developer Console follows these principles:

- Single Responsibility Principle
- Separation of Concerns
- Composition over inheritance
- Explicit validation
- Consistent error handling
- Layered architecture
- Strong typing
- Test-first mindset
- Reusable integrations

---

# Development Workflow

When implementing a new integration:

1. Create enums
2. Create models
3. Create validators
4. Create wrappers
5. Create services
6. Create interfaces
7. Create caches
8. Create exceptions
9. Write tests
10. Update documentation

Following this workflow ensures every integration has a consistent
architecture.


