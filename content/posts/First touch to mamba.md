---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJRALRTL%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T204803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBOgIdUv2%2BHpOVf9pNUbXWkA%2B2dyAWXWko2%2FEJGXXUSLAiAHiK1B7G%2FSiCdqJlIIeWfheZDrxeZY6FLKx4umAPj2fyqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2vKlgtYZYnU2q8yqKtwDZP292EIgLpddSvuk%2B%2FlsV8pfY%2FPRAtrwr9XV92DVUjM%2BdLMFFAZkDMpozxRmurKyUeEmfZcdWj7kXBujAzmdq2sG9Kr4BWJ1rJI376tNzIb3%2BtcySj133IDlENbwM72u3ECC%2FkZ3OgAxyJ9ROjJeTP38UrpO8JDFh4VQBg2ofhKglUJ0HuWJgSQw%2FkYfsjB%2FG5vah9%2FCt6UEk5P0azMcE5XfI%2FHkyfm84ZU433bwcyeMw9li8LIYL0Pdt5nc9art%2B%2FFWEnrL6Cr0PfDOXvo%2BYkEhDL11MmVT1krKxc3xq8pCQpJcqK8Ow0eXjjKkwbJF0ONonp5Vw76cphK3GFsbSY9lXgm2WM85nBu%2Fah9mC%2FGVNd9o2LVmgfqqHXjFPfmVK%2Bmko2YnZLWaPPu%2BS7dB4SALTzPYnfUFab%2FLkSkyk1sFW%2BZ7iaWkS8FPXXEyJOzLlfSwsrovzTRzHv1mVdbBAltkHQT73TTNF%2BKyiEsWuHKnyDQ4Nq9DprLwp1g3cqOOGhbJAg2IwboTwN5Q6KbTkLEJPLqCx%2Fej8Mgsei0ldvA3tDEoa8bY0E6W7nC%2Fjj8FbaLwMSIP8NnmZqw4uIlE7mSxg%2FsY%2F5EOcR0Z8jyqziNY9YCREuyCAdyH4xswu5mA0gY6pgGUpgnSdelnRQ1%2F%2BHEfF2hi1HkIkievguWQaCkcPIjuFwJ4Yg0nCGiLfZv6CelVNgGVO4IU1PlBjc8nO9jN3ieMbqFgnYAKPKewHohwQW911CHz6ojz0p%2BJfW%2FpKipiRvMSFpEfhAGWoaA1bSipIjoTDrlswWUumueKT%2BjokEXIsZlq%2Fa6aeCr%2Fg75eejblW60F5EMXTzKKQUQYjLzhU3OQOLmNfkIj&X-Amz-Signature=7ae242758cee5487cfb56fbee5fcde451a6187d73d3ae21cf5cd7e131ff38230&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
