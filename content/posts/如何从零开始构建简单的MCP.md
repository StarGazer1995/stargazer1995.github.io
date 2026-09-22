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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7f0e8a0b-c4e1-4f01-9374-57601ba10ab2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QW725ZG2%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T235502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlg2NoJ6J2Q8FfU%2BoNJSS%2B9e8jbiro6wzhmP77XIQ3nQIhAIYP9IsnVXu9z3pmvPrQ2cZy5raBtpi2o1mWKWOyOvpJKogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzxB00RqZHedPQan7sq3ANrwa3PdVsH%2F2lqDGc%2BYKFFfEZ3bI5WNTfETVB2QNIbkFFU47NrW4yz3tDSl04iqFaRxQCideh%2Ft%2B84mJ1QbzyZLUBMvU%2BjgGDATMS9YSTxcnN2E4OqNSZ4g8KntiHJszEV%2B%2BXt64pV1BrHfYb5Kt7K2PAlVTlp3eyJdaANJAA%2BD3%2Fu%2FD3VZuhhYZSHeC6gtkIO9bZUkTm%2Fcgdn7hxF9emefbbNxWeKb4KFsf9MFd%2FqaN5wvHGSVmB2caNICH9%2BplGEc%2BU%2B60jXsjULJGs%2FnZOJKFFymsm5B0NcpZmuPDU3wwkktIxNQHXHGTjzSzkb5Z4cCil57Z06biHSjOK95eO70b%2Bbt8Dt0fydS%2Fsm%2BGUEvwPYn73kyiQTY4eALhRL4NSavUJhb6lO75sdjDDZiZZTszwL%2FCjIF4GifwSMmAOmus50BZRfk76UScO1vBQHiFYnSLVSDspIyTl1saUl%2BXM4oKmcDZP6o%2BkI60zKvyUTfZPt4fkGUvi4v7Vb8lx13NEBo%2FPOp9Pjt2dBPPgFRKyi4ri9oQKz2TesoRBd4OCJZHcB3SvIxtOvLS7TRKbfg%2BcbkQEmqwRuqFUuYtsbaR95BnxUeLY%2Bd8vsG%2FJH9cNtsoCyoUTNRLtXtt5g7TDe1MvVBjqkAaEJMf1CTBPm7iELUP6amuWtEkpjNiOtjCaTAz6YAXyDX8NU4iNZWida3oBqdHB57tH1XHav7xuDqX4JLZQ6KPn1Lf9krrjv1JcAnW3k2Ayt8GyRXWFnUUChtg7gxHn6qTnt4gJ%2BaQXu699C4egi4TyF%2FwIs2oAqJLWIiLNaB%2BSyY2tJD9UzIzfxAolLaIovt5%2BNI7P9Iz39kLwYdIcUCko%2BIGBM&X-Amz-Signature=a41141a9535d95eb836212c39d6935c17617c85ce2449bad72c9cd727e0e9740&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/1daf1736-35f7-48c2-9156-c98068ca2637/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QW725ZG2%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T235502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlg2NoJ6J2Q8FfU%2BoNJSS%2B9e8jbiro6wzhmP77XIQ3nQIhAIYP9IsnVXu9z3pmvPrQ2cZy5raBtpi2o1mWKWOyOvpJKogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzxB00RqZHedPQan7sq3ANrwa3PdVsH%2F2lqDGc%2BYKFFfEZ3bI5WNTfETVB2QNIbkFFU47NrW4yz3tDSl04iqFaRxQCideh%2Ft%2B84mJ1QbzyZLUBMvU%2BjgGDATMS9YSTxcnN2E4OqNSZ4g8KntiHJszEV%2B%2BXt64pV1BrHfYb5Kt7K2PAlVTlp3eyJdaANJAA%2BD3%2Fu%2FD3VZuhhYZSHeC6gtkIO9bZUkTm%2Fcgdn7hxF9emefbbNxWeKb4KFsf9MFd%2FqaN5wvHGSVmB2caNICH9%2BplGEc%2BU%2B60jXsjULJGs%2FnZOJKFFymsm5B0NcpZmuPDU3wwkktIxNQHXHGTjzSzkb5Z4cCil57Z06biHSjOK95eO70b%2Bbt8Dt0fydS%2Fsm%2BGUEvwPYn73kyiQTY4eALhRL4NSavUJhb6lO75sdjDDZiZZTszwL%2FCjIF4GifwSMmAOmus50BZRfk76UScO1vBQHiFYnSLVSDspIyTl1saUl%2BXM4oKmcDZP6o%2BkI60zKvyUTfZPt4fkGUvi4v7Vb8lx13NEBo%2FPOp9Pjt2dBPPgFRKyi4ri9oQKz2TesoRBd4OCJZHcB3SvIxtOvLS7TRKbfg%2BcbkQEmqwRuqFUuYtsbaR95BnxUeLY%2Bd8vsG%2FJH9cNtsoCyoUTNRLtXtt5g7TDe1MvVBjqkAaEJMf1CTBPm7iELUP6amuWtEkpjNiOtjCaTAz6YAXyDX8NU4iNZWida3oBqdHB57tH1XHav7xuDqX4JLZQ6KPn1Lf9krrjv1JcAnW3k2Ayt8GyRXWFnUUChtg7gxHn6qTnt4gJ%2BaQXu699C4egi4TyF%2FwIs2oAqJLWIiLNaB%2BSyY2tJD9UzIzfxAolLaIovt5%2BNI7P9Iz39kLwYdIcUCko%2BIGBM&X-Amz-Signature=2c62a0089e154d8f270d3d2334cdbb379bf99b23770e66014d91393474ff18f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这些信息告诉你，mcp inspector 正在 6274 端口运行，你可以通过它提供的 URL 链接访问。MCP inspector 是我们验证服务器是否起来的工具。我们不会花太多时间来介绍。

