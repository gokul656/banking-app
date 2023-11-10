# Banking app

## Overview
This application simulates a basic banking system. It is built following Clean Architecture principles



### Prerequisites
- Python 3.0 or higher

### To run the application
```
python3 main.py
```

### Structure
The application is organized as follows:
```
src/
├── domain/                  # Contains business entities and domain logic.
├── exception/               # Custom exception classes for domain-specific errors.
├── infrastructure/          # Data persistence and infrastructure services.
├── use_cases/               # Application use cases encapsulating business rules.
└── config/                  # Centralized configuration and application context.
└── main.py                  # Entry point for the application flow.
```
