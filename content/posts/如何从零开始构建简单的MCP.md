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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7f0e8a0b-c4e1-4f01-9374-57601ba10ab2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZDC3M2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T152852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGg%2Bmtzeo4TxaiihT15%2FhuPEGdl5Ndvlv0c4i%2BrKI4OkAiEAhwQzZx%2BAL6L%2F4kCMfYzx%2B7MkBMXLXOdibu9QseiIUVAqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKAUdr0kjBk%2BQxqjySrcA1Dt4vkKjLcFKJ2SMdQXynf6gxaBk%2FXgNhrqkaBn1wap3eX1T6zH2Cqm6N%2F2QVggjVXhZPbDZLt5qAUiNQUmlVG89UV8rpLkMNecGUQkJMke%2FvU0h7ORsVHzqYYwqcA2SWaAvx5xUIX1w66kryoLaHQaDGpAhP9ebAjm9iQf5MdmPwLPWrbC%2FMqYlq29IqL08yEDJCPvO4QmVzl%2B8P9pVtDBy%2FHeL8tSEoELNWTZiVjVyCNDYxr25dLXd5jy1C4x42PYCQu%2Buzl9EQs0vlOysLUs0lOUmcrHVc6wumu7nSMNkQCZJdFP6Bl6J%2B5YNOp%2FN%2BFweWBFWlCPcLtwl21d6Lvljp7pAUaUXRsrH44Vu3oCIBRhtzfPV%2BXqW5qcwxEuTva1eZK%2FHuBPcZ%2F6hDhWBMDu4To25ci7%2FMQHdlFdvu3lTP1gg34p3ysfQHHBbgtgbx2n%2FkVJ6mXcHAXr6xVn%2BavedM0y5clkybW6DZny%2FOgQaCsUZREnyIZfT15lQn9SFBm3CP%2BbLi949eheebPUia9vAHqp%2BRGYpj%2BvnoTTcTA%2B%2BnLLChNTmmJkmW9V8shm3%2FmZwiAQOlfOGtm3acYbgZu7Iu0DMJMBkDnfchKo84BpvrBr2vWfHyGzKWxOMJr4%2FdIGOqUB0UhvIFB07pgcn9p0KhSyTkKLxW9ReoeN634PfEXRQRWTfHDZP8OLC9rvO86zdj1%2BaaQr2CaeD0IUue4X2FOpR95ePVRRrJByKSnL8Zjpu%2BgtcY3UBCSq7ihuEq4HcIoiPx2gH57xX1UWB1KxX5wx100R%2Fi8MYEhcPRTUr0N4gozs7bfhK1D5ieG9PDCNvSmOp2d2Syjyya7Tr%2BYNXdwhdhkaiNQH&X-Amz-Signature=4fdac54ce7e99966226b578968e357f09c7315ea1177f3fde4aa48ba213a7a25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/1daf1736-35f7-48c2-9156-c98068ca2637/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZDC3M2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T152852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGg%2Bmtzeo4TxaiihT15%2FhuPEGdl5Ndvlv0c4i%2BrKI4OkAiEAhwQzZx%2BAL6L%2F4kCMfYzx%2B7MkBMXLXOdibu9QseiIUVAqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKAUdr0kjBk%2BQxqjySrcA1Dt4vkKjLcFKJ2SMdQXynf6gxaBk%2FXgNhrqkaBn1wap3eX1T6zH2Cqm6N%2F2QVggjVXhZPbDZLt5qAUiNQUmlVG89UV8rpLkMNecGUQkJMke%2FvU0h7ORsVHzqYYwqcA2SWaAvx5xUIX1w66kryoLaHQaDGpAhP9ebAjm9iQf5MdmPwLPWrbC%2FMqYlq29IqL08yEDJCPvO4QmVzl%2B8P9pVtDBy%2FHeL8tSEoELNWTZiVjVyCNDYxr25dLXd5jy1C4x42PYCQu%2Buzl9EQs0vlOysLUs0lOUmcrHVc6wumu7nSMNkQCZJdFP6Bl6J%2B5YNOp%2FN%2BFweWBFWlCPcLtwl21d6Lvljp7pAUaUXRsrH44Vu3oCIBRhtzfPV%2BXqW5qcwxEuTva1eZK%2FHuBPcZ%2F6hDhWBMDu4To25ci7%2FMQHdlFdvu3lTP1gg34p3ysfQHHBbgtgbx2n%2FkVJ6mXcHAXr6xVn%2BavedM0y5clkybW6DZny%2FOgQaCsUZREnyIZfT15lQn9SFBm3CP%2BbLi949eheebPUia9vAHqp%2BRGYpj%2BvnoTTcTA%2B%2BnLLChNTmmJkmW9V8shm3%2FmZwiAQOlfOGtm3acYbgZu7Iu0DMJMBkDnfchKo84BpvrBr2vWfHyGzKWxOMJr4%2FdIGOqUB0UhvIFB07pgcn9p0KhSyTkKLxW9ReoeN634PfEXRQRWTfHDZP8OLC9rvO86zdj1%2BaaQr2CaeD0IUue4X2FOpR95ePVRRrJByKSnL8Zjpu%2BgtcY3UBCSq7ihuEq4HcIoiPx2gH57xX1UWB1KxX5wx100R%2Fi8MYEhcPRTUr0N4gozs7bfhK1D5ieG9PDCNvSmOp2d2Syjyya7Tr%2BYNXdwhdhkaiNQH&X-Amz-Signature=357124d5c4295e373c917cc5d56914fc59afe21c5719647aa5e7aaa749efe431&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这些信息告诉你，mcp inspector 正在 6274 端口运行，你可以通过它提供的 URL 链接访问。MCP inspector 是我们验证服务器是否起来的工具。我们不会花太多时间来介绍。

