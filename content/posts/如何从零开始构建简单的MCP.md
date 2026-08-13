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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7f0e8a0b-c4e1-4f01-9374-57601ba10ab2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LNIWYH2%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T164345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIGmfrJdTIPpqvDgeWC3PzsyjpSbGZOVno3zQMRO4ssgDAiBktpk%2B%2BDRD7ICQx%2FOabrwC%2Fx62a9Yq9PLE93iQ0%2FCcLCqIBAjp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsyHBBFYrYUCfAZv5KtwDdcqZQRwasapjuA64JuzGt7828d%2FsqActpqDdP2kyih1yi2Yh9loN2xYeXghENxVla864QCnGqoLlgfG43J%2FuKy%2BryozWbn0N8sAdgZ%2BXiM1TavOUV7kiCxcvBDWrWT7BAqVgLEOD%2B%2Bfx2zEKn8c75f2rSHaAFYewkT7mvWN473br3sk%2B79mjZOf3RMh8rqBpU932X4VD053wfFchFcM5Hd9LejOATEA54rTkLiasdSbYoKYogxPNCsebLeaoKSwGGiACJ4pB%2FPpeXwOszXzITMPQnwXVQzr09Dfjw%2BkG4O2B%2Bqw0KFXNCiQi26nRC6FK1yiqmXauxqO8WW5V4TLc63KXu1DvTHi6zvII4NT4KqF%2B11J64eOzGJ%2FFcCNJf2hPxrA8kLUgAwETRkjHL9ViROph4U7lYBznHLULTNbebErl8cS07k7r%2Be5AhFm8xsZxyDeLGO1f%2FiufbROXo97UUD4VDVHowxZoAc%2Fy2C1MkpUA4kjzvO95OT8BR8g1wED88uFki0vQ5sHJ40VHVotvH%2BR5hXqD10omFu1um11kKT%2Bj7EPvJEvpAgQtyfCf7cRjkf8Vm65tQOTAVW8%2FmgtTwV%2BMprw045vQs1jcvZBJPVGNdQGQcN03gkXCOlcw%2F9v30wY6pgFS6OKtyfm7hFm7nweQrnYBkW6RL6oXSMq3RPHPffuLHPcee2Nmosc7ESkNT7jXSxw4O7WhOhkja%2BCg9DUx2hLkbnv6Ks7n188lkrxAtJEwpjfa8uEt18hnjcpGspHTH9yZD6tCuDXQ6JOocgH6ARVDLBW0kERpgZFPIGwjix%2BUxNOS9ISwuFt%2BAZotT4398YmFgIemEHkCKrSgTaADxihkGK%2Bd476N&X-Amz-Signature=e3c122a4b7e3114b6599383aad06a17b39c9443f81c6bb32298cf42410600b6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/1daf1736-35f7-48c2-9156-c98068ca2637/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LNIWYH2%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T164345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIGmfrJdTIPpqvDgeWC3PzsyjpSbGZOVno3zQMRO4ssgDAiBktpk%2B%2BDRD7ICQx%2FOabrwC%2Fx62a9Yq9PLE93iQ0%2FCcLCqIBAjp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsyHBBFYrYUCfAZv5KtwDdcqZQRwasapjuA64JuzGt7828d%2FsqActpqDdP2kyih1yi2Yh9loN2xYeXghENxVla864QCnGqoLlgfG43J%2FuKy%2BryozWbn0N8sAdgZ%2BXiM1TavOUV7kiCxcvBDWrWT7BAqVgLEOD%2B%2Bfx2zEKn8c75f2rSHaAFYewkT7mvWN473br3sk%2B79mjZOf3RMh8rqBpU932X4VD053wfFchFcM5Hd9LejOATEA54rTkLiasdSbYoKYogxPNCsebLeaoKSwGGiACJ4pB%2FPpeXwOszXzITMPQnwXVQzr09Dfjw%2BkG4O2B%2Bqw0KFXNCiQi26nRC6FK1yiqmXauxqO8WW5V4TLc63KXu1DvTHi6zvII4NT4KqF%2B11J64eOzGJ%2FFcCNJf2hPxrA8kLUgAwETRkjHL9ViROph4U7lYBznHLULTNbebErl8cS07k7r%2Be5AhFm8xsZxyDeLGO1f%2FiufbROXo97UUD4VDVHowxZoAc%2Fy2C1MkpUA4kjzvO95OT8BR8g1wED88uFki0vQ5sHJ40VHVotvH%2BR5hXqD10omFu1um11kKT%2Bj7EPvJEvpAgQtyfCf7cRjkf8Vm65tQOTAVW8%2FmgtTwV%2BMprw045vQs1jcvZBJPVGNdQGQcN03gkXCOlcw%2F9v30wY6pgFS6OKtyfm7hFm7nweQrnYBkW6RL6oXSMq3RPHPffuLHPcee2Nmosc7ESkNT7jXSxw4O7WhOhkja%2BCg9DUx2hLkbnv6Ks7n188lkrxAtJEwpjfa8uEt18hnjcpGspHTH9yZD6tCuDXQ6JOocgH6ARVDLBW0kERpgZFPIGwjix%2BUxNOS9ISwuFt%2BAZotT4398YmFgIemEHkCKrSgTaADxihkGK%2Bd476N&X-Amz-Signature=60178410c488a22d675604ecf7f50c5699819a427f3fe31af45346604a27ef43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这些信息告诉你，mcp inspector 正在 6274 端口运行，你可以通过它提供的 URL 链接访问。MCP inspector 是我们验证服务器是否起来的工具。我们不会花太多时间来介绍。

