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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7f0e8a0b-c4e1-4f01-9374-57601ba10ab2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676RZZ3AP%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T154428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuLT4YUY5ulUn%2B5TSFjL%2FVMRbZASYLQJl7FyKHdhnRXgIhAKbKRFT9kR454QKlaffdVAqTm5WLHwBK58sKcGtwNfmwKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxlg4PCMHCEetGKGTMq3AP9fTY0bYZnTRS7nXvvwqER1Xim4l2BTyEfJCZmGTRhq%2BqT1kxnTRxLyrXI8BDR6YXjY34sUwF08x1btpm7Nshb9lvx0UhkVu1liRzkBovFPom6NcvAqzESuDTpeVuJ9Wmd2j16U9UCqEzCtBQYC6mBQkFqUhiU8yt0omeGbtTvZm7NQZhGKzzZmvVZjSd0kHwWUn3AWrmZGsbhaCbLUxHlMM0y1oAOWUqWX%2BuJ4ZXTJqApoANf2T8Noy5VlHyroUdS%2FFoupkymi7XBQVmGSrbFwyh880yaYQaE1eCNpzcU9H0YOruDssA3O4kN9HrkSPu29T0i%2FvaxF6t5yrVLTkqLmFYyDpROKxQPKCKZf54u0lKozayfkMkmlo0%2BaP9U3k4uCBwIsF4vioKsJXvp8SOc0w7XqEhpfu%2BsjzTzaYQes9fNYEbXO%2FoR6Oeo0iLTtM3KYeCQf6OwizVSN63cJYoMpduM4k9UyZV976gXW%2BELz3pCJwi43MoOmfi6VYKfUU6d6TLiyh0ys%2BiRTHVgREjgABZiiN3OHE6nUBey18C0i9vUoVLAyWiKu1cA4L51%2BXTE%2Fc7fxZ2cxwjnAkXROffB98NibI%2BkGlSEQfVWlgvPI8ROdYHV9qC0ISxsRTC74PjSBjqkAQYbnuCO9Vane2Qbn37XkAXbbiqTMJ7yuKV2zDd9t3YbjjBTQ5zpnp3p0sCWnszCKtzdwuCDx8li3o3sczCvGBXHwtq2nrUjM3ERPnTVyR4b8TdqbGOBgmkrO4jFjcBdnR37aPCrHJ0i80JLeRtzu0X5Jl6NAjKSoSHllV9Th0Zwn0E9a2vfe4QUkApa7Eqtba8LJGvfxHLi8XLLGMNcNdqwaWaG&X-Amz-Signature=6f68e34b5225a4c7f6574e361ec81aa001d1f504ab2ced4dba0cb2f7015b71c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/1daf1736-35f7-48c2-9156-c98068ca2637/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676RZZ3AP%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T154429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuLT4YUY5ulUn%2B5TSFjL%2FVMRbZASYLQJl7FyKHdhnRXgIhAKbKRFT9kR454QKlaffdVAqTm5WLHwBK58sKcGtwNfmwKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxlg4PCMHCEetGKGTMq3AP9fTY0bYZnTRS7nXvvwqER1Xim4l2BTyEfJCZmGTRhq%2BqT1kxnTRxLyrXI8BDR6YXjY34sUwF08x1btpm7Nshb9lvx0UhkVu1liRzkBovFPom6NcvAqzESuDTpeVuJ9Wmd2j16U9UCqEzCtBQYC6mBQkFqUhiU8yt0omeGbtTvZm7NQZhGKzzZmvVZjSd0kHwWUn3AWrmZGsbhaCbLUxHlMM0y1oAOWUqWX%2BuJ4ZXTJqApoANf2T8Noy5VlHyroUdS%2FFoupkymi7XBQVmGSrbFwyh880yaYQaE1eCNpzcU9H0YOruDssA3O4kN9HrkSPu29T0i%2FvaxF6t5yrVLTkqLmFYyDpROKxQPKCKZf54u0lKozayfkMkmlo0%2BaP9U3k4uCBwIsF4vioKsJXvp8SOc0w7XqEhpfu%2BsjzTzaYQes9fNYEbXO%2FoR6Oeo0iLTtM3KYeCQf6OwizVSN63cJYoMpduM4k9UyZV976gXW%2BELz3pCJwi43MoOmfi6VYKfUU6d6TLiyh0ys%2BiRTHVgREjgABZiiN3OHE6nUBey18C0i9vUoVLAyWiKu1cA4L51%2BXTE%2Fc7fxZ2cxwjnAkXROffB98NibI%2BkGlSEQfVWlgvPI8ROdYHV9qC0ISxsRTC74PjSBjqkAQYbnuCO9Vane2Qbn37XkAXbbiqTMJ7yuKV2zDd9t3YbjjBTQ5zpnp3p0sCWnszCKtzdwuCDx8li3o3sczCvGBXHwtq2nrUjM3ERPnTVyR4b8TdqbGOBgmkrO4jFjcBdnR37aPCrHJ0i80JLeRtzu0X5Jl6NAjKSoSHllV9Th0Zwn0E9a2vfe4QUkApa7Eqtba8LJGvfxHLi8XLLGMNcNdqwaWaG&X-Amz-Signature=145e9e79e0b3feb41ac4bcc29b15456df4eb073b88854abe348f183b553b1a7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这些信息告诉你，mcp inspector 正在 6274 端口运行，你可以通过它提供的 URL 链接访问。MCP inspector 是我们验证服务器是否起来的工具。我们不会花太多时间来介绍。

