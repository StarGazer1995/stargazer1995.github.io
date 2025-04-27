---
created: 2025-04-27T06:09:00+00:00
categories:
  - Blog
updated: 2025-04-27T06:34:00+00:00
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7f0e8a0b-c4e1-4f01-9374-57601ba10ab2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPKIQPPP%2F20250427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250427T065840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOFW%2BfCmn5M4TQvIJ%2BjTvZOuiCHt8SemEpyUgenM1diAIhANk3cMtEuSI90Bm%2FWydYAa%2FUs6F2uyoXH13pNYKAv3wAKv8DCFYQABoMNjM3NDIzMTgzODA1IgyaDIkhT4c3u0JLg14q3APIQy8dHqWf0DFe%2FpHfdAeCCRks3sM9TWb6kcK%2B3kE%2BGUT43Md%2B%2BXMHOv8YoJ35ijtvVJ%2BCk6rv35wlXftLUoMJHbcaP5Uhfr3kp%2FkP1t8zkANKlku2LtnWTIcdc1yQoYz0zitjnGesnMY32UfGMIyPTD%2B9Sdw5WZ9TBYnuPO2vpoPB4crBg1Bn5jDjh83Bkpafq8lHNEb9CHXXZ1wRPZbrShlykWuO92BG%2FzS1neUotkqH9V8Xo%2Bl85ay6XvWK8DeTu6xB8s78qIg83gx3G5TczyGPD0uGCIwJIC%2F7GeuQmJHLkOhx1ifg39gwnXTGtu7%2F4Fu9%2FaboQY39nS1N7SsPevO5XJ49J8%2FYcB9XhSPedDpXFqvmtzIdYd4a6KrKnAaqcgjND7nfA5KD5YekP81Sm8zrOKYozVTZKCe%2FMo%2Bq1jZz8eE%2Fb3pE%2FqXxmZ%2BkYR8XLHw0k88t48gJ%2BqAx90dG0SfyBSzZt9FcP6%2FiGxTkbZ915ow%2F4Vs7qjJ4o%2FdpJAaGWENclsrkpH8PNdK37p447eE%2Ffd0g3hJ96%2FmTNC2zh3vR87JHIvKFD5URYvEGGCSzuEES5PHAeNnyitJ2dbeNZhHgCOvZSOynbRp2b1x7HRwjTmBQCsh15ar6uDD67LbABjqkARAya3mG8ktbXbTvP2jCKN%2FpqJr5TPWOpvtDzg7deXSxidriUhypgmoujbATU%2FoZxM%2BXnqUyRfq6tVBKYk1CZUeIUmg8PfxG29zCSz8EHf7OmQ3xPGOQEBTtQuXuZ%2FN%2B8O6dRDldSi%2Fcy8fGHyjefXQDlG99EjDvvCM9ShPpQOpXkOycZhJe0kjW9JQPkcvFmoVNRAPfoAh14qMdlksl2BA1S9eE&X-Amz-Signature=c7d1b4d01cc7c92580c5482e9716cea7ace3855fd5f344c305ff47b402510706&X-Amz-SignedHeaders=host&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/1daf1736-35f7-48c2-9156-c98068ca2637/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPKIQPPP%2F20250427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250427T065840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOFW%2BfCmn5M4TQvIJ%2BjTvZOuiCHt8SemEpyUgenM1diAIhANk3cMtEuSI90Bm%2FWydYAa%2FUs6F2uyoXH13pNYKAv3wAKv8DCFYQABoMNjM3NDIzMTgzODA1IgyaDIkhT4c3u0JLg14q3APIQy8dHqWf0DFe%2FpHfdAeCCRks3sM9TWb6kcK%2B3kE%2BGUT43Md%2B%2BXMHOv8YoJ35ijtvVJ%2BCk6rv35wlXftLUoMJHbcaP5Uhfr3kp%2FkP1t8zkANKlku2LtnWTIcdc1yQoYz0zitjnGesnMY32UfGMIyPTD%2B9Sdw5WZ9TBYnuPO2vpoPB4crBg1Bn5jDjh83Bkpafq8lHNEb9CHXXZ1wRPZbrShlykWuO92BG%2FzS1neUotkqH9V8Xo%2Bl85ay6XvWK8DeTu6xB8s78qIg83gx3G5TczyGPD0uGCIwJIC%2F7GeuQmJHLkOhx1ifg39gwnXTGtu7%2F4Fu9%2FaboQY39nS1N7SsPevO5XJ49J8%2FYcB9XhSPedDpXFqvmtzIdYd4a6KrKnAaqcgjND7nfA5KD5YekP81Sm8zrOKYozVTZKCe%2FMo%2Bq1jZz8eE%2Fb3pE%2FqXxmZ%2BkYR8XLHw0k88t48gJ%2BqAx90dG0SfyBSzZt9FcP6%2FiGxTkbZ915ow%2F4Vs7qjJ4o%2FdpJAaGWENclsrkpH8PNdK37p447eE%2Ffd0g3hJ96%2FmTNC2zh3vR87JHIvKFD5URYvEGGCSzuEES5PHAeNnyitJ2dbeNZhHgCOvZSOynbRp2b1x7HRwjTmBQCsh15ar6uDD67LbABjqkARAya3mG8ktbXbTvP2jCKN%2FpqJr5TPWOpvtDzg7deXSxidriUhypgmoujbATU%2FoZxM%2BXnqUyRfq6tVBKYk1CZUeIUmg8PfxG29zCSz8EHf7OmQ3xPGOQEBTtQuXuZ%2FN%2B8O6dRDldSi%2Fcy8fGHyjefXQDlG99EjDvvCM9ShPpQOpXkOycZhJe0kjW9JQPkcvFmoVNRAPfoAh14qMdlksl2BA1S9eE&X-Amz-Signature=ac61ce46c417d332eb81f788ee98014131d986729bd88fba0d69979ba5d42c0a&X-Amz-SignedHeaders=host&x-id=GetObject)

