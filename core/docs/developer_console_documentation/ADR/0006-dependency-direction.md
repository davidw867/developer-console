# ADR 0006 – One-Way Dependency Rule

## Status

Accepted

## Context

As Developer Console grows, maintaining a clear dependency hierarchy is critical
to avoid circular imports, hidden coupling, and architectural drift.

Every package should have a single direction of dependency.

Higher-level layers orchestrate lower-level layers.

Lower-level layers must never depend on higher-level layers.

## Decision

Developer Console follows a strict one-way dependency graph.

Dependencies may only flow downward.

Commands
    ↓
Services
    ↓
Validators
    ↓
Wrappers
    ↓
Interfaces
    ↓
Models

The following foundational packages may be imported by any layer:

• Constants
• Enums
• Exceptions
• Logging
• Utilities

These foundational packages must never import higher-level layers.

## Dependency Map

                Commands
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
               Interfaces
                    │
                    ▼
                 Models

────────────────────────────────────────

Available to ALL layers:

Constants
Enums
Exceptions
Logging
Utilities

## Rules

Commands may import:

- Services
- Validators
- Models
- Exceptions
- Constants
- Enums
- Logging
- Utilities

Services may import:

- Validators
- Wrappers
- Interfaces
- Models
- Exceptions
- Constants
- Enums
- Logging
- Utilities

Validators may import:

- Wrappers (only if required)
- Interfaces
- Models
- Exceptions
- Constants
- Enums
- Logging
- Utilities

Wrappers may import:

- Interfaces
- Models
- Exceptions
- Constants
- Enums
- Logging
- Utilities

Interfaces may import:

- Models
- Exceptions
- Constants
- Enums

Models may import:

- Constants
- Enums

Models should never depend on Wrappers, Services, or Commands.

## Consequences

Advantages

- Prevents circular imports.
- Makes testing easier.
- Keeps responsibilities isolated.
- Allows providers to be replaced independently.
- Supports long-term maintainability.

Disadvantages

- Requires discipline.
- Sometimes requires dependency injection instead of direct imports.