访问检查器服务器后，你会看到如下界面。点击左侧的连接按钮。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2ace1a7c-a49b-49f6-a297-fa126365c60a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676RZZ3AP%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T154429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuLT4YUY5ulUn%2B5TSFjL%2FVMRbZASYLQJl7FyKHdhnRXgIhAKbKRFT9kR454QKlaffdVAqTm5WLHwBK58sKcGtwNfmwKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxlg4PCMHCEetGKGTMq3AP9fTY0bYZnTRS7nXvvwqER1Xim4l2BTyEfJCZmGTRhq%2BqT1kxnTRxLyrXI8BDR6YXjY34sUwF08x1btpm7Nshb9lvx0UhkVu1liRzkBovFPom6NcvAqzESuDTpeVuJ9Wmd2j16U9UCqEzCtBQYC6mBQkFqUhiU8yt0omeGbtTvZm7NQZhGKzzZmvVZjSd0kHwWUn3AWrmZGsbhaCbLUxHlMM0y1oAOWUqWX%2BuJ4ZXTJqApoANf2T8Noy5VlHyroUdS%2FFoupkymi7XBQVmGSrbFwyh880yaYQaE1eCNpzcU9H0YOruDssA3O4kN9HrkSPu29T0i%2FvaxF6t5yrVLTkqLmFYyDpROKxQPKCKZf54u0lKozayfkMkmlo0%2BaP9U3k4uCBwIsF4vioKsJXvp8SOc0w7XqEhpfu%2BsjzTzaYQes9fNYEbXO%2FoR6Oeo0iLTtM3KYeCQf6OwizVSN63cJYoMpduM4k9UyZV976gXW%2BELz3pCJwi43MoOmfi6VYKfUU6d6TLiyh0ys%2BiRTHVgREjgABZiiN3OHE6nUBey18C0i9vUoVLAyWiKu1cA4L51%2BXTE%2Fc7fxZ2cxwjnAkXROffB98NibI%2BkGlSEQfVWlgvPI8ROdYHV9qC0ISxsRTC74PjSBjqkAQYbnuCO9Vane2Qbn37XkAXbbiqTMJ7yuKV2zDd9t3YbjjBTQ5zpnp3p0sCWnszCKtzdwuCDx8li3o3sczCvGBXHwtq2nrUjM3ERPnTVyR4b8TdqbGOBgmkrO4jFjcBdnR37aPCrHJ0i80JLeRtzu0X5Jl6NAjKSoSHllV9Th0Zwn0E9a2vfe4QUkApa7Eqtba8LJGvfxHLi8XLLGMNcNdqwaWaG&X-Amz-Signature=b94923a1cbe0e0a30d89496a3897fface2ec96f803fe1ae717163724ea00a0d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

