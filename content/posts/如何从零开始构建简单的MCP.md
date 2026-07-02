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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7f0e8a0b-c4e1-4f01-9374-57601ba10ab2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIXAVMY4%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T190705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJFMEMCH2pFXK5SfoYMQLMEtiPSqOYt4Pl%2FQyHMs0UxN%2FaWsdkCIF1BMNUv4YOR59og9TrXypSRcPl%2Bi61F6q0Nnz05PZTIKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igye9ASCJ3HCurVMZwYq3APO4vY8GugaIMvUo0Q%2FEq1pqRGqS3RaI39T%2BEC%2FFEmTSgZH4IOrqqmOG6%2FnjQQxv60L%2BA9qc2VtH5zLq44EZZ%2FAA2mH0tzhnhS3gp%2FjY0B38Q%2FKhvPRPSG99M5eZMzNbAKJgJUJs3PTnnfSPzuCNEgBidb7kom1Z3liDnP2DrtDSj2%2FGnHGoD%2FQAXE8seI7QPSHAjZGdwzT0L1qeO5sDF7Im3wYn1YxnMcVkEpF3ooLaYKm73%2BQDZQXsP4ORPYRs5RXlu9JIW2q5oplfPSc3hs5txa2Qa%2FwIwxvkg3mti%2BjKxcGz8krrUlEI7olr227%2BxtaiM1LpQsb39VtwpysKyNdzO1CEZ8glPdM0tf0biXNDIXWV3Ykiiymfemc%2FshNrNI5l5f3XVhREqE5IS8gNVyY5LFWwJOImV7ME4C5tGdPjfEQT5xp8iYr37O8oTSIGmix9fQMJwVAK9kDUNscklSVidXqgakwNOZeJXN31nKwIkS2mBjIyVYyWEiUZOhrVef4qJnyFUAV9koYrgmwgY7djtp4UsRjn%2FwzuIJITan0U7LMPzharjrTVBkO%2Bi7MXCBubl1vMATCod2%2FL%2FZ%2FZvObJWDNP6xRvuifehHkuLz7FhEKTonqBV4iOFQhfzDowprSBjqnAUOMq0HAG8ny0Mwq8Pug43ZI2oH5g%2F1d2Wb4wGiNwnDN%2FBUNZTtppHsX2cgswhmit4n%2BK7YMmmlnlx%2FY9zLSx5Sy56%2FEckfORirKArGONsLMWNQkCuX3iUI92pheTcfg6h8mY95NkrjLWJa1xICpe3egNHUiDsgvs8BsXt%2B70FipYC%2FnCkJMeEs4MAwlUKp%2FT%2FaCouhOVuod4n55GdGaTndcMyVbZ6Qx&X-Amz-Signature=c34f1f0b8e2a571ccacb6972cff46c957142b2e0dcb16720f5bcf4f21eeaffa6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/1daf1736-35f7-48c2-9156-c98068ca2637/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIXAVMY4%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T190705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJFMEMCH2pFXK5SfoYMQLMEtiPSqOYt4Pl%2FQyHMs0UxN%2FaWsdkCIF1BMNUv4YOR59og9TrXypSRcPl%2Bi61F6q0Nnz05PZTIKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igye9ASCJ3HCurVMZwYq3APO4vY8GugaIMvUo0Q%2FEq1pqRGqS3RaI39T%2BEC%2FFEmTSgZH4IOrqqmOG6%2FnjQQxv60L%2BA9qc2VtH5zLq44EZZ%2FAA2mH0tzhnhS3gp%2FjY0B38Q%2FKhvPRPSG99M5eZMzNbAKJgJUJs3PTnnfSPzuCNEgBidb7kom1Z3liDnP2DrtDSj2%2FGnHGoD%2FQAXE8seI7QPSHAjZGdwzT0L1qeO5sDF7Im3wYn1YxnMcVkEpF3ooLaYKm73%2BQDZQXsP4ORPYRs5RXlu9JIW2q5oplfPSc3hs5txa2Qa%2FwIwxvkg3mti%2BjKxcGz8krrUlEI7olr227%2BxtaiM1LpQsb39VtwpysKyNdzO1CEZ8glPdM0tf0biXNDIXWV3Ykiiymfemc%2FshNrNI5l5f3XVhREqE5IS8gNVyY5LFWwJOImV7ME4C5tGdPjfEQT5xp8iYr37O8oTSIGmix9fQMJwVAK9kDUNscklSVidXqgakwNOZeJXN31nKwIkS2mBjIyVYyWEiUZOhrVef4qJnyFUAV9koYrgmwgY7djtp4UsRjn%2FwzuIJITan0U7LMPzharjrTVBkO%2Bi7MXCBubl1vMATCod2%2FL%2FZ%2FZvObJWDNP6xRvuifehHkuLz7FhEKTonqBV4iOFQhfzDowprSBjqnAUOMq0HAG8ny0Mwq8Pug43ZI2oH5g%2F1d2Wb4wGiNwnDN%2FBUNZTtppHsX2cgswhmit4n%2BK7YMmmlnlx%2FY9zLSx5Sy56%2FEckfORirKArGONsLMWNQkCuX3iUI92pheTcfg6h8mY95NkrjLWJa1xICpe3egNHUiDsgvs8BsXt%2B70FipYC%2FnCkJMeEs4MAwlUKp%2FT%2FaCouhOVuod4n55GdGaTndcMyVbZ6Qx&X-Amz-Signature=0ccf80e84e444d493320f2623e3223f18900f8ab45884752b6291165bed8c7bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这些信息告诉你，mcp inspector 正在 6274 端口运行，你可以通过它提供的 URL 链接访问。MCP inspector 是我们验证服务器是否起来的工具。我们不会花太多时间来介绍。

