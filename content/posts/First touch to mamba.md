---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPDD63SL%2F20261015%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261015T084009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIEzs9bVcnbDo%2Fym3NHb3C6njydlj6SBCW90E%2FGVKbRAQAiEA3G9mWcWs0zUzS0g2i45hWLQsfxPv%2B%2FY4P3ol4Xkq5tkqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGxVny%2BMWJwcsCDT8ircA2jhJxifwx%2BVvCh7fyD6JU7w9kRyn1RX8RR3ms343fnn4Ha%2FT6y3ocErnZVZeylwyBvphjo%2BKLDwzxuW3v%2BMDBIErS42XuG%2FLtDGt6E2VZtacJa0q7WNUWtYxpwKCAj%2BHDxxGv5C7xZir4hniHtaVbSX8KXfggvFsiY7750mqom%2F7E%2B1KWJWWAps%2FKMHcBTW3CGzADitetKFgX5l%2FCgP%2BXrvG72Pe4mq9QdJ7Y0darU6m%2FPbDPBda%2FCGqbg5IozIU76x5LGl1YRf1jMYzNKWx8bfnS5bhD%2BctgIGD5y6H%2Fac5d%2FpLv7athl%2B7gr2IqXxZho5aZP4%2BuyA9Ut6G36YM6gIVmkPIm5e33rJ6YUbp3P7vSSwS6GZTRaixkC3ri%2BfeJsR26lHCBCb0s3whr8r3Fw4B805oSOZJ0Rg9xatPvg6GJRcczNNoKbd0uf%2BtDG2V7dzdrPylNt%2F945wJzRpBL69NwSUm8wubXjibtRwHdiqRm5yYv2HbcWrRpxAjcOrFzjAYu4%2B2Y6%2FDSTwquIIvs8773oA6SeizNJdWA1UAH%2FB7rI2v1N1OVLnGu8tOwvXB%2FMvWLkCUpv87xtEoxiGnHVOJrJVVxUpcP0OVlCZE2BxPWZRwLu7gL7e17ylMPCNwtYGOqUBEp6u6lRImXMaoKMoUZpWw%2BYnmuupPOz6Aol4PqdBnKzZqfsWWpSZUcrkilUOgVuZgXqs425oG8N3x0v1XKqy9pdmqzTdIYGQTDjCXRa4dl%2FpAmhzoCnEnRqcQGJbb6YNQFoT%2BYqNIQtm7OBqu6lvcAUMEBKfJZpfqRtS3795J2SYNAgJgnsNNHJYaBXunsvusUViM2k2vvXjrq278AtwkhSBfsF7&X-Amz-Signature=d887ed7f23574725eaa229778e1cf6a2d8842ef1cbe09ffb83c8667388f8707d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
