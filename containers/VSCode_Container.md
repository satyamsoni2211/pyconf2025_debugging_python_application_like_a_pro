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

# Container Debugging in Visual Studio Code



### Remote Debugging ( manual )

1. Install **ptvsd** or **debugpy** for remote access.
2. Configure the target application to accept debugger connections.
3. Attach to the remote debugger in VS Code.

---

### Remote Debugging witth configurations.

1. Go to settings and select `Docker: Initialize for Debugging`.
2. Select the type of module you want to debug and fill in the details.
3. This will add Docker build and run tasks and create a launch configuration.
4. Click on debug and start debugging your container.

![debug](./images/vscode_settings.png)


---

# Summary

### Key Takeaways
- Configure debugging for simple scripts, Django, and Flask.
- Utilize VS Code’s debugging tools:
  - Breakpoints
  - Attach to processes
  - Debug across environments.
- Streamline Python debugging locally and remotely.

---

# Questions?

Thank you!
