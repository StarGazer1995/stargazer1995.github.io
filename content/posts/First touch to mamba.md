---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQHVPKX5%2F20260607%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260607T151813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQddPNWDbOhfNhJ4BRCAP2kO5ltskioTcCJBetW5ahPAIgL2nMN6FpCfISFPYYOPJoBZp8F%2BsuUNefIQwHecgKIYMqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDecG6P2smpgJCOjAircA1N3IhrnPjp5qOwI2G5D7ZjE9iwGBVqvwFd3NWdntKvsctzLr94fmjvsN%2FyNMwco4bMVlLMdElJztD1gGokK4ZrE239DkLJVtwDTXsOG5uVuIoRy3bjRFHpNEaA3IqyuLti%2FMVo%2FmZmV7LgyACW0mtor%2B%2BN47qJJ4weOH1CQ4iNXKIBfTLqG0oZZvJ8wjJostdoBARTHPQ9feX0wehgsciaEd77Uyvrk3%2BNUnZ1AHVS8PaId%2BP70Yo3r7Z3Jao8Tx0JtTtehq%2Fk5jyBYYNf9qFybCSpDrXtjKl3q8NggdTiiaMb0WTAVMlDigyGItaOPWxIXiqD7wNhfSGX4cQNs4jIrzPyQ%2BugNhFtceayHEdtATAxPYX9k37GMewPOmsyP6fLQURImK8ncIAfErsYwqMN6bWTBU3Ie3935Tckyj1Ozr3Kw%2FCyeH5TCKgClhdwakszjYeQ%2FPTJ0d5yWcUDXAHRzduCjueAW%2BUFUO8lKCAMLzIhJHs0gXZ%2B%2FkmRs0E85B1uWofr0Mb2UAGf75NCRFsUZnHK0vRHgjIY2kq7LEC7G1evHpcPp78cL%2FNgavvD%2BjqNg4qFI08njsZxX0wyUo%2B7AabKyJp235YDFCHEutBvf0B%2BIu5pOd4dYu%2F5hMNCuldEGOqUBK44d8%2B32dd4YhI3bTvqiGE5L8oyBeUiQ4mUN4ZVNUF7YK8pteYH9iHDf0SlPoO6UmAVLqwiPXC8R2FLi7KgE15CNuNazTFiKyMClxWvnIfnJE8tQptd54JMzuV5DHjY3YI3%2Bg9%2FDOGciN0mMhATrrv3bqn7okBi5LjuMdEBGZJKL7SiVBwOgscET3HTSVtzA0b3s7q8I2rn9sOidNhucnAbYwcMB&X-Amz-Signature=759c9994c27349fe4e779aeed3d5b034e61e6eccedf5e0da9e6bb45eeb42e271&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
