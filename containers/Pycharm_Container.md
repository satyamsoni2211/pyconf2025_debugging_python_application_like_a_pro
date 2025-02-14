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

# Debugging Containers in PyCharm

---
<style scoped>
section {
   font-size: 22px;
}
</style>

### Adding a Remote Interpreter

1. **Open Interpreter Settings**: Click on "Add New Interpreter" located on the bottom right bar of PyCharm.
2. **Select Docker**: Choose "On Docker" from the options.
3. **Configure Docker**: Select your Docker file and context folder.
   - If required, provide additional options like tags and other variables.
4. **Finalize Setup**: Click "Next" to create and inspect a Docker container.

![add new interpreter](./images/add_interpreter.png)

---

<style scoped>
section {
   font-size: 22px;
}
</style>

### Adding Debugging Configuration

1. **Use Remote Interpreter**: Ensure you have set up the remote interpreter from the previous step.
2. **Edit Configurations**: Go to the Debug tab and select "Edit Configurations."
3. **Add New Configuration**: Click to add a new configuration and Choose the appropriate module or requirements (e.g., FastAPI, Flask, Django, Script).
4. **Docker Configuration**: The Docker configuration will automatically be added to the debugging configuration.
5. **Save and Debug**: Save the configuration and click "Debug". PyCharm will start a new Docker container and attach the debugger to it (PyCharm uses Pydevd).

![debugger](./images/image.png)

---

# Questions?

Thank you!