访问检查器服务器后，你会看到如下界面。点击左侧的连接按钮。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2ace1a7c-a49b-49f6-a297-fa126365c60a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIXAVMY4%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T190705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJFMEMCH2pFXK5SfoYMQLMEtiPSqOYt4Pl%2FQyHMs0UxN%2FaWsdkCIF1BMNUv4YOR59og9TrXypSRcPl%2Bi61F6q0Nnz05PZTIKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igye9ASCJ3HCurVMZwYq3APO4vY8GugaIMvUo0Q%2FEq1pqRGqS3RaI39T%2BEC%2FFEmTSgZH4IOrqqmOG6%2FnjQQxv60L%2BA9qc2VtH5zLq44EZZ%2FAA2mH0tzhnhS3gp%2FjY0B38Q%2FKhvPRPSG99M5eZMzNbAKJgJUJs3PTnnfSPzuCNEgBidb7kom1Z3liDnP2DrtDSj2%2FGnHGoD%2FQAXE8seI7QPSHAjZGdwzT0L1qeO5sDF7Im3wYn1YxnMcVkEpF3ooLaYKm73%2BQDZQXsP4ORPYRs5RXlu9JIW2q5oplfPSc3hs5txa2Qa%2FwIwxvkg3mti%2BjKxcGz8krrUlEI7olr227%2BxtaiM1LpQsb39VtwpysKyNdzO1CEZ8glPdM0tf0biXNDIXWV3Ykiiymfemc%2FshNrNI5l5f3XVhREqE5IS8gNVyY5LFWwJOImV7ME4C5tGdPjfEQT5xp8iYr37O8oTSIGmix9fQMJwVAK9kDUNscklSVidXqgakwNOZeJXN31nKwIkS2mBjIyVYyWEiUZOhrVef4qJnyFUAV9koYrgmwgY7djtp4UsRjn%2FwzuIJITan0U7LMPzharjrTVBkO%2Bi7MXCBubl1vMATCod2%2FL%2FZ%2FZvObJWDNP6xRvuifehHkuLz7FhEKTonqBV4iOFQhfzDowprSBjqnAUOMq0HAG8ny0Mwq8Pug43ZI2oH5g%2F1d2Wb4wGiNwnDN%2FBUNZTtppHsX2cgswhmit4n%2BK7YMmmlnlx%2FY9zLSx5Sy56%2FEckfORirKArGONsLMWNQkCuX3iUI92pheTcfg6h8mY95NkrjLWJa1xICpe3egNHUiDsgvs8BsXt%2B70FipYC%2FnCkJMeEs4MAwlUKp%2FT%2FaCouhOVuod4n55GdGaTndcMyVbZ6Qx&X-Amz-Signature=ef705aecbe310016515eb5fd6699865f63d8bbc3885313fadd864da9e20cb43e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

