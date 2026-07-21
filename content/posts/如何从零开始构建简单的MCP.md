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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7f0e8a0b-c4e1-4f01-9374-57601ba10ab2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN6Y7NNL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T080519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAI8dP0SSmYLFDG%2BwNnmDh3vuGtXxWAFbSvtLcUn4q1IAiEAwaWya8X4wkfuPcAGJ27QAv7nSGtfv4DmTQ1HGcdZrvcqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FxtwtswV8qUJVOESrcAyBTFFABxZ%2F4fVH7qYW7eeIig2Tdjk3HVgEjvr9fNOyjAO7r%2BqtIwuKIQbJdi%2BSti8REehqE5B5lmMUSmPE7pmMXTtrxiPYS10dkmpNffBFMHS%2B4kwKKpmItPB%2F%2BRnecxoJSxwgWQ%2FiO9%2BOBZchUa5dIGiGX1H1AoapvWYDVhUHXaNegpGQq6M%2FX26X5Gp6uiCuinDk6xb%2BCROMUPDknuVM90rl7RiQ5wrncAO7YhK48WP7etTctT7B%2FZi%2BmVTLZNE5SmjQN7k7YMma0qH1bGan%2FNSV4UKGixhCb6qLd29qAm4hk5VugOiW2bTqhHSstRE9kkN9zhI5J5ub%2BTNTLn6jJIJVk1tp69jrIreKnxDzxYpyrocCYM1s9Uy6NWF85sgFA8fHsV3BRz9x6G9aS6OIF5wVp0XUtfiHbId%2BJp2GTMzkkaLxJimbjtHySCY6Hnx3W%2FEBlTw8kso0nwdfMA8gOMrqHN1%2BvKQQv64d7WOfZTkYgUmK38Hwen4JJa1f5vpQdrh1rDilKc%2F3Ry1duFXlYmo%2BIqCC5D5sYjCW83mu8HysddPVNIeyXTFPpsXiZSn3RMuzqFn1rzKzxdsW0PLRAsyHRLJzy5%2FxPqO5ZVdR44Y%2BKQpyi%2FdBSq4FvMI%2Bo%2FNIGOqUByrc64z9VP0vT7f40vrH7Po3hgB0Dol93EQwNzkBfUJ9GCsuRl%2FfRYRPXpZnm7OxzgiTN7Il5EubcAB5MZG81UwdHb%2FuTRQkg1oKEL0d0hmcSrrTPL3pKAUKaZUoTVhPz%2FamC1bNDDvR8eY%2FCAHAvpCjD4ddZDAGJJGBLDxDztRROL51KSchERNcOMketcvNIYN4HKHZCfkX3BCsrJn%2F0thO8U4mm&X-Amz-Signature=8f5dd132d1fdbd5086cbdba54007b613ff09663db5cb0be970f9321aae88feb9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/1daf1736-35f7-48c2-9156-c98068ca2637/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN6Y7NNL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T080519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAI8dP0SSmYLFDG%2BwNnmDh3vuGtXxWAFbSvtLcUn4q1IAiEAwaWya8X4wkfuPcAGJ27QAv7nSGtfv4DmTQ1HGcdZrvcqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FxtwtswV8qUJVOESrcAyBTFFABxZ%2F4fVH7qYW7eeIig2Tdjk3HVgEjvr9fNOyjAO7r%2BqtIwuKIQbJdi%2BSti8REehqE5B5lmMUSmPE7pmMXTtrxiPYS10dkmpNffBFMHS%2B4kwKKpmItPB%2F%2BRnecxoJSxwgWQ%2FiO9%2BOBZchUa5dIGiGX1H1AoapvWYDVhUHXaNegpGQq6M%2FX26X5Gp6uiCuinDk6xb%2BCROMUPDknuVM90rl7RiQ5wrncAO7YhK48WP7etTctT7B%2FZi%2BmVTLZNE5SmjQN7k7YMma0qH1bGan%2FNSV4UKGixhCb6qLd29qAm4hk5VugOiW2bTqhHSstRE9kkN9zhI5J5ub%2BTNTLn6jJIJVk1tp69jrIreKnxDzxYpyrocCYM1s9Uy6NWF85sgFA8fHsV3BRz9x6G9aS6OIF5wVp0XUtfiHbId%2BJp2GTMzkkaLxJimbjtHySCY6Hnx3W%2FEBlTw8kso0nwdfMA8gOMrqHN1%2BvKQQv64d7WOfZTkYgUmK38Hwen4JJa1f5vpQdrh1rDilKc%2F3Ry1duFXlYmo%2BIqCC5D5sYjCW83mu8HysddPVNIeyXTFPpsXiZSn3RMuzqFn1rzKzxdsW0PLRAsyHRLJzy5%2FxPqO5ZVdR44Y%2BKQpyi%2FdBSq4FvMI%2Bo%2FNIGOqUByrc64z9VP0vT7f40vrH7Po3hgB0Dol93EQwNzkBfUJ9GCsuRl%2FfRYRPXpZnm7OxzgiTN7Il5EubcAB5MZG81UwdHb%2FuTRQkg1oKEL0d0hmcSrrTPL3pKAUKaZUoTVhPz%2FamC1bNDDvR8eY%2FCAHAvpCjD4ddZDAGJJGBLDxDztRROL51KSchERNcOMketcvNIYN4HKHZCfkX3BCsrJn%2F0thO8U4mm&X-Amz-Signature=f4c795ad6da885b5b86f9338f574ef1c367bb05732dbf9a9c2bd1f6a87eb5f62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这些信息告诉你，mcp inspector 正在 6274 端口运行，你可以通过它提供的 URL 链接访问。MCP inspector 是我们验证服务器是否起来的工具。我们不会花太多时间来介绍。

