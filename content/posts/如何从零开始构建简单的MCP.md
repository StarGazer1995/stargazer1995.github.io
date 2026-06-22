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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7f0e8a0b-c4e1-4f01-9374-57601ba10ab2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUU5N4BQ%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T093755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCIDIQLAExY8%2FpbS0w2uDSl4OOAgZuWmheOpO4znlr26qgAiAgCO%2BRiMfEbMvL76MM38V0rIaJ3GGTlCHDqaHTdIXSBSr%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIMQ2qSEp5SDMjfJpIXKtwDt9RHk9GFki9OHtaerrMZk2vv5Fm%2FC3BOM18ou2xUDHqFeO5LpMy%2FNxMB%2FvrFS08fbHLQOLmC2O203vtSb2iR%2Fhn%2BVRIkshtoh7r4vf10VHf1cGsaBayv5ilxoYvJSn5s4Wj5rliMLTrhT8%2BzacR%2FgS2cSa0JV%2BAmBBHtuxpGVWhyVg7i6wmwLMtP6wRndi2hjXL0Ky8Q2%2FAVBxjTDuzTuUjk5R9s8Bb3QyhYDcTg3L4QHsDYZCGiFeg90zJzOVlx9vyrWQay%2BH8%2FsUrhOJKnQztV9FZV%2FUSfYMpPT7BUMUnnVaCUifR%2BFmNrVqKOZzbGJJ0si0Om0%2Bf3srfrNN5vmwcIOFtouOZ0RzUsnmfKzJqTxjh37xpPORQfnCyzqj8uk8sEfZJB5DwnVCbiriTtrlaTdURBHfwwkjYNugCA30W0KKFeZllD5o95JfmC91dSivfb0HknMJ%2B375R8ceK59KVATl4eXYrHz8Xyal7jfcsEazD2AHUwO%2FmU2rvlZuKd637eEfdQ04qoY8EFgwxelymiWt5mMGoJN%2FZvu%2FgHvc3317QCP16lc8dm8zjYnLettWNY4WQZp%2FYeEaQFHNiMQ7FyN%2BJXugcv7PywEGT9sxakoGvKPZHU%2FFynAvsw2fXj0QY6pgFkziWtzfDNgfJ3MeC31lDB0K8NYi5JMUYNxXyFa8GxcuH0LMLn2JtHIrrYJQ%2FdmTocLklJuQr5xKhtViswTc4wfege1H04Wam%2FR%2FSzgTIRdXQYcopT%2BF4l8B76dZ%2FonlBdGT9ZR4lXuONGo9t97VOv5OG%2FENHlabOYgTOh1vSZ1VBN5Krd1HzpyHAFzAExOedPN2Vw1tZ5glaHSx3wOkUUmHH%2F9e0g&X-Amz-Signature=ff1531433e9c2a0512abfbd53b1fc9904f436ffcd44de9caece711b348520da0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/1daf1736-35f7-48c2-9156-c98068ca2637/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUU5N4BQ%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T093756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCIDIQLAExY8%2FpbS0w2uDSl4OOAgZuWmheOpO4znlr26qgAiAgCO%2BRiMfEbMvL76MM38V0rIaJ3GGTlCHDqaHTdIXSBSr%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIMQ2qSEp5SDMjfJpIXKtwDt9RHk9GFki9OHtaerrMZk2vv5Fm%2FC3BOM18ou2xUDHqFeO5LpMy%2FNxMB%2FvrFS08fbHLQOLmC2O203vtSb2iR%2Fhn%2BVRIkshtoh7r4vf10VHf1cGsaBayv5ilxoYvJSn5s4Wj5rliMLTrhT8%2BzacR%2FgS2cSa0JV%2BAmBBHtuxpGVWhyVg7i6wmwLMtP6wRndi2hjXL0Ky8Q2%2FAVBxjTDuzTuUjk5R9s8Bb3QyhYDcTg3L4QHsDYZCGiFeg90zJzOVlx9vyrWQay%2BH8%2FsUrhOJKnQztV9FZV%2FUSfYMpPT7BUMUnnVaCUifR%2BFmNrVqKOZzbGJJ0si0Om0%2Bf3srfrNN5vmwcIOFtouOZ0RzUsnmfKzJqTxjh37xpPORQfnCyzqj8uk8sEfZJB5DwnVCbiriTtrlaTdURBHfwwkjYNugCA30W0KKFeZllD5o95JfmC91dSivfb0HknMJ%2B375R8ceK59KVATl4eXYrHz8Xyal7jfcsEazD2AHUwO%2FmU2rvlZuKd637eEfdQ04qoY8EFgwxelymiWt5mMGoJN%2FZvu%2FgHvc3317QCP16lc8dm8zjYnLettWNY4WQZp%2FYeEaQFHNiMQ7FyN%2BJXugcv7PywEGT9sxakoGvKPZHU%2FFynAvsw2fXj0QY6pgFkziWtzfDNgfJ3MeC31lDB0K8NYi5JMUYNxXyFa8GxcuH0LMLn2JtHIrrYJQ%2FdmTocLklJuQr5xKhtViswTc4wfege1H04Wam%2FR%2FSzgTIRdXQYcopT%2BF4l8B76dZ%2FonlBdGT9ZR4lXuONGo9t97VOv5OG%2FENHlabOYgTOh1vSZ1VBN5Krd1HzpyHAFzAExOedPN2Vw1tZ5glaHSx3wOkUUmHH%2F9e0g&X-Amz-Signature=94385bc25f1e169f5996c0deb86a8f75cba9be434cd28fe6b934ceca8207abc2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这些信息告诉你，mcp inspector 正在 6274 端口运行，你可以通过它提供的 URL 链接访问。MCP inspector 是我们验证服务器是否起来的工具。我们不会花太多时间来介绍。

