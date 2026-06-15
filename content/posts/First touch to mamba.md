---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEVRBBLD%2F20260615%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260615T221024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBBwHzQhAsPKGZiFU2POrCh%2Bgrqjv7eQ9pmooUXPAT9yAiEAxGM%2FWMDgoVxYoyIGCgfpePgD01BF9A4KiTjlhZqYLN4q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDFx7nRzirzDczQ3JLSrcA9DdeEBR2yX09bLt9OzsIEsEDZy0hX8maiBW1%2BmQ0WETVlmlVQobrnE5JD61%2B89U4%2Ft9Gl9aE47aL8psel6Pa89gbRuX6LqE6AGLlAJlYITsl7bpnbNoDbUyAnBGhdOee%2BDPVArVLX%2BZIAv4DLKNUduvH2EBlE9vacX2cm9KxhFVRMRkMhOGVuuoS2MJa5pawwWUnNlqODT%2F7oE%2ByaDklhVx8EIc4U4rx8xjA4vIYxrZa5yh%2FuJsl3GTLiZJ8heoKk7Ier7YEL04g2eNTieUw7sB9LoatJpTpwi2vjGeenYGhAHYHq%2ByUgYJUn5IMRAPgPZrpJKAlK8tWB5iYnspJIBxAdvITVnx%2BTlOquO8SobF2fk6hwJG7YKvWFO8qRXYqiq6mnxdz%2FI%2FXtPD1W86n%2BuaE%2FgJ6kBArvhod60uYXrtgo%2FT2JdWIpvqs6pZFEiSMk8b%2Bj2x%2BEvuLjsaDkukROpbjE66l7p%2FeVo820AqWfl243EFkWNxIW5SExdr4TZ1gNlWN%2Boigu4MjbdaOOtJodtUUviZ3Pb6TepeeNwQFzs4%2FEtQIhQvbAyelSl6k0RUtS6AbgdMUyNU%2BIrvR%2BrY3QXJ8FFhgOkPBQgLjivN5onF8NZo4CimNjJfA2emMNjUwdEGOqUBAOgPuNPgJoHXEokHME81Il2gGBfWwLdS9WWHbPiBJqOyMJrsH7VoFERAj1lrmsHdGOKkOvsgqVjWbQlos2qBuFhYxAQ5F%2B6XUBAYAObQr3U%2B3o0Sd74ZFf6qVs7dmDwY2PC7lSp4Nec6G9hjTF61F7wLrR%2B7wPkHa2%2FyN8LsnQQUEvoZmEyVg59i7Tmauct9QKcf735HkUjbs9q4OKBIVExAFQxg&X-Amz-Signature=08308808d090101aeec7e7cbd829a0ff8c4173a9ab618de595bdc914cbbfd553&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

From the perceptive of the structure of mamba, this is a discrete selective space machine that runs in linear time using linear space.

lets say, matrix A is a state space matrix for the last system status h(t). we then can calculate the next h(t+1) based on the following equation:

$$
\begin{equation}h(t) = A*h(t-1) + B*x(t)\end{equation}
$$

$$
y = C*h(t)
$$

Where B is a weight for input x(t) and C is the weight for output y.

We define A matrix in a HiPPO matrix manner.

$$
A = \begin{cases} \sqrt{(2n+1)(2k+1)} && everything-below -diagonal \\
n+1 && on-diagonal \\
0 && everything-beyond-diagonal \end{cases}
$$

By doing this, we can use SVD partition for reducing the computing demand.

$$
A=V\Lambda V^* - PQ^T = V(\Lambda - (V^*P)(V^*Q)^*)V
$$

This can be done