访问检查器服务器后，你会看到如下界面。点击左侧的连接按钮。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2ace1a7c-a49b-49f6-a297-fa126365c60a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN6Y7NNL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T080519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAI8dP0SSmYLFDG%2BwNnmDh3vuGtXxWAFbSvtLcUn4q1IAiEAwaWya8X4wkfuPcAGJ27QAv7nSGtfv4DmTQ1HGcdZrvcqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FxtwtswV8qUJVOESrcAyBTFFABxZ%2F4fVH7qYW7eeIig2Tdjk3HVgEjvr9fNOyjAO7r%2BqtIwuKIQbJdi%2BSti8REehqE5B5lmMUSmPE7pmMXTtrxiPYS10dkmpNffBFMHS%2B4kwKKpmItPB%2F%2BRnecxoJSxwgWQ%2FiO9%2BOBZchUa5dIGiGX1H1AoapvWYDVhUHXaNegpGQq6M%2FX26X5Gp6uiCuinDk6xb%2BCROMUPDknuVM90rl7RiQ5wrncAO7YhK48WP7etTctT7B%2FZi%2BmVTLZNE5SmjQN7k7YMma0qH1bGan%2FNSV4UKGixhCb6qLd29qAm4hk5VugOiW2bTqhHSstRE9kkN9zhI5J5ub%2BTNTLn6jJIJVk1tp69jrIreKnxDzxYpyrocCYM1s9Uy6NWF85sgFA8fHsV3BRz9x6G9aS6OIF5wVp0XUtfiHbId%2BJp2GTMzkkaLxJimbjtHySCY6Hnx3W%2FEBlTw8kso0nwdfMA8gOMrqHN1%2BvKQQv64d7WOfZTkYgUmK38Hwen4JJa1f5vpQdrh1rDilKc%2F3Ry1duFXlYmo%2BIqCC5D5sYjCW83mu8HysddPVNIeyXTFPpsXiZSn3RMuzqFn1rzKzxdsW0PLRAsyHRLJzy5%2FxPqO5ZVdR44Y%2BKQpyi%2FdBSq4FvMI%2Bo%2FNIGOqUByrc64z9VP0vT7f40vrH7Po3hgB0Dol93EQwNzkBfUJ9GCsuRl%2FfRYRPXpZnm7OxzgiTN7Il5EubcAB5MZG81UwdHb%2FuTRQkg1oKEL0d0hmcSrrTPL3pKAUKaZUoTVhPz%2FamC1bNDDvR8eY%2FCAHAvpCjD4ddZDAGJJGBLDxDztRROL51KSchERNcOMketcvNIYN4HKHZCfkX3BCsrJn%2F0thO8U4mm&X-Amz-Signature=84873b61ee8e746bf0b17ce4ad770026e792c6e81fe3b794afe7a5229c9f2661&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