连接建立后，界面会变成这样。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/63247ba5-0aa1-47c6-bb5e-d878adca18c9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIXAVMY4%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T190705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJFMEMCH2pFXK5SfoYMQLMEtiPSqOYt4Pl%2FQyHMs0UxN%2FaWsdkCIF1BMNUv4YOR59og9TrXypSRcPl%2Bi61F6q0Nnz05PZTIKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igye9ASCJ3HCurVMZwYq3APO4vY8GugaIMvUo0Q%2FEq1pqRGqS3RaI39T%2BEC%2FFEmTSgZH4IOrqqmOG6%2FnjQQxv60L%2BA9qc2VtH5zLq44EZZ%2FAA2mH0tzhnhS3gp%2FjY0B38Q%2FKhvPRPSG99M5eZMzNbAKJgJUJs3PTnnfSPzuCNEgBidb7kom1Z3liDnP2DrtDSj2%2FGnHGoD%2FQAXE8seI7QPSHAjZGdwzT0L1qeO5sDF7Im3wYn1YxnMcVkEpF3ooLaYKm73%2BQDZQXsP4ORPYRs5RXlu9JIW2q5oplfPSc3hs5txa2Qa%2FwIwxvkg3mti%2BjKxcGz8krrUlEI7olr227%2BxtaiM1LpQsb39VtwpysKyNdzO1CEZ8glPdM0tf0biXNDIXWV3Ykiiymfemc%2FshNrNI5l5f3XVhREqE5IS8gNVyY5LFWwJOImV7ME4C5tGdPjfEQT5xp8iYr37O8oTSIGmix9fQMJwVAK9kDUNscklSVidXqgakwNOZeJXN31nKwIkS2mBjIyVYyWEiUZOhrVef4qJnyFUAV9koYrgmwgY7djtp4UsRjn%2FwzuIJITan0U7LMPzharjrTVBkO%2Bi7MXCBubl1vMATCod2%2FL%2FZ%2FZvObJWDNP6xRvuifehHkuLz7FhEKTonqBV4iOFQhfzDowprSBjqnAUOMq0HAG8ny0Mwq8Pug43ZI2oH5g%2F1d2Wb4wGiNwnDN%2FBUNZTtppHsX2cgswhmit4n%2BK7YMmmlnlx%2FY9zLSx5Sy56%2FEckfORirKArGONsLMWNQkCuX3iUI92pheTcfg6h8mY95NkrjLWJa1xICpe3egNHUiDsgvs8BsXt%2B70FipYC%2FnCkJMeEs4MAwlUKp%2FT%2FaCouhOVuod4n55GdGaTndcMyVbZ6Qx&X-Amz-Signature=48716b5bfe2dabcc475d1f6fb2f3aa7aa84f5f5882c4f6486401549a3d0837d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们首先点击 "工具 "按钮，然后选择 "列表工具"，检查我们所使用的工具。然后运行。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/dd91f8d0-b87a-419a-aec0-ceb20c207b9a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIXAVMY4%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T190705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJFMEMCH2pFXK5SfoYMQLMEtiPSqOYt4Pl%2FQyHMs0UxN%2FaWsdkCIF1BMNUv4YOR59og9TrXypSRcPl%2Bi61F6q0Nnz05PZTIKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igye9ASCJ3HCurVMZwYq3APO4vY8GugaIMvUo0Q%2FEq1pqRGqS3RaI39T%2BEC%2FFEmTSgZH4IOrqqmOG6%2FnjQQxv60L%2BA9qc2VtH5zLq44EZZ%2FAA2mH0tzhnhS3gp%2FjY0B38Q%2FKhvPRPSG99M5eZMzNbAKJgJUJs3PTnnfSPzuCNEgBidb7kom1Z3liDnP2DrtDSj2%2FGnHGoD%2FQAXE8seI7QPSHAjZGdwzT0L1qeO5sDF7Im3wYn1YxnMcVkEpF3ooLaYKm73%2BQDZQXsP4ORPYRs5RXlu9JIW2q5oplfPSc3hs5txa2Qa%2FwIwxvkg3mti%2BjKxcGz8krrUlEI7olr227%2BxtaiM1LpQsb39VtwpysKyNdzO1CEZ8glPdM0tf0biXNDIXWV3Ykiiymfemc%2FshNrNI5l5f3XVhREqE5IS8gNVyY5LFWwJOImV7ME4C5tGdPjfEQT5xp8iYr37O8oTSIGmix9fQMJwVAK9kDUNscklSVidXqgakwNOZeJXN31nKwIkS2mBjIyVYyWEiUZOhrVef4qJnyFUAV9koYrgmwgY7djtp4UsRjn%2FwzuIJITan0U7LMPzharjrTVBkO%2Bi7MXCBubl1vMATCod2%2FL%2FZ%2FZvObJWDNP6xRvuifehHkuLz7FhEKTonqBV4iOFQhfzDowprSBjqnAUOMq0HAG8ny0Mwq8Pug43ZI2oH5g%2F1d2Wb4wGiNwnDN%2FBUNZTtppHsX2cgswhmit4n%2BK7YMmmlnlx%2FY9zLSx5Sy56%2FEckfORirKArGONsLMWNQkCuX3iUI92pheTcfg6h8mY95NkrjLWJa1xICpe3egNHUiDsgvs8BsXt%2B70FipYC%2FnCkJMeEs4MAwlUKp%2FT%2FaCouhOVuod4n55GdGaTndcMyVbZ6Qx&X-Amz-Signature=cf4a43c573cd03dc8bb33e53d0be9a9d65b9f01aceb4c59473c046fc456afbae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果工具执行成功，就会看到如下界面的结果。那么你就成功运行了一个 mcp 工具。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/70e0fd59-96fd-4056-9142-dc77071a18bf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIXAVMY4%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T190705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJFMEMCH2pFXK5SfoYMQLMEtiPSqOYt4Pl%2FQyHMs0UxN%2FaWsdkCIF1BMNUv4YOR59og9TrXypSRcPl%2Bi61F6q0Nnz05PZTIKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igye9ASCJ3HCurVMZwYq3APO4vY8GugaIMvUo0Q%2FEq1pqRGqS3RaI39T%2BEC%2FFEmTSgZH4IOrqqmOG6%2FnjQQxv60L%2BA9qc2VtH5zLq44EZZ%2FAA2mH0tzhnhS3gp%2FjY0B38Q%2FKhvPRPSG99M5eZMzNbAKJgJUJs3PTnnfSPzuCNEgBidb7kom1Z3liDnP2DrtDSj2%2FGnHGoD%2FQAXE8seI7QPSHAjZGdwzT0L1qeO5sDF7Im3wYn1YxnMcVkEpF3ooLaYKm73%2BQDZQXsP4ORPYRs5RXlu9JIW2q5oplfPSc3hs5txa2Qa%2FwIwxvkg3mti%2BjKxcGz8krrUlEI7olr227%2BxtaiM1LpQsb39VtwpysKyNdzO1CEZ8glPdM0tf0biXNDIXWV3Ykiiymfemc%2FshNrNI5l5f3XVhREqE5IS8gNVyY5LFWwJOImV7ME4C5tGdPjfEQT5xp8iYr37O8oTSIGmix9fQMJwVAK9kDUNscklSVidXqgakwNOZeJXN31nKwIkS2mBjIyVYyWEiUZOhrVef4qJnyFUAV9koYrgmwgY7djtp4UsRjn%2FwzuIJITan0U7LMPzharjrTVBkO%2Bi7MXCBubl1vMATCod2%2FL%2FZ%2FZvObJWDNP6xRvuifehHkuLz7FhEKTonqBV4iOFQhfzDowprSBjqnAUOMq0HAG8ny0Mwq8Pug43ZI2oH5g%2F1d2Wb4wGiNwnDN%2FBUNZTtppHsX2cgswhmit4n%2BK7YMmmlnlx%2FY9zLSx5Sy56%2FEckfORirKArGONsLMWNQkCuX3iUI92pheTcfg6h8mY95NkrjLWJa1xICpe3egNHUiDsgvs8BsXt%2B70FipYC%2FnCkJMeEs4MAwlUKp%2FT%2FaCouhOVuod4n55GdGaTndcMyVbZ6Qx&X-Amz-Signature=622683774643861843815c8c6c9e55da6b10637b753005555dab06d87659ab20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/129cc91e-3fce-4702-9189-a7d04991a5d4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIXAVMY4%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T190705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJFMEMCH2pFXK5SfoYMQLMEtiPSqOYt4Pl%2FQyHMs0UxN%2FaWsdkCIF1BMNUv4YOR59og9TrXypSRcPl%2Bi61F6q0Nnz05PZTIKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igye9ASCJ3HCurVMZwYq3APO4vY8GugaIMvUo0Q%2FEq1pqRGqS3RaI39T%2BEC%2FFEmTSgZH4IOrqqmOG6%2FnjQQxv60L%2BA9qc2VtH5zLq44EZZ%2FAA2mH0tzhnhS3gp%2FjY0B38Q%2FKhvPRPSG99M5eZMzNbAKJgJUJs3PTnnfSPzuCNEgBidb7kom1Z3liDnP2DrtDSj2%2FGnHGoD%2FQAXE8seI7QPSHAjZGdwzT0L1qeO5sDF7Im3wYn1YxnMcVkEpF3ooLaYKm73%2BQDZQXsP4ORPYRs5RXlu9JIW2q5oplfPSc3hs5txa2Qa%2FwIwxvkg3mti%2BjKxcGz8krrUlEI7olr227%2BxtaiM1LpQsb39VtwpysKyNdzO1CEZ8glPdM0tf0biXNDIXWV3Ykiiymfemc%2FshNrNI5l5f3XVhREqE5IS8gNVyY5LFWwJOImV7ME4C5tGdPjfEQT5xp8iYr37O8oTSIGmix9fQMJwVAK9kDUNscklSVidXqgakwNOZeJXN31nKwIkS2mBjIyVYyWEiUZOhrVef4qJnyFUAV9koYrgmwgY7djtp4UsRjn%2FwzuIJITan0U7LMPzharjrTVBkO%2Bi7MXCBubl1vMATCod2%2FL%2FZ%2FZvObJWDNP6xRvuifehHkuLz7FhEKTonqBV4iOFQhfzDowprSBjqnAUOMq0HAG8ny0Mwq8Pug43ZI2oH5g%2F1d2Wb4wGiNwnDN%2FBUNZTtppHsX2cgswhmit4n%2BK7YMmmlnlx%2FY9zLSx5Sy56%2FEckfORirKArGONsLMWNQkCuX3iUI92pheTcfg6h8mY95NkrjLWJa1xICpe3egNHUiDsgvs8BsXt%2B70FipYC%2FnCkJMeEs4MAwlUKp%2FT%2FaCouhOVuod4n55GdGaTndcMyVbZ6Qx&X-Amz-Signature=fe6515bba5320c74a8dc24103a2e6aeeaa8f1dab249f9b3ff249be30d4a06edb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