访问检查器服务器后，你会看到如下界面。点击左侧的连接按钮。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2ace1a7c-a49b-49f6-a297-fa126365c60a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LNIWYH2%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T164345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIGmfrJdTIPpqvDgeWC3PzsyjpSbGZOVno3zQMRO4ssgDAiBktpk%2B%2BDRD7ICQx%2FOabrwC%2Fx62a9Yq9PLE93iQ0%2FCcLCqIBAjp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsyHBBFYrYUCfAZv5KtwDdcqZQRwasapjuA64JuzGt7828d%2FsqActpqDdP2kyih1yi2Yh9loN2xYeXghENxVla864QCnGqoLlgfG43J%2FuKy%2BryozWbn0N8sAdgZ%2BXiM1TavOUV7kiCxcvBDWrWT7BAqVgLEOD%2B%2Bfx2zEKn8c75f2rSHaAFYewkT7mvWN473br3sk%2B79mjZOf3RMh8rqBpU932X4VD053wfFchFcM5Hd9LejOATEA54rTkLiasdSbYoKYogxPNCsebLeaoKSwGGiACJ4pB%2FPpeXwOszXzITMPQnwXVQzr09Dfjw%2BkG4O2B%2Bqw0KFXNCiQi26nRC6FK1yiqmXauxqO8WW5V4TLc63KXu1DvTHi6zvII4NT4KqF%2B11J64eOzGJ%2FFcCNJf2hPxrA8kLUgAwETRkjHL9ViROph4U7lYBznHLULTNbebErl8cS07k7r%2Be5AhFm8xsZxyDeLGO1f%2FiufbROXo97UUD4VDVHowxZoAc%2Fy2C1MkpUA4kjzvO95OT8BR8g1wED88uFki0vQ5sHJ40VHVotvH%2BR5hXqD10omFu1um11kKT%2Bj7EPvJEvpAgQtyfCf7cRjkf8Vm65tQOTAVW8%2FmgtTwV%2BMprw045vQs1jcvZBJPVGNdQGQcN03gkXCOlcw%2F9v30wY6pgFS6OKtyfm7hFm7nweQrnYBkW6RL6oXSMq3RPHPffuLHPcee2Nmosc7ESkNT7jXSxw4O7WhOhkja%2BCg9DUx2hLkbnv6Ks7n188lkrxAtJEwpjfa8uEt18hnjcpGspHTH9yZD6tCuDXQ6JOocgH6ARVDLBW0kERpgZFPIGwjix%2BUxNOS9ISwuFt%2BAZotT4398YmFgIemEHkCKrSgTaADxihkGK%2Bd476N&X-Amz-Signature=71dffadcdb1528287f6d06f2ea85324c0b5e1b3b0f2e8ae65deb60cdafef8d7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

