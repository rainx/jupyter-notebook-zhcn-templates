# jupyter-notebook-zhcn-templates

Jupyter Notebook的中文汉化模板

## 使用

### 注意

只针对特定版本,当前的翻译模板针对jupyter notebook 4.2.3

### 安装

```bash

> pip3 install git+https://github.com/rainx/jupyter-notebook-zhcn-templates.git

或者

> git clone https://github.com/rainx/jupyter-notebook-zhcn-templates.git
> python setup.py install

```
### 配置

修改 ```jupyter_notebook_config.py```

```python
import notebookcn
c.NotebookApp.extra_static_paths = [notebookcn.static_path]
c.NotebookApp.extra_template_paths = [notebookcn.templates_path]
```