访问检查器服务器后，你会看到如下界面。点击左侧的连接按钮。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2ace1a7c-a49b-49f6-a297-fa126365c60a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUU5N4BQ%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T093756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCIDIQLAExY8%2FpbS0w2uDSl4OOAgZuWmheOpO4znlr26qgAiAgCO%2BRiMfEbMvL76MM38V0rIaJ3GGTlCHDqaHTdIXSBSr%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIMQ2qSEp5SDMjfJpIXKtwDt9RHk9GFki9OHtaerrMZk2vv5Fm%2FC3BOM18ou2xUDHqFeO5LpMy%2FNxMB%2FvrFS08fbHLQOLmC2O203vtSb2iR%2Fhn%2BVRIkshtoh7r4vf10VHf1cGsaBayv5ilxoYvJSn5s4Wj5rliMLTrhT8%2BzacR%2FgS2cSa0JV%2BAmBBHtuxpGVWhyVg7i6wmwLMtP6wRndi2hjXL0Ky8Q2%2FAVBxjTDuzTuUjk5R9s8Bb3QyhYDcTg3L4QHsDYZCGiFeg90zJzOVlx9vyrWQay%2BH8%2FsUrhOJKnQztV9FZV%2FUSfYMpPT7BUMUnnVaCUifR%2BFmNrVqKOZzbGJJ0si0Om0%2Bf3srfrNN5vmwcIOFtouOZ0RzUsnmfKzJqTxjh37xpPORQfnCyzqj8uk8sEfZJB5DwnVCbiriTtrlaTdURBHfwwkjYNugCA30W0KKFeZllD5o95JfmC91dSivfb0HknMJ%2B375R8ceK59KVATl4eXYrHz8Xyal7jfcsEazD2AHUwO%2FmU2rvlZuKd637eEfdQ04qoY8EFgwxelymiWt5mMGoJN%2FZvu%2FgHvc3317QCP16lc8dm8zjYnLettWNY4WQZp%2FYeEaQFHNiMQ7FyN%2BJXugcv7PywEGT9sxakoGvKPZHU%2FFynAvsw2fXj0QY6pgFkziWtzfDNgfJ3MeC31lDB0K8NYi5JMUYNxXyFa8GxcuH0LMLn2JtHIrrYJQ%2FdmTocLklJuQr5xKhtViswTc4wfege1H04Wam%2FR%2FSzgTIRdXQYcopT%2BF4l8B76dZ%2FonlBdGT9ZR4lXuONGo9t97VOv5OG%2FENHlabOYgTOh1vSZ1VBN5Krd1HzpyHAFzAExOedPN2Vw1tZ5glaHSx3wOkUUmHH%2F9e0g&X-Amz-Signature=0bc8ea72c8ab825cdf95ec1b92c4cc9301ccdda33ce58b0a0fd1348fe0e243a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

