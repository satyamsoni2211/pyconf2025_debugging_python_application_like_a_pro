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
- Configure debugging for various project types.
- Utilize PyCharm’s debugging interface effectively.
- Debug Python applications in diverse environments.

Reference Document: [Python Debugging in PyCharm](https://www.jetbrains.com/pycharm/features/debugger.html)

---

# Configuring Debugging

### Simple Scripts
1. Open your project in PyCharm.
2. Select your interpreter (PyCharm automatically detects it).
3. Open your script, go to run/debug configurations, and select `current file`.
4. Click on the debugger logo.

![w:600 h:200 right](https://www.jetbrains.com/pycharm/features/screenshots/debugger.png)

---

### Creating Launch Configurations

1. Go to the debugger toolbar and in the dropdown select `Edit Configurations`.
2. Choose the type of configuration you would like to select.
3. Fill in the required details and save.
4. Click on the debugger logo to start debugging.

![image](./images/image.png)

---

### FastAPI, Django, or Flask Applications

1. Select the Python interpreter for your project (Virtual Environment).
2. Ensure your app’s dependencies are installed.
3. Select the appropriate debugging configuration.
4. Click on the debugger logo to start debugging.

---

# PyCharm’s Debugging Interface

### Key Features
- **Breakpoints**: Pause execution at specific lines.
- **Variables**: Inspect variable states dynamically.
- **Call Stack**: Navigate the order of function calls.
- **Watch**: Monitor expressions in real-time.
- **Debug Console**: Execute commands during debugging.

---

### Setting Breakpoints
1. Click in the margin next to a line number.
2. Conditional breakpoints:
   - Right-click a breakpoint.
   - Add conditions like `x > 5`.

---

# Summary

### Key Takeaways
- Configure debugging for simple scripts, Django, and Flask.
- Utilize PyCharm’s debugging tools:
  - Breakpoints
  - Attach to processes
  - Debug across environments.
- Streamline Python debugging locally and remotely.

---

# Questions?

Thank you!