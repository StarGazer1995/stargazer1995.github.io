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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7f0e8a0b-c4e1-4f01-9374-57601ba10ab2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NK2A5OY%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T080833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJIMEYCIQC6Q8knv%2FuxdKU1jIcodZ4d9F4JvpCjPhgimhoGSj1J%2FQIhALOrT3Vto5C0ea3dxVLNALVaaxviF0Hyq%2B6k%2F1d0oEtrKogECOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVa%2BES0kZ2yL%2BY%2BDkq3AMVTLNwnWUvLq4pf6GiGKOYRqM6jw2ZHh4bF0JvnNSAnkD28EVuKAlkDENZu9H2A4mIuliEEOUQDTmFT8NzoO49Vd9Y7Nzk%2BzWIQ7pbh%2B%2Bf1%2B5ak5BnbTmuK980qai02wz9z7Cbr5K6ZWhWCwcRjuGVfQn%2FB59EVV7aop9QlF8fR4M2anItappuLmuu%2BoJomlxqfjxvbbVE%2FnSOWbPFTYrG%2FmF1%2FXdgzJZ%2BBa5ourOSYDQfiQ%2Fa394rKK5LVCFlsRlq8AQK7YFL9tZbdeipaYNl5llEZGRL8umHjGDDEw6oCxWCaUgIeb9I9nZ7AmE6ZYu1cJnpFLNJixdLVEC03NCQ68%2FjLfcAKWlJHPuXXFJZB4xsJAi8jwz2TvRvPuhSyN21OzG4wEFND8a8SUhEQu07iPuRhtRMGsun5bQ8zMR%2FvsStoMduNTw9hUMnxWn574SgU36caEGe%2FlWjd0%2F9AcNi7UK5rh6CIZWye%2F%2Bw48BKwVMV9PC6NUQ3BvrdhdecLKf9O2zaPO1dsj4%2BboWV1vMMX%2FAKvR7nOqgiy1p%2F627DPsMCy2PPTsqqSES9YW%2BniJgpR6u6zPh115UW9DiUSJC2D5acyjSei4vyPPdsgSRZopEwSmOnJijZGGkcpTCr7IbTBjqkAYH1e5lspZf%2F2YB%2B69RbtTzAYrq65KycBMtxpISIxJpOXgpqtKk06AnmVTjncdmhdiWoT5uAqyt8BNC6aijaUDu%2BScCipxGfyBFBAdzAfWmtJAFmqACk%2Fy8b8nFG4ukEib31%2FB%2BPhF4VP16ZVftxjkv%2BKf06o0MJbxekgX6jca1uI8QS0SZa9LU8WI7H%2Bi0WySxuQAh21dRt9yiMlXlNbzZoBA4i&X-Amz-Signature=a65688cc9dd9b3dc8af76018272285cff06b1765569c4fb827a0bc15a3d71dd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/1daf1736-35f7-48c2-9156-c98068ca2637/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NK2A5OY%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T080833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJIMEYCIQC6Q8knv%2FuxdKU1jIcodZ4d9F4JvpCjPhgimhoGSj1J%2FQIhALOrT3Vto5C0ea3dxVLNALVaaxviF0Hyq%2B6k%2F1d0oEtrKogECOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVa%2BES0kZ2yL%2BY%2BDkq3AMVTLNwnWUvLq4pf6GiGKOYRqM6jw2ZHh4bF0JvnNSAnkD28EVuKAlkDENZu9H2A4mIuliEEOUQDTmFT8NzoO49Vd9Y7Nzk%2BzWIQ7pbh%2B%2Bf1%2B5ak5BnbTmuK980qai02wz9z7Cbr5K6ZWhWCwcRjuGVfQn%2FB59EVV7aop9QlF8fR4M2anItappuLmuu%2BoJomlxqfjxvbbVE%2FnSOWbPFTYrG%2FmF1%2FXdgzJZ%2BBa5ourOSYDQfiQ%2Fa394rKK5LVCFlsRlq8AQK7YFL9tZbdeipaYNl5llEZGRL8umHjGDDEw6oCxWCaUgIeb9I9nZ7AmE6ZYu1cJnpFLNJixdLVEC03NCQ68%2FjLfcAKWlJHPuXXFJZB4xsJAi8jwz2TvRvPuhSyN21OzG4wEFND8a8SUhEQu07iPuRhtRMGsun5bQ8zMR%2FvsStoMduNTw9hUMnxWn574SgU36caEGe%2FlWjd0%2F9AcNi7UK5rh6CIZWye%2F%2Bw48BKwVMV9PC6NUQ3BvrdhdecLKf9O2zaPO1dsj4%2BboWV1vMMX%2FAKvR7nOqgiy1p%2F627DPsMCy2PPTsqqSES9YW%2BniJgpR6u6zPh115UW9DiUSJC2D5acyjSei4vyPPdsgSRZopEwSmOnJijZGGkcpTCr7IbTBjqkAYH1e5lspZf%2F2YB%2B69RbtTzAYrq65KycBMtxpISIxJpOXgpqtKk06AnmVTjncdmhdiWoT5uAqyt8BNC6aijaUDu%2BScCipxGfyBFBAdzAfWmtJAFmqACk%2Fy8b8nFG4ukEib31%2FB%2BPhF4VP16ZVftxjkv%2BKf06o0MJbxekgX6jca1uI8QS0SZa9LU8WI7H%2Bi0WySxuQAh21dRt9yiMlXlNbzZoBA4i&X-Amz-Signature=7016dd7dc2602744798cb4390dd754977f178685eb5bcf016cd24a6b66df5735&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这些信息告诉你，mcp inspector 正在 6274 端口运行，你可以通过它提供的 URL 链接访问。MCP inspector 是我们验证服务器是否起来的工具。我们不会花太多时间来介绍。

