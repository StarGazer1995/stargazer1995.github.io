---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QZH7YFT%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T204542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCnvbnZNbMAmSYeFibo8%2FcIboyE4gig0fVrxYlVa9AqDgIgWt00RJkptTVwNNowQv7nZzKhsf%2FRB48in36GqA8p6Dsq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDDphW8TaJRYEPzTaJyrcA0kReejLtaUKe0FQ25VN1Ks12xJOz7%2FnJ%2BOjx3XYxhB6pHguA7j0XIuVeBsbJa2gcPAcAjtmh0QdwRQpeq1IlQnznr%2FO40FdyXLMQ9PYmLHGLcbuMVWq0E8GO04fBolpoeerWWHCeR6QZ0Q6R1GZ6AtWeXFmnYx4BMoZToxltzf5P5gQ%2ByNaF1To06VlCaJKUCM%2FXhST1rNxoGLL%2F7NaaEwSQJ97d%2BGcO7xYgzyszJd7V5dwNnFKTqmvkg6uwELXSZ4u9moceZCjqm91CzTqkYW%2FM2BJIv4uKzKfRrBisfqVI4nGpIMXCC8LvF40DD94WpAOITiy4PwVs1FF45tPm7TSv7U9MLqNJ6TbUNiPJ8UzboTvv%2Fj4yzwrFrdefyfA6QcrY4foloBvemJ5Hfgr9cI5YOtPBIUPB%2Bo7LxkmIRXLVw29ZF6k67%2B%2BcISPK4%2F5%2B9nAovKvkvgQn6I8fuw6rMm1lUEM7KblnESb6QxcLejh6mQCTdV5JyYymwiOMGxGf34cVifAYd2HjScyZp2ZZ9F6LCj9oZckUEjEjuiQax5xHtipuODNiOio0dHbaSbJ70YsHKygYgbWLUXYx%2BZ49UxTj4zQ9jd1WjxAFrY3y%2FFpySa5vj%2FJe%2Fplns6vMPPTqtIGOqUBjIwMbixAU8jXuAziVdW90Z1YcwIkCNsE83aevjoNU7DJH2WbXrv6dgeFbAnitYCZs4T7OThVz3O%2FwKyhcAwl1igjBe9x0A7plVfe0iVz3KBwGpwJDDL7zak0HqYN3OGUfye5QkeFFlN1H8KSrYXs%2FckvUWH0w%2Bm3pgXmC8AE5IKKyuxwi8B2wnD%2F9ZcSHlCjXkSY2tsKPdGv31%2BlQxiMZSp1yx%2BJ&X-Amz-Signature=a16b15554de9483732306bec1fc59cbc774b01022f1279db8c2adfe2ed0833a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