这些信息告诉你，mcp inspector 正在 6274 端口运行，你可以通过它提供的 URL 链接访问。MCP inspector 是我们验证服务器是否起来的工具。我们不会花太多时间来介绍。

访问检查器服务器后，你会看到如下界面。点击左侧的连接按钮。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2ace1a7c-a49b-49f6-a297-fa126365c60a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPKIQPPP%2F20250427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250427T065840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOFW%2BfCmn5M4TQvIJ%2BjTvZOuiCHt8SemEpyUgenM1diAIhANk3cMtEuSI90Bm%2FWydYAa%2FUs6F2uyoXH13pNYKAv3wAKv8DCFYQABoMNjM3NDIzMTgzODA1IgyaDIkhT4c3u0JLg14q3APIQy8dHqWf0DFe%2FpHfdAeCCRks3sM9TWb6kcK%2B3kE%2BGUT43Md%2B%2BXMHOv8YoJ35ijtvVJ%2BCk6rv35wlXftLUoMJHbcaP5Uhfr3kp%2FkP1t8zkANKlku2LtnWTIcdc1yQoYz0zitjnGesnMY32UfGMIyPTD%2B9Sdw5WZ9TBYnuPO2vpoPB4crBg1Bn5jDjh83Bkpafq8lHNEb9CHXXZ1wRPZbrShlykWuO92BG%2FzS1neUotkqH9V8Xo%2Bl85ay6XvWK8DeTu6xB8s78qIg83gx3G5TczyGPD0uGCIwJIC%2F7GeuQmJHLkOhx1ifg39gwnXTGtu7%2F4Fu9%2FaboQY39nS1N7SsPevO5XJ49J8%2FYcB9XhSPedDpXFqvmtzIdYd4a6KrKnAaqcgjND7nfA5KD5YekP81Sm8zrOKYozVTZKCe%2FMo%2Bq1jZz8eE%2Fb3pE%2FqXxmZ%2BkYR8XLHw0k88t48gJ%2BqAx90dG0SfyBSzZt9FcP6%2FiGxTkbZ915ow%2F4Vs7qjJ4o%2FdpJAaGWENclsrkpH8PNdK37p447eE%2Ffd0g3hJ96%2FmTNC2zh3vR87JHIvKFD5URYvEGGCSzuEES5PHAeNnyitJ2dbeNZhHgCOvZSOynbRp2b1x7HRwjTmBQCsh15ar6uDD67LbABjqkARAya3mG8ktbXbTvP2jCKN%2FpqJr5TPWOpvtDzg7deXSxidriUhypgmoujbATU%2FoZxM%2BXnqUyRfq6tVBKYk1CZUeIUmg8PfxG29zCSz8EHf7OmQ3xPGOQEBTtQuXuZ%2FN%2B8O6dRDldSi%2Fcy8fGHyjefXQDlG99EjDvvCM9ShPpQOpXkOycZhJe0kjW9JQPkcvFmoVNRAPfoAh14qMdlksl2BA1S9eE&X-Amz-Signature=1368b7bcaad294f88343735220d13a727671b9fd880282cbd34909476c9505fd&X-Amz-SignedHeaders=host&x-id=GetObject)