访问检查器服务器后，你会看到如下界面。点击左侧的连接按钮。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2ace1a7c-a49b-49f6-a297-fa126365c60a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NK2A5OY%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T080833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJIMEYCIQC6Q8knv%2FuxdKU1jIcodZ4d9F4JvpCjPhgimhoGSj1J%2FQIhALOrT3Vto5C0ea3dxVLNALVaaxviF0Hyq%2B6k%2F1d0oEtrKogECOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVa%2BES0kZ2yL%2BY%2BDkq3AMVTLNwnWUvLq4pf6GiGKOYRqM6jw2ZHh4bF0JvnNSAnkD28EVuKAlkDENZu9H2A4mIuliEEOUQDTmFT8NzoO49Vd9Y7Nzk%2BzWIQ7pbh%2B%2Bf1%2B5ak5BnbTmuK980qai02wz9z7Cbr5K6ZWhWCwcRjuGVfQn%2FB59EVV7aop9QlF8fR4M2anItappuLmuu%2BoJomlxqfjxvbbVE%2FnSOWbPFTYrG%2FmF1%2FXdgzJZ%2BBa5ourOSYDQfiQ%2Fa394rKK5LVCFlsRlq8AQK7YFL9tZbdeipaYNl5llEZGRL8umHjGDDEw6oCxWCaUgIeb9I9nZ7AmE6ZYu1cJnpFLNJixdLVEC03NCQ68%2FjLfcAKWlJHPuXXFJZB4xsJAi8jwz2TvRvPuhSyN21OzG4wEFND8a8SUhEQu07iPuRhtRMGsun5bQ8zMR%2FvsStoMduNTw9hUMnxWn574SgU36caEGe%2FlWjd0%2F9AcNi7UK5rh6CIZWye%2F%2Bw48BKwVMV9PC6NUQ3BvrdhdecLKf9O2zaPO1dsj4%2BboWV1vMMX%2FAKvR7nOqgiy1p%2F627DPsMCy2PPTsqqSES9YW%2BniJgpR6u6zPh115UW9DiUSJC2D5acyjSei4vyPPdsgSRZopEwSmOnJijZGGkcpTCr7IbTBjqkAYH1e5lspZf%2F2YB%2B69RbtTzAYrq65KycBMtxpISIxJpOXgpqtKk06AnmVTjncdmhdiWoT5uAqyt8BNC6aijaUDu%2BScCipxGfyBFBAdzAfWmtJAFmqACk%2Fy8b8nFG4ukEib31%2FB%2BPhF4VP16ZVftxjkv%2BKf06o0MJbxekgX6jca1uI8QS0SZa9LU8WI7H%2Bi0WySxuQAh21dRt9yiMlXlNbzZoBA4i&X-Amz-Signature=8ecf71e80007a19169d29ac71da769d3d6fd6a2f6f897df0df2c4ecd0fc1d789&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

