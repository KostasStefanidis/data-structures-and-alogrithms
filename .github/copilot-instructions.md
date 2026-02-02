# Copilot Instructions for Data Structures and Algorithms

## Project Overview

Educational Python 3.12 project implementing fundamental data structures with comprehensive type hints, OOP patterns, and parametric polymorphism using `TypeVar` and `Generic`.

## Core Architecture

### Structure Pattern
All data structures follow a consistent pattern:
- Located in [src/data_structures/](src/data_structures/)
- Use `TypeVar` for generic type support: `T = TypeVar("T")` or `K, V = TypeVar("K"), TypeVar("V")`
- Implement `__init__`, `__repr__`, `__str__`, `__len__`, and comparison magic methods
- Support both single items and collections in constructors where applicable
- Prefix private/internal methods with underscore: `_reallocate_array()`, `_heapify_up()`

### Type Hints Requirements
- ALL methods must include complete type hints for parameters and return types
- Use modern Python 3.12+ union syntax: `Node[T] | None` (not `Optional[Node[T]]`)
- Use PEP 604 union syntax: `list[T] | tuple[T]` (not `Union[List[T], Tuple[T]]`)
- Generic classes inherit from `Generic[T]` or `Generic[K, V]`

## Key Implementation Patterns

### Capacity Management
Dynamic structures (ArrayList, HashMap, RingBuffer) implement automatic resizing:
- Default capacity constants (e.g., `DEFAULT_CAPACITY = 4`)
- `_reallocate_array()` or `_reallocate_container()` methods double capacity
- Load factor checks trigger reallocation (HashMap uses 0.7 load factor)

### Error Handling
- Raise `IndexError` with descriptive messages for out-of-bounds access
- Raise `KeyError` for missing keys in HashMap/LRUCache
- Raise `TypeError` for invalid type comparisons with custom message format:
  ```python
  raise TypeError(f"Cannot compare {self.__class__.__name__} object to {type(other)}")
  ```

### Composition Over Inheritance
- HashMap and LRUCache compose ArrayList for internal storage
- Heap extends abstract base class `AbstractHeap` with `@abstractmethod` declarations
<!-- - Node classes are defined inline with their container classes -->


## Development Workflow

### Running Tests
```bash
python -m pytest tests/              # Run all tests
python -m pytest tests/test_ClassName.py  # Run specific test file
```

### CI/CD
- GitHub Actions run pytest and pylint on push/PR to main
- Test matrix: Python 3.10, 3.11, 3.12, 3.13, 3.14
- Workflows use reusable workflows from `KostasStefanidis/github-workflows`
- Both workflows require `security-events: write` permissions

### Code Quality Tools
```bash
pylint src/                          # Lint source code
black src/ tests/                    # Format code
isort src/ tests/                    # Sort imports
pytest-cov                           # Test coverage available
```

## Import Conventions

- Relative imports within [src/data_structures/](src/data_structures/) for composition:
  ```python
  from ArrayList import ArrayList  # Within same package
  from HashMap import HashMap
  ```
- Absolute imports from tests:
  ```python
  from src.data_structures.ArrayList import ArrayList
  ```

## When Adding New Data Structures

1. Create `src/data_structures/NewStructure.py` with:
   - TypeVar declarations at module level
   - Generic class with comprehensive magic methods
   - Private methods prefixed with underscore
   - Full type hints using modern syntax

2. Create `tests/test_NewStructure.py` with:
   - `TestNewStructure` class
   - Parametrized tests for all public methods
   - Edge case and error condition tests

3. Update README.md with:
   - Structure description and features
   - Time complexity analysis
   - Usage example

4. Run full test suite and linting before committing