连接建立后，界面会变成这样。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/63247ba5-0aa1-47c6-bb5e-d878adca18c9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LNIWYH2%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T164345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIGmfrJdTIPpqvDgeWC3PzsyjpSbGZOVno3zQMRO4ssgDAiBktpk%2B%2BDRD7ICQx%2FOabrwC%2Fx62a9Yq9PLE93iQ0%2FCcLCqIBAjp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsyHBBFYrYUCfAZv5KtwDdcqZQRwasapjuA64JuzGt7828d%2FsqActpqDdP2kyih1yi2Yh9loN2xYeXghENxVla864QCnGqoLlgfG43J%2FuKy%2BryozWbn0N8sAdgZ%2BXiM1TavOUV7kiCxcvBDWrWT7BAqVgLEOD%2B%2Bfx2zEKn8c75f2rSHaAFYewkT7mvWN473br3sk%2B79mjZOf3RMh8rqBpU932X4VD053wfFchFcM5Hd9LejOATEA54rTkLiasdSbYoKYogxPNCsebLeaoKSwGGiACJ4pB%2FPpeXwOszXzITMPQnwXVQzr09Dfjw%2BkG4O2B%2Bqw0KFXNCiQi26nRC6FK1yiqmXauxqO8WW5V4TLc63KXu1DvTHi6zvII4NT4KqF%2B11J64eOzGJ%2FFcCNJf2hPxrA8kLUgAwETRkjHL9ViROph4U7lYBznHLULTNbebErl8cS07k7r%2Be5AhFm8xsZxyDeLGO1f%2FiufbROXo97UUD4VDVHowxZoAc%2Fy2C1MkpUA4kjzvO95OT8BR8g1wED88uFki0vQ5sHJ40VHVotvH%2BR5hXqD10omFu1um11kKT%2Bj7EPvJEvpAgQtyfCf7cRjkf8Vm65tQOTAVW8%2FmgtTwV%2BMprw045vQs1jcvZBJPVGNdQGQcN03gkXCOlcw%2F9v30wY6pgFS6OKtyfm7hFm7nweQrnYBkW6RL6oXSMq3RPHPffuLHPcee2Nmosc7ESkNT7jXSxw4O7WhOhkja%2BCg9DUx2hLkbnv6Ks7n188lkrxAtJEwpjfa8uEt18hnjcpGspHTH9yZD6tCuDXQ6JOocgH6ARVDLBW0kERpgZFPIGwjix%2BUxNOS9ISwuFt%2BAZotT4398YmFgIemEHkCKrSgTaADxihkGK%2Bd476N&X-Amz-Signature=95942acaba864db94853915148ab1c356a0bac33faaa2dd5da154bf774455e16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们首先点击 "工具 "按钮，然后选择 "列表工具"，检查我们所使用的工具。然后运行。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/dd91f8d0-b87a-419a-aec0-ceb20c207b9a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LNIWYH2%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T164345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIGmfrJdTIPpqvDgeWC3PzsyjpSbGZOVno3zQMRO4ssgDAiBktpk%2B%2BDRD7ICQx%2FOabrwC%2Fx62a9Yq9PLE93iQ0%2FCcLCqIBAjp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsyHBBFYrYUCfAZv5KtwDdcqZQRwasapjuA64JuzGt7828d%2FsqActpqDdP2kyih1yi2Yh9loN2xYeXghENxVla864QCnGqoLlgfG43J%2FuKy%2BryozWbn0N8sAdgZ%2BXiM1TavOUV7kiCxcvBDWrWT7BAqVgLEOD%2B%2Bfx2zEKn8c75f2rSHaAFYewkT7mvWN473br3sk%2B79mjZOf3RMh8rqBpU932X4VD053wfFchFcM5Hd9LejOATEA54rTkLiasdSbYoKYogxPNCsebLeaoKSwGGiACJ4pB%2FPpeXwOszXzITMPQnwXVQzr09Dfjw%2BkG4O2B%2Bqw0KFXNCiQi26nRC6FK1yiqmXauxqO8WW5V4TLc63KXu1DvTHi6zvII4NT4KqF%2B11J64eOzGJ%2FFcCNJf2hPxrA8kLUgAwETRkjHL9ViROph4U7lYBznHLULTNbebErl8cS07k7r%2Be5AhFm8xsZxyDeLGO1f%2FiufbROXo97UUD4VDVHowxZoAc%2Fy2C1MkpUA4kjzvO95OT8BR8g1wED88uFki0vQ5sHJ40VHVotvH%2BR5hXqD10omFu1um11kKT%2Bj7EPvJEvpAgQtyfCf7cRjkf8Vm65tQOTAVW8%2FmgtTwV%2BMprw045vQs1jcvZBJPVGNdQGQcN03gkXCOlcw%2F9v30wY6pgFS6OKtyfm7hFm7nweQrnYBkW6RL6oXSMq3RPHPffuLHPcee2Nmosc7ESkNT7jXSxw4O7WhOhkja%2BCg9DUx2hLkbnv6Ks7n188lkrxAtJEwpjfa8uEt18hnjcpGspHTH9yZD6tCuDXQ6JOocgH6ARVDLBW0kERpgZFPIGwjix%2BUxNOS9ISwuFt%2BAZotT4398YmFgIemEHkCKrSgTaADxihkGK%2Bd476N&X-Amz-Signature=1fbc99cb09b12077df478db263eeaa090a3648d62a54154579308ac0bf07b223&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果工具执行成功，就会看到如下界面的结果。那么你就成功运行了一个 mcp 工具。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/70e0fd59-96fd-4056-9142-dc77071a18bf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LNIWYH2%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T164345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIGmfrJdTIPpqvDgeWC3PzsyjpSbGZOVno3zQMRO4ssgDAiBktpk%2B%2BDRD7ICQx%2FOabrwC%2Fx62a9Yq9PLE93iQ0%2FCcLCqIBAjp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsyHBBFYrYUCfAZv5KtwDdcqZQRwasapjuA64JuzGt7828d%2FsqActpqDdP2kyih1yi2Yh9loN2xYeXghENxVla864QCnGqoLlgfG43J%2FuKy%2BryozWbn0N8sAdgZ%2BXiM1TavOUV7kiCxcvBDWrWT7BAqVgLEOD%2B%2Bfx2zEKn8c75f2rSHaAFYewkT7mvWN473br3sk%2B79mjZOf3RMh8rqBpU932X4VD053wfFchFcM5Hd9LejOATEA54rTkLiasdSbYoKYogxPNCsebLeaoKSwGGiACJ4pB%2FPpeXwOszXzITMPQnwXVQzr09Dfjw%2BkG4O2B%2Bqw0KFXNCiQi26nRC6FK1yiqmXauxqO8WW5V4TLc63KXu1DvTHi6zvII4NT4KqF%2B11J64eOzGJ%2FFcCNJf2hPxrA8kLUgAwETRkjHL9ViROph4U7lYBznHLULTNbebErl8cS07k7r%2Be5AhFm8xsZxyDeLGO1f%2FiufbROXo97UUD4VDVHowxZoAc%2Fy2C1MkpUA4kjzvO95OT8BR8g1wED88uFki0vQ5sHJ40VHVotvH%2BR5hXqD10omFu1um11kKT%2Bj7EPvJEvpAgQtyfCf7cRjkf8Vm65tQOTAVW8%2FmgtTwV%2BMprw045vQs1jcvZBJPVGNdQGQcN03gkXCOlcw%2F9v30wY6pgFS6OKtyfm7hFm7nweQrnYBkW6RL6oXSMq3RPHPffuLHPcee2Nmosc7ESkNT7jXSxw4O7WhOhkja%2BCg9DUx2hLkbnv6Ks7n188lkrxAtJEwpjfa8uEt18hnjcpGspHTH9yZD6tCuDXQ6JOocgH6ARVDLBW0kERpgZFPIGwjix%2BUxNOS9ISwuFt%2BAZotT4398YmFgIemEHkCKrSgTaADxihkGK%2Bd476N&X-Amz-Signature=d2b67e486cb04a3a0e15f074817c5f34451e2c8dba72ad037324be23a967ba31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/129cc91e-3fce-4702-9189-a7d04991a5d4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LNIWYH2%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T164345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIGmfrJdTIPpqvDgeWC3PzsyjpSbGZOVno3zQMRO4ssgDAiBktpk%2B%2BDRD7ICQx%2FOabrwC%2Fx62a9Yq9PLE93iQ0%2FCcLCqIBAjp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsyHBBFYrYUCfAZv5KtwDdcqZQRwasapjuA64JuzGt7828d%2FsqActpqDdP2kyih1yi2Yh9loN2xYeXghENxVla864QCnGqoLlgfG43J%2FuKy%2BryozWbn0N8sAdgZ%2BXiM1TavOUV7kiCxcvBDWrWT7BAqVgLEOD%2B%2Bfx2zEKn8c75f2rSHaAFYewkT7mvWN473br3sk%2B79mjZOf3RMh8rqBpU932X4VD053wfFchFcM5Hd9LejOATEA54rTkLiasdSbYoKYogxPNCsebLeaoKSwGGiACJ4pB%2FPpeXwOszXzITMPQnwXVQzr09Dfjw%2BkG4O2B%2Bqw0KFXNCiQi26nRC6FK1yiqmXauxqO8WW5V4TLc63KXu1DvTHi6zvII4NT4KqF%2B11J64eOzGJ%2FFcCNJf2hPxrA8kLUgAwETRkjHL9ViROph4U7lYBznHLULTNbebErl8cS07k7r%2Be5AhFm8xsZxyDeLGO1f%2FiufbROXo97UUD4VDVHowxZoAc%2Fy2C1MkpUA4kjzvO95OT8BR8g1wED88uFki0vQ5sHJ40VHVotvH%2BR5hXqD10omFu1um11kKT%2Bj7EPvJEvpAgQtyfCf7cRjkf8Vm65tQOTAVW8%2FmgtTwV%2BMprw045vQs1jcvZBJPVGNdQGQcN03gkXCOlcw%2F9v30wY6pgFS6OKtyfm7hFm7nweQrnYBkW6RL6oXSMq3RPHPffuLHPcee2Nmosc7ESkNT7jXSxw4O7WhOhkja%2BCg9DUx2hLkbnv6Ks7n188lkrxAtJEwpjfa8uEt18hnjcpGspHTH9yZD6tCuDXQ6JOocgH6ARVDLBW0kERpgZFPIGwjix%2BUxNOS9ISwuFt%2BAZotT4398YmFgIemEHkCKrSgTaADxihkGK%2Bd476N&X-Amz-Signature=2f132be0afa8a48d190f520f7d06d7b5eacc7162a28e7edb2855481da9b84869&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