连接建立后，界面会变成这样。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/63247ba5-0aa1-47c6-bb5e-d878adca18c9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPKIQPPP%2F20250427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250427T065840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOFW%2BfCmn5M4TQvIJ%2BjTvZOuiCHt8SemEpyUgenM1diAIhANk3cMtEuSI90Bm%2FWydYAa%2FUs6F2uyoXH13pNYKAv3wAKv8DCFYQABoMNjM3NDIzMTgzODA1IgyaDIkhT4c3u0JLg14q3APIQy8dHqWf0DFe%2FpHfdAeCCRks3sM9TWb6kcK%2B3kE%2BGUT43Md%2B%2BXMHOv8YoJ35ijtvVJ%2BCk6rv35wlXftLUoMJHbcaP5Uhfr3kp%2FkP1t8zkANKlku2LtnWTIcdc1yQoYz0zitjnGesnMY32UfGMIyPTD%2B9Sdw5WZ9TBYnuPO2vpoPB4crBg1Bn5jDjh83Bkpafq8lHNEb9CHXXZ1wRPZbrShlykWuO92BG%2FzS1neUotkqH9V8Xo%2Bl85ay6XvWK8DeTu6xB8s78qIg83gx3G5TczyGPD0uGCIwJIC%2F7GeuQmJHLkOhx1ifg39gwnXTGtu7%2F4Fu9%2FaboQY39nS1N7SsPevO5XJ49J8%2FYcB9XhSPedDpXFqvmtzIdYd4a6KrKnAaqcgjND7nfA5KD5YekP81Sm8zrOKYozVTZKCe%2FMo%2Bq1jZz8eE%2Fb3pE%2FqXxmZ%2BkYR8XLHw0k88t48gJ%2BqAx90dG0SfyBSzZt9FcP6%2FiGxTkbZ915ow%2F4Vs7qjJ4o%2FdpJAaGWENclsrkpH8PNdK37p447eE%2Ffd0g3hJ96%2FmTNC2zh3vR87JHIvKFD5URYvEGGCSzuEES5PHAeNnyitJ2dbeNZhHgCOvZSOynbRp2b1x7HRwjTmBQCsh15ar6uDD67LbABjqkARAya3mG8ktbXbTvP2jCKN%2FpqJr5TPWOpvtDzg7deXSxidriUhypgmoujbATU%2FoZxM%2BXnqUyRfq6tVBKYk1CZUeIUmg8PfxG29zCSz8EHf7OmQ3xPGOQEBTtQuXuZ%2FN%2B8O6dRDldSi%2Fcy8fGHyjefXQDlG99EjDvvCM9ShPpQOpXkOycZhJe0kjW9JQPkcvFmoVNRAPfoAh14qMdlksl2BA1S9eE&X-Amz-Signature=0d1c2b233572b6627b3afc7a54b17b145e040c449db18eaf34e856390345106e&X-Amz-SignedHeaders=host&x-id=GetObject)

