# Developer Console Architecture — Executive Overview

**Architecture version:** 1.0  
**Status:** Frozen  
**Primary target:** Termux  
**Secondary target:** Linux

Developer Console uses a layered, provider-oriented architecture. Commands delegate to services. Services coordinate behavior through wrappers and interfaces. Wrappers isolate external APIs, tools, filesystems, and subprocesses. Models carry data, validators protect boundaries, and dependency injection assembles the system.

```text
Commands → Services → Wrappers → Interfaces → Providers / External Systems
```

Supporting layers include models, validators, exceptions, constants, enums, utilities, logging, events, and dependency injection.

---

# Developer Console Architecture — Core Design Principles

The architecture follows separation of concerns, dependency inversion, explicit dependency injection, provider isolation, minimal dependencies, predictable errors, data-focused models, stateless utilities, centralized logging, and testability.

High-level behavior depends on interfaces rather than concrete provider implementations. External exceptions are translated into project exceptions before crossing wrapper boundaries. The standard library is preferred where practical, and every layer must be testable in isolation.

---

# Developer Console Architecture — Complete Directory Structure

```text
core/
├── commands/
├── constants/
├── dependency_injection/
├── enums/
├── events/
├── exceptions/
├── interfaces/
├── logging/
├── models/
├── services/
├── tests/
├── utils/
├── validators/
└── wrappers/
```

Provider folders may include `aws`, `azure`, `bitbucket`, `docker`, `filesystem`, `git`, `github`, `gitlab`, `kubernetes`, `repository`, and `terminal`.

A provider folder should only be created in a layer when that provider actually needs code in that layer.

---

# Developer Console Architecture — Layer Responsibilities

Commands parse user intent and delegate to services. Services coordinate use cases. Wrappers adapt external systems. Interfaces define stable contracts. Models carry structured data. Validators reject invalid input or state. Exceptions communicate meaningful failure categories. Utilities provide small stateless helpers. Events describe that something happened and must not own business logic.

Commands must not call SDKs directly. Services must not parse raw CLI input. Wrappers must translate provider errors. Models must not orchestrate workflows.

---

# Developer Console Architecture — Data and Control Flow

```text
User → Command Parser → Command → Validator → Service → Interface → Wrapper → Provider
```

Responses return through wrapper normalization into internal models, then through the service and command output layer.

External errors are caught by wrappers, translated into project exceptions, optionally enriched by services, and converted into user-facing output by commands.

Validation happens near the protected boundary: CLI syntax at commands, domain values in models or validators, provider prerequisites before wrappers, and response validation inside wrappers.

---

# Developer Console Architecture — Dependency Injection

The application uses one clear composition root to create configuration, loggers, provider clients, wrappers, services, commands, and event dispatchers.

Constructor injection is the default. Business classes must not read global configuration directly. Services must not instantiate wrappers. Tests should substitute fakes without credentials. The dependency injection system must remain lightweight and understandable.

---

# Developer Console Architecture — Services, Wrappers, and Interfaces

```text
Service → Interface ← Wrapper
```

Services depend on interfaces. Wrappers implement interfaces. Interfaces use internal models and project exceptions rather than provider SDK types.

Wrappers own SDK calls, HTTP calls, subprocess interaction, filesystem boundary behavior, provider data mapping, and external exception translation. Services own use-case coordination and application rules.

---

# Developer Console Architecture — Models, Validators, and Exceptions

Models represent stable internal data and should not depend on provider SDK response classes.

Validators protect input and state but do not perform API calls, modify files, or coordinate services.

The exception hierarchy should distinguish validation, configuration, provider, authentication, permission, not-found, command, and filesystem failures. Error messages should guide action without leaking sensitive information.

---

# Developer Console Architecture — Logging and Events

Logging flows from application modules through a central logger, formatter, and handler to console, file, or test capture.

Use `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL` consistently. Never log tokens, passwords, private keys, authorization headers, or sensitive environment values.

Events are immutable descriptions such as `RepositoryCloned`, `AuthenticationFailed`, `CommandCompleted`, or `ProviderUnavailable`. They may support audit logging, metrics, notifications, or cache invalidation but must not become a hidden service layer.

---

# Developer Console Architecture — Provider Expansion Strategy

To add a provider: identify the capability, reuse or define an interface, add constants and enums only when needed, define provider exceptions, map data into internal models, implement validators and wrappers, extend services and commands, register dependencies, and add tests and documentation.

Generic services should not branch repeatedly on provider names. Dependency selection belongs in the composition root. Providers may have different capabilities; interfaces should represent real common behavior rather than force false equivalence.

---

# Developer Console Architecture — Coding and Testing Standards

Use type hints for public behavior, small modules, explicit returns, dataclasses where suitable, directional imports, and no mutable global state.

Circular imports are prohibited. Every behavior change should include deterministic tests. Unit tests avoid network access and real credentials. Filesystem tests use temporary directories. External providers are mocked or replaced with fakes.

Recommended lightweight tools include `pytest`, `ruff`, `mypy`, and `coverage`.

---

# Developer Console Architecture — Freeze Policy and Future Evolution

Architecture version 1.0 is frozen. Adding classes, provider modules, tests, utilities, commands, or documentation within existing boundaries does not require an ADR.

Adding or removing a core layer, reversing dependency direction, introducing a framework-level DI container, adding a plugin runtime, changing the event model, replacing the command architecture, or changing the primary platform strategy requires an ADR.

Possible future capabilities include plugin discovery, remote execution, secure credential stores, background jobs, rich terminal interfaces, and web or desktop front ends. None should compromise the lightweight Termux-first core.
