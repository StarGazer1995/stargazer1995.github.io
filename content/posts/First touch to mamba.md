---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEYGIVAQ%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T145632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQDjswk0njCi3uwImI%2Bnelz5EBCyG76YDhcpsnuBYQ05WAIgND6JdoY9IL5me%2B%2BgmVJ6N%2BJ%2Frzimh33icNoiRBLjq1Uq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDHFbK5BVMNyPyKU44yrcA4oKZY0c14xjxbDFYkz7wEUobxfiqHpwhmoq5lZ3lx3Js8oriVgnDwLFLIy2KUdHgtyYSNXTmU%2BNTh4vlA7wbf3aOwrXTyAr6P5aZFKvyrgsR6ZjJAFfsU7vvk3tMSrT0PGUt5wjEmTVxwr%2BlJ39S0cDqotmKbr3SqqLRIpXk2JbRyU%2B7f05vpHE5b%2B9E1kIAGiSXiZ6h39i3cfGSLrPXxJiNEfJ%2BYqKW2S5tY8I8sJY1TtSKzIUl1yu2xLq6Dhci3cVrFTcPnq%2FoPY71u08MXRZlAE4%2FrBinQR2nnROiJEp0weT3kOxSxxiGc9cgxX29wp5%2F7oinBAzPGxWU5UjheBDG4QF7pzFPnENRfTLAVhixG5cAh6Gy%2FntN%2Fxa5O6Rngh2gEusYE8sWzkkPFd1YI042naHX%2BggrnB%2BwLfTHAt4k4PYAiSjvhT8OjtKARs032S%2BYE4Bzbeq3yQTBi2l4tF3m1KJZMh7Dkwd8IWpPOjJtjf9RTnK3cT1Gd6TcZM48IWldCG6Mz8LwlBnhUKxoyAxDVl4CyRoYQt0ySAkq61JHgjmMlL0eePgz0WsIry0LUseK7Spx6XwSA%2F1gD%2BcCW7Oca9qsaGYDNI6Y7ChIHCY2k2HDZJYiKsXRqh1MJzHl9MGOqUBMk0y%2BxxYcbsghiU2z4ymwzjNhzuoR4iRhKumecYyjTrnMtEpAC29npd8oCELy37UBX2H6HtohcGn2kmDeytfeVRyFkAaZy6A6igNEaWP1mdweN2eCLdZxZwluryY0CJo1kU%2BAoW%2FBHSfBqNm45Vgl7a0Dh91cKWLhjfgspmSYmlp3VmQq0A6hhTXhIHtsa8DVtgeZjESccKdtyLrYs2JShJY13gP&X-Amz-Signature=a3e2ccdf5f849273a3177fa9f2eb53f70a8b70bf8d8830a9e50c2bfa3b32410d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