访问检查器服务器后，你会看到如下界面。点击左侧的连接按钮。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2ace1a7c-a49b-49f6-a297-fa126365c60a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QW725ZG2%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T235502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlg2NoJ6J2Q8FfU%2BoNJSS%2B9e8jbiro6wzhmP77XIQ3nQIhAIYP9IsnVXu9z3pmvPrQ2cZy5raBtpi2o1mWKWOyOvpJKogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzxB00RqZHedPQan7sq3ANrwa3PdVsH%2F2lqDGc%2BYKFFfEZ3bI5WNTfETVB2QNIbkFFU47NrW4yz3tDSl04iqFaRxQCideh%2Ft%2B84mJ1QbzyZLUBMvU%2BjgGDATMS9YSTxcnN2E4OqNSZ4g8KntiHJszEV%2B%2BXt64pV1BrHfYb5Kt7K2PAlVTlp3eyJdaANJAA%2BD3%2Fu%2FD3VZuhhYZSHeC6gtkIO9bZUkTm%2Fcgdn7hxF9emefbbNxWeKb4KFsf9MFd%2FqaN5wvHGSVmB2caNICH9%2BplGEc%2BU%2B60jXsjULJGs%2FnZOJKFFymsm5B0NcpZmuPDU3wwkktIxNQHXHGTjzSzkb5Z4cCil57Z06biHSjOK95eO70b%2Bbt8Dt0fydS%2Fsm%2BGUEvwPYn73kyiQTY4eALhRL4NSavUJhb6lO75sdjDDZiZZTszwL%2FCjIF4GifwSMmAOmus50BZRfk76UScO1vBQHiFYnSLVSDspIyTl1saUl%2BXM4oKmcDZP6o%2BkI60zKvyUTfZPt4fkGUvi4v7Vb8lx13NEBo%2FPOp9Pjt2dBPPgFRKyi4ri9oQKz2TesoRBd4OCJZHcB3SvIxtOvLS7TRKbfg%2BcbkQEmqwRuqFUuYtsbaR95BnxUeLY%2Bd8vsG%2FJH9cNtsoCyoUTNRLtXtt5g7TDe1MvVBjqkAaEJMf1CTBPm7iELUP6amuWtEkpjNiOtjCaTAz6YAXyDX8NU4iNZWida3oBqdHB57tH1XHav7xuDqX4JLZQ6KPn1Lf9krrjv1JcAnW3k2Ayt8GyRXWFnUUChtg7gxHn6qTnt4gJ%2BaQXu699C4egi4TyF%2FwIs2oAqJLWIiLNaB%2BSyY2tJD9UzIzfxAolLaIovt5%2BNI7P9Iz39kLwYdIcUCko%2BIGBM&X-Amz-Signature=061c96efeee9b90b10ab21062b123d255f4546d0a7290968b0bb1ad647a4adf8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

