---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662I22RHCT%2F20260616%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260616T145224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUeiof14KGmZoIGt0dq0D%2FtDROG4Pb6HTT7mTKKlTpGgIhAOpA7GYusbJdUoX55w5s%2FgWyPXq0M0wmfXx4LqOamjRyKv8DCHcQABoMNjM3NDIzMTgzODA1IgyWL1vXKZvWlSfeWiwq3AN4ht%2BTtbBUKZIEWMBfOdwx4wg%2FZ5%2FBeQvlRilKhpZuAi9gcEr%2Bmyu%2FZOpmr7zp2GnMwot2pDwcoqrjjCnHKBKXqOoPfjikDP3gCOWdKop3mggZE8b%2BBhBhAbjNgbuybDv1ropYb8vgjj3tWjZ4dqADlqenVLaaFvQ4txmKRhkZV4WjeLvnJ8HacERjd08SZQ2pkVOi6gmXyxpb%2BICVuTtZH7zsLJqXz1oDNtXNM%2BVaO21%2BAlNXVOLRtSIggiqzET8gIeyv9rGjEe67rKl%2B5RxlIgjLmyPzehI6d43JWiKfjCXp5IFe9K9wB698mb%2Bc4jkay7pNLBttun2xSl%2FWJSXnE7m5ZC1Npjm1omDk2vV8PAspSntH%2FtUh435nHsIjp4n1cMuvA%2F01OF9V7HgiLVuOht5ziPTMAnJLUzld31ivtVzmo9ShlxSTfXIOqwrSrx5iXI%2BDqwUNxcvvJpVFeL9epgCGtpIrRuTQvWHAPw4WQCb0A9tndAVGZsWtCpGVM6a4BPD3YbjnQ%2FR782dZnSmpG6Q3eFc%2BWxq4Z%2BBQvFSJ12kNAQIzYpCh%2BJ9%2BJBpY4AsUKttq6uhrJKV7AUANy4%2F2pXzNQKgs6ENYlYUxW2LZaLzwJSFJuaoAv45T5zDfqMXRBjqkAdSyCikTs7%2F30cnIwS5aXfEqPCeAHV7s6HFr%2ByHF9XBLJgu5H9eigT0FGj0kh2X2bQntYeWWr0c6QYp4%2F0%2BXyruV0W3Dcj4%2FmaEWBcMeSSAB16KnTqigrkTmkoGiX0CS%2BXHEpuNxgHVkLsy1MVxN%2FmLb2qhohEZ4eJZtoFyKVWzAcicbzZRYoNF9Y%2BKewoAIs2h7wLtHSNC1VG2781r73R%2BQ9hJn&X-Amz-Signature=14094175b8faa67d5680689789e2cebc64fa736f10c4ab7112808063b0432f18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
