---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZYVWG44%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T014712Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQC%2FHYtbHtO7hSRxK4hWRH9%2BbkkSoRFGkx5z%2BU71s1S4PQIgKGYuWJn%2FYiVEMjcGdU7PnCsUyLVzthdnyU055T%2FpXuQqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFkG4x0kGSQ1pYH%2FvCrcAxI7RQgKr5IW4Xu%2FWiZcyeGfs4kFQt9V5J8G69ud3JohFd%2Fp%2B22obT0VHfhXyFAFCfboX4J4YKsHHYSjEYyRhFlUQyPhR6QghGI9OmWNPgsUGViHrJeE5aaEhnyjq9v5%2FGeXtjNrsoTmc2ODZOktKFjgi5kjIMN%2B0tnFZBzcuEgCZ8h%2B%2BYXzw%2BA1BvIa3gxjH42gLup%2BpqG8nedo799jp5w1yzMMz8Q7cBEe3cTtHdcOelTGUuLIps9uRB1xd8eUoP9g3gW1s2fyBHEG1z16BUrExy6GTNoYAgtOg5nCATg3DZIbk1zZkoo7Rb7pjpH32dWIeuh%2BGgnaQxHN8TAqHW79Nx%2FJ5qoTJ21U2FxzA79wn2kLuvV%2FT5H45QcRQ6V%2BX6E7%2FYP3zGHQfGiSs9iIVQFNVr%2FCRYnGqcGmoUjKU%2FRHukt0AD3o7Itoss6U%2Bm%2BqxrvUTw3rs0Wp4jqKirV2AAualKh55U9Zd%2Bngal9jr4%2FQzVh1grX24DTFFaXr%2FOKuo5N1R6ZMFVxTzvQN0XD1pfjGS0KIByj%2FSQBRA2BbNThvWvFC5kJCHH43onRZWfd4B1lXukR97KgDmn99lAcDVEH5alHoTLjyUGjm5a6tZzcAAJB%2FqZJc0g3U8ojIMO6L%2Bs8GOqUB9YVpYgAysk%2FgO%2FYSQfIO040OFpz5Mt8vx3vIktQ1GcRTU2PDB6cU0FqvRgD0n1AOo5pFs1UDO54eWsaLFp6Wu9HEilHpj6zlX2JqpSu8GICA70k1SGgGjEBObcz0n4C7Usb8G%2FzlZ6ehF8fGHwYY9s10PNWGPuDomtyc9IAko25nFKA3x5KL8oV7KtiOsqZYlUq%2Bm4z%2FazgS2UmFd0XO1cQ4Ay07&X-Amz-Signature=8b5a7d7a374d6bb8970be8fd0e6eca543a39b8144f831cf21bed557706e5dbc1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