我们首先点击 "工具 "按钮，然后选择 "列表工具"，检查我们所使用的工具。然后运行。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/dd91f8d0-b87a-419a-aec0-ceb20c207b9a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPKIQPPP%2F20250427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250427T065840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOFW%2BfCmn5M4TQvIJ%2BjTvZOuiCHt8SemEpyUgenM1diAIhANk3cMtEuSI90Bm%2FWydYAa%2FUs6F2uyoXH13pNYKAv3wAKv8DCFYQABoMNjM3NDIzMTgzODA1IgyaDIkhT4c3u0JLg14q3APIQy8dHqWf0DFe%2FpHfdAeCCRks3sM9TWb6kcK%2B3kE%2BGUT43Md%2B%2BXMHOv8YoJ35ijtvVJ%2BCk6rv35wlXftLUoMJHbcaP5Uhfr3kp%2FkP1t8zkANKlku2LtnWTIcdc1yQoYz0zitjnGesnMY32UfGMIyPTD%2B9Sdw5WZ9TBYnuPO2vpoPB4crBg1Bn5jDjh83Bkpafq8lHNEb9CHXXZ1wRPZbrShlykWuO92BG%2FzS1neUotkqH9V8Xo%2Bl85ay6XvWK8DeTu6xB8s78qIg83gx3G5TczyGPD0uGCIwJIC%2F7GeuQmJHLkOhx1ifg39gwnXTGtu7%2F4Fu9%2FaboQY39nS1N7SsPevO5XJ49J8%2FYcB9XhSPedDpXFqvmtzIdYd4a6KrKnAaqcgjND7nfA5KD5YekP81Sm8zrOKYozVTZKCe%2FMo%2Bq1jZz8eE%2Fb3pE%2FqXxmZ%2BkYR8XLHw0k88t48gJ%2BqAx90dG0SfyBSzZt9FcP6%2FiGxTkbZ915ow%2F4Vs7qjJ4o%2FdpJAaGWENclsrkpH8PNdK37p447eE%2Ffd0g3hJ96%2FmTNC2zh3vR87JHIvKFD5URYvEGGCSzuEES5PHAeNnyitJ2dbeNZhHgCOvZSOynbRp2b1x7HRwjTmBQCsh15ar6uDD67LbABjqkARAya3mG8ktbXbTvP2jCKN%2FpqJr5TPWOpvtDzg7deXSxidriUhypgmoujbATU%2FoZxM%2BXnqUyRfq6tVBKYk1CZUeIUmg8PfxG29zCSz8EHf7OmQ3xPGOQEBTtQuXuZ%2FN%2B8O6dRDldSi%2Fcy8fGHyjefXQDlG99EjDvvCM9ShPpQOpXkOycZhJe0kjW9JQPkcvFmoVNRAPfoAh14qMdlksl2BA1S9eE&X-Amz-Signature=704f0aaafdb65a3117bbf8ab437b6c12277fe896d212dbcdb9effee609bf5888&X-Amz-SignedHeaders=host&x-id=GetObject)

