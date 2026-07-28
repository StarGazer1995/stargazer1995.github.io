---
created: 2025-04-27T06:09:00+00:00
categories:
  - Blog
updated: 2025-04-28T03:43:00+00:00
date: 2025-04-27T06:10:00+00:00
title: 如何从零开始构建简单的MCP
id: 1e2b3b02-81c4-807b-9333-e823c19c0124
---

[link_to_page](1d9b3b02-81c4-80a6-8258-d7032725746f)

# 简介

这是一篇介绍如何从零开始构建 MCP server 的简单说明。本说明由三部分组成：UV 介绍、代码开发和部署。

# UV 简介

[UV](https://docs.astral.sh/uv/)是一个基于 rust 的 Python 软件包和项目管理器。除了 UV 非常快之外，UV 与其他管理器没有什么区别。此外，MCP 使用 UVX（运行 python 包的 UV 工具）来运行服务器。因此，在本说明中，我们将使用 UV 来管理我们的项目。

## 安装

UV 现在可以使用 PyPi 进行安装：

```shell
pip install uv
```

### [optional] 更改源代码

由于特殊的网络环境，我们有时需要更改 UV 的源。需要在环境中添加下面的命令。

```shell
export UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple
```

此命令将 UV 的源从官方网站暂时改为 TUNA。可以参考[文档](https://mirror.tuna.tsinghua.edu.cn/help/pypi/)来彻底对源的使用路径进行彻底修改。

## Python 设置

为方便起见，我们使用 UV 设置 python 解释器。

```shell
uv python install
```

然后，我们使用下面的命令在一个目录中设置一个 Python 项目。

```shell
mkdir note # build a new directory for our code
uv init ./note # setup the direcory as our workspace
cd note # get into the workspace
uv venv # starts a new virtual environment
```

如果成功，UV 会生成一些新文件，如下图所示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7f0e8a0b-c4e1-4f01-9374-57601ba10ab2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KBB76XA%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T132653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDLgVZRB5z7pAgmiHi6hNzXu6kZE8XzR3afdXFyPKwiIAiEAmmMx2yrMH6fTx0VDdNwBfLWk%2FTLAcif3llr6pkZXhIoq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDKWqKOsKBdNBS021wyrcA6RqfUyRDWtOeDVTB3BEvt5uv6d9%2FPb2JWTzjPo26p%2F5ixU4BMz1OsGdbRD0nRBlrTCLediy5Q%2FjBUxaPy8uM610FRLXnvnvJ2q5zsp7mT5s1uRXDNRMu2NO4XN4Lastl8wip5FNYjtueiyIWjYAmaqUMnior2023OoUbbRGdF3hSR3Nc4%2F75XNlMXOHq68%2BO%2FVS1MdJWCO5K02nQ6UqsByhudY7m09E9qosYYQMQGjsaw57YZ5zJ%2BTMxquAbwVGYX7R4X8IyVc9sFrwd0sm2rGe0ug0QQ4lJmKJR%2Fcnt29agAe8hI2GtYSilZUQLikjzunAh%2B45jvqdbxb%2FUq4iOe0iQO%2Ff%2Be43fz8GsexQWE5QpnnkfJ8Y6FnDRDU4f9%2Fz%2BH21LoZT9H9UG0skycboUB78Nhv4L3HfdMHQfBkeWa8oKY3r5zCLVFIYL3IWQ1sb42lVlyv3eR6deBpS35fzQIBhXCfOZBZA3ULhcFvs5NY6lM6P%2BJpNySCpckcWEN%2Fn0W4o4OB5nBxtvR3JNf7B7PBCU0ikmfqvOyEvNCLPcqQPCPk7n259qVXPOggz0TSv6d3Y7suUzmW7afxtPYuwDzPux3rmadOld958ZNkKW%2BViM6AWg9OHwZ%2Flhtm3MJvVotMGOqUBhjjFLpwmG36ovOJSDaPSaQlGOOvDiwdDlFNypQbvdI8soGaZ%2BmiyBs3JfnVyFOu7u2S69t2XlMsQpbLM9nPyfjoRdZbRf1TQTQwilvy0X3KCNucKlYwAGyI2YiHPYEm6k7e6feEGem9Nd1%2FsyFdAy%2BYaWYzhjd8OB55%2Bs2mHi6PWAnV44U6H0bh%2B0eEPzb04QJQPD5pyMGY5MUnWTXNdnvsDEjvF&X-Amz-Signature=0fb733903a2fda4d44ea078aa4a2c6f68a0fc24346f573ef19a711e9ae685724&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 总结

我们已经安装了 UV，设置了解释器，并为我们的项目初始化了一个新的工作区。下一步，我们将完成项目，并实现一个非常简单的 MCP 服务器。

# 代码开发

在本节中，我们将开始实现一个非常简单的 MCP 服务器。首先，我们将浏览 workspace，安装一些项目以来，执行一些代码来验证 pipeline 是否通畅。

## 浏览工作区

我们可以在[这里](/1e2b3b0281c4807b9333e823c19c0124)看到我们的项目结构。工作区中有一些由 UV 生成的文件。不过不用担心。我们只需注意三个文件：main.py、README.md 和 pyproject.toml。

- [main.py](http://main.py/)文件是执行代码的地方。
- 在[README.md](http://readme.md/)文件中，你可能想写下一些关于代码的内容。
- pyproject.toml 是打包时管理项目的文件，稍后会介绍。

### 安装依赖项

在本项目中，我们主要使用 FastMCP 。有关该 python 软件包的信息，请[点击此处](https://github.com/jlowin/fastmcp)。简而言之，FastMCP 是使用 python 实现 MCP 服务器的一个简单但非常有用的工具。这里直接使用 uv 来进行安装。

```shell
uv pip install fastmcp
```

## 执行代码

安装好 FastMCP 后，我们就可以像下面这样执行代码了。

```python
from fastmcp import FastMCP  # Import the FastMCP class from the fastmcp module

# Create a FastMCP server instance with the name "note"
server = FastMCP("note")

# Register a tool/endpoint named "hello_world" using the @server.tool() decorator
@server.tool()
def hello_world():
    return "Hello World"  # The function returns "Hello World" when called

def main():
    server.run()

# Standard Python idiom to check if the script is being run directly
if __name__ == "__main__":
    main()  # Start the FastMCP server
```

## 如何运行代码

在终端中，我们可以使用 fastmcp 命令运行代码。

```python
# in our project directory
source .venv/bin/activate #activate the virtual environment we built
fastmcp dev main.py # run the code in development code
```

如果运行顺利，你会在终端中看到一些信息。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/1daf1736-35f7-48c2-9156-c98068ca2637/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KBB76XA%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T132653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDLgVZRB5z7pAgmiHi6hNzXu6kZE8XzR3afdXFyPKwiIAiEAmmMx2yrMH6fTx0VDdNwBfLWk%2FTLAcif3llr6pkZXhIoq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDKWqKOsKBdNBS021wyrcA6RqfUyRDWtOeDVTB3BEvt5uv6d9%2FPb2JWTzjPo26p%2F5ixU4BMz1OsGdbRD0nRBlrTCLediy5Q%2FjBUxaPy8uM610FRLXnvnvJ2q5zsp7mT5s1uRXDNRMu2NO4XN4Lastl8wip5FNYjtueiyIWjYAmaqUMnior2023OoUbbRGdF3hSR3Nc4%2F75XNlMXOHq68%2BO%2FVS1MdJWCO5K02nQ6UqsByhudY7m09E9qosYYQMQGjsaw57YZ5zJ%2BTMxquAbwVGYX7R4X8IyVc9sFrwd0sm2rGe0ug0QQ4lJmKJR%2Fcnt29agAe8hI2GtYSilZUQLikjzunAh%2B45jvqdbxb%2FUq4iOe0iQO%2Ff%2Be43fz8GsexQWE5QpnnkfJ8Y6FnDRDU4f9%2Fz%2BH21LoZT9H9UG0skycboUB78Nhv4L3HfdMHQfBkeWa8oKY3r5zCLVFIYL3IWQ1sb42lVlyv3eR6deBpS35fzQIBhXCfOZBZA3ULhcFvs5NY6lM6P%2BJpNySCpckcWEN%2Fn0W4o4OB5nBxtvR3JNf7B7PBCU0ikmfqvOyEvNCLPcqQPCPk7n259qVXPOggz0TSv6d3Y7suUzmW7afxtPYuwDzPux3rmadOld958ZNkKW%2BViM6AWg9OHwZ%2Flhtm3MJvVotMGOqUBhjjFLpwmG36ovOJSDaPSaQlGOOvDiwdDlFNypQbvdI8soGaZ%2BmiyBs3JfnVyFOu7u2S69t2XlMsQpbLM9nPyfjoRdZbRf1TQTQwilvy0X3KCNucKlYwAGyI2YiHPYEm6k7e6feEGem9Nd1%2FsyFdAy%2BYaWYzhjd8OB55%2Bs2mHi6PWAnV44U6H0bh%2B0eEPzb04QJQPD5pyMGY5MUnWTXNdnvsDEjvF&X-Amz-Signature=b14678fdc09069181582b397a0eb533aac64f77c0a77f8d05c93833d01c7ea7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这些信息告诉你，mcp inspector 正在 6274 端口运行，你可以通过它提供的 URL 链接访问。MCP inspector 是我们验证服务器是否起来的工具。我们不会花太多时间来介绍。

访问检查器服务器后，你会看到如下界面。点击左侧的连接按钮。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2ace1a7c-a49b-49f6-a297-fa126365c60a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KBB76XA%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T132653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDLgVZRB5z7pAgmiHi6hNzXu6kZE8XzR3afdXFyPKwiIAiEAmmMx2yrMH6fTx0VDdNwBfLWk%2FTLAcif3llr6pkZXhIoq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDKWqKOsKBdNBS021wyrcA6RqfUyRDWtOeDVTB3BEvt5uv6d9%2FPb2JWTzjPo26p%2F5ixU4BMz1OsGdbRD0nRBlrTCLediy5Q%2FjBUxaPy8uM610FRLXnvnvJ2q5zsp7mT5s1uRXDNRMu2NO4XN4Lastl8wip5FNYjtueiyIWjYAmaqUMnior2023OoUbbRGdF3hSR3Nc4%2F75XNlMXOHq68%2BO%2FVS1MdJWCO5K02nQ6UqsByhudY7m09E9qosYYQMQGjsaw57YZ5zJ%2BTMxquAbwVGYX7R4X8IyVc9sFrwd0sm2rGe0ug0QQ4lJmKJR%2Fcnt29agAe8hI2GtYSilZUQLikjzunAh%2B45jvqdbxb%2FUq4iOe0iQO%2Ff%2Be43fz8GsexQWE5QpnnkfJ8Y6FnDRDU4f9%2Fz%2BH21LoZT9H9UG0skycboUB78Nhv4L3HfdMHQfBkeWa8oKY3r5zCLVFIYL3IWQ1sb42lVlyv3eR6deBpS35fzQIBhXCfOZBZA3ULhcFvs5NY6lM6P%2BJpNySCpckcWEN%2Fn0W4o4OB5nBxtvR3JNf7B7PBCU0ikmfqvOyEvNCLPcqQPCPk7n259qVXPOggz0TSv6d3Y7suUzmW7afxtPYuwDzPux3rmadOld958ZNkKW%2BViM6AWg9OHwZ%2Flhtm3MJvVotMGOqUBhjjFLpwmG36ovOJSDaPSaQlGOOvDiwdDlFNypQbvdI8soGaZ%2BmiyBs3JfnVyFOu7u2S69t2XlMsQpbLM9nPyfjoRdZbRf1TQTQwilvy0X3KCNucKlYwAGyI2YiHPYEm6k7e6feEGem9Nd1%2FsyFdAy%2BYaWYzhjd8OB55%2Bs2mHi6PWAnV44U6H0bh%2B0eEPzb04QJQPD5pyMGY5MUnWTXNdnvsDEjvF&X-Amz-Signature=daca6089e58c8fadef5fa6d27a49b2fce2d9fc082223a17d8f34d35e0acc06ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

连接建立后，界面会变成这样。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/63247ba5-0aa1-47c6-bb5e-d878adca18c9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KBB76XA%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T132653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDLgVZRB5z7pAgmiHi6hNzXu6kZE8XzR3afdXFyPKwiIAiEAmmMx2yrMH6fTx0VDdNwBfLWk%2FTLAcif3llr6pkZXhIoq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDKWqKOsKBdNBS021wyrcA6RqfUyRDWtOeDVTB3BEvt5uv6d9%2FPb2JWTzjPo26p%2F5ixU4BMz1OsGdbRD0nRBlrTCLediy5Q%2FjBUxaPy8uM610FRLXnvnvJ2q5zsp7mT5s1uRXDNRMu2NO4XN4Lastl8wip5FNYjtueiyIWjYAmaqUMnior2023OoUbbRGdF3hSR3Nc4%2F75XNlMXOHq68%2BO%2FVS1MdJWCO5K02nQ6UqsByhudY7m09E9qosYYQMQGjsaw57YZ5zJ%2BTMxquAbwVGYX7R4X8IyVc9sFrwd0sm2rGe0ug0QQ4lJmKJR%2Fcnt29agAe8hI2GtYSilZUQLikjzunAh%2B45jvqdbxb%2FUq4iOe0iQO%2Ff%2Be43fz8GsexQWE5QpnnkfJ8Y6FnDRDU4f9%2Fz%2BH21LoZT9H9UG0skycboUB78Nhv4L3HfdMHQfBkeWa8oKY3r5zCLVFIYL3IWQ1sb42lVlyv3eR6deBpS35fzQIBhXCfOZBZA3ULhcFvs5NY6lM6P%2BJpNySCpckcWEN%2Fn0W4o4OB5nBxtvR3JNf7B7PBCU0ikmfqvOyEvNCLPcqQPCPk7n259qVXPOggz0TSv6d3Y7suUzmW7afxtPYuwDzPux3rmadOld958ZNkKW%2BViM6AWg9OHwZ%2Flhtm3MJvVotMGOqUBhjjFLpwmG36ovOJSDaPSaQlGOOvDiwdDlFNypQbvdI8soGaZ%2BmiyBs3JfnVyFOu7u2S69t2XlMsQpbLM9nPyfjoRdZbRf1TQTQwilvy0X3KCNucKlYwAGyI2YiHPYEm6k7e6feEGem9Nd1%2FsyFdAy%2BYaWYzhjd8OB55%2Bs2mHi6PWAnV44U6H0bh%2B0eEPzb04QJQPD5pyMGY5MUnWTXNdnvsDEjvF&X-Amz-Signature=69ccc50d71a2ca1708f2e185e696e8ba8a59f850a3855d6a19822ece14e5e036&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们首先点击 "工具 "按钮，然后选择 "列表工具"，检查我们所使用的工具。然后运行。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/dd91f8d0-b87a-419a-aec0-ceb20c207b9a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KBB76XA%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T132653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDLgVZRB5z7pAgmiHi6hNzXu6kZE8XzR3afdXFyPKwiIAiEAmmMx2yrMH6fTx0VDdNwBfLWk%2FTLAcif3llr6pkZXhIoq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDKWqKOsKBdNBS021wyrcA6RqfUyRDWtOeDVTB3BEvt5uv6d9%2FPb2JWTzjPo26p%2F5ixU4BMz1OsGdbRD0nRBlrTCLediy5Q%2FjBUxaPy8uM610FRLXnvnvJ2q5zsp7mT5s1uRXDNRMu2NO4XN4Lastl8wip5FNYjtueiyIWjYAmaqUMnior2023OoUbbRGdF3hSR3Nc4%2F75XNlMXOHq68%2BO%2FVS1MdJWCO5K02nQ6UqsByhudY7m09E9qosYYQMQGjsaw57YZ5zJ%2BTMxquAbwVGYX7R4X8IyVc9sFrwd0sm2rGe0ug0QQ4lJmKJR%2Fcnt29agAe8hI2GtYSilZUQLikjzunAh%2B45jvqdbxb%2FUq4iOe0iQO%2Ff%2Be43fz8GsexQWE5QpnnkfJ8Y6FnDRDU4f9%2Fz%2BH21LoZT9H9UG0skycboUB78Nhv4L3HfdMHQfBkeWa8oKY3r5zCLVFIYL3IWQ1sb42lVlyv3eR6deBpS35fzQIBhXCfOZBZA3ULhcFvs5NY6lM6P%2BJpNySCpckcWEN%2Fn0W4o4OB5nBxtvR3JNf7B7PBCU0ikmfqvOyEvNCLPcqQPCPk7n259qVXPOggz0TSv6d3Y7suUzmW7afxtPYuwDzPux3rmadOld958ZNkKW%2BViM6AWg9OHwZ%2Flhtm3MJvVotMGOqUBhjjFLpwmG36ovOJSDaPSaQlGOOvDiwdDlFNypQbvdI8soGaZ%2BmiyBs3JfnVyFOu7u2S69t2XlMsQpbLM9nPyfjoRdZbRf1TQTQwilvy0X3KCNucKlYwAGyI2YiHPYEm6k7e6feEGem9Nd1%2FsyFdAy%2BYaWYzhjd8OB55%2Bs2mHi6PWAnV44U6H0bh%2B0eEPzb04QJQPD5pyMGY5MUnWTXNdnvsDEjvF&X-Amz-Signature=5686ba69a016fe42ca8f2bba1afb123cb1cc0190e77097ac54772e8789f789e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果工具执行成功，就会看到如下界面的结果。那么你就成功运行了一个 mcp 工具。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/70e0fd59-96fd-4056-9142-dc77071a18bf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KBB76XA%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T132653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDLgVZRB5z7pAgmiHi6hNzXu6kZE8XzR3afdXFyPKwiIAiEAmmMx2yrMH6fTx0VDdNwBfLWk%2FTLAcif3llr6pkZXhIoq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDKWqKOsKBdNBS021wyrcA6RqfUyRDWtOeDVTB3BEvt5uv6d9%2FPb2JWTzjPo26p%2F5ixU4BMz1OsGdbRD0nRBlrTCLediy5Q%2FjBUxaPy8uM610FRLXnvnvJ2q5zsp7mT5s1uRXDNRMu2NO4XN4Lastl8wip5FNYjtueiyIWjYAmaqUMnior2023OoUbbRGdF3hSR3Nc4%2F75XNlMXOHq68%2BO%2FVS1MdJWCO5K02nQ6UqsByhudY7m09E9qosYYQMQGjsaw57YZ5zJ%2BTMxquAbwVGYX7R4X8IyVc9sFrwd0sm2rGe0ug0QQ4lJmKJR%2Fcnt29agAe8hI2GtYSilZUQLikjzunAh%2B45jvqdbxb%2FUq4iOe0iQO%2Ff%2Be43fz8GsexQWE5QpnnkfJ8Y6FnDRDU4f9%2Fz%2BH21LoZT9H9UG0skycboUB78Nhv4L3HfdMHQfBkeWa8oKY3r5zCLVFIYL3IWQ1sb42lVlyv3eR6deBpS35fzQIBhXCfOZBZA3ULhcFvs5NY6lM6P%2BJpNySCpckcWEN%2Fn0W4o4OB5nBxtvR3JNf7B7PBCU0ikmfqvOyEvNCLPcqQPCPk7n259qVXPOggz0TSv6d3Y7suUzmW7afxtPYuwDzPux3rmadOld958ZNkKW%2BViM6AWg9OHwZ%2Flhtm3MJvVotMGOqUBhjjFLpwmG36ovOJSDaPSaQlGOOvDiwdDlFNypQbvdI8soGaZ%2BmiyBs3JfnVyFOu7u2S69t2XlMsQpbLM9nPyfjoRdZbRf1TQTQwilvy0X3KCNucKlYwAGyI2YiHPYEm6k7e6feEGem9Nd1%2FsyFdAy%2BYaWYzhjd8OB55%2Bs2mHi6PWAnV44U6H0bh%2B0eEPzb04QJQPD5pyMGY5MUnWTXNdnvsDEjvF&X-Amz-Signature=4d782d13f5cb1f217f9c86a810f29245362d20066c3ede9f3701eae98adcb77d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 调试代码

我个人建议使用 UT、AT 或回归测试等各种测试在本地测试代码。因为这样更方便我们使用。MCP inspector 提供的工具不太好用。

## 一些建议

1. 给函数写一些详细的注释，这样 llm 方便理解这个函数是什么「可以用 LLM 来生成」。
2. 在输入跟输出中添加所期望的类型信息，可以避免一些因为输入类型带来的错误。

# 软件包部署

在本节中，我们可以部署 mcp 服务器供 LLM 使用。我们需要更新之前提到的 pyproject.toml 以打包我们的代码。

## 更新可执行信息

在我们的项目中，在 pyproject.toml 中添加以下几行：

```python
[project.scripts]
note = "main:main"  # Executes the `main()` function in `main.py`
```

## 添加依赖项信息

我们还需要为软件包添加依赖项，可以使用以下命令将我们使用的软件包添加到 pyproject.toml 中

```shell
uv add fastmcp
```

当然，如果我们有很多软件包需要依赖，这看起来会很不舒服。我们也可以使用其他工具来实现这一点。

## 部署代码

我们使用以下命令打包代码并运行。

```shell
uv build --wheel # packaging your code into wheel
uv install ${PATHTOYOURPACKAGE} # install the packaged code
uvx --python=$(which python) ${PACKAGE} # run the package using specific python interpreter
```

如果一切顺利，你会在 CLI 中看到以下信息。它会告诉你 MCP 服务器正在运行。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/129cc91e-3fce-4702-9189-a7d04991a5d4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KBB76XA%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T132653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDLgVZRB5z7pAgmiHi6hNzXu6kZE8XzR3afdXFyPKwiIAiEAmmMx2yrMH6fTx0VDdNwBfLWk%2FTLAcif3llr6pkZXhIoq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDKWqKOsKBdNBS021wyrcA6RqfUyRDWtOeDVTB3BEvt5uv6d9%2FPb2JWTzjPo26p%2F5ixU4BMz1OsGdbRD0nRBlrTCLediy5Q%2FjBUxaPy8uM610FRLXnvnvJ2q5zsp7mT5s1uRXDNRMu2NO4XN4Lastl8wip5FNYjtueiyIWjYAmaqUMnior2023OoUbbRGdF3hSR3Nc4%2F75XNlMXOHq68%2BO%2FVS1MdJWCO5K02nQ6UqsByhudY7m09E9qosYYQMQGjsaw57YZ5zJ%2BTMxquAbwVGYX7R4X8IyVc9sFrwd0sm2rGe0ug0QQ4lJmKJR%2Fcnt29agAe8hI2GtYSilZUQLikjzunAh%2B45jvqdbxb%2FUq4iOe0iQO%2Ff%2Be43fz8GsexQWE5QpnnkfJ8Y6FnDRDU4f9%2Fz%2BH21LoZT9H9UG0skycboUB78Nhv4L3HfdMHQfBkeWa8oKY3r5zCLVFIYL3IWQ1sb42lVlyv3eR6deBpS35fzQIBhXCfOZBZA3ULhcFvs5NY6lM6P%2BJpNySCpckcWEN%2Fn0W4o4OB5nBxtvR3JNf7B7PBCU0ikmfqvOyEvNCLPcqQPCPk7n259qVXPOggz0TSv6d3Y7suUzmW7afxtPYuwDzPux3rmadOld958ZNkKW%2BViM6AWg9OHwZ%2Flhtm3MJvVotMGOqUBhjjFLpwmG36ovOJSDaPSaQlGOOvDiwdDlFNypQbvdI8soGaZ%2BmiyBs3JfnVyFOu7u2S69t2XlMsQpbLM9nPyfjoRdZbRf1TQTQwilvy0X3KCNucKlYwAGyI2YiHPYEm6k7e6feEGem9Nd1%2FsyFdAy%2BYaWYzhjd8OB55%2Bs2mHi6PWAnV44U6H0bh%2B0eEPzb04QJQPD5pyMGY5MUnWTXNdnvsDEjvF&X-Amz-Signature=da6e5d98724174cdb18593a971511202b78404e5e63270903ed6256c374690a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