连接建立后，界面会变成这样。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/63247ba5-0aa1-47c6-bb5e-d878adca18c9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NK2A5OY%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T080833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJIMEYCIQC6Q8knv%2FuxdKU1jIcodZ4d9F4JvpCjPhgimhoGSj1J%2FQIhALOrT3Vto5C0ea3dxVLNALVaaxviF0Hyq%2B6k%2F1d0oEtrKogECOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVa%2BES0kZ2yL%2BY%2BDkq3AMVTLNwnWUvLq4pf6GiGKOYRqM6jw2ZHh4bF0JvnNSAnkD28EVuKAlkDENZu9H2A4mIuliEEOUQDTmFT8NzoO49Vd9Y7Nzk%2BzWIQ7pbh%2B%2Bf1%2B5ak5BnbTmuK980qai02wz9z7Cbr5K6ZWhWCwcRjuGVfQn%2FB59EVV7aop9QlF8fR4M2anItappuLmuu%2BoJomlxqfjxvbbVE%2FnSOWbPFTYrG%2FmF1%2FXdgzJZ%2BBa5ourOSYDQfiQ%2Fa394rKK5LVCFlsRlq8AQK7YFL9tZbdeipaYNl5llEZGRL8umHjGDDEw6oCxWCaUgIeb9I9nZ7AmE6ZYu1cJnpFLNJixdLVEC03NCQ68%2FjLfcAKWlJHPuXXFJZB4xsJAi8jwz2TvRvPuhSyN21OzG4wEFND8a8SUhEQu07iPuRhtRMGsun5bQ8zMR%2FvsStoMduNTw9hUMnxWn574SgU36caEGe%2FlWjd0%2F9AcNi7UK5rh6CIZWye%2F%2Bw48BKwVMV9PC6NUQ3BvrdhdecLKf9O2zaPO1dsj4%2BboWV1vMMX%2FAKvR7nOqgiy1p%2F627DPsMCy2PPTsqqSES9YW%2BniJgpR6u6zPh115UW9DiUSJC2D5acyjSei4vyPPdsgSRZopEwSmOnJijZGGkcpTCr7IbTBjqkAYH1e5lspZf%2F2YB%2B69RbtTzAYrq65KycBMtxpISIxJpOXgpqtKk06AnmVTjncdmhdiWoT5uAqyt8BNC6aijaUDu%2BScCipxGfyBFBAdzAfWmtJAFmqACk%2Fy8b8nFG4ukEib31%2FB%2BPhF4VP16ZVftxjkv%2BKf06o0MJbxekgX6jca1uI8QS0SZa9LU8WI7H%2Bi0WySxuQAh21dRt9yiMlXlNbzZoBA4i&X-Amz-Signature=18ae4ee3e9318e23c37b474e9abe1aa6f95fcca93912d1856ac1ec194fce8747&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们首先点击 "工具 "按钮，然后选择 "列表工具"，检查我们所使用的工具。然后运行。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/dd91f8d0-b87a-419a-aec0-ceb20c207b9a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NK2A5OY%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T080834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJIMEYCIQC6Q8knv%2FuxdKU1jIcodZ4d9F4JvpCjPhgimhoGSj1J%2FQIhALOrT3Vto5C0ea3dxVLNALVaaxviF0Hyq%2B6k%2F1d0oEtrKogECOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVa%2BES0kZ2yL%2BY%2BDkq3AMVTLNwnWUvLq4pf6GiGKOYRqM6jw2ZHh4bF0JvnNSAnkD28EVuKAlkDENZu9H2A4mIuliEEOUQDTmFT8NzoO49Vd9Y7Nzk%2BzWIQ7pbh%2B%2Bf1%2B5ak5BnbTmuK980qai02wz9z7Cbr5K6ZWhWCwcRjuGVfQn%2FB59EVV7aop9QlF8fR4M2anItappuLmuu%2BoJomlxqfjxvbbVE%2FnSOWbPFTYrG%2FmF1%2FXdgzJZ%2BBa5ourOSYDQfiQ%2Fa394rKK5LVCFlsRlq8AQK7YFL9tZbdeipaYNl5llEZGRL8umHjGDDEw6oCxWCaUgIeb9I9nZ7AmE6ZYu1cJnpFLNJixdLVEC03NCQ68%2FjLfcAKWlJHPuXXFJZB4xsJAi8jwz2TvRvPuhSyN21OzG4wEFND8a8SUhEQu07iPuRhtRMGsun5bQ8zMR%2FvsStoMduNTw9hUMnxWn574SgU36caEGe%2FlWjd0%2F9AcNi7UK5rh6CIZWye%2F%2Bw48BKwVMV9PC6NUQ3BvrdhdecLKf9O2zaPO1dsj4%2BboWV1vMMX%2FAKvR7nOqgiy1p%2F627DPsMCy2PPTsqqSES9YW%2BniJgpR6u6zPh115UW9DiUSJC2D5acyjSei4vyPPdsgSRZopEwSmOnJijZGGkcpTCr7IbTBjqkAYH1e5lspZf%2F2YB%2B69RbtTzAYrq65KycBMtxpISIxJpOXgpqtKk06AnmVTjncdmhdiWoT5uAqyt8BNC6aijaUDu%2BScCipxGfyBFBAdzAfWmtJAFmqACk%2Fy8b8nFG4ukEib31%2FB%2BPhF4VP16ZVftxjkv%2BKf06o0MJbxekgX6jca1uI8QS0SZa9LU8WI7H%2Bi0WySxuQAh21dRt9yiMlXlNbzZoBA4i&X-Amz-Signature=be3407272fed70fbc21f4564916ae4fecf611558eb78e10d3aee1e1baa86ea40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果工具执行成功，就会看到如下界面的结果。那么你就成功运行了一个 mcp 工具。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/70e0fd59-96fd-4056-9142-dc77071a18bf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NK2A5OY%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T080834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJIMEYCIQC6Q8knv%2FuxdKU1jIcodZ4d9F4JvpCjPhgimhoGSj1J%2FQIhALOrT3Vto5C0ea3dxVLNALVaaxviF0Hyq%2B6k%2F1d0oEtrKogECOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVa%2BES0kZ2yL%2BY%2BDkq3AMVTLNwnWUvLq4pf6GiGKOYRqM6jw2ZHh4bF0JvnNSAnkD28EVuKAlkDENZu9H2A4mIuliEEOUQDTmFT8NzoO49Vd9Y7Nzk%2BzWIQ7pbh%2B%2Bf1%2B5ak5BnbTmuK980qai02wz9z7Cbr5K6ZWhWCwcRjuGVfQn%2FB59EVV7aop9QlF8fR4M2anItappuLmuu%2BoJomlxqfjxvbbVE%2FnSOWbPFTYrG%2FmF1%2FXdgzJZ%2BBa5ourOSYDQfiQ%2Fa394rKK5LVCFlsRlq8AQK7YFL9tZbdeipaYNl5llEZGRL8umHjGDDEw6oCxWCaUgIeb9I9nZ7AmE6ZYu1cJnpFLNJixdLVEC03NCQ68%2FjLfcAKWlJHPuXXFJZB4xsJAi8jwz2TvRvPuhSyN21OzG4wEFND8a8SUhEQu07iPuRhtRMGsun5bQ8zMR%2FvsStoMduNTw9hUMnxWn574SgU36caEGe%2FlWjd0%2F9AcNi7UK5rh6CIZWye%2F%2Bw48BKwVMV9PC6NUQ3BvrdhdecLKf9O2zaPO1dsj4%2BboWV1vMMX%2FAKvR7nOqgiy1p%2F627DPsMCy2PPTsqqSES9YW%2BniJgpR6u6zPh115UW9DiUSJC2D5acyjSei4vyPPdsgSRZopEwSmOnJijZGGkcpTCr7IbTBjqkAYH1e5lspZf%2F2YB%2B69RbtTzAYrq65KycBMtxpISIxJpOXgpqtKk06AnmVTjncdmhdiWoT5uAqyt8BNC6aijaUDu%2BScCipxGfyBFBAdzAfWmtJAFmqACk%2Fy8b8nFG4ukEib31%2FB%2BPhF4VP16ZVftxjkv%2BKf06o0MJbxekgX6jca1uI8QS0SZa9LU8WI7H%2Bi0WySxuQAh21dRt9yiMlXlNbzZoBA4i&X-Amz-Signature=f6fe0ccb8c4d5e4a79e80f441a33760dec7241f73e66c276ed5042625d5e92b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/129cc91e-3fce-4702-9189-a7d04991a5d4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NK2A5OY%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T080834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJIMEYCIQC6Q8knv%2FuxdKU1jIcodZ4d9F4JvpCjPhgimhoGSj1J%2FQIhALOrT3Vto5C0ea3dxVLNALVaaxviF0Hyq%2B6k%2F1d0oEtrKogECOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVa%2BES0kZ2yL%2BY%2BDkq3AMVTLNwnWUvLq4pf6GiGKOYRqM6jw2ZHh4bF0JvnNSAnkD28EVuKAlkDENZu9H2A4mIuliEEOUQDTmFT8NzoO49Vd9Y7Nzk%2BzWIQ7pbh%2B%2Bf1%2B5ak5BnbTmuK980qai02wz9z7Cbr5K6ZWhWCwcRjuGVfQn%2FB59EVV7aop9QlF8fR4M2anItappuLmuu%2BoJomlxqfjxvbbVE%2FnSOWbPFTYrG%2FmF1%2FXdgzJZ%2BBa5ourOSYDQfiQ%2Fa394rKK5LVCFlsRlq8AQK7YFL9tZbdeipaYNl5llEZGRL8umHjGDDEw6oCxWCaUgIeb9I9nZ7AmE6ZYu1cJnpFLNJixdLVEC03NCQ68%2FjLfcAKWlJHPuXXFJZB4xsJAi8jwz2TvRvPuhSyN21OzG4wEFND8a8SUhEQu07iPuRhtRMGsun5bQ8zMR%2FvsStoMduNTw9hUMnxWn574SgU36caEGe%2FlWjd0%2F9AcNi7UK5rh6CIZWye%2F%2Bw48BKwVMV9PC6NUQ3BvrdhdecLKf9O2zaPO1dsj4%2BboWV1vMMX%2FAKvR7nOqgiy1p%2F627DPsMCy2PPTsqqSES9YW%2BniJgpR6u6zPh115UW9DiUSJC2D5acyjSei4vyPPdsgSRZopEwSmOnJijZGGkcpTCr7IbTBjqkAYH1e5lspZf%2F2YB%2B69RbtTzAYrq65KycBMtxpISIxJpOXgpqtKk06AnmVTjncdmhdiWoT5uAqyt8BNC6aijaUDu%2BScCipxGfyBFBAdzAfWmtJAFmqACk%2Fy8b8nFG4ukEib31%2FB%2BPhF4VP16ZVftxjkv%2BKf06o0MJbxekgX6jca1uI8QS0SZa9LU8WI7H%2Bi0WySxuQAh21dRt9yiMlXlNbzZoBA4i&X-Amz-Signature=4892253562f4a7ec62fcf73a5d786867e8eb83ff0f38b50f11e35f242a93c701&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
