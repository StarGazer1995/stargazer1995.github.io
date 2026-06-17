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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7f0e8a0b-c4e1-4f01-9374-57601ba10ab2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMNV4XRA%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T085350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwoBdk22H9nQyh2b5gGoSLlMiK5%2BEbrJ8XbuErdgHJcAIhAO44y4YwcC0SppG4NIBtTa%2BlpxvFHaO4Fh2u9CcH8CfcKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2Fknd14%2BtT0sYk9mkq3AOCBngzkH61nAIq1PY0GHOqgf7So8yfaw4OmdWm2bz8lHZ4z1dzE4vp%2B5HIRMyJhJV8Q0%2B%2F1h5tPgV0ImN9Wnn7YaVnLb%2Byxr5jRH3nS03FRK7tp%2BWgiv6tDkk6dX6ABj6k9Q%2B9JA3Jo4OOeMY5nHOylAcNYZHq3lhSAh9LaNjMFu90m5KP%2F6VzCaLiev6qIGMZp9BNpJbabqzz3nc%2Blyi4Tik184KA9vhewA9QZKZbsd%2BatxqK9yqwS6EfAm40j8qwnAqyCGHbMrqPYkH7sbKEHXscqE8zbPe4QnRad0bpHZSrhCr6g0dg9TB%2Bw6yK8Y1rqR2QSQZ5kwwvEzDi0dIbpq5ATPUtFhqPjX%2B5oNXwVSDXNmng1vMaiEx2hXd%2Bpd9CXEzfk%2FhPTvy9Gt%2BT6BPChUd2hL%2BQTTjEqmiTMPZDFY6Lg1%2F%2B3SIbcoXYEEuS%2BJ2XWVufRbx6QttI5Byb2d2ptbuuJ8AR8Uspo47ktQTwDSqM%2BquHgxl8xgXW2XBkURksh%2BCzAMcBypzjr8HtiKtGhRuEMsjDE%2F5BB3sHn%2BA21aNS6fIeoHqfFw%2BJf49mZf86ROqQ4SMQAW5GaxIVTnu3NUybd0l5b%2ByPqlHUPxVY4sQWLpZbxt3qXwROiDDIs8nRBjqkATnr6O4KmgYl%2BLoyeoAnFiTsAgonhxlvUIA6Lcv9LSNDGh04%2BNwXUR27JGsY7Z%2BUbJOAl8YAJzK62C6T%2BoC1f9mo4WBuTLaUDPOyjtDFsEcH4%2F3jmBAl2rfpidjFNo9oxJAYQE03V9fmzxc3EmTBMBTnV7Z6NYGhYnI1m7wgSS5f1Dl6QdT%2BfodGMd7n2SjdTJIKA0sMUrbDSqUSXzdbs6EAvjl0&X-Amz-Signature=a1aea7410861323b0c17ec549514c9deb4882ed05173c21655b5164c4d5dfb01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/1daf1736-35f7-48c2-9156-c98068ca2637/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMNV4XRA%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T085350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwoBdk22H9nQyh2b5gGoSLlMiK5%2BEbrJ8XbuErdgHJcAIhAO44y4YwcC0SppG4NIBtTa%2BlpxvFHaO4Fh2u9CcH8CfcKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2Fknd14%2BtT0sYk9mkq3AOCBngzkH61nAIq1PY0GHOqgf7So8yfaw4OmdWm2bz8lHZ4z1dzE4vp%2B5HIRMyJhJV8Q0%2B%2F1h5tPgV0ImN9Wnn7YaVnLb%2Byxr5jRH3nS03FRK7tp%2BWgiv6tDkk6dX6ABj6k9Q%2B9JA3Jo4OOeMY5nHOylAcNYZHq3lhSAh9LaNjMFu90m5KP%2F6VzCaLiev6qIGMZp9BNpJbabqzz3nc%2Blyi4Tik184KA9vhewA9QZKZbsd%2BatxqK9yqwS6EfAm40j8qwnAqyCGHbMrqPYkH7sbKEHXscqE8zbPe4QnRad0bpHZSrhCr6g0dg9TB%2Bw6yK8Y1rqR2QSQZ5kwwvEzDi0dIbpq5ATPUtFhqPjX%2B5oNXwVSDXNmng1vMaiEx2hXd%2Bpd9CXEzfk%2FhPTvy9Gt%2BT6BPChUd2hL%2BQTTjEqmiTMPZDFY6Lg1%2F%2B3SIbcoXYEEuS%2BJ2XWVufRbx6QttI5Byb2d2ptbuuJ8AR8Uspo47ktQTwDSqM%2BquHgxl8xgXW2XBkURksh%2BCzAMcBypzjr8HtiKtGhRuEMsjDE%2F5BB3sHn%2BA21aNS6fIeoHqfFw%2BJf49mZf86ROqQ4SMQAW5GaxIVTnu3NUybd0l5b%2ByPqlHUPxVY4sQWLpZbxt3qXwROiDDIs8nRBjqkATnr6O4KmgYl%2BLoyeoAnFiTsAgonhxlvUIA6Lcv9LSNDGh04%2BNwXUR27JGsY7Z%2BUbJOAl8YAJzK62C6T%2BoC1f9mo4WBuTLaUDPOyjtDFsEcH4%2F3jmBAl2rfpidjFNo9oxJAYQE03V9fmzxc3EmTBMBTnV7Z6NYGhYnI1m7wgSS5f1Dl6QdT%2BfodGMd7n2SjdTJIKA0sMUrbDSqUSXzdbs6EAvjl0&X-Amz-Signature=1fea3bf3b658eecdc2349b6c75e524d166c64273546cf08fb5b5b8533cf475ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这些信息告诉你，mcp inspector 正在 6274 端口运行，你可以通过它提供的 URL 链接访问。MCP inspector 是我们验证服务器是否起来的工具。我们不会花太多时间来介绍。

