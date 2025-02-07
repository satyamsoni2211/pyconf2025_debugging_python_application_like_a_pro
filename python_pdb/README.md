---
marp: true
title: PDB Debugger
---

# PDB Debugger

## Introduction


The **PDB Debugger** is a vital tool for Python developers, offering an interactive command-line interface to debug code. It allows you to set breakpoints, step through execution, and inspect variables, making it easier to identify and fix bugs efficiently.


---

## What is PDB?

- The Python Debugger (PDB) is a powerful interactive tool.
- It allows developers to debug Python programs.

---

## Changes since Python 3.7

- **Breakpoint Function**: Python 3.7 introduced the built-in `breakpoint()` function, which simplifies the process of entering the debugger. By default, it calls `pdb.set_trace()`, but it can be customized via the `PYTHONBREAKPOINT` environment variable.
- **Improved Display of Tracebacks**: The tracebacks in Python 3.7 are more informative, showing the variables involved in the error, which aids in quicker debugging.
- **Data Classes**: While not directly related to PDB, the introduction of data classes in Python 3.7 can make debugging easier by providing a clearer structure for data, which PDB can then inspect.
- **Context Variables**: Python 3.7 introduced context variables, which can be useful in asynchronous programming. PDB can be used to inspect these context variables during debugging sessions.

---

## Key Features

- Command-line interface for:
  - Setting breakpoints
  - Stepping through code
  - Inspecting variables
  - Evaluating expressions

---

## Why Use PDB?

- Essential for diagnosing and fixing issues in Python code.
- Helps understand the flow of execution.
- Identifies bugs effectively.

---

# Invoking PDB

## How to Use

- Directly from the command line.
- Integrated into Python scripts using the `pdb` module.

---

## Benefits

- Useful for debugging complex applications.
- Provides deeper insights into code behavior.
- Improves software quality.

---

# PDB Cheat Sheet

## Common Commands

| Command | Description |
|---------|-------------|
| `b`     | Set a breakpoint. |
| `c`     | Continue execution. |
| `s`     | Step into function. |

---

## More Commands

| Command | Description |
|---------|-------------|
| `n`     | Next line. |
| `l`     | List source code. |
| `p`     | Print expression. |

---

## Additional Commands

| Command | Description |
|---------|-------------|
| `q`     | Quit debugger. |
| `h`     | Help command. |
| `w`     | Stack trace. |

---

# Basic Commands

## Breakpoint (`b`)

- **Usage**: `b [lineno|function]`
- **Description**: Sets a breakpoint at a line or function.

---

## Continue (`c`)

- **Usage**: `c`
- **Description**: Continues execution until the next breakpoint.

---

## Step (`s`)

- **Usage**: `s`
- **Description**: Steps into the function call.

---

## Next (`n`)

- **Usage**: `n`
- **Description**: Steps to the next line in the current function.

---

## Print (`p`)

- **Usage**: `p expression`
- **Description**: Prints the value of an expression.

---

## Quit (`q`)

- **Usage**: `q`
- **Description**: Quits the debugger and terminates the program.

---

## Args (`a`)

- **Usage**: `a`
- **Description**: Prints the argument list of the current function.

---

## Return (`r`)

- **Usage**: `r`
- **Description**: Continues execution until the current function returns.

---

## Help (`h`)

- **Usage**: `h [command]`
- **Description**: Displays help for a specific command.

### Example Usage

- **General Help**: `h`
  - Displays a list of all available commands with brief descriptions.

- **Specific Command Help**: `h n`
  - Displays detailed help for the `next` command.

This command is particularly useful for beginners or when you need a quick reminder of what a command does.

---

# Conclusion

- PDB is a vital tool for Python developers.
- Enhances debugging capabilities and code quality.