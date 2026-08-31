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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7f0e8a0b-c4e1-4f01-9374-57601ba10ab2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSZNDVSN%2F20260831%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260831T155042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIETaZa3T4TKkLPL6%2FSEIVjDa6LK6Pe1rbx9plr%2B3Cz4iAiEA0Fae%2FrWDk6mmhKPglb6GH%2BKlpKXDKehYXKO8pBxT5XMqiAQImP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM%2FegE6tPUp%2BWV3O5yrcAzrXOXvkAXEPpYY2CWB4TTJuLuz6T6FBsyoKI%2FuYPZIapOhSEe6VyEY7To4N5Dx2YkLnMCLO7ogRZkBw8Ru89hWCggEfsdPyDV9ELyF1ZvGh2kJhkil12q314tQ9zzDaK4IZaEwwHaWSmRRbRymAmyGl%2FAyCZmsXRQEy7opSZojprC6zefV2ArBB7iuFjNCg%2BD5NlhjpFSL5HAEr1rgzE6KZEearWcEXn3H88Yp1yzKJIMMUNMH94kzFFxm099hxHJRNekxDfwNiUuwvFg4WWHqLRl3xwPT8KiKzgxhRYJ1qayTsRoKhhzUi2Mu3uh3OjaV%2BJRHLSwjjpfJVof5%2BT2nr1qW5vi6LBGTZAyAa0LBX5DK5Rak22vcXqucVseHNfkdw3Dx1XfAlwgenJ%2BjS9s11hLaRjebGRvi0XdvvvBkDQM2WlnHRMC6vPyBhnhBeVU8rzToyHkyt4sg9IzKjsadIpVyK3RNcj8x2ppDAQOTztv5LEcN0dZ%2FVZFzKX6S2iV69A%2FPkV0K%2BVi5so1DsKlmxCn%2FFoIu1p4rWNhTQJ4DIOODpSSInYoPJqkpI2KqP1atIW9g6Q7fZsAtvzRdcOGOc2dhM2KRFaPwT6XNn7ugWHZ9dDx7Ee2XOX%2FtkMNOq1tQGOqUBgczI0EukiaOwVD%2F%2F6mu9u8aVr%2FJVix4%2FhJSgJT8IxIjm1vQ%2FdFYHU%2FlRI5RAJDCS3guj8F8OgvJL3Wbcj%2F00IOAFZ%2BHXxxU%2BJyZKwTnyPtBEIwarX8XtxqgZfRcAy0lTD%2Fod4DhCDvgfD2Np925E48%2BlR1DPa%2Bhm8lhhaPglzzazZUUCewnCu%2BJAFt0HHJRcPCTvF6IidC8R8%2FyNrSUb8Lk0R%2BNL&X-Amz-Signature=80a0ccc6a40c67aa01d57d2ea39211edb009b73e8e165ddafbbbdd80eeb928e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/1daf1736-35f7-48c2-9156-c98068ca2637/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSZNDVSN%2F20260831%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260831T155042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIETaZa3T4TKkLPL6%2FSEIVjDa6LK6Pe1rbx9plr%2B3Cz4iAiEA0Fae%2FrWDk6mmhKPglb6GH%2BKlpKXDKehYXKO8pBxT5XMqiAQImP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM%2FegE6tPUp%2BWV3O5yrcAzrXOXvkAXEPpYY2CWB4TTJuLuz6T6FBsyoKI%2FuYPZIapOhSEe6VyEY7To4N5Dx2YkLnMCLO7ogRZkBw8Ru89hWCggEfsdPyDV9ELyF1ZvGh2kJhkil12q314tQ9zzDaK4IZaEwwHaWSmRRbRymAmyGl%2FAyCZmsXRQEy7opSZojprC6zefV2ArBB7iuFjNCg%2BD5NlhjpFSL5HAEr1rgzE6KZEearWcEXn3H88Yp1yzKJIMMUNMH94kzFFxm099hxHJRNekxDfwNiUuwvFg4WWHqLRl3xwPT8KiKzgxhRYJ1qayTsRoKhhzUi2Mu3uh3OjaV%2BJRHLSwjjpfJVof5%2BT2nr1qW5vi6LBGTZAyAa0LBX5DK5Rak22vcXqucVseHNfkdw3Dx1XfAlwgenJ%2BjS9s11hLaRjebGRvi0XdvvvBkDQM2WlnHRMC6vPyBhnhBeVU8rzToyHkyt4sg9IzKjsadIpVyK3RNcj8x2ppDAQOTztv5LEcN0dZ%2FVZFzKX6S2iV69A%2FPkV0K%2BVi5so1DsKlmxCn%2FFoIu1p4rWNhTQJ4DIOODpSSInYoPJqkpI2KqP1atIW9g6Q7fZsAtvzRdcOGOc2dhM2KRFaPwT6XNn7ugWHZ9dDx7Ee2XOX%2FtkMNOq1tQGOqUBgczI0EukiaOwVD%2F%2F6mu9u8aVr%2FJVix4%2FhJSgJT8IxIjm1vQ%2FdFYHU%2FlRI5RAJDCS3guj8F8OgvJL3Wbcj%2F00IOAFZ%2BHXxxU%2BJyZKwTnyPtBEIwarX8XtxqgZfRcAy0lTD%2Fod4DhCDvgfD2Np925E48%2BlR1DPa%2Bhm8lhhaPglzzazZUUCewnCu%2BJAFt0HHJRcPCTvF6IidC8R8%2FyNrSUb8Lk0R%2BNL&X-Amz-Signature=ff6fcfed54979af045cf6196f1c13d5c36bb9f9e01c0013769243eeb04d81963&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这些信息告诉你，mcp inspector 正在 6274 端口运行，你可以通过它提供的 URL 链接访问。MCP inspector 是我们验证服务器是否起来的工具。我们不会花太多时间来介绍。

