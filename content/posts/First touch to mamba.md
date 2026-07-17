---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIULDDEF%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T045158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGVwsohL%2FPxzIvVvgJSMi77O%2BQTMXlP7ohBgHUVaqEI7AiEAw3FCmCft%2Fhs8t4dpSF%2B8EZ7loEMgm31zodHI0YTxvrkq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDE%2F17v%2F9zlKilXT6pCrcA4zDgzgylrx7ujH8PHpUtpnlAzfgKfIPbZZJ08CdTG3b6E7%2FX9Y%2Ffgs%2FLzFm3%2BjzDql7NGHsRdJkJXa51muqxhtH7TapS2MxhqNglBOPbTk6F7WpnzmkaG0A5C3cYAEeZ6AaoO4cmEQFSH9omBIBfLGxdpFsZbprUshPWmunfdO10FT5UjvibHrZGkut%2BLwnuK2orKn%2FhRZtPpvemrjdUYc94gHclVXRvVmhMfMlP4QuOQuZNBqmqmhGdlKuNQaDVXUweWWNAikVXR%2Fmrafao9N84o2KMADLzi2ChCi7uDst%2BM1zMDPDgz7w%2Fv0ojSlmpv6%2BMu8%2BL%2Fgn5aUlVy42PUjlGAoP7E2GShF8GCfzaFIBKXjR7tOVL51zhkR%2Fi5XD8ZLwpuOj2H%2FCFFTmygfwGGCrxDiItime%2BAs9NjokvVN7oiB3iXjAGz4ovzti8rsG%2F70%2F7zdtGXHZJqoDfqvFDfHMn%2F2fXyKDYSIHXwtSpA%2BhJJvZBnX7Nx4FzH3%2BJr3X480mQqc%2BLO3j9BKGRD7k69mA%2FMmJ1xJr1oLjOekt0yNHN2a7c7W%2BV64ylVHtGDmj8J4%2F6cpUVUkuQV56Xtc7dH3VbsZYt%2FeeavHwtR0nxD1T7cSNSZmV%2F1Ef%2BEXhMKbb5tIGOqUBURW15X%2FOcJCL9UJ68XmdaJAgxUph0I%2FT19H3Qf5lh5pag5tFEDCe7TBpfny%2BUdwoAFuhrenQqa0OSnWZWXeNaXmGUWhYe%2FqL7mBzgHWKj5b%2BtGBNlGzp03bBKJVrIz3kphRgBnJVIiNj3IC8qTEZDoghDpFIi77X1Tn2kY211ZY5I1W8UUdIPIluipbysReE5dhCXkgJiGFO1G8d9HNc4fItHgZs&X-Amz-Signature=b365822b03457de0e2646105007d6b77ece82c110085adf2e3879d350d3eb92c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