访问检查器服务器后，你会看到如下界面。点击左侧的连接按钮。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2ace1a7c-a49b-49f6-a297-fa126365c60a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZDC3M2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T152852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGg%2Bmtzeo4TxaiihT15%2FhuPEGdl5Ndvlv0c4i%2BrKI4OkAiEAhwQzZx%2BAL6L%2F4kCMfYzx%2B7MkBMXLXOdibu9QseiIUVAqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKAUdr0kjBk%2BQxqjySrcA1Dt4vkKjLcFKJ2SMdQXynf6gxaBk%2FXgNhrqkaBn1wap3eX1T6zH2Cqm6N%2F2QVggjVXhZPbDZLt5qAUiNQUmlVG89UV8rpLkMNecGUQkJMke%2FvU0h7ORsVHzqYYwqcA2SWaAvx5xUIX1w66kryoLaHQaDGpAhP9ebAjm9iQf5MdmPwLPWrbC%2FMqYlq29IqL08yEDJCPvO4QmVzl%2B8P9pVtDBy%2FHeL8tSEoELNWTZiVjVyCNDYxr25dLXd5jy1C4x42PYCQu%2Buzl9EQs0vlOysLUs0lOUmcrHVc6wumu7nSMNkQCZJdFP6Bl6J%2B5YNOp%2FN%2BFweWBFWlCPcLtwl21d6Lvljp7pAUaUXRsrH44Vu3oCIBRhtzfPV%2BXqW5qcwxEuTva1eZK%2FHuBPcZ%2F6hDhWBMDu4To25ci7%2FMQHdlFdvu3lTP1gg34p3ysfQHHBbgtgbx2n%2FkVJ6mXcHAXr6xVn%2BavedM0y5clkybW6DZny%2FOgQaCsUZREnyIZfT15lQn9SFBm3CP%2BbLi949eheebPUia9vAHqp%2BRGYpj%2BvnoTTcTA%2B%2BnLLChNTmmJkmW9V8shm3%2FmZwiAQOlfOGtm3acYbgZu7Iu0DMJMBkDnfchKo84BpvrBr2vWfHyGzKWxOMJr4%2FdIGOqUB0UhvIFB07pgcn9p0KhSyTkKLxW9ReoeN634PfEXRQRWTfHDZP8OLC9rvO86zdj1%2BaaQr2CaeD0IUue4X2FOpR95ePVRRrJByKSnL8Zjpu%2BgtcY3UBCSq7ihuEq4HcIoiPx2gH57xX1UWB1KxX5wx100R%2Fi8MYEhcPRTUr0N4gozs7bfhK1D5ieG9PDCNvSmOp2d2Syjyya7Tr%2BYNXdwhdhkaiNQH&X-Amz-Signature=8e095f68f0e307f577eae3638c67f9674ff6b3d2615022560a00f162e142b781&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

