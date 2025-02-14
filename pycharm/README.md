---
marp: true
theme: gaia
paginate: true
class:
  - lead
  - invert
header: 'Debugging Python Applications Like a Pro'
footer: 'Satyam Soni | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/-satyamsoni/)'
---
<style>
section {
   font-size: 27px;
}
</style>

# Debugging in PyCharm

### Overview

- Learn to configure debugging for various project types.
- Master PyCharm’s debugging interface for effective use.
- Debug Python applications in diverse environments with ease.

Reference Document: [Python Debugging in PyCharm](https://www.jetbrains.com/pycharm/features/debugger.html)

---

<style scoped>
section {
   font-size: 22px;
}
</style>

# Configuring Debugging

### Simple Scripts
1. **Open your project** in PyCharm.
2. **Select your interpreter**: PyCharm usually detects it automatically, but you can set it manually via `File > Settings > Project: <project_name> > Python Interpreter`.
3. **Open your script**: Navigate to `Run > Edit Configurations`, and select `Add New Configuration` > `Python`.
4. **Set the script path**: Ensure the `Script path` is set to your current file.
5. **Run the debugger**: Click on the debugger logo or press `Shift + F9`.

![w:600 h:150 right](https://www.jetbrains.com/pycharm/features/screenshots/debugger.png)

---
<style scoped>
section {
   font-size: 22px;
}
</style>

### Creating Launch Configurations

<style scoped>
section {
   font-size: 22px;
}
</style>

1. **Access configurations**: Go to the debugger toolbar and select `Edit Configurations`.
2. **Choose configuration type**: Select the type of configuration you need (e.g., Python, Django, Flask).
3. **Fill in details**: Provide necessary details like script path, working directory, and environment variables.
4. **Save and run**: Save the configuration and click the debugger logo to start debugging.

![image](./images/image.png)

---

### FastAPI, Django, or Flask Applications

<style scoped>
section {
   font-size: 22px;
}
</style>

1. **Select the Python interpreter**: Ensure you are using the correct Virtual Environment for your project.
2. **Install dependencies**: Make sure all your app’s dependencies are installed via `pip install -r requirements.txt`.
3. **Select debugging configuration**: Choose the appropriate configuration for your framework (e.g., Django, Flask).
4. **Start debugging**: Click on the debugger logo or use `Shift + F9`.

---

# PyCharm’s Debugging Interface

<style scoped>
section {
   font-size: 22px;
}
</style>

### Key Features
- **Breakpoints**: Pause execution at specific lines to inspect the state.
- **Variables**: Dynamically inspect and modify variable states.
- **Call Stack**: Navigate through the order of function calls to understand execution flow.
- **Watch**: Monitor specific expressions or variables in real-time.
- **Debug Console**: Execute commands and evaluate expressions during debugging sessions.

---

### Setting Breakpoints
1. **Add a breakpoint**: Click in the margin next to a line number where you want to pause execution.
2. **Conditional breakpoints**:
   - Right-click a breakpoint.
   - Add conditions like `x > 5` to pause only when the condition is met.

---
<style scoped>
section {
   font-size: 22px;
}
</style>

# Summary

### Key Takeaways
- Configure debugging for simple scripts, Django, and Flask applications.
- Utilize PyCharm’s debugging tools effectively:
  - Breakpoints
  - Attach to processes
  - Debug across different environments.
- Streamline Python debugging both locally and remotely.

---

# Questions?

Thank you!
