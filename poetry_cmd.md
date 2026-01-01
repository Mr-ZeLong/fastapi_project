# Poetry 命令
1. 初始化项目
   ```bash
   poetry init
   ```
   
2. 创建虚拟环境
   ```bash
   poetry env use python3
   ```

3. 激活环境
The poetry env activate command prints the activate command of the virtual environment to the console.
You can run the output command manually or feed it to the eval command of your shell to activate the environment. 
This way you won’t leave the current shell.
   ```bash
   eval $(poetry env activate)
   ```


4. 在当前环境种添加依赖
   ```bash
   poetry add fastapi
   ```



# 参考文档
https://python-poetry.org/docs/basic-usage/