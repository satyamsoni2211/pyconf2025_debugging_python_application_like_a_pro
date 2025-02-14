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

### Adding a Remote Interpreter

1. Select "Add New Interpreter" on the bottom right bar.
2. Choose "On Docker" and then select your Docker file and context folder.
3. If required, provide additional options like tags and other variables.
4. Click "Next" to create and inspect a Docker container.

![add new interpreter](./images/add_interpreter.png)

---

### Adding Debugging Configuration

1. Use the remote interpreter setup from the previous step.
2. Select "Edit Configurations" on the Debug tab and add a new configuration.
3. Choose the appropriate module or requirements (FastAPI, Flask, Django, Script).
4. The Docker configuration will automatically be added to the debugging configuration.
5. Save and click "Debug."
6. PyCharm will start a new Docker container and attach the debugger to it (PyCharm uses Pydevd).

![debugger](./images/image.png)

---

# Questions?

Thank you!