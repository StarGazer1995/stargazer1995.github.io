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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7f0e8a0b-c4e1-4f01-9374-57601ba10ab2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7M2NKNB%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T015408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIH%2FW6NekVkJPrgtKClpA0EN%2FKwGBXDVHTCjN70IqpgnBAiEAwPBP9eCAeXT8l6qczWOeFoKuPMKOGGW27McTGjOsEiYqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL5B%2BhxTMBLZMQ55LyrcA8E4%2FyzsU81xZZpmgtHieURzAerblus0MMZUT3oguEBCD8z0aQWIHZkj3nUPGSu6NRzK0FAvngbhUZuLNVDTb8s2s9hsgCZumC5RGf1MtIirF0Jr%2BH3RmHSfD2HnasCmwSPPQejLZtZth3W%2B5ViWhvHYZuV2IBi4ugQ2lVuwLpMKgB8esb4eGnsyF05KjLlF5gXHBk%2B5F4eKUR5v%2BXyWxRboSYb%2FQP%2B6FH7fXj3umMbvxrnZ9HLQU5aBM9vRxPrX0FRoI1q%2FU3gx8ZX6U7i16oHX3epzapa8d2RzRiY46DKn3ZhHn1eJmb4SB0jRxOCX8%2FVfugRd7NHs%2FOl8lQ5x8V8BD67ViLPxwAc%2BOL1J41Yk1bSeVaYGS9NwH11du4Ed9kpV407GOnbKvetH6qE0GTj5Pmo9YAtPVE3NMIqlce3hGgwjn2yxfqiKkbs0TcOATfn1L3Y36a85Cq4d332fHYAGs5MZFvkk8DHC85btONxVlCXPWd0Wo2HzfIClZZ5ywOaLi6Erwc2u93EgFSh2nyKT6wHins%2BVXYSGcYVaskt8k9KcVmnNe%2FOvJ27n%2B3Gyh7jyJssKSiJd32sikYELSbqlTUNI8XHdLuJPJ095irUua77cX9gs5JdcGu0PMIf96NAGOqUBMh01xb2%2FNwGdOLiHBkw1ufMnKiKq4dUKoHWZahdZUHstKDtukNKgSrqvpLTKXChlrBsRqz3Ck20yRX%2Bh64FXDgr7iO3M0oDA3ZslpYNnR1uyWnc5mVLXfd3eN6lJ0F%2FHxxa%2FHXSL6HotVUVU28XXmwTY6mfqOX02eHHaY0Nn177nFzv31WQc%2B1Lnew%2BUa40N1s2JjFOO86%2B8zi5x79E05vGWOE%2Bb&X-Amz-Signature=2420f4a19f8889ed991e4606ddc6d68dafe6faba4bfb54d1f3cbedbb2213294b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/1daf1736-35f7-48c2-9156-c98068ca2637/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7M2NKNB%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T015408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIH%2FW6NekVkJPrgtKClpA0EN%2FKwGBXDVHTCjN70IqpgnBAiEAwPBP9eCAeXT8l6qczWOeFoKuPMKOGGW27McTGjOsEiYqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL5B%2BhxTMBLZMQ55LyrcA8E4%2FyzsU81xZZpmgtHieURzAerblus0MMZUT3oguEBCD8z0aQWIHZkj3nUPGSu6NRzK0FAvngbhUZuLNVDTb8s2s9hsgCZumC5RGf1MtIirF0Jr%2BH3RmHSfD2HnasCmwSPPQejLZtZth3W%2B5ViWhvHYZuV2IBi4ugQ2lVuwLpMKgB8esb4eGnsyF05KjLlF5gXHBk%2B5F4eKUR5v%2BXyWxRboSYb%2FQP%2B6FH7fXj3umMbvxrnZ9HLQU5aBM9vRxPrX0FRoI1q%2FU3gx8ZX6U7i16oHX3epzapa8d2RzRiY46DKn3ZhHn1eJmb4SB0jRxOCX8%2FVfugRd7NHs%2FOl8lQ5x8V8BD67ViLPxwAc%2BOL1J41Yk1bSeVaYGS9NwH11du4Ed9kpV407GOnbKvetH6qE0GTj5Pmo9YAtPVE3NMIqlce3hGgwjn2yxfqiKkbs0TcOATfn1L3Y36a85Cq4d332fHYAGs5MZFvkk8DHC85btONxVlCXPWd0Wo2HzfIClZZ5ywOaLi6Erwc2u93EgFSh2nyKT6wHins%2BVXYSGcYVaskt8k9KcVmnNe%2FOvJ27n%2B3Gyh7jyJssKSiJd32sikYELSbqlTUNI8XHdLuJPJ095irUua77cX9gs5JdcGu0PMIf96NAGOqUBMh01xb2%2FNwGdOLiHBkw1ufMnKiKq4dUKoHWZahdZUHstKDtukNKgSrqvpLTKXChlrBsRqz3Ck20yRX%2Bh64FXDgr7iO3M0oDA3ZslpYNnR1uyWnc5mVLXfd3eN6lJ0F%2FHxxa%2FHXSL6HotVUVU28XXmwTY6mfqOX02eHHaY0Nn177nFzv31WQc%2B1Lnew%2BUa40N1s2JjFOO86%2B8zi5x79E05vGWOE%2Bb&X-Amz-Signature=6591a8c20190994aec4b12621b9ee5592d33f000f78c9a719db912afa1dfb19f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这些信息告诉你，mcp inspector 正在 6274 端口运行，你可以通过它提供的 URL 链接访问。MCP inspector 是我们验证服务器是否起来的工具。我们不会花太多时间来介绍。

