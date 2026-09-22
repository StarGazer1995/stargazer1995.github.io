---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNEMAYJR%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T002132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmIccvKE0nKJgl%2FhnLvWMwWC0BjjXwwHCB9zQINpAK%2FwIgb4JwxjNmMauU18LwZ6bNdyiy68nagDHXGTzpBENDw2QqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNKijRCkhdg9VnNvayrcA5xKFmzA25VYCAamJNf3IxLG26TlPWdQ0DCAawtrltFYn%2FfR3YWGMa3GW7QGSBVKJ1sYkP7tBigynz5zGKeImEODd2ig9x7rasitEvxwxlpCwCQYUONPw9BUhw47X7WQgJvWDfnx5JKmSX%2FyEtd6CdMg33tyIMC2jryeo4z81BypPhVFtaddWMewdrIV0P1WB06tTYpqJ5lkLFMlxo%2B8hTS2jFort6JlRgNu7RXgXoqeqmxdU68b4z0DqVgI1HNgHuYcPpPGzH3ihAxQVlmpt5lp69seamZ%2F39Av4od3f5EkCX5bj1ZqczLvDxtE76Sd5AaFsgTHq88P9480EfHr9H9sW%2B2xj7QskF1%2FMBQd9BwM04xTYfBwUu0oiUz2ORgMglVNJgjflBj%2B3W3%2FHhIx2%2F1sx1D4ixN7NBETDi92yijP%2BPrfa5fNEjinP%2Ftrmqlp1CMS37uRNFAxLqDBsxjXdXSZi6tQsoe%2BJxTDFT7Kw1LQpUIO9x4ApsvhjwT1XevzRz2wFMH4x%2F5wdXBm5W4rBRd%2FQJIDsPyHnoF8DJiRb3X18s8D8vrlmWeStsKdouhocWmS7hhYiTqAEqlkzYXFzwa42AcAFgrc3PORWJXTyy3hjb8tK4GOcRyM7y97MIy%2FxtUGOqUBEcGb4DC0QqEJ0fpAELgOF%2BVf%2FLofhdfWoe1tH1PWdDFD8EJzJkr8gTlG0lwSo71uaSBLaMbTYdmjZyozE9dijgMbtZ64sQV3dxHa21FB7sZLt3JzztPZzXcZCavQzzHqDBV8t7jML%2BHTfscNubEs%2B1PmDnDFPIk24XFn7UkKdaGHwFh6qFVonWd0sFT93j2K0LINDhI%2Fcg6BvndRwtxsV7y6TwbP&X-Amz-Signature=1fd0694436e76847ea127ce235c95dd6445d9aca10f84b645d71cfbe262ba020&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
