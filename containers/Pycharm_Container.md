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

# Debugging Containers in PyCharm.

---

### Adding remote interpreter.

1. Select add new interpreter on the bottom right bar.
2. Select On Docker and then select your docker file and context folder.
3. If required you can provide additional options like tag and other variables.
4. On clicking next, this would create a docker container and inspect it.

![add new interpreter](./images/add_interpreter.png)





---

### Adding Debugging Configuration

1. Select remote interpreter setup in previous step.
2. Select `Edit Configurations` on Debug Tab and Add a new configuration.
3. Select approriate module or requirements ( FastAPI, Flask, Django, Script ).
4. Since remote interpreter is selected, it will automatically add Docker configuration to debugging configuration.
5. Save and click on debug.
6. PyCharm will start a new docker container and attach debugger to it. (Pycharm uses Pydevd)

![debugger](./images/image.png)

---

# Questions?

Thank you!