访问检查器服务器后，你会看到如下界面。点击左侧的连接按钮。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2ace1a7c-a49b-49f6-a297-fa126365c60a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7M2NKNB%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T015408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIH%2FW6NekVkJPrgtKClpA0EN%2FKwGBXDVHTCjN70IqpgnBAiEAwPBP9eCAeXT8l6qczWOeFoKuPMKOGGW27McTGjOsEiYqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL5B%2BhxTMBLZMQ55LyrcA8E4%2FyzsU81xZZpmgtHieURzAerblus0MMZUT3oguEBCD8z0aQWIHZkj3nUPGSu6NRzK0FAvngbhUZuLNVDTb8s2s9hsgCZumC5RGf1MtIirF0Jr%2BH3RmHSfD2HnasCmwSPPQejLZtZth3W%2B5ViWhvHYZuV2IBi4ugQ2lVuwLpMKgB8esb4eGnsyF05KjLlF5gXHBk%2B5F4eKUR5v%2BXyWxRboSYb%2FQP%2B6FH7fXj3umMbvxrnZ9HLQU5aBM9vRxPrX0FRoI1q%2FU3gx8ZX6U7i16oHX3epzapa8d2RzRiY46DKn3ZhHn1eJmb4SB0jRxOCX8%2FVfugRd7NHs%2FOl8lQ5x8V8BD67ViLPxwAc%2BOL1J41Yk1bSeVaYGS9NwH11du4Ed9kpV407GOnbKvetH6qE0GTj5Pmo9YAtPVE3NMIqlce3hGgwjn2yxfqiKkbs0TcOATfn1L3Y36a85Cq4d332fHYAGs5MZFvkk8DHC85btONxVlCXPWd0Wo2HzfIClZZ5ywOaLi6Erwc2u93EgFSh2nyKT6wHins%2BVXYSGcYVaskt8k9KcVmnNe%2FOvJ27n%2B3Gyh7jyJssKSiJd32sikYELSbqlTUNI8XHdLuJPJ095irUua77cX9gs5JdcGu0PMIf96NAGOqUBMh01xb2%2FNwGdOLiHBkw1ufMnKiKq4dUKoHWZahdZUHstKDtukNKgSrqvpLTKXChlrBsRqz3Ck20yRX%2Bh64FXDgr7iO3M0oDA3ZslpYNnR1uyWnc5mVLXfd3eN6lJ0F%2FHxxa%2FHXSL6HotVUVU28XXmwTY6mfqOX02eHHaY0Nn177nFzv31WQc%2B1Lnew%2BUa40N1s2JjFOO86%2B8zi5x79E05vGWOE%2Bb&X-Amz-Signature=990c9a47b5d3b78a7a46aacc0ad3d70096f90399df701c88cc52836dc032ae6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