连接建立后，界面会变成这样。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/63247ba5-0aa1-47c6-bb5e-d878adca18c9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676RZZ3AP%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T154429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuLT4YUY5ulUn%2B5TSFjL%2FVMRbZASYLQJl7FyKHdhnRXgIhAKbKRFT9kR454QKlaffdVAqTm5WLHwBK58sKcGtwNfmwKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxlg4PCMHCEetGKGTMq3AP9fTY0bYZnTRS7nXvvwqER1Xim4l2BTyEfJCZmGTRhq%2BqT1kxnTRxLyrXI8BDR6YXjY34sUwF08x1btpm7Nshb9lvx0UhkVu1liRzkBovFPom6NcvAqzESuDTpeVuJ9Wmd2j16U9UCqEzCtBQYC6mBQkFqUhiU8yt0omeGbtTvZm7NQZhGKzzZmvVZjSd0kHwWUn3AWrmZGsbhaCbLUxHlMM0y1oAOWUqWX%2BuJ4ZXTJqApoANf2T8Noy5VlHyroUdS%2FFoupkymi7XBQVmGSrbFwyh880yaYQaE1eCNpzcU9H0YOruDssA3O4kN9HrkSPu29T0i%2FvaxF6t5yrVLTkqLmFYyDpROKxQPKCKZf54u0lKozayfkMkmlo0%2BaP9U3k4uCBwIsF4vioKsJXvp8SOc0w7XqEhpfu%2BsjzTzaYQes9fNYEbXO%2FoR6Oeo0iLTtM3KYeCQf6OwizVSN63cJYoMpduM4k9UyZV976gXW%2BELz3pCJwi43MoOmfi6VYKfUU6d6TLiyh0ys%2BiRTHVgREjgABZiiN3OHE6nUBey18C0i9vUoVLAyWiKu1cA4L51%2BXTE%2Fc7fxZ2cxwjnAkXROffB98NibI%2BkGlSEQfVWlgvPI8ROdYHV9qC0ISxsRTC74PjSBjqkAQYbnuCO9Vane2Qbn37XkAXbbiqTMJ7yuKV2zDd9t3YbjjBTQ5zpnp3p0sCWnszCKtzdwuCDx8li3o3sczCvGBXHwtq2nrUjM3ERPnTVyR4b8TdqbGOBgmkrO4jFjcBdnR37aPCrHJ0i80JLeRtzu0X5Jl6NAjKSoSHllV9Th0Zwn0E9a2vfe4QUkApa7Eqtba8LJGvfxHLi8XLLGMNcNdqwaWaG&X-Amz-Signature=c68ae01e05d221c8cf55f30200b19a4c0cf8f25d8ea82454e160a17f3d0a3fd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们首先点击 "工具 "按钮，然后选择 "列表工具"，检查我们所使用的工具。然后运行。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/dd91f8d0-b87a-419a-aec0-ceb20c207b9a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676RZZ3AP%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T154429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuLT4YUY5ulUn%2B5TSFjL%2FVMRbZASYLQJl7FyKHdhnRXgIhAKbKRFT9kR454QKlaffdVAqTm5WLHwBK58sKcGtwNfmwKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxlg4PCMHCEetGKGTMq3AP9fTY0bYZnTRS7nXvvwqER1Xim4l2BTyEfJCZmGTRhq%2BqT1kxnTRxLyrXI8BDR6YXjY34sUwF08x1btpm7Nshb9lvx0UhkVu1liRzkBovFPom6NcvAqzESuDTpeVuJ9Wmd2j16U9UCqEzCtBQYC6mBQkFqUhiU8yt0omeGbtTvZm7NQZhGKzzZmvVZjSd0kHwWUn3AWrmZGsbhaCbLUxHlMM0y1oAOWUqWX%2BuJ4ZXTJqApoANf2T8Noy5VlHyroUdS%2FFoupkymi7XBQVmGSrbFwyh880yaYQaE1eCNpzcU9H0YOruDssA3O4kN9HrkSPu29T0i%2FvaxF6t5yrVLTkqLmFYyDpROKxQPKCKZf54u0lKozayfkMkmlo0%2BaP9U3k4uCBwIsF4vioKsJXvp8SOc0w7XqEhpfu%2BsjzTzaYQes9fNYEbXO%2FoR6Oeo0iLTtM3KYeCQf6OwizVSN63cJYoMpduM4k9UyZV976gXW%2BELz3pCJwi43MoOmfi6VYKfUU6d6TLiyh0ys%2BiRTHVgREjgABZiiN3OHE6nUBey18C0i9vUoVLAyWiKu1cA4L51%2BXTE%2Fc7fxZ2cxwjnAkXROffB98NibI%2BkGlSEQfVWlgvPI8ROdYHV9qC0ISxsRTC74PjSBjqkAQYbnuCO9Vane2Qbn37XkAXbbiqTMJ7yuKV2zDd9t3YbjjBTQ5zpnp3p0sCWnszCKtzdwuCDx8li3o3sczCvGBXHwtq2nrUjM3ERPnTVyR4b8TdqbGOBgmkrO4jFjcBdnR37aPCrHJ0i80JLeRtzu0X5Jl6NAjKSoSHllV9Th0Zwn0E9a2vfe4QUkApa7Eqtba8LJGvfxHLi8XLLGMNcNdqwaWaG&X-Amz-Signature=f4e8382d386ece6ae3cd43dbfe50c78739713a501f6472e4426988546a8e27be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果工具执行成功，就会看到如下界面的结果。那么你就成功运行了一个 mcp 工具。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/70e0fd59-96fd-4056-9142-dc77071a18bf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676RZZ3AP%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T154429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuLT4YUY5ulUn%2B5TSFjL%2FVMRbZASYLQJl7FyKHdhnRXgIhAKbKRFT9kR454QKlaffdVAqTm5WLHwBK58sKcGtwNfmwKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxlg4PCMHCEetGKGTMq3AP9fTY0bYZnTRS7nXvvwqER1Xim4l2BTyEfJCZmGTRhq%2BqT1kxnTRxLyrXI8BDR6YXjY34sUwF08x1btpm7Nshb9lvx0UhkVu1liRzkBovFPom6NcvAqzESuDTpeVuJ9Wmd2j16U9UCqEzCtBQYC6mBQkFqUhiU8yt0omeGbtTvZm7NQZhGKzzZmvVZjSd0kHwWUn3AWrmZGsbhaCbLUxHlMM0y1oAOWUqWX%2BuJ4ZXTJqApoANf2T8Noy5VlHyroUdS%2FFoupkymi7XBQVmGSrbFwyh880yaYQaE1eCNpzcU9H0YOruDssA3O4kN9HrkSPu29T0i%2FvaxF6t5yrVLTkqLmFYyDpROKxQPKCKZf54u0lKozayfkMkmlo0%2BaP9U3k4uCBwIsF4vioKsJXvp8SOc0w7XqEhpfu%2BsjzTzaYQes9fNYEbXO%2FoR6Oeo0iLTtM3KYeCQf6OwizVSN63cJYoMpduM4k9UyZV976gXW%2BELz3pCJwi43MoOmfi6VYKfUU6d6TLiyh0ys%2BiRTHVgREjgABZiiN3OHE6nUBey18C0i9vUoVLAyWiKu1cA4L51%2BXTE%2Fc7fxZ2cxwjnAkXROffB98NibI%2BkGlSEQfVWlgvPI8ROdYHV9qC0ISxsRTC74PjSBjqkAQYbnuCO9Vane2Qbn37XkAXbbiqTMJ7yuKV2zDd9t3YbjjBTQ5zpnp3p0sCWnszCKtzdwuCDx8li3o3sczCvGBXHwtq2nrUjM3ERPnTVyR4b8TdqbGOBgmkrO4jFjcBdnR37aPCrHJ0i80JLeRtzu0X5Jl6NAjKSoSHllV9Th0Zwn0E9a2vfe4QUkApa7Eqtba8LJGvfxHLi8XLLGMNcNdqwaWaG&X-Amz-Signature=d7fee878cd212fe6436e123528cefd91b1d4e17e7df9ae76db7aa13631698182&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/129cc91e-3fce-4702-9189-a7d04991a5d4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676RZZ3AP%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T154429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuLT4YUY5ulUn%2B5TSFjL%2FVMRbZASYLQJl7FyKHdhnRXgIhAKbKRFT9kR454QKlaffdVAqTm5WLHwBK58sKcGtwNfmwKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxlg4PCMHCEetGKGTMq3AP9fTY0bYZnTRS7nXvvwqER1Xim4l2BTyEfJCZmGTRhq%2BqT1kxnTRxLyrXI8BDR6YXjY34sUwF08x1btpm7Nshb9lvx0UhkVu1liRzkBovFPom6NcvAqzESuDTpeVuJ9Wmd2j16U9UCqEzCtBQYC6mBQkFqUhiU8yt0omeGbtTvZm7NQZhGKzzZmvVZjSd0kHwWUn3AWrmZGsbhaCbLUxHlMM0y1oAOWUqWX%2BuJ4ZXTJqApoANf2T8Noy5VlHyroUdS%2FFoupkymi7XBQVmGSrbFwyh880yaYQaE1eCNpzcU9H0YOruDssA3O4kN9HrkSPu29T0i%2FvaxF6t5yrVLTkqLmFYyDpROKxQPKCKZf54u0lKozayfkMkmlo0%2BaP9U3k4uCBwIsF4vioKsJXvp8SOc0w7XqEhpfu%2BsjzTzaYQes9fNYEbXO%2FoR6Oeo0iLTtM3KYeCQf6OwizVSN63cJYoMpduM4k9UyZV976gXW%2BELz3pCJwi43MoOmfi6VYKfUU6d6TLiyh0ys%2BiRTHVgREjgABZiiN3OHE6nUBey18C0i9vUoVLAyWiKu1cA4L51%2BXTE%2Fc7fxZ2cxwjnAkXROffB98NibI%2BkGlSEQfVWlgvPI8ROdYHV9qC0ISxsRTC74PjSBjqkAQYbnuCO9Vane2Qbn37XkAXbbiqTMJ7yuKV2zDd9t3YbjjBTQ5zpnp3p0sCWnszCKtzdwuCDx8li3o3sczCvGBXHwtq2nrUjM3ERPnTVyR4b8TdqbGOBgmkrO4jFjcBdnR37aPCrHJ0i80JLeRtzu0X5Jl6NAjKSoSHllV9Th0Zwn0E9a2vfe4QUkApa7Eqtba8LJGvfxHLi8XLLGMNcNdqwaWaG&X-Amz-Signature=6fd1321a2d763fcd9a4fec39439b3ebefe04516ecc97721ea6ba11334073483d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
