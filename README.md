# Developer Console

A modular, extensible command-line toolkit for developers.

Developer Console provides a unified interface for common development tools such as GitHub, Git, repositories, configuration management, and future integrations including Docker, Kubernetes, Azure, AWS, and more.

The project is built around a layered architecture that emphasizes maintainability, testability, and clean separation of responsibilities.

---

## Project Goals

- Lightweight
- Cross-platform
- Termux-first
- Testable
- Extensible
- SOLID architecture
- Separation of responsibilities
- Minimal dependencies

---

## Project Status

**Current Version:** Architecture v1.0

The Developer Console architecture is now complete and frozen.

Development has transitioned from architecture design into implementation.

Future commits will primarily focus on implementing functionality, writing tests, and expanding provider support rather than reorganizing the project structure.

---

## Architecture

The project follows a layered architecture.

```
Application
    │
    ▼
Services
    │
    ▼
Validators
    │
    ▼
Wrappers
    │
    ▼
External CLI / APIs
```

Each layer has a single responsibility.

| Layer | Responsibility |
|-------|----------------|
| Validators | Validate all incoming data |
| Services | Business logic and orchestration |
| Wrappers | Execute external commands |
| Models | Domain objects |
| Interfaces | Contracts between implementations |
| Exceptions | Custom exception hierarchy |
| Caches | Temporary caching of external data |

For a complete description see:

```
docs/ARCHITECTURE.md
```

---

## Features

- Modular architecture
- Provider abstraction layer
- Dependency Injection
- Command architecture
- Service layer
- Wrapper layer
- Validation framework
- Domain models
- Centralized logging
- Utility library
- Event system foundation
- Git support
- GitHub support
- Extensible provider architecture

---
## Planned Provider Support

### Source Control

- Git
- GitHub
- GitLab
- Bitbucket

### Cloud

- AWS
- Azure

### Containers

- Docker
- Kubernetes

### Local

- Filesystem
- Repository
- Terminal

---

## Development Workflow

1. Implement feature
2. Write unit tests
3. Verify tests pass
4. Commit changes

The project should remain in a working state after every commit.
---
## Testing

Tests mirror the production code structure.

```
tests/
    test_models/
    test_services/
    test_validators/
    test_wrappers/
```

This organization makes every production component easy to locate and test.

---

## Project Structure

```
core/
docs/
tests/
wrappers/
```

Additional packages will be introduced as the project grows while maintaining the existing layered architecture.

---

## Design Principles

- Single Responsibility Principle
- Separation of Concerns
- Explicit Validation
- Composition over duplication
- Interface-driven development
- Small, testable components
- Readability over cleverness

---

## Development Roadmap

### Phase 1

- GitHub integration
- Validators
- Wrappers
- Services
- Models
- Unit tests

### Phase 2

- Git integration
- Repository management
- Configuration improvements

### Phase 3

- Docker
- Kubernetes
- Cloud providers
- Additional developer tooling

---

## Contributing

Please read:

```
docs/CONTRIBUTING.md
```

before submitting changes.

---

## License

Licensed under the Apache License, Version 2.0.

See the LICENSE file for details.
---

## Copyright

Copyright © 2026 David Anthony Workman

Licensed under the Apache License, Version 2.0.