连接建立后，界面会变成这样。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/63247ba5-0aa1-47c6-bb5e-d878adca18c9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7M2NKNB%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T015408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIH%2FW6NekVkJPrgtKClpA0EN%2FKwGBXDVHTCjN70IqpgnBAiEAwPBP9eCAeXT8l6qczWOeFoKuPMKOGGW27McTGjOsEiYqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL5B%2BhxTMBLZMQ55LyrcA8E4%2FyzsU81xZZpmgtHieURzAerblus0MMZUT3oguEBCD8z0aQWIHZkj3nUPGSu6NRzK0FAvngbhUZuLNVDTb8s2s9hsgCZumC5RGf1MtIirF0Jr%2BH3RmHSfD2HnasCmwSPPQejLZtZth3W%2B5ViWhvHYZuV2IBi4ugQ2lVuwLpMKgB8esb4eGnsyF05KjLlF5gXHBk%2B5F4eKUR5v%2BXyWxRboSYb%2FQP%2B6FH7fXj3umMbvxrnZ9HLQU5aBM9vRxPrX0FRoI1q%2FU3gx8ZX6U7i16oHX3epzapa8d2RzRiY46DKn3ZhHn1eJmb4SB0jRxOCX8%2FVfugRd7NHs%2FOl8lQ5x8V8BD67ViLPxwAc%2BOL1J41Yk1bSeVaYGS9NwH11du4Ed9kpV407GOnbKvetH6qE0GTj5Pmo9YAtPVE3NMIqlce3hGgwjn2yxfqiKkbs0TcOATfn1L3Y36a85Cq4d332fHYAGs5MZFvkk8DHC85btONxVlCXPWd0Wo2HzfIClZZ5ywOaLi6Erwc2u93EgFSh2nyKT6wHins%2BVXYSGcYVaskt8k9KcVmnNe%2FOvJ27n%2B3Gyh7jyJssKSiJd32sikYELSbqlTUNI8XHdLuJPJ095irUua77cX9gs5JdcGu0PMIf96NAGOqUBMh01xb2%2FNwGdOLiHBkw1ufMnKiKq4dUKoHWZahdZUHstKDtukNKgSrqvpLTKXChlrBsRqz3Ck20yRX%2Bh64FXDgr7iO3M0oDA3ZslpYNnR1uyWnc5mVLXfd3eN6lJ0F%2FHxxa%2FHXSL6HotVUVU28XXmwTY6mfqOX02eHHaY0Nn177nFzv31WQc%2B1Lnew%2BUa40N1s2JjFOO86%2B8zi5x79E05vGWOE%2Bb&X-Amz-Signature=4a25a337225755ce9220bb30df3634a0242cd70cd19b97b4a6b93c2bc3a7423b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们首先点击 "工具 "按钮，然后选择 "列表工具"，检查我们所使用的工具。然后运行。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/dd91f8d0-b87a-419a-aec0-ceb20c207b9a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7M2NKNB%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T015409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIH%2FW6NekVkJPrgtKClpA0EN%2FKwGBXDVHTCjN70IqpgnBAiEAwPBP9eCAeXT8l6qczWOeFoKuPMKOGGW27McTGjOsEiYqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL5B%2BhxTMBLZMQ55LyrcA8E4%2FyzsU81xZZpmgtHieURzAerblus0MMZUT3oguEBCD8z0aQWIHZkj3nUPGSu6NRzK0FAvngbhUZuLNVDTb8s2s9hsgCZumC5RGf1MtIirF0Jr%2BH3RmHSfD2HnasCmwSPPQejLZtZth3W%2B5ViWhvHYZuV2IBi4ugQ2lVuwLpMKgB8esb4eGnsyF05KjLlF5gXHBk%2B5F4eKUR5v%2BXyWxRboSYb%2FQP%2B6FH7fXj3umMbvxrnZ9HLQU5aBM9vRxPrX0FRoI1q%2FU3gx8ZX6U7i16oHX3epzapa8d2RzRiY46DKn3ZhHn1eJmb4SB0jRxOCX8%2FVfugRd7NHs%2FOl8lQ5x8V8BD67ViLPxwAc%2BOL1J41Yk1bSeVaYGS9NwH11du4Ed9kpV407GOnbKvetH6qE0GTj5Pmo9YAtPVE3NMIqlce3hGgwjn2yxfqiKkbs0TcOATfn1L3Y36a85Cq4d332fHYAGs5MZFvkk8DHC85btONxVlCXPWd0Wo2HzfIClZZ5ywOaLi6Erwc2u93EgFSh2nyKT6wHins%2BVXYSGcYVaskt8k9KcVmnNe%2FOvJ27n%2B3Gyh7jyJssKSiJd32sikYELSbqlTUNI8XHdLuJPJ095irUua77cX9gs5JdcGu0PMIf96NAGOqUBMh01xb2%2FNwGdOLiHBkw1ufMnKiKq4dUKoHWZahdZUHstKDtukNKgSrqvpLTKXChlrBsRqz3Ck20yRX%2Bh64FXDgr7iO3M0oDA3ZslpYNnR1uyWnc5mVLXfd3eN6lJ0F%2FHxxa%2FHXSL6HotVUVU28XXmwTY6mfqOX02eHHaY0Nn177nFzv31WQc%2B1Lnew%2BUa40N1s2JjFOO86%2B8zi5x79E05vGWOE%2Bb&X-Amz-Signature=f937184bdedc7074f9c235498a594c1e0268035cd95e231559d196b3239bbbe7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果工具执行成功，就会看到如下界面的结果。那么你就成功运行了一个 mcp 工具。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/70e0fd59-96fd-4056-9142-dc77071a18bf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7M2NKNB%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T015409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIH%2FW6NekVkJPrgtKClpA0EN%2FKwGBXDVHTCjN70IqpgnBAiEAwPBP9eCAeXT8l6qczWOeFoKuPMKOGGW27McTGjOsEiYqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL5B%2BhxTMBLZMQ55LyrcA8E4%2FyzsU81xZZpmgtHieURzAerblus0MMZUT3oguEBCD8z0aQWIHZkj3nUPGSu6NRzK0FAvngbhUZuLNVDTb8s2s9hsgCZumC5RGf1MtIirF0Jr%2BH3RmHSfD2HnasCmwSPPQejLZtZth3W%2B5ViWhvHYZuV2IBi4ugQ2lVuwLpMKgB8esb4eGnsyF05KjLlF5gXHBk%2B5F4eKUR5v%2BXyWxRboSYb%2FQP%2B6FH7fXj3umMbvxrnZ9HLQU5aBM9vRxPrX0FRoI1q%2FU3gx8ZX6U7i16oHX3epzapa8d2RzRiY46DKn3ZhHn1eJmb4SB0jRxOCX8%2FVfugRd7NHs%2FOl8lQ5x8V8BD67ViLPxwAc%2BOL1J41Yk1bSeVaYGS9NwH11du4Ed9kpV407GOnbKvetH6qE0GTj5Pmo9YAtPVE3NMIqlce3hGgwjn2yxfqiKkbs0TcOATfn1L3Y36a85Cq4d332fHYAGs5MZFvkk8DHC85btONxVlCXPWd0Wo2HzfIClZZ5ywOaLi6Erwc2u93EgFSh2nyKT6wHins%2BVXYSGcYVaskt8k9KcVmnNe%2FOvJ27n%2B3Gyh7jyJssKSiJd32sikYELSbqlTUNI8XHdLuJPJ095irUua77cX9gs5JdcGu0PMIf96NAGOqUBMh01xb2%2FNwGdOLiHBkw1ufMnKiKq4dUKoHWZahdZUHstKDtukNKgSrqvpLTKXChlrBsRqz3Ck20yRX%2Bh64FXDgr7iO3M0oDA3ZslpYNnR1uyWnc5mVLXfd3eN6lJ0F%2FHxxa%2FHXSL6HotVUVU28XXmwTY6mfqOX02eHHaY0Nn177nFzv31WQc%2B1Lnew%2BUa40N1s2JjFOO86%2B8zi5x79E05vGWOE%2Bb&X-Amz-Signature=f877e531d9c9b284f3d9f22966183a926493607f6dbc6769182ff92e5ee76385&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/129cc91e-3fce-4702-9189-a7d04991a5d4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7M2NKNB%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T015409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIH%2FW6NekVkJPrgtKClpA0EN%2FKwGBXDVHTCjN70IqpgnBAiEAwPBP9eCAeXT8l6qczWOeFoKuPMKOGGW27McTGjOsEiYqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL5B%2BhxTMBLZMQ55LyrcA8E4%2FyzsU81xZZpmgtHieURzAerblus0MMZUT3oguEBCD8z0aQWIHZkj3nUPGSu6NRzK0FAvngbhUZuLNVDTb8s2s9hsgCZumC5RGf1MtIirF0Jr%2BH3RmHSfD2HnasCmwSPPQejLZtZth3W%2B5ViWhvHYZuV2IBi4ugQ2lVuwLpMKgB8esb4eGnsyF05KjLlF5gXHBk%2B5F4eKUR5v%2BXyWxRboSYb%2FQP%2B6FH7fXj3umMbvxrnZ9HLQU5aBM9vRxPrX0FRoI1q%2FU3gx8ZX6U7i16oHX3epzapa8d2RzRiY46DKn3ZhHn1eJmb4SB0jRxOCX8%2FVfugRd7NHs%2FOl8lQ5x8V8BD67ViLPxwAc%2BOL1J41Yk1bSeVaYGS9NwH11du4Ed9kpV407GOnbKvetH6qE0GTj5Pmo9YAtPVE3NMIqlce3hGgwjn2yxfqiKkbs0TcOATfn1L3Y36a85Cq4d332fHYAGs5MZFvkk8DHC85btONxVlCXPWd0Wo2HzfIClZZ5ywOaLi6Erwc2u93EgFSh2nyKT6wHins%2BVXYSGcYVaskt8k9KcVmnNe%2FOvJ27n%2B3Gyh7jyJssKSiJd32sikYELSbqlTUNI8XHdLuJPJ095irUua77cX9gs5JdcGu0PMIf96NAGOqUBMh01xb2%2FNwGdOLiHBkw1ufMnKiKq4dUKoHWZahdZUHstKDtukNKgSrqvpLTKXChlrBsRqz3Ck20yRX%2Bh64FXDgr7iO3M0oDA3ZslpYNnR1uyWnc5mVLXfd3eN6lJ0F%2FHxxa%2FHXSL6HotVUVU28XXmwTY6mfqOX02eHHaY0Nn177nFzv31WQc%2B1Lnew%2BUa40N1s2JjFOO86%2B8zi5x79E05vGWOE%2Bb&X-Amz-Signature=ae0603d80a09c0a40688eaa477d12c7372135a4a000e98b5d5898ebfc7972384&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