访问检查器服务器后，你会看到如下界面。点击左侧的连接按钮。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2ace1a7c-a49b-49f6-a297-fa126365c60a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMNV4XRA%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T085350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwoBdk22H9nQyh2b5gGoSLlMiK5%2BEbrJ8XbuErdgHJcAIhAO44y4YwcC0SppG4NIBtTa%2BlpxvFHaO4Fh2u9CcH8CfcKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2Fknd14%2BtT0sYk9mkq3AOCBngzkH61nAIq1PY0GHOqgf7So8yfaw4OmdWm2bz8lHZ4z1dzE4vp%2B5HIRMyJhJV8Q0%2B%2F1h5tPgV0ImN9Wnn7YaVnLb%2Byxr5jRH3nS03FRK7tp%2BWgiv6tDkk6dX6ABj6k9Q%2B9JA3Jo4OOeMY5nHOylAcNYZHq3lhSAh9LaNjMFu90m5KP%2F6VzCaLiev6qIGMZp9BNpJbabqzz3nc%2Blyi4Tik184KA9vhewA9QZKZbsd%2BatxqK9yqwS6EfAm40j8qwnAqyCGHbMrqPYkH7sbKEHXscqE8zbPe4QnRad0bpHZSrhCr6g0dg9TB%2Bw6yK8Y1rqR2QSQZ5kwwvEzDi0dIbpq5ATPUtFhqPjX%2B5oNXwVSDXNmng1vMaiEx2hXd%2Bpd9CXEzfk%2FhPTvy9Gt%2BT6BPChUd2hL%2BQTTjEqmiTMPZDFY6Lg1%2F%2B3SIbcoXYEEuS%2BJ2XWVufRbx6QttI5Byb2d2ptbuuJ8AR8Uspo47ktQTwDSqM%2BquHgxl8xgXW2XBkURksh%2BCzAMcBypzjr8HtiKtGhRuEMsjDE%2F5BB3sHn%2BA21aNS6fIeoHqfFw%2BJf49mZf86ROqQ4SMQAW5GaxIVTnu3NUybd0l5b%2ByPqlHUPxVY4sQWLpZbxt3qXwROiDDIs8nRBjqkATnr6O4KmgYl%2BLoyeoAnFiTsAgonhxlvUIA6Lcv9LSNDGh04%2BNwXUR27JGsY7Z%2BUbJOAl8YAJzK62C6T%2BoC1f9mo4WBuTLaUDPOyjtDFsEcH4%2F3jmBAl2rfpidjFNo9oxJAYQE03V9fmzxc3EmTBMBTnV7Z6NYGhYnI1m7wgSS5f1Dl6QdT%2BfodGMd7n2SjdTJIKA0sMUrbDSqUSXzdbs6EAvjl0&X-Amz-Signature=f6f2c0a674f94dd0b863d1b7ffc0a1674de829e325d7304bd7d84b61c2015824&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

