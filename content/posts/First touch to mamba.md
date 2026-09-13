---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQL6GSZA%2F20260913%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260913T014352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE4hy9Q47LLttTphCMsIiyN5jHflpPYnYKH7hmXSf9OHAiASRTeRerAa%2FfgR%2BvF8HgJSnLl%2B51aoQZUCC7rTztp14CqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPpdZOjB%2BqNyvEof2KtwDI07tu76fnGCgOAjG8Lo%2FAjrmEeQaPKrI9GCS%2BdFY55CuDb57Js%2Br8A3HxuJ37Fp1jLxh%2FRjqNwBBiwwcL03ffh%2BdMCVATDu9jTRxfANKfnRgFBwEoURTskjBE%2Fl6fXhPg5REDTUIhQvl1iCONvbGcLCLxunfQmkqSTpfYOWzujte9KKuk5fzzS2IBNBsgwTdQw0dRTwcAvY03%2BluKbBPzjiRrHxtobuhnn5RNP4rw6e1o%2B1GBqzG4%2Fvu97v2tdzqtkYK58PdThymIDbHdcPhs7j22%2BlB03X1fFFLeW7H4U%2FuF2WjuxE7GiMYD4aZD9A7tvqNISQTQdqep0MVaN2jDBAYmYfyT83vYoXJKh%2Bg937EiubMDQmAgYGGG9BUxjYGvRg6a2Ckll4B9xkMCcW1Sbnk13XdoIMBWt14sRIwm4yWtNyPHNWyvYdE9Cx47N8k%2BielusytudPy%2FfqQv4CfZg50LufEO%2B3%2FOX3veTUyrnlCxXgRbqA9L1RCh40m5JW6ASZhhvzrrn5H9UpFFJaaBf0EmpkgYxwL2RqKDUfNjyjHwGv36GqJw7YTGts2WS%2B1c7wklhs3KxCpHtKUTdFysvkIBO9t2%2BRSDGlgvdHtqFH9YNrpXKC4fneV02Mw%2FuKX1QY6pgEmmocXG6vyG4zYXd100Jcjm4T7c61S3UESoPezkb2cN7IEmyLrdbjDXQXvwW9CrzQEI9FNa3enTBwlkdaVm2JFm9%2B3dWjLH3wQ%2BZ9g4vgdtcACHDgcNw6yAZQG8pyk4sp9BAh4rP6GyFx97N8n9NhA6mY7CvavQog%2Fz3hp4f3A1DuVq9G8k27ICDBxrgVBr8q%2FUzOKv7OluZxqm%2FsmhM8ZsNPUmJ35&X-Amz-Signature=057d1a9edf73c70167bd8e0370d4c5c43b5de5c8d93f2389dcd01407f6ec7657&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