连接建立后，界面会变成这样。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/63247ba5-0aa1-47c6-bb5e-d878adca18c9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QW725ZG2%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T235502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlg2NoJ6J2Q8FfU%2BoNJSS%2B9e8jbiro6wzhmP77XIQ3nQIhAIYP9IsnVXu9z3pmvPrQ2cZy5raBtpi2o1mWKWOyOvpJKogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzxB00RqZHedPQan7sq3ANrwa3PdVsH%2F2lqDGc%2BYKFFfEZ3bI5WNTfETVB2QNIbkFFU47NrW4yz3tDSl04iqFaRxQCideh%2Ft%2B84mJ1QbzyZLUBMvU%2BjgGDATMS9YSTxcnN2E4OqNSZ4g8KntiHJszEV%2B%2BXt64pV1BrHfYb5Kt7K2PAlVTlp3eyJdaANJAA%2BD3%2Fu%2FD3VZuhhYZSHeC6gtkIO9bZUkTm%2Fcgdn7hxF9emefbbNxWeKb4KFsf9MFd%2FqaN5wvHGSVmB2caNICH9%2BplGEc%2BU%2B60jXsjULJGs%2FnZOJKFFymsm5B0NcpZmuPDU3wwkktIxNQHXHGTjzSzkb5Z4cCil57Z06biHSjOK95eO70b%2Bbt8Dt0fydS%2Fsm%2BGUEvwPYn73kyiQTY4eALhRL4NSavUJhb6lO75sdjDDZiZZTszwL%2FCjIF4GifwSMmAOmus50BZRfk76UScO1vBQHiFYnSLVSDspIyTl1saUl%2BXM4oKmcDZP6o%2BkI60zKvyUTfZPt4fkGUvi4v7Vb8lx13NEBo%2FPOp9Pjt2dBPPgFRKyi4ri9oQKz2TesoRBd4OCJZHcB3SvIxtOvLS7TRKbfg%2BcbkQEmqwRuqFUuYtsbaR95BnxUeLY%2Bd8vsG%2FJH9cNtsoCyoUTNRLtXtt5g7TDe1MvVBjqkAaEJMf1CTBPm7iELUP6amuWtEkpjNiOtjCaTAz6YAXyDX8NU4iNZWida3oBqdHB57tH1XHav7xuDqX4JLZQ6KPn1Lf9krrjv1JcAnW3k2Ayt8GyRXWFnUUChtg7gxHn6qTnt4gJ%2BaQXu699C4egi4TyF%2FwIs2oAqJLWIiLNaB%2BSyY2tJD9UzIzfxAolLaIovt5%2BNI7P9Iz39kLwYdIcUCko%2BIGBM&X-Amz-Signature=df0c6ae1612c0c41ac3f25efa878e3ad1fb43b5472eac8cda413787215813f12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们首先点击 "工具 "按钮，然后选择 "列表工具"，检查我们所使用的工具。然后运行。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/dd91f8d0-b87a-419a-aec0-ceb20c207b9a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QW725ZG2%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T235502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlg2NoJ6J2Q8FfU%2BoNJSS%2B9e8jbiro6wzhmP77XIQ3nQIhAIYP9IsnVXu9z3pmvPrQ2cZy5raBtpi2o1mWKWOyOvpJKogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzxB00RqZHedPQan7sq3ANrwa3PdVsH%2F2lqDGc%2BYKFFfEZ3bI5WNTfETVB2QNIbkFFU47NrW4yz3tDSl04iqFaRxQCideh%2Ft%2B84mJ1QbzyZLUBMvU%2BjgGDATMS9YSTxcnN2E4OqNSZ4g8KntiHJszEV%2B%2BXt64pV1BrHfYb5Kt7K2PAlVTlp3eyJdaANJAA%2BD3%2Fu%2FD3VZuhhYZSHeC6gtkIO9bZUkTm%2Fcgdn7hxF9emefbbNxWeKb4KFsf9MFd%2FqaN5wvHGSVmB2caNICH9%2BplGEc%2BU%2B60jXsjULJGs%2FnZOJKFFymsm5B0NcpZmuPDU3wwkktIxNQHXHGTjzSzkb5Z4cCil57Z06biHSjOK95eO70b%2Bbt8Dt0fydS%2Fsm%2BGUEvwPYn73kyiQTY4eALhRL4NSavUJhb6lO75sdjDDZiZZTszwL%2FCjIF4GifwSMmAOmus50BZRfk76UScO1vBQHiFYnSLVSDspIyTl1saUl%2BXM4oKmcDZP6o%2BkI60zKvyUTfZPt4fkGUvi4v7Vb8lx13NEBo%2FPOp9Pjt2dBPPgFRKyi4ri9oQKz2TesoRBd4OCJZHcB3SvIxtOvLS7TRKbfg%2BcbkQEmqwRuqFUuYtsbaR95BnxUeLY%2Bd8vsG%2FJH9cNtsoCyoUTNRLtXtt5g7TDe1MvVBjqkAaEJMf1CTBPm7iELUP6amuWtEkpjNiOtjCaTAz6YAXyDX8NU4iNZWida3oBqdHB57tH1XHav7xuDqX4JLZQ6KPn1Lf9krrjv1JcAnW3k2Ayt8GyRXWFnUUChtg7gxHn6qTnt4gJ%2BaQXu699C4egi4TyF%2FwIs2oAqJLWIiLNaB%2BSyY2tJD9UzIzfxAolLaIovt5%2BNI7P9Iz39kLwYdIcUCko%2BIGBM&X-Amz-Signature=9e5c0e43ca803281c2fe1d2b69d7ec2c4ab82864ff53796b5c65968d55d19532&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果工具执行成功，就会看到如下界面的结果。那么你就成功运行了一个 mcp 工具。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/70e0fd59-96fd-4056-9142-dc77071a18bf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QW725ZG2%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T235502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlg2NoJ6J2Q8FfU%2BoNJSS%2B9e8jbiro6wzhmP77XIQ3nQIhAIYP9IsnVXu9z3pmvPrQ2cZy5raBtpi2o1mWKWOyOvpJKogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzxB00RqZHedPQan7sq3ANrwa3PdVsH%2F2lqDGc%2BYKFFfEZ3bI5WNTfETVB2QNIbkFFU47NrW4yz3tDSl04iqFaRxQCideh%2Ft%2B84mJ1QbzyZLUBMvU%2BjgGDATMS9YSTxcnN2E4OqNSZ4g8KntiHJszEV%2B%2BXt64pV1BrHfYb5Kt7K2PAlVTlp3eyJdaANJAA%2BD3%2Fu%2FD3VZuhhYZSHeC6gtkIO9bZUkTm%2Fcgdn7hxF9emefbbNxWeKb4KFsf9MFd%2FqaN5wvHGSVmB2caNICH9%2BplGEc%2BU%2B60jXsjULJGs%2FnZOJKFFymsm5B0NcpZmuPDU3wwkktIxNQHXHGTjzSzkb5Z4cCil57Z06biHSjOK95eO70b%2Bbt8Dt0fydS%2Fsm%2BGUEvwPYn73kyiQTY4eALhRL4NSavUJhb6lO75sdjDDZiZZTszwL%2FCjIF4GifwSMmAOmus50BZRfk76UScO1vBQHiFYnSLVSDspIyTl1saUl%2BXM4oKmcDZP6o%2BkI60zKvyUTfZPt4fkGUvi4v7Vb8lx13NEBo%2FPOp9Pjt2dBPPgFRKyi4ri9oQKz2TesoRBd4OCJZHcB3SvIxtOvLS7TRKbfg%2BcbkQEmqwRuqFUuYtsbaR95BnxUeLY%2Bd8vsG%2FJH9cNtsoCyoUTNRLtXtt5g7TDe1MvVBjqkAaEJMf1CTBPm7iELUP6amuWtEkpjNiOtjCaTAz6YAXyDX8NU4iNZWida3oBqdHB57tH1XHav7xuDqX4JLZQ6KPn1Lf9krrjv1JcAnW3k2Ayt8GyRXWFnUUChtg7gxHn6qTnt4gJ%2BaQXu699C4egi4TyF%2FwIs2oAqJLWIiLNaB%2BSyY2tJD9UzIzfxAolLaIovt5%2BNI7P9Iz39kLwYdIcUCko%2BIGBM&X-Amz-Signature=f06ad778737b1a26f5ea318b00b5fb06bef8ee24889823317d86903ad3fa8fad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/129cc91e-3fce-4702-9189-a7d04991a5d4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QW725ZG2%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T235502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlg2NoJ6J2Q8FfU%2BoNJSS%2B9e8jbiro6wzhmP77XIQ3nQIhAIYP9IsnVXu9z3pmvPrQ2cZy5raBtpi2o1mWKWOyOvpJKogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzxB00RqZHedPQan7sq3ANrwa3PdVsH%2F2lqDGc%2BYKFFfEZ3bI5WNTfETVB2QNIbkFFU47NrW4yz3tDSl04iqFaRxQCideh%2Ft%2B84mJ1QbzyZLUBMvU%2BjgGDATMS9YSTxcnN2E4OqNSZ4g8KntiHJszEV%2B%2BXt64pV1BrHfYb5Kt7K2PAlVTlp3eyJdaANJAA%2BD3%2Fu%2FD3VZuhhYZSHeC6gtkIO9bZUkTm%2Fcgdn7hxF9emefbbNxWeKb4KFsf9MFd%2FqaN5wvHGSVmB2caNICH9%2BplGEc%2BU%2B60jXsjULJGs%2FnZOJKFFymsm5B0NcpZmuPDU3wwkktIxNQHXHGTjzSzkb5Z4cCil57Z06biHSjOK95eO70b%2Bbt8Dt0fydS%2Fsm%2BGUEvwPYn73kyiQTY4eALhRL4NSavUJhb6lO75sdjDDZiZZTszwL%2FCjIF4GifwSMmAOmus50BZRfk76UScO1vBQHiFYnSLVSDspIyTl1saUl%2BXM4oKmcDZP6o%2BkI60zKvyUTfZPt4fkGUvi4v7Vb8lx13NEBo%2FPOp9Pjt2dBPPgFRKyi4ri9oQKz2TesoRBd4OCJZHcB3SvIxtOvLS7TRKbfg%2BcbkQEmqwRuqFUuYtsbaR95BnxUeLY%2Bd8vsG%2FJH9cNtsoCyoUTNRLtXtt5g7TDe1MvVBjqkAaEJMf1CTBPm7iELUP6amuWtEkpjNiOtjCaTAz6YAXyDX8NU4iNZWida3oBqdHB57tH1XHav7xuDqX4JLZQ6KPn1Lf9krrjv1JcAnW3k2Ayt8GyRXWFnUUChtg7gxHn6qTnt4gJ%2BaQXu699C4egi4TyF%2FwIs2oAqJLWIiLNaB%2BSyY2tJD9UzIzfxAolLaIovt5%2BNI7P9Iz39kLwYdIcUCko%2BIGBM&X-Amz-Signature=82fd6f0b001a185fd29b255a8fc1d6a172a1c5c04f6f78a6def2d87893c9c895&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