连接建立后，界面会变成这样。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/63247ba5-0aa1-47c6-bb5e-d878adca18c9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMNV4XRA%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T085350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwoBdk22H9nQyh2b5gGoSLlMiK5%2BEbrJ8XbuErdgHJcAIhAO44y4YwcC0SppG4NIBtTa%2BlpxvFHaO4Fh2u9CcH8CfcKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2Fknd14%2BtT0sYk9mkq3AOCBngzkH61nAIq1PY0GHOqgf7So8yfaw4OmdWm2bz8lHZ4z1dzE4vp%2B5HIRMyJhJV8Q0%2B%2F1h5tPgV0ImN9Wnn7YaVnLb%2Byxr5jRH3nS03FRK7tp%2BWgiv6tDkk6dX6ABj6k9Q%2B9JA3Jo4OOeMY5nHOylAcNYZHq3lhSAh9LaNjMFu90m5KP%2F6VzCaLiev6qIGMZp9BNpJbabqzz3nc%2Blyi4Tik184KA9vhewA9QZKZbsd%2BatxqK9yqwS6EfAm40j8qwnAqyCGHbMrqPYkH7sbKEHXscqE8zbPe4QnRad0bpHZSrhCr6g0dg9TB%2Bw6yK8Y1rqR2QSQZ5kwwvEzDi0dIbpq5ATPUtFhqPjX%2B5oNXwVSDXNmng1vMaiEx2hXd%2Bpd9CXEzfk%2FhPTvy9Gt%2BT6BPChUd2hL%2BQTTjEqmiTMPZDFY6Lg1%2F%2B3SIbcoXYEEuS%2BJ2XWVufRbx6QttI5Byb2d2ptbuuJ8AR8Uspo47ktQTwDSqM%2BquHgxl8xgXW2XBkURksh%2BCzAMcBypzjr8HtiKtGhRuEMsjDE%2F5BB3sHn%2BA21aNS6fIeoHqfFw%2BJf49mZf86ROqQ4SMQAW5GaxIVTnu3NUybd0l5b%2ByPqlHUPxVY4sQWLpZbxt3qXwROiDDIs8nRBjqkATnr6O4KmgYl%2BLoyeoAnFiTsAgonhxlvUIA6Lcv9LSNDGh04%2BNwXUR27JGsY7Z%2BUbJOAl8YAJzK62C6T%2BoC1f9mo4WBuTLaUDPOyjtDFsEcH4%2F3jmBAl2rfpidjFNo9oxJAYQE03V9fmzxc3EmTBMBTnV7Z6NYGhYnI1m7wgSS5f1Dl6QdT%2BfodGMd7n2SjdTJIKA0sMUrbDSqUSXzdbs6EAvjl0&X-Amz-Signature=07b3262c0342a9aa957cf76c465bc74f6e55e5ce76980237532ecb81ced7dd58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们首先点击 "工具 "按钮，然后选择 "列表工具"，检查我们所使用的工具。然后运行。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/dd91f8d0-b87a-419a-aec0-ceb20c207b9a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMNV4XRA%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T085350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwoBdk22H9nQyh2b5gGoSLlMiK5%2BEbrJ8XbuErdgHJcAIhAO44y4YwcC0SppG4NIBtTa%2BlpxvFHaO4Fh2u9CcH8CfcKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2Fknd14%2BtT0sYk9mkq3AOCBngzkH61nAIq1PY0GHOqgf7So8yfaw4OmdWm2bz8lHZ4z1dzE4vp%2B5HIRMyJhJV8Q0%2B%2F1h5tPgV0ImN9Wnn7YaVnLb%2Byxr5jRH3nS03FRK7tp%2BWgiv6tDkk6dX6ABj6k9Q%2B9JA3Jo4OOeMY5nHOylAcNYZHq3lhSAh9LaNjMFu90m5KP%2F6VzCaLiev6qIGMZp9BNpJbabqzz3nc%2Blyi4Tik184KA9vhewA9QZKZbsd%2BatxqK9yqwS6EfAm40j8qwnAqyCGHbMrqPYkH7sbKEHXscqE8zbPe4QnRad0bpHZSrhCr6g0dg9TB%2Bw6yK8Y1rqR2QSQZ5kwwvEzDi0dIbpq5ATPUtFhqPjX%2B5oNXwVSDXNmng1vMaiEx2hXd%2Bpd9CXEzfk%2FhPTvy9Gt%2BT6BPChUd2hL%2BQTTjEqmiTMPZDFY6Lg1%2F%2B3SIbcoXYEEuS%2BJ2XWVufRbx6QttI5Byb2d2ptbuuJ8AR8Uspo47ktQTwDSqM%2BquHgxl8xgXW2XBkURksh%2BCzAMcBypzjr8HtiKtGhRuEMsjDE%2F5BB3sHn%2BA21aNS6fIeoHqfFw%2BJf49mZf86ROqQ4SMQAW5GaxIVTnu3NUybd0l5b%2ByPqlHUPxVY4sQWLpZbxt3qXwROiDDIs8nRBjqkATnr6O4KmgYl%2BLoyeoAnFiTsAgonhxlvUIA6Lcv9LSNDGh04%2BNwXUR27JGsY7Z%2BUbJOAl8YAJzK62C6T%2BoC1f9mo4WBuTLaUDPOyjtDFsEcH4%2F3jmBAl2rfpidjFNo9oxJAYQE03V9fmzxc3EmTBMBTnV7Z6NYGhYnI1m7wgSS5f1Dl6QdT%2BfodGMd7n2SjdTJIKA0sMUrbDSqUSXzdbs6EAvjl0&X-Amz-Signature=ec2a3b6be13d7d82a30adb614210e051b9390676d7ba5303ed9f951a69791ec1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果工具执行成功，就会看到如下界面的结果。那么你就成功运行了一个 mcp 工具。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/70e0fd59-96fd-4056-9142-dc77071a18bf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMNV4XRA%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T085350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwoBdk22H9nQyh2b5gGoSLlMiK5%2BEbrJ8XbuErdgHJcAIhAO44y4YwcC0SppG4NIBtTa%2BlpxvFHaO4Fh2u9CcH8CfcKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2Fknd14%2BtT0sYk9mkq3AOCBngzkH61nAIq1PY0GHOqgf7So8yfaw4OmdWm2bz8lHZ4z1dzE4vp%2B5HIRMyJhJV8Q0%2B%2F1h5tPgV0ImN9Wnn7YaVnLb%2Byxr5jRH3nS03FRK7tp%2BWgiv6tDkk6dX6ABj6k9Q%2B9JA3Jo4OOeMY5nHOylAcNYZHq3lhSAh9LaNjMFu90m5KP%2F6VzCaLiev6qIGMZp9BNpJbabqzz3nc%2Blyi4Tik184KA9vhewA9QZKZbsd%2BatxqK9yqwS6EfAm40j8qwnAqyCGHbMrqPYkH7sbKEHXscqE8zbPe4QnRad0bpHZSrhCr6g0dg9TB%2Bw6yK8Y1rqR2QSQZ5kwwvEzDi0dIbpq5ATPUtFhqPjX%2B5oNXwVSDXNmng1vMaiEx2hXd%2Bpd9CXEzfk%2FhPTvy9Gt%2BT6BPChUd2hL%2BQTTjEqmiTMPZDFY6Lg1%2F%2B3SIbcoXYEEuS%2BJ2XWVufRbx6QttI5Byb2d2ptbuuJ8AR8Uspo47ktQTwDSqM%2BquHgxl8xgXW2XBkURksh%2BCzAMcBypzjr8HtiKtGhRuEMsjDE%2F5BB3sHn%2BA21aNS6fIeoHqfFw%2BJf49mZf86ROqQ4SMQAW5GaxIVTnu3NUybd0l5b%2ByPqlHUPxVY4sQWLpZbxt3qXwROiDDIs8nRBjqkATnr6O4KmgYl%2BLoyeoAnFiTsAgonhxlvUIA6Lcv9LSNDGh04%2BNwXUR27JGsY7Z%2BUbJOAl8YAJzK62C6T%2BoC1f9mo4WBuTLaUDPOyjtDFsEcH4%2F3jmBAl2rfpidjFNo9oxJAYQE03V9fmzxc3EmTBMBTnV7Z6NYGhYnI1m7wgSS5f1Dl6QdT%2BfodGMd7n2SjdTJIKA0sMUrbDSqUSXzdbs6EAvjl0&X-Amz-Signature=a5244288805c287bbd6c2edba08b15b448910e79b6e2d09455c3e3f4c29bb213&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/129cc91e-3fce-4702-9189-a7d04991a5d4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMNV4XRA%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T085350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwoBdk22H9nQyh2b5gGoSLlMiK5%2BEbrJ8XbuErdgHJcAIhAO44y4YwcC0SppG4NIBtTa%2BlpxvFHaO4Fh2u9CcH8CfcKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2Fknd14%2BtT0sYk9mkq3AOCBngzkH61nAIq1PY0GHOqgf7So8yfaw4OmdWm2bz8lHZ4z1dzE4vp%2B5HIRMyJhJV8Q0%2B%2F1h5tPgV0ImN9Wnn7YaVnLb%2Byxr5jRH3nS03FRK7tp%2BWgiv6tDkk6dX6ABj6k9Q%2B9JA3Jo4OOeMY5nHOylAcNYZHq3lhSAh9LaNjMFu90m5KP%2F6VzCaLiev6qIGMZp9BNpJbabqzz3nc%2Blyi4Tik184KA9vhewA9QZKZbsd%2BatxqK9yqwS6EfAm40j8qwnAqyCGHbMrqPYkH7sbKEHXscqE8zbPe4QnRad0bpHZSrhCr6g0dg9TB%2Bw6yK8Y1rqR2QSQZ5kwwvEzDi0dIbpq5ATPUtFhqPjX%2B5oNXwVSDXNmng1vMaiEx2hXd%2Bpd9CXEzfk%2FhPTvy9Gt%2BT6BPChUd2hL%2BQTTjEqmiTMPZDFY6Lg1%2F%2B3SIbcoXYEEuS%2BJ2XWVufRbx6QttI5Byb2d2ptbuuJ8AR8Uspo47ktQTwDSqM%2BquHgxl8xgXW2XBkURksh%2BCzAMcBypzjr8HtiKtGhRuEMsjDE%2F5BB3sHn%2BA21aNS6fIeoHqfFw%2BJf49mZf86ROqQ4SMQAW5GaxIVTnu3NUybd0l5b%2ByPqlHUPxVY4sQWLpZbxt3qXwROiDDIs8nRBjqkATnr6O4KmgYl%2BLoyeoAnFiTsAgonhxlvUIA6Lcv9LSNDGh04%2BNwXUR27JGsY7Z%2BUbJOAl8YAJzK62C6T%2BoC1f9mo4WBuTLaUDPOyjtDFsEcH4%2F3jmBAl2rfpidjFNo9oxJAYQE03V9fmzxc3EmTBMBTnV7Z6NYGhYnI1m7wgSS5f1Dl6QdT%2BfodGMd7n2SjdTJIKA0sMUrbDSqUSXzdbs6EAvjl0&X-Amz-Signature=31b5f82a06584825f4a7ef7f2bbf89442ce823057af1f16e1b850fe834fbba9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