连接建立后，界面会变成这样。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/63247ba5-0aa1-47c6-bb5e-d878adca18c9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN6Y7NNL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T080519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAI8dP0SSmYLFDG%2BwNnmDh3vuGtXxWAFbSvtLcUn4q1IAiEAwaWya8X4wkfuPcAGJ27QAv7nSGtfv4DmTQ1HGcdZrvcqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FxtwtswV8qUJVOESrcAyBTFFABxZ%2F4fVH7qYW7eeIig2Tdjk3HVgEjvr9fNOyjAO7r%2BqtIwuKIQbJdi%2BSti8REehqE5B5lmMUSmPE7pmMXTtrxiPYS10dkmpNffBFMHS%2B4kwKKpmItPB%2F%2BRnecxoJSxwgWQ%2FiO9%2BOBZchUa5dIGiGX1H1AoapvWYDVhUHXaNegpGQq6M%2FX26X5Gp6uiCuinDk6xb%2BCROMUPDknuVM90rl7RiQ5wrncAO7YhK48WP7etTctT7B%2FZi%2BmVTLZNE5SmjQN7k7YMma0qH1bGan%2FNSV4UKGixhCb6qLd29qAm4hk5VugOiW2bTqhHSstRE9kkN9zhI5J5ub%2BTNTLn6jJIJVk1tp69jrIreKnxDzxYpyrocCYM1s9Uy6NWF85sgFA8fHsV3BRz9x6G9aS6OIF5wVp0XUtfiHbId%2BJp2GTMzkkaLxJimbjtHySCY6Hnx3W%2FEBlTw8kso0nwdfMA8gOMrqHN1%2BvKQQv64d7WOfZTkYgUmK38Hwen4JJa1f5vpQdrh1rDilKc%2F3Ry1duFXlYmo%2BIqCC5D5sYjCW83mu8HysddPVNIeyXTFPpsXiZSn3RMuzqFn1rzKzxdsW0PLRAsyHRLJzy5%2FxPqO5ZVdR44Y%2BKQpyi%2FdBSq4FvMI%2Bo%2FNIGOqUByrc64z9VP0vT7f40vrH7Po3hgB0Dol93EQwNzkBfUJ9GCsuRl%2FfRYRPXpZnm7OxzgiTN7Il5EubcAB5MZG81UwdHb%2FuTRQkg1oKEL0d0hmcSrrTPL3pKAUKaZUoTVhPz%2FamC1bNDDvR8eY%2FCAHAvpCjD4ddZDAGJJGBLDxDztRROL51KSchERNcOMketcvNIYN4HKHZCfkX3BCsrJn%2F0thO8U4mm&X-Amz-Signature=23a6403e41005104fbb6358d5b75230aeb323dd32b96c37b5fc62399455b7a04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们首先点击 "工具 "按钮，然后选择 "列表工具"，检查我们所使用的工具。然后运行。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/dd91f8d0-b87a-419a-aec0-ceb20c207b9a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN6Y7NNL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T080519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAI8dP0SSmYLFDG%2BwNnmDh3vuGtXxWAFbSvtLcUn4q1IAiEAwaWya8X4wkfuPcAGJ27QAv7nSGtfv4DmTQ1HGcdZrvcqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FxtwtswV8qUJVOESrcAyBTFFABxZ%2F4fVH7qYW7eeIig2Tdjk3HVgEjvr9fNOyjAO7r%2BqtIwuKIQbJdi%2BSti8REehqE5B5lmMUSmPE7pmMXTtrxiPYS10dkmpNffBFMHS%2B4kwKKpmItPB%2F%2BRnecxoJSxwgWQ%2FiO9%2BOBZchUa5dIGiGX1H1AoapvWYDVhUHXaNegpGQq6M%2FX26X5Gp6uiCuinDk6xb%2BCROMUPDknuVM90rl7RiQ5wrncAO7YhK48WP7etTctT7B%2FZi%2BmVTLZNE5SmjQN7k7YMma0qH1bGan%2FNSV4UKGixhCb6qLd29qAm4hk5VugOiW2bTqhHSstRE9kkN9zhI5J5ub%2BTNTLn6jJIJVk1tp69jrIreKnxDzxYpyrocCYM1s9Uy6NWF85sgFA8fHsV3BRz9x6G9aS6OIF5wVp0XUtfiHbId%2BJp2GTMzkkaLxJimbjtHySCY6Hnx3W%2FEBlTw8kso0nwdfMA8gOMrqHN1%2BvKQQv64d7WOfZTkYgUmK38Hwen4JJa1f5vpQdrh1rDilKc%2F3Ry1duFXlYmo%2BIqCC5D5sYjCW83mu8HysddPVNIeyXTFPpsXiZSn3RMuzqFn1rzKzxdsW0PLRAsyHRLJzy5%2FxPqO5ZVdR44Y%2BKQpyi%2FdBSq4FvMI%2Bo%2FNIGOqUByrc64z9VP0vT7f40vrH7Po3hgB0Dol93EQwNzkBfUJ9GCsuRl%2FfRYRPXpZnm7OxzgiTN7Il5EubcAB5MZG81UwdHb%2FuTRQkg1oKEL0d0hmcSrrTPL3pKAUKaZUoTVhPz%2FamC1bNDDvR8eY%2FCAHAvpCjD4ddZDAGJJGBLDxDztRROL51KSchERNcOMketcvNIYN4HKHZCfkX3BCsrJn%2F0thO8U4mm&X-Amz-Signature=2f6f986ee940e775f7672434c27015659f2246771ae7921322a723c164a210c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果工具执行成功，就会看到如下界面的结果。那么你就成功运行了一个 mcp 工具。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/70e0fd59-96fd-4056-9142-dc77071a18bf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN6Y7NNL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T080519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAI8dP0SSmYLFDG%2BwNnmDh3vuGtXxWAFbSvtLcUn4q1IAiEAwaWya8X4wkfuPcAGJ27QAv7nSGtfv4DmTQ1HGcdZrvcqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FxtwtswV8qUJVOESrcAyBTFFABxZ%2F4fVH7qYW7eeIig2Tdjk3HVgEjvr9fNOyjAO7r%2BqtIwuKIQbJdi%2BSti8REehqE5B5lmMUSmPE7pmMXTtrxiPYS10dkmpNffBFMHS%2B4kwKKpmItPB%2F%2BRnecxoJSxwgWQ%2FiO9%2BOBZchUa5dIGiGX1H1AoapvWYDVhUHXaNegpGQq6M%2FX26X5Gp6uiCuinDk6xb%2BCROMUPDknuVM90rl7RiQ5wrncAO7YhK48WP7etTctT7B%2FZi%2BmVTLZNE5SmjQN7k7YMma0qH1bGan%2FNSV4UKGixhCb6qLd29qAm4hk5VugOiW2bTqhHSstRE9kkN9zhI5J5ub%2BTNTLn6jJIJVk1tp69jrIreKnxDzxYpyrocCYM1s9Uy6NWF85sgFA8fHsV3BRz9x6G9aS6OIF5wVp0XUtfiHbId%2BJp2GTMzkkaLxJimbjtHySCY6Hnx3W%2FEBlTw8kso0nwdfMA8gOMrqHN1%2BvKQQv64d7WOfZTkYgUmK38Hwen4JJa1f5vpQdrh1rDilKc%2F3Ry1duFXlYmo%2BIqCC5D5sYjCW83mu8HysddPVNIeyXTFPpsXiZSn3RMuzqFn1rzKzxdsW0PLRAsyHRLJzy5%2FxPqO5ZVdR44Y%2BKQpyi%2FdBSq4FvMI%2Bo%2FNIGOqUByrc64z9VP0vT7f40vrH7Po3hgB0Dol93EQwNzkBfUJ9GCsuRl%2FfRYRPXpZnm7OxzgiTN7Il5EubcAB5MZG81UwdHb%2FuTRQkg1oKEL0d0hmcSrrTPL3pKAUKaZUoTVhPz%2FamC1bNDDvR8eY%2FCAHAvpCjD4ddZDAGJJGBLDxDztRROL51KSchERNcOMketcvNIYN4HKHZCfkX3BCsrJn%2F0thO8U4mm&X-Amz-Signature=81376933bb8a6197b73f4ff63010367852a3a82a37b8abee55204b2ae57a7e04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/129cc91e-3fce-4702-9189-a7d04991a5d4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN6Y7NNL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T080519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAI8dP0SSmYLFDG%2BwNnmDh3vuGtXxWAFbSvtLcUn4q1IAiEAwaWya8X4wkfuPcAGJ27QAv7nSGtfv4DmTQ1HGcdZrvcqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FxtwtswV8qUJVOESrcAyBTFFABxZ%2F4fVH7qYW7eeIig2Tdjk3HVgEjvr9fNOyjAO7r%2BqtIwuKIQbJdi%2BSti8REehqE5B5lmMUSmPE7pmMXTtrxiPYS10dkmpNffBFMHS%2B4kwKKpmItPB%2F%2BRnecxoJSxwgWQ%2FiO9%2BOBZchUa5dIGiGX1H1AoapvWYDVhUHXaNegpGQq6M%2FX26X5Gp6uiCuinDk6xb%2BCROMUPDknuVM90rl7RiQ5wrncAO7YhK48WP7etTctT7B%2FZi%2BmVTLZNE5SmjQN7k7YMma0qH1bGan%2FNSV4UKGixhCb6qLd29qAm4hk5VugOiW2bTqhHSstRE9kkN9zhI5J5ub%2BTNTLn6jJIJVk1tp69jrIreKnxDzxYpyrocCYM1s9Uy6NWF85sgFA8fHsV3BRz9x6G9aS6OIF5wVp0XUtfiHbId%2BJp2GTMzkkaLxJimbjtHySCY6Hnx3W%2FEBlTw8kso0nwdfMA8gOMrqHN1%2BvKQQv64d7WOfZTkYgUmK38Hwen4JJa1f5vpQdrh1rDilKc%2F3Ry1duFXlYmo%2BIqCC5D5sYjCW83mu8HysddPVNIeyXTFPpsXiZSn3RMuzqFn1rzKzxdsW0PLRAsyHRLJzy5%2FxPqO5ZVdR44Y%2BKQpyi%2FdBSq4FvMI%2Bo%2FNIGOqUByrc64z9VP0vT7f40vrH7Po3hgB0Dol93EQwNzkBfUJ9GCsuRl%2FfRYRPXpZnm7OxzgiTN7Il5EubcAB5MZG81UwdHb%2FuTRQkg1oKEL0d0hmcSrrTPL3pKAUKaZUoTVhPz%2FamC1bNDDvR8eY%2FCAHAvpCjD4ddZDAGJJGBLDxDztRROL51KSchERNcOMketcvNIYN4HKHZCfkX3BCsrJn%2F0thO8U4mm&X-Amz-Signature=0d2f46c21f1109a948b31839dfcd63f0d7a1984995b5f263cda4db2dd40daa9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