访问检查器服务器后，你会看到如下界面。点击左侧的连接按钮。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2ace1a7c-a49b-49f6-a297-fa126365c60a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSZNDVSN%2F20260831%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260831T155042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIETaZa3T4TKkLPL6%2FSEIVjDa6LK6Pe1rbx9plr%2B3Cz4iAiEA0Fae%2FrWDk6mmhKPglb6GH%2BKlpKXDKehYXKO8pBxT5XMqiAQImP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM%2FegE6tPUp%2BWV3O5yrcAzrXOXvkAXEPpYY2CWB4TTJuLuz6T6FBsyoKI%2FuYPZIapOhSEe6VyEY7To4N5Dx2YkLnMCLO7ogRZkBw8Ru89hWCggEfsdPyDV9ELyF1ZvGh2kJhkil12q314tQ9zzDaK4IZaEwwHaWSmRRbRymAmyGl%2FAyCZmsXRQEy7opSZojprC6zefV2ArBB7iuFjNCg%2BD5NlhjpFSL5HAEr1rgzE6KZEearWcEXn3H88Yp1yzKJIMMUNMH94kzFFxm099hxHJRNekxDfwNiUuwvFg4WWHqLRl3xwPT8KiKzgxhRYJ1qayTsRoKhhzUi2Mu3uh3OjaV%2BJRHLSwjjpfJVof5%2BT2nr1qW5vi6LBGTZAyAa0LBX5DK5Rak22vcXqucVseHNfkdw3Dx1XfAlwgenJ%2BjS9s11hLaRjebGRvi0XdvvvBkDQM2WlnHRMC6vPyBhnhBeVU8rzToyHkyt4sg9IzKjsadIpVyK3RNcj8x2ppDAQOTztv5LEcN0dZ%2FVZFzKX6S2iV69A%2FPkV0K%2BVi5so1DsKlmxCn%2FFoIu1p4rWNhTQJ4DIOODpSSInYoPJqkpI2KqP1atIW9g6Q7fZsAtvzRdcOGOc2dhM2KRFaPwT6XNn7ugWHZ9dDx7Ee2XOX%2FtkMNOq1tQGOqUBgczI0EukiaOwVD%2F%2F6mu9u8aVr%2FJVix4%2FhJSgJT8IxIjm1vQ%2FdFYHU%2FlRI5RAJDCS3guj8F8OgvJL3Wbcj%2F00IOAFZ%2BHXxxU%2BJyZKwTnyPtBEIwarX8XtxqgZfRcAy0lTD%2Fod4DhCDvgfD2Np925E48%2BlR1DPa%2Bhm8lhhaPglzzazZUUCewnCu%2BJAFt0HHJRcPCTvF6IidC8R8%2FyNrSUb8Lk0R%2BNL&X-Amz-Signature=c1138fe95557c50a346d9af81ed5d4114d0cab98bbbe99e4bc006e0864be5370&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