如果工具执行成功，就会看到如下界面的结果。那么你就成功运行了一个 mcp 工具。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/70e0fd59-96fd-4056-9142-dc77071a18bf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPKIQPPP%2F20250427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250427T065840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOFW%2BfCmn5M4TQvIJ%2BjTvZOuiCHt8SemEpyUgenM1diAIhANk3cMtEuSI90Bm%2FWydYAa%2FUs6F2uyoXH13pNYKAv3wAKv8DCFYQABoMNjM3NDIzMTgzODA1IgyaDIkhT4c3u0JLg14q3APIQy8dHqWf0DFe%2FpHfdAeCCRks3sM9TWb6kcK%2B3kE%2BGUT43Md%2B%2BXMHOv8YoJ35ijtvVJ%2BCk6rv35wlXftLUoMJHbcaP5Uhfr3kp%2FkP1t8zkANKlku2LtnWTIcdc1yQoYz0zitjnGesnMY32UfGMIyPTD%2B9Sdw5WZ9TBYnuPO2vpoPB4crBg1Bn5jDjh83Bkpafq8lHNEb9CHXXZ1wRPZbrShlykWuO92BG%2FzS1neUotkqH9V8Xo%2Bl85ay6XvWK8DeTu6xB8s78qIg83gx3G5TczyGPD0uGCIwJIC%2F7GeuQmJHLkOhx1ifg39gwnXTGtu7%2F4Fu9%2FaboQY39nS1N7SsPevO5XJ49J8%2FYcB9XhSPedDpXFqvmtzIdYd4a6KrKnAaqcgjND7nfA5KD5YekP81Sm8zrOKYozVTZKCe%2FMo%2Bq1jZz8eE%2Fb3pE%2FqXxmZ%2BkYR8XLHw0k88t48gJ%2BqAx90dG0SfyBSzZt9FcP6%2FiGxTkbZ915ow%2F4Vs7qjJ4o%2FdpJAaGWENclsrkpH8PNdK37p447eE%2Ffd0g3hJ96%2FmTNC2zh3vR87JHIvKFD5URYvEGGCSzuEES5PHAeNnyitJ2dbeNZhHgCOvZSOynbRp2b1x7HRwjTmBQCsh15ar6uDD67LbABjqkARAya3mG8ktbXbTvP2jCKN%2FpqJr5TPWOpvtDzg7deXSxidriUhypgmoujbATU%2FoZxM%2BXnqUyRfq6tVBKYk1CZUeIUmg8PfxG29zCSz8EHf7OmQ3xPGOQEBTtQuXuZ%2FN%2B8O6dRDldSi%2Fcy8fGHyjefXQDlG99EjDvvCM9ShPpQOpXkOycZhJe0kjW9JQPkcvFmoVNRAPfoAh14qMdlksl2BA1S9eE&X-Amz-Signature=bc11af2040c3f0435ef10da7d1d8841bc54d7db6ff35074ae5b5a264819fe08c&X-Amz-SignedHeaders=host&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/129cc91e-3fce-4702-9189-a7d04991a5d4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPKIQPPP%2F20250427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250427T065840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOFW%2BfCmn5M4TQvIJ%2BjTvZOuiCHt8SemEpyUgenM1diAIhANk3cMtEuSI90Bm%2FWydYAa%2FUs6F2uyoXH13pNYKAv3wAKv8DCFYQABoMNjM3NDIzMTgzODA1IgyaDIkhT4c3u0JLg14q3APIQy8dHqWf0DFe%2FpHfdAeCCRks3sM9TWb6kcK%2B3kE%2BGUT43Md%2B%2BXMHOv8YoJ35ijtvVJ%2BCk6rv35wlXftLUoMJHbcaP5Uhfr3kp%2FkP1t8zkANKlku2LtnWTIcdc1yQoYz0zitjnGesnMY32UfGMIyPTD%2B9Sdw5WZ9TBYnuPO2vpoPB4crBg1Bn5jDjh83Bkpafq8lHNEb9CHXXZ1wRPZbrShlykWuO92BG%2FzS1neUotkqH9V8Xo%2Bl85ay6XvWK8DeTu6xB8s78qIg83gx3G5TczyGPD0uGCIwJIC%2F7GeuQmJHLkOhx1ifg39gwnXTGtu7%2F4Fu9%2FaboQY39nS1N7SsPevO5XJ49J8%2FYcB9XhSPedDpXFqvmtzIdYd4a6KrKnAaqcgjND7nfA5KD5YekP81Sm8zrOKYozVTZKCe%2FMo%2Bq1jZz8eE%2Fb3pE%2FqXxmZ%2BkYR8XLHw0k88t48gJ%2BqAx90dG0SfyBSzZt9FcP6%2FiGxTkbZ915ow%2F4Vs7qjJ4o%2FdpJAaGWENclsrkpH8PNdK37p447eE%2Ffd0g3hJ96%2FmTNC2zh3vR87JHIvKFD5URYvEGGCSzuEES5PHAeNnyitJ2dbeNZhHgCOvZSOynbRp2b1x7HRwjTmBQCsh15ar6uDD67LbABjqkARAya3mG8ktbXbTvP2jCKN%2FpqJr5TPWOpvtDzg7deXSxidriUhypgmoujbATU%2FoZxM%2BXnqUyRfq6tVBKYk1CZUeIUmg8PfxG29zCSz8EHf7OmQ3xPGOQEBTtQuXuZ%2FN%2B8O6dRDldSi%2Fcy8fGHyjefXQDlG99EjDvvCM9ShPpQOpXkOycZhJe0kjW9JQPkcvFmoVNRAPfoAh14qMdlksl2BA1S9eE&X-Amz-Signature=627ec0870376902b531cc08513174ea831b4d9c70967bccb69480853e1444b34&X-Amz-SignedHeaders=host&x-id=GetObject)