连接建立后，界面会变成这样。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/63247ba5-0aa1-47c6-bb5e-d878adca18c9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUU5N4BQ%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T093756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCIDIQLAExY8%2FpbS0w2uDSl4OOAgZuWmheOpO4znlr26qgAiAgCO%2BRiMfEbMvL76MM38V0rIaJ3GGTlCHDqaHTdIXSBSr%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIMQ2qSEp5SDMjfJpIXKtwDt9RHk9GFki9OHtaerrMZk2vv5Fm%2FC3BOM18ou2xUDHqFeO5LpMy%2FNxMB%2FvrFS08fbHLQOLmC2O203vtSb2iR%2Fhn%2BVRIkshtoh7r4vf10VHf1cGsaBayv5ilxoYvJSn5s4Wj5rliMLTrhT8%2BzacR%2FgS2cSa0JV%2BAmBBHtuxpGVWhyVg7i6wmwLMtP6wRndi2hjXL0Ky8Q2%2FAVBxjTDuzTuUjk5R9s8Bb3QyhYDcTg3L4QHsDYZCGiFeg90zJzOVlx9vyrWQay%2BH8%2FsUrhOJKnQztV9FZV%2FUSfYMpPT7BUMUnnVaCUifR%2BFmNrVqKOZzbGJJ0si0Om0%2Bf3srfrNN5vmwcIOFtouOZ0RzUsnmfKzJqTxjh37xpPORQfnCyzqj8uk8sEfZJB5DwnVCbiriTtrlaTdURBHfwwkjYNugCA30W0KKFeZllD5o95JfmC91dSivfb0HknMJ%2B375R8ceK59KVATl4eXYrHz8Xyal7jfcsEazD2AHUwO%2FmU2rvlZuKd637eEfdQ04qoY8EFgwxelymiWt5mMGoJN%2FZvu%2FgHvc3317QCP16lc8dm8zjYnLettWNY4WQZp%2FYeEaQFHNiMQ7FyN%2BJXugcv7PywEGT9sxakoGvKPZHU%2FFynAvsw2fXj0QY6pgFkziWtzfDNgfJ3MeC31lDB0K8NYi5JMUYNxXyFa8GxcuH0LMLn2JtHIrrYJQ%2FdmTocLklJuQr5xKhtViswTc4wfege1H04Wam%2FR%2FSzgTIRdXQYcopT%2BF4l8B76dZ%2FonlBdGT9ZR4lXuONGo9t97VOv5OG%2FENHlabOYgTOh1vSZ1VBN5Krd1HzpyHAFzAExOedPN2Vw1tZ5glaHSx3wOkUUmHH%2F9e0g&X-Amz-Signature=e3d0b25242af0d96559ec13a93ec97b95d740070c2e52fc24dee06e4344e84b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们首先点击 "工具 "按钮，然后选择 "列表工具"，检查我们所使用的工具。然后运行。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/dd91f8d0-b87a-419a-aec0-ceb20c207b9a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUU5N4BQ%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T093756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCIDIQLAExY8%2FpbS0w2uDSl4OOAgZuWmheOpO4znlr26qgAiAgCO%2BRiMfEbMvL76MM38V0rIaJ3GGTlCHDqaHTdIXSBSr%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIMQ2qSEp5SDMjfJpIXKtwDt9RHk9GFki9OHtaerrMZk2vv5Fm%2FC3BOM18ou2xUDHqFeO5LpMy%2FNxMB%2FvrFS08fbHLQOLmC2O203vtSb2iR%2Fhn%2BVRIkshtoh7r4vf10VHf1cGsaBayv5ilxoYvJSn5s4Wj5rliMLTrhT8%2BzacR%2FgS2cSa0JV%2BAmBBHtuxpGVWhyVg7i6wmwLMtP6wRndi2hjXL0Ky8Q2%2FAVBxjTDuzTuUjk5R9s8Bb3QyhYDcTg3L4QHsDYZCGiFeg90zJzOVlx9vyrWQay%2BH8%2FsUrhOJKnQztV9FZV%2FUSfYMpPT7BUMUnnVaCUifR%2BFmNrVqKOZzbGJJ0si0Om0%2Bf3srfrNN5vmwcIOFtouOZ0RzUsnmfKzJqTxjh37xpPORQfnCyzqj8uk8sEfZJB5DwnVCbiriTtrlaTdURBHfwwkjYNugCA30W0KKFeZllD5o95JfmC91dSivfb0HknMJ%2B375R8ceK59KVATl4eXYrHz8Xyal7jfcsEazD2AHUwO%2FmU2rvlZuKd637eEfdQ04qoY8EFgwxelymiWt5mMGoJN%2FZvu%2FgHvc3317QCP16lc8dm8zjYnLettWNY4WQZp%2FYeEaQFHNiMQ7FyN%2BJXugcv7PywEGT9sxakoGvKPZHU%2FFynAvsw2fXj0QY6pgFkziWtzfDNgfJ3MeC31lDB0K8NYi5JMUYNxXyFa8GxcuH0LMLn2JtHIrrYJQ%2FdmTocLklJuQr5xKhtViswTc4wfege1H04Wam%2FR%2FSzgTIRdXQYcopT%2BF4l8B76dZ%2FonlBdGT9ZR4lXuONGo9t97VOv5OG%2FENHlabOYgTOh1vSZ1VBN5Krd1HzpyHAFzAExOedPN2Vw1tZ5glaHSx3wOkUUmHH%2F9e0g&X-Amz-Signature=4dfbd11136c520dc322ea43d6a63f7a71922c1da4f3e6b5b5836495ca0ef3b4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果工具执行成功，就会看到如下界面的结果。那么你就成功运行了一个 mcp 工具。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/70e0fd59-96fd-4056-9142-dc77071a18bf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUU5N4BQ%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T093756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCIDIQLAExY8%2FpbS0w2uDSl4OOAgZuWmheOpO4znlr26qgAiAgCO%2BRiMfEbMvL76MM38V0rIaJ3GGTlCHDqaHTdIXSBSr%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIMQ2qSEp5SDMjfJpIXKtwDt9RHk9GFki9OHtaerrMZk2vv5Fm%2FC3BOM18ou2xUDHqFeO5LpMy%2FNxMB%2FvrFS08fbHLQOLmC2O203vtSb2iR%2Fhn%2BVRIkshtoh7r4vf10VHf1cGsaBayv5ilxoYvJSn5s4Wj5rliMLTrhT8%2BzacR%2FgS2cSa0JV%2BAmBBHtuxpGVWhyVg7i6wmwLMtP6wRndi2hjXL0Ky8Q2%2FAVBxjTDuzTuUjk5R9s8Bb3QyhYDcTg3L4QHsDYZCGiFeg90zJzOVlx9vyrWQay%2BH8%2FsUrhOJKnQztV9FZV%2FUSfYMpPT7BUMUnnVaCUifR%2BFmNrVqKOZzbGJJ0si0Om0%2Bf3srfrNN5vmwcIOFtouOZ0RzUsnmfKzJqTxjh37xpPORQfnCyzqj8uk8sEfZJB5DwnVCbiriTtrlaTdURBHfwwkjYNugCA30W0KKFeZllD5o95JfmC91dSivfb0HknMJ%2B375R8ceK59KVATl4eXYrHz8Xyal7jfcsEazD2AHUwO%2FmU2rvlZuKd637eEfdQ04qoY8EFgwxelymiWt5mMGoJN%2FZvu%2FgHvc3317QCP16lc8dm8zjYnLettWNY4WQZp%2FYeEaQFHNiMQ7FyN%2BJXugcv7PywEGT9sxakoGvKPZHU%2FFynAvsw2fXj0QY6pgFkziWtzfDNgfJ3MeC31lDB0K8NYi5JMUYNxXyFa8GxcuH0LMLn2JtHIrrYJQ%2FdmTocLklJuQr5xKhtViswTc4wfege1H04Wam%2FR%2FSzgTIRdXQYcopT%2BF4l8B76dZ%2FonlBdGT9ZR4lXuONGo9t97VOv5OG%2FENHlabOYgTOh1vSZ1VBN5Krd1HzpyHAFzAExOedPN2Vw1tZ5glaHSx3wOkUUmHH%2F9e0g&X-Amz-Signature=58b110944ec005e83e320403234205e1d1bdba3f0198ecbb20388ff4c4de276d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/129cc91e-3fce-4702-9189-a7d04991a5d4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUU5N4BQ%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T093756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCIDIQLAExY8%2FpbS0w2uDSl4OOAgZuWmheOpO4znlr26qgAiAgCO%2BRiMfEbMvL76MM38V0rIaJ3GGTlCHDqaHTdIXSBSr%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIMQ2qSEp5SDMjfJpIXKtwDt9RHk9GFki9OHtaerrMZk2vv5Fm%2FC3BOM18ou2xUDHqFeO5LpMy%2FNxMB%2FvrFS08fbHLQOLmC2O203vtSb2iR%2Fhn%2BVRIkshtoh7r4vf10VHf1cGsaBayv5ilxoYvJSn5s4Wj5rliMLTrhT8%2BzacR%2FgS2cSa0JV%2BAmBBHtuxpGVWhyVg7i6wmwLMtP6wRndi2hjXL0Ky8Q2%2FAVBxjTDuzTuUjk5R9s8Bb3QyhYDcTg3L4QHsDYZCGiFeg90zJzOVlx9vyrWQay%2BH8%2FsUrhOJKnQztV9FZV%2FUSfYMpPT7BUMUnnVaCUifR%2BFmNrVqKOZzbGJJ0si0Om0%2Bf3srfrNN5vmwcIOFtouOZ0RzUsnmfKzJqTxjh37xpPORQfnCyzqj8uk8sEfZJB5DwnVCbiriTtrlaTdURBHfwwkjYNugCA30W0KKFeZllD5o95JfmC91dSivfb0HknMJ%2B375R8ceK59KVATl4eXYrHz8Xyal7jfcsEazD2AHUwO%2FmU2rvlZuKd637eEfdQ04qoY8EFgwxelymiWt5mMGoJN%2FZvu%2FgHvc3317QCP16lc8dm8zjYnLettWNY4WQZp%2FYeEaQFHNiMQ7FyN%2BJXugcv7PywEGT9sxakoGvKPZHU%2FFynAvsw2fXj0QY6pgFkziWtzfDNgfJ3MeC31lDB0K8NYi5JMUYNxXyFa8GxcuH0LMLn2JtHIrrYJQ%2FdmTocLklJuQr5xKhtViswTc4wfege1H04Wam%2FR%2FSzgTIRdXQYcopT%2BF4l8B76dZ%2FonlBdGT9ZR4lXuONGo9t97VOv5OG%2FENHlabOYgTOh1vSZ1VBN5Krd1HzpyHAFzAExOedPN2Vw1tZ5glaHSx3wOkUUmHH%2F9e0g&X-Amz-Signature=69b3ed101f8ff5814fdb46eca2ee0433e1a3a838646c80a41ccb829f79b29fb4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