连接建立后，界面会变成这样。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/63247ba5-0aa1-47c6-bb5e-d878adca18c9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSZNDVSN%2F20260831%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260831T155042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIETaZa3T4TKkLPL6%2FSEIVjDa6LK6Pe1rbx9plr%2B3Cz4iAiEA0Fae%2FrWDk6mmhKPglb6GH%2BKlpKXDKehYXKO8pBxT5XMqiAQImP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM%2FegE6tPUp%2BWV3O5yrcAzrXOXvkAXEPpYY2CWB4TTJuLuz6T6FBsyoKI%2FuYPZIapOhSEe6VyEY7To4N5Dx2YkLnMCLO7ogRZkBw8Ru89hWCggEfsdPyDV9ELyF1ZvGh2kJhkil12q314tQ9zzDaK4IZaEwwHaWSmRRbRymAmyGl%2FAyCZmsXRQEy7opSZojprC6zefV2ArBB7iuFjNCg%2BD5NlhjpFSL5HAEr1rgzE6KZEearWcEXn3H88Yp1yzKJIMMUNMH94kzFFxm099hxHJRNekxDfwNiUuwvFg4WWHqLRl3xwPT8KiKzgxhRYJ1qayTsRoKhhzUi2Mu3uh3OjaV%2BJRHLSwjjpfJVof5%2BT2nr1qW5vi6LBGTZAyAa0LBX5DK5Rak22vcXqucVseHNfkdw3Dx1XfAlwgenJ%2BjS9s11hLaRjebGRvi0XdvvvBkDQM2WlnHRMC6vPyBhnhBeVU8rzToyHkyt4sg9IzKjsadIpVyK3RNcj8x2ppDAQOTztv5LEcN0dZ%2FVZFzKX6S2iV69A%2FPkV0K%2BVi5so1DsKlmxCn%2FFoIu1p4rWNhTQJ4DIOODpSSInYoPJqkpI2KqP1atIW9g6Q7fZsAtvzRdcOGOc2dhM2KRFaPwT6XNn7ugWHZ9dDx7Ee2XOX%2FtkMNOq1tQGOqUBgczI0EukiaOwVD%2F%2F6mu9u8aVr%2FJVix4%2FhJSgJT8IxIjm1vQ%2FdFYHU%2FlRI5RAJDCS3guj8F8OgvJL3Wbcj%2F00IOAFZ%2BHXxxU%2BJyZKwTnyPtBEIwarX8XtxqgZfRcAy0lTD%2Fod4DhCDvgfD2Np925E48%2BlR1DPa%2Bhm8lhhaPglzzazZUUCewnCu%2BJAFt0HHJRcPCTvF6IidC8R8%2FyNrSUb8Lk0R%2BNL&X-Amz-Signature=42b6b83456dfb1f85a2d283b16b39ab46a8f4fb6833d45250055e0cc6f7517bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们首先点击 "工具 "按钮，然后选择 "列表工具"，检查我们所使用的工具。然后运行。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/dd91f8d0-b87a-419a-aec0-ceb20c207b9a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSZNDVSN%2F20260831%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260831T155042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIETaZa3T4TKkLPL6%2FSEIVjDa6LK6Pe1rbx9plr%2B3Cz4iAiEA0Fae%2FrWDk6mmhKPglb6GH%2BKlpKXDKehYXKO8pBxT5XMqiAQImP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM%2FegE6tPUp%2BWV3O5yrcAzrXOXvkAXEPpYY2CWB4TTJuLuz6T6FBsyoKI%2FuYPZIapOhSEe6VyEY7To4N5Dx2YkLnMCLO7ogRZkBw8Ru89hWCggEfsdPyDV9ELyF1ZvGh2kJhkil12q314tQ9zzDaK4IZaEwwHaWSmRRbRymAmyGl%2FAyCZmsXRQEy7opSZojprC6zefV2ArBB7iuFjNCg%2BD5NlhjpFSL5HAEr1rgzE6KZEearWcEXn3H88Yp1yzKJIMMUNMH94kzFFxm099hxHJRNekxDfwNiUuwvFg4WWHqLRl3xwPT8KiKzgxhRYJ1qayTsRoKhhzUi2Mu3uh3OjaV%2BJRHLSwjjpfJVof5%2BT2nr1qW5vi6LBGTZAyAa0LBX5DK5Rak22vcXqucVseHNfkdw3Dx1XfAlwgenJ%2BjS9s11hLaRjebGRvi0XdvvvBkDQM2WlnHRMC6vPyBhnhBeVU8rzToyHkyt4sg9IzKjsadIpVyK3RNcj8x2ppDAQOTztv5LEcN0dZ%2FVZFzKX6S2iV69A%2FPkV0K%2BVi5so1DsKlmxCn%2FFoIu1p4rWNhTQJ4DIOODpSSInYoPJqkpI2KqP1atIW9g6Q7fZsAtvzRdcOGOc2dhM2KRFaPwT6XNn7ugWHZ9dDx7Ee2XOX%2FtkMNOq1tQGOqUBgczI0EukiaOwVD%2F%2F6mu9u8aVr%2FJVix4%2FhJSgJT8IxIjm1vQ%2FdFYHU%2FlRI5RAJDCS3guj8F8OgvJL3Wbcj%2F00IOAFZ%2BHXxxU%2BJyZKwTnyPtBEIwarX8XtxqgZfRcAy0lTD%2Fod4DhCDvgfD2Np925E48%2BlR1DPa%2Bhm8lhhaPglzzazZUUCewnCu%2BJAFt0HHJRcPCTvF6IidC8R8%2FyNrSUb8Lk0R%2BNL&X-Amz-Signature=65c0114db0e3d6ed1c5e983652dfbef200f0b58564a83f15806dd5df68b6e131&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果工具执行成功，就会看到如下界面的结果。那么你就成功运行了一个 mcp 工具。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/70e0fd59-96fd-4056-9142-dc77071a18bf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSZNDVSN%2F20260831%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260831T155042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIETaZa3T4TKkLPL6%2FSEIVjDa6LK6Pe1rbx9plr%2B3Cz4iAiEA0Fae%2FrWDk6mmhKPglb6GH%2BKlpKXDKehYXKO8pBxT5XMqiAQImP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM%2FegE6tPUp%2BWV3O5yrcAzrXOXvkAXEPpYY2CWB4TTJuLuz6T6FBsyoKI%2FuYPZIapOhSEe6VyEY7To4N5Dx2YkLnMCLO7ogRZkBw8Ru89hWCggEfsdPyDV9ELyF1ZvGh2kJhkil12q314tQ9zzDaK4IZaEwwHaWSmRRbRymAmyGl%2FAyCZmsXRQEy7opSZojprC6zefV2ArBB7iuFjNCg%2BD5NlhjpFSL5HAEr1rgzE6KZEearWcEXn3H88Yp1yzKJIMMUNMH94kzFFxm099hxHJRNekxDfwNiUuwvFg4WWHqLRl3xwPT8KiKzgxhRYJ1qayTsRoKhhzUi2Mu3uh3OjaV%2BJRHLSwjjpfJVof5%2BT2nr1qW5vi6LBGTZAyAa0LBX5DK5Rak22vcXqucVseHNfkdw3Dx1XfAlwgenJ%2BjS9s11hLaRjebGRvi0XdvvvBkDQM2WlnHRMC6vPyBhnhBeVU8rzToyHkyt4sg9IzKjsadIpVyK3RNcj8x2ppDAQOTztv5LEcN0dZ%2FVZFzKX6S2iV69A%2FPkV0K%2BVi5so1DsKlmxCn%2FFoIu1p4rWNhTQJ4DIOODpSSInYoPJqkpI2KqP1atIW9g6Q7fZsAtvzRdcOGOc2dhM2KRFaPwT6XNn7ugWHZ9dDx7Ee2XOX%2FtkMNOq1tQGOqUBgczI0EukiaOwVD%2F%2F6mu9u8aVr%2FJVix4%2FhJSgJT8IxIjm1vQ%2FdFYHU%2FlRI5RAJDCS3guj8F8OgvJL3Wbcj%2F00IOAFZ%2BHXxxU%2BJyZKwTnyPtBEIwarX8XtxqgZfRcAy0lTD%2Fod4DhCDvgfD2Np925E48%2BlR1DPa%2Bhm8lhhaPglzzazZUUCewnCu%2BJAFt0HHJRcPCTvF6IidC8R8%2FyNrSUb8Lk0R%2BNL&X-Amz-Signature=ee9aea7206567ac4038f7e1cbf3d67e9bc14e81f0eee787adb28fd50f4b05ec9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/129cc91e-3fce-4702-9189-a7d04991a5d4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSZNDVSN%2F20260831%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260831T155042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIETaZa3T4TKkLPL6%2FSEIVjDa6LK6Pe1rbx9plr%2B3Cz4iAiEA0Fae%2FrWDk6mmhKPglb6GH%2BKlpKXDKehYXKO8pBxT5XMqiAQImP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM%2FegE6tPUp%2BWV3O5yrcAzrXOXvkAXEPpYY2CWB4TTJuLuz6T6FBsyoKI%2FuYPZIapOhSEe6VyEY7To4N5Dx2YkLnMCLO7ogRZkBw8Ru89hWCggEfsdPyDV9ELyF1ZvGh2kJhkil12q314tQ9zzDaK4IZaEwwHaWSmRRbRymAmyGl%2FAyCZmsXRQEy7opSZojprC6zefV2ArBB7iuFjNCg%2BD5NlhjpFSL5HAEr1rgzE6KZEearWcEXn3H88Yp1yzKJIMMUNMH94kzFFxm099hxHJRNekxDfwNiUuwvFg4WWHqLRl3xwPT8KiKzgxhRYJ1qayTsRoKhhzUi2Mu3uh3OjaV%2BJRHLSwjjpfJVof5%2BT2nr1qW5vi6LBGTZAyAa0LBX5DK5Rak22vcXqucVseHNfkdw3Dx1XfAlwgenJ%2BjS9s11hLaRjebGRvi0XdvvvBkDQM2WlnHRMC6vPyBhnhBeVU8rzToyHkyt4sg9IzKjsadIpVyK3RNcj8x2ppDAQOTztv5LEcN0dZ%2FVZFzKX6S2iV69A%2FPkV0K%2BVi5so1DsKlmxCn%2FFoIu1p4rWNhTQJ4DIOODpSSInYoPJqkpI2KqP1atIW9g6Q7fZsAtvzRdcOGOc2dhM2KRFaPwT6XNn7ugWHZ9dDx7Ee2XOX%2FtkMNOq1tQGOqUBgczI0EukiaOwVD%2F%2F6mu9u8aVr%2FJVix4%2FhJSgJT8IxIjm1vQ%2FdFYHU%2FlRI5RAJDCS3guj8F8OgvJL3Wbcj%2F00IOAFZ%2BHXxxU%2BJyZKwTnyPtBEIwarX8XtxqgZfRcAy0lTD%2Fod4DhCDvgfD2Np925E48%2BlR1DPa%2Bhm8lhhaPglzzazZUUCewnCu%2BJAFt0HHJRcPCTvF6IidC8R8%2FyNrSUb8Lk0R%2BNL&X-Amz-Signature=f716b374c510e696b802716d7173aa04f3b2cbf998b6674ca037deb03a164a02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