连接建立后，界面会变成这样。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/63247ba5-0aa1-47c6-bb5e-d878adca18c9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZDC3M2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T152852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGg%2Bmtzeo4TxaiihT15%2FhuPEGdl5Ndvlv0c4i%2BrKI4OkAiEAhwQzZx%2BAL6L%2F4kCMfYzx%2B7MkBMXLXOdibu9QseiIUVAqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKAUdr0kjBk%2BQxqjySrcA1Dt4vkKjLcFKJ2SMdQXynf6gxaBk%2FXgNhrqkaBn1wap3eX1T6zH2Cqm6N%2F2QVggjVXhZPbDZLt5qAUiNQUmlVG89UV8rpLkMNecGUQkJMke%2FvU0h7ORsVHzqYYwqcA2SWaAvx5xUIX1w66kryoLaHQaDGpAhP9ebAjm9iQf5MdmPwLPWrbC%2FMqYlq29IqL08yEDJCPvO4QmVzl%2B8P9pVtDBy%2FHeL8tSEoELNWTZiVjVyCNDYxr25dLXd5jy1C4x42PYCQu%2Buzl9EQs0vlOysLUs0lOUmcrHVc6wumu7nSMNkQCZJdFP6Bl6J%2B5YNOp%2FN%2BFweWBFWlCPcLtwl21d6Lvljp7pAUaUXRsrH44Vu3oCIBRhtzfPV%2BXqW5qcwxEuTva1eZK%2FHuBPcZ%2F6hDhWBMDu4To25ci7%2FMQHdlFdvu3lTP1gg34p3ysfQHHBbgtgbx2n%2FkVJ6mXcHAXr6xVn%2BavedM0y5clkybW6DZny%2FOgQaCsUZREnyIZfT15lQn9SFBm3CP%2BbLi949eheebPUia9vAHqp%2BRGYpj%2BvnoTTcTA%2B%2BnLLChNTmmJkmW9V8shm3%2FmZwiAQOlfOGtm3acYbgZu7Iu0DMJMBkDnfchKo84BpvrBr2vWfHyGzKWxOMJr4%2FdIGOqUB0UhvIFB07pgcn9p0KhSyTkKLxW9ReoeN634PfEXRQRWTfHDZP8OLC9rvO86zdj1%2BaaQr2CaeD0IUue4X2FOpR95ePVRRrJByKSnL8Zjpu%2BgtcY3UBCSq7ihuEq4HcIoiPx2gH57xX1UWB1KxX5wx100R%2Fi8MYEhcPRTUr0N4gozs7bfhK1D5ieG9PDCNvSmOp2d2Syjyya7Tr%2BYNXdwhdhkaiNQH&X-Amz-Signature=0bb4aede49a94448f7f888a02c60a18bd1c9ea3e32fa56f89506349246f08c3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们首先点击 "工具 "按钮，然后选择 "列表工具"，检查我们所使用的工具。然后运行。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/dd91f8d0-b87a-419a-aec0-ceb20c207b9a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZDC3M2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T152852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGg%2Bmtzeo4TxaiihT15%2FhuPEGdl5Ndvlv0c4i%2BrKI4OkAiEAhwQzZx%2BAL6L%2F4kCMfYzx%2B7MkBMXLXOdibu9QseiIUVAqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKAUdr0kjBk%2BQxqjySrcA1Dt4vkKjLcFKJ2SMdQXynf6gxaBk%2FXgNhrqkaBn1wap3eX1T6zH2Cqm6N%2F2QVggjVXhZPbDZLt5qAUiNQUmlVG89UV8rpLkMNecGUQkJMke%2FvU0h7ORsVHzqYYwqcA2SWaAvx5xUIX1w66kryoLaHQaDGpAhP9ebAjm9iQf5MdmPwLPWrbC%2FMqYlq29IqL08yEDJCPvO4QmVzl%2B8P9pVtDBy%2FHeL8tSEoELNWTZiVjVyCNDYxr25dLXd5jy1C4x42PYCQu%2Buzl9EQs0vlOysLUs0lOUmcrHVc6wumu7nSMNkQCZJdFP6Bl6J%2B5YNOp%2FN%2BFweWBFWlCPcLtwl21d6Lvljp7pAUaUXRsrH44Vu3oCIBRhtzfPV%2BXqW5qcwxEuTva1eZK%2FHuBPcZ%2F6hDhWBMDu4To25ci7%2FMQHdlFdvu3lTP1gg34p3ysfQHHBbgtgbx2n%2FkVJ6mXcHAXr6xVn%2BavedM0y5clkybW6DZny%2FOgQaCsUZREnyIZfT15lQn9SFBm3CP%2BbLi949eheebPUia9vAHqp%2BRGYpj%2BvnoTTcTA%2B%2BnLLChNTmmJkmW9V8shm3%2FmZwiAQOlfOGtm3acYbgZu7Iu0DMJMBkDnfchKo84BpvrBr2vWfHyGzKWxOMJr4%2FdIGOqUB0UhvIFB07pgcn9p0KhSyTkKLxW9ReoeN634PfEXRQRWTfHDZP8OLC9rvO86zdj1%2BaaQr2CaeD0IUue4X2FOpR95ePVRRrJByKSnL8Zjpu%2BgtcY3UBCSq7ihuEq4HcIoiPx2gH57xX1UWB1KxX5wx100R%2Fi8MYEhcPRTUr0N4gozs7bfhK1D5ieG9PDCNvSmOp2d2Syjyya7Tr%2BYNXdwhdhkaiNQH&X-Amz-Signature=df725153036fb7e52d87e3c440ae129ea829d2fd9abb37c1fc327bba6fb4ab86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果工具执行成功，就会看到如下界面的结果。那么你就成功运行了一个 mcp 工具。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/70e0fd59-96fd-4056-9142-dc77071a18bf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZDC3M2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T152852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGg%2Bmtzeo4TxaiihT15%2FhuPEGdl5Ndvlv0c4i%2BrKI4OkAiEAhwQzZx%2BAL6L%2F4kCMfYzx%2B7MkBMXLXOdibu9QseiIUVAqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKAUdr0kjBk%2BQxqjySrcA1Dt4vkKjLcFKJ2SMdQXynf6gxaBk%2FXgNhrqkaBn1wap3eX1T6zH2Cqm6N%2F2QVggjVXhZPbDZLt5qAUiNQUmlVG89UV8rpLkMNecGUQkJMke%2FvU0h7ORsVHzqYYwqcA2SWaAvx5xUIX1w66kryoLaHQaDGpAhP9ebAjm9iQf5MdmPwLPWrbC%2FMqYlq29IqL08yEDJCPvO4QmVzl%2B8P9pVtDBy%2FHeL8tSEoELNWTZiVjVyCNDYxr25dLXd5jy1C4x42PYCQu%2Buzl9EQs0vlOysLUs0lOUmcrHVc6wumu7nSMNkQCZJdFP6Bl6J%2B5YNOp%2FN%2BFweWBFWlCPcLtwl21d6Lvljp7pAUaUXRsrH44Vu3oCIBRhtzfPV%2BXqW5qcwxEuTva1eZK%2FHuBPcZ%2F6hDhWBMDu4To25ci7%2FMQHdlFdvu3lTP1gg34p3ysfQHHBbgtgbx2n%2FkVJ6mXcHAXr6xVn%2BavedM0y5clkybW6DZny%2FOgQaCsUZREnyIZfT15lQn9SFBm3CP%2BbLi949eheebPUia9vAHqp%2BRGYpj%2BvnoTTcTA%2B%2BnLLChNTmmJkmW9V8shm3%2FmZwiAQOlfOGtm3acYbgZu7Iu0DMJMBkDnfchKo84BpvrBr2vWfHyGzKWxOMJr4%2FdIGOqUB0UhvIFB07pgcn9p0KhSyTkKLxW9ReoeN634PfEXRQRWTfHDZP8OLC9rvO86zdj1%2BaaQr2CaeD0IUue4X2FOpR95ePVRRrJByKSnL8Zjpu%2BgtcY3UBCSq7ihuEq4HcIoiPx2gH57xX1UWB1KxX5wx100R%2Fi8MYEhcPRTUr0N4gozs7bfhK1D5ieG9PDCNvSmOp2d2Syjyya7Tr%2BYNXdwhdhkaiNQH&X-Amz-Signature=20c362e29b1b0b1873d3023c4a68b8a87273a69348929e3a2e1303ed2d6725c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/129cc91e-3fce-4702-9189-a7d04991a5d4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZDC3M2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T152852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGg%2Bmtzeo4TxaiihT15%2FhuPEGdl5Ndvlv0c4i%2BrKI4OkAiEAhwQzZx%2BAL6L%2F4kCMfYzx%2B7MkBMXLXOdibu9QseiIUVAqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKAUdr0kjBk%2BQxqjySrcA1Dt4vkKjLcFKJ2SMdQXynf6gxaBk%2FXgNhrqkaBn1wap3eX1T6zH2Cqm6N%2F2QVggjVXhZPbDZLt5qAUiNQUmlVG89UV8rpLkMNecGUQkJMke%2FvU0h7ORsVHzqYYwqcA2SWaAvx5xUIX1w66kryoLaHQaDGpAhP9ebAjm9iQf5MdmPwLPWrbC%2FMqYlq29IqL08yEDJCPvO4QmVzl%2B8P9pVtDBy%2FHeL8tSEoELNWTZiVjVyCNDYxr25dLXd5jy1C4x42PYCQu%2Buzl9EQs0vlOysLUs0lOUmcrHVc6wumu7nSMNkQCZJdFP6Bl6J%2B5YNOp%2FN%2BFweWBFWlCPcLtwl21d6Lvljp7pAUaUXRsrH44Vu3oCIBRhtzfPV%2BXqW5qcwxEuTva1eZK%2FHuBPcZ%2F6hDhWBMDu4To25ci7%2FMQHdlFdvu3lTP1gg34p3ysfQHHBbgtgbx2n%2FkVJ6mXcHAXr6xVn%2BavedM0y5clkybW6DZny%2FOgQaCsUZREnyIZfT15lQn9SFBm3CP%2BbLi949eheebPUia9vAHqp%2BRGYpj%2BvnoTTcTA%2B%2BnLLChNTmmJkmW9V8shm3%2FmZwiAQOlfOGtm3acYbgZu7Iu0DMJMBkDnfchKo84BpvrBr2vWfHyGzKWxOMJr4%2FdIGOqUB0UhvIFB07pgcn9p0KhSyTkKLxW9ReoeN634PfEXRQRWTfHDZP8OLC9rvO86zdj1%2BaaQr2CaeD0IUue4X2FOpR95ePVRRrJByKSnL8Zjpu%2BgtcY3UBCSq7ihuEq4HcIoiPx2gH57xX1UWB1KxX5wx100R%2Fi8MYEhcPRTUr0N4gozs7bfhK1D5ieG9PDCNvSmOp2d2Syjyya7Tr%2BYNXdwhdhkaiNQH&X-Amz-Signature=c8b039ef07c046a4b8dff0cd9f2d1e3c134fcc79ae5a23bab6b29480def5f5c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
