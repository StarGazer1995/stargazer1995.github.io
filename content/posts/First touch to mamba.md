---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7K4C5KH%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T124943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIG9z8yQLs37aGTJOC0RVqxdBY8HY8I4wupQmCwWbMx3oAiEA%2BtZGQJNeVA9iPzhc85MyCj7oSIADCz9jG0CdUTxyJcUqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBbVMPk2IGJ8gEUSrircAzn4YjWl2TrukN%2B5i2FFBJHUt4Nvg7PuHboT5WEpdCi6ZQyJRcvBCVPjfXdamu9VfVgch0gHKATVOFJ88Qj%2BBYumjLPYoYe1TMe%2FHxLgXQTxGfeJNY%2FXHpwRzaOzt5vjcnip3Qx9ZdrdnQ2HMRcMx06MtM3d2zw%2BKJjzbg0%2B%2Fu%2BdMF74Ae1n6WJHmaA%2F21k22hQT%2BL36P9n%2BIqO8lPbPW3LjQEN%2FTqcRg%2FUVnWYWww%2Fs3chUyvDA6vhdxzB8GEPPlKEepsYwbU4MPY7oW6vweLR0GaMB%2BEq7GDuc3BWeEmIUNeNjff4ypZpgDHpy5XBUJaaImIykvJihkkBlFtqVweWARos9zaR1wptJLMJlV26E2MqAqWcNBYS%2FDform9wceQq14K971ZEtR9i7%2BWFTv%2FM2%2FXVrFN10e9nKbJp9Y258JlJ1T8F5BmxlRg3A03uSz0V3WVRX2RoC8%2BpZQG27wHVBDI1Gc6LsGPvZ%2BlbEODheRZmWQtAZ1d%2FSMylAsRyLiraHfs1QZgLYdekZ1rKffgdrOFTLyLgpz0dQP57kzEP2Vt4jQ5oy01RMp5sn7bWovOs8kyFRjFJ1FXx7dJvWQTYQR2ev%2FBs34Hgmdgzda1EicxMBK2pb%2BLJ94bR0MJv3%2B88GOqUBKVv7vqLlOOEDHbfIvL9fFcqKfpavAsyuI183PRiKlWcd6Ep9M5IIsiYfkbHK4oQRvoqyAWdl2T9i8klU5BnJsnYLiXequ4wDTR%2F52o8iCCaASKvHiR8nl7tQ6YWFdbO645NppTWIHPkoctYfWdIAq0RhRwy%2Bj05C9o8ZSJ2PI8PLRWGzNbkGla2P57al8ALLO4SkROaHIXYVTWjcElRQsNZHQOt1&X-Amz-Signature=bcffbad6a2caca675a6b055fdf20d8f0f76546e76acb798d542273ac8a44e57b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
