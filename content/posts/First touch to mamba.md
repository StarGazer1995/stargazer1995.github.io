---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPHWFDHG%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T223037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGZDJa9K%2BHL80ivyii%2B1XUbVe%2F8MRhHGG4qoHPQEzBpJAiAGeJZsEipKvZrKyDS6o2QuNErlEHlKHkny%2F7Jqp4CUXCqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8fjhyEPg8gSfxQtNKtwD7DC%2BGJbDiDzXsjaCiru6rdXjWjV6YCus4%2B%2B2QMp%2B0CQUx%2FTIBmIuq81IXtjxSs7svLogBWtjCDfWg0QTIQUABFh5Ybp%2BnieQtl5nBkjE0E8Efr8psAR%2Fz1d8FYyvkgUTU2CGt9QzqZyt4QTRvB1uzuyZXG57jo4volI4hYV4hU2tVlW3%2BuPxn5DkXBZ0VIRn5%2FtE9nG0BxlywFkrFmb4nSQZyRrb6VauDRMrrDVvvZMwS%2F9Z%2FclOnwNNE29UoIN96KDdoFeRxi1oiTQTmcoqQRK8KtzHpC3Vmz7XzDTosN9FBkl1XLHjYlpwbqBWXCo0lSacTpOU5gIXBpsWXDaSwwLIKg5Dlxoii1qRWS3JxWl0YC2JWQPF49OHuCxDjv0XfsKliB%2F4F%2BEIQZDeXZKGZ8%2FM5Vtb01lRc0w%2FKBzeNZ6lr7Kv58bbK6XZu7%2FM6mwld4%2Bp3VBqJUcUpVHqSNqY6Rwy3M05cEU%2BbaI9sb17Q4X08vbO8PCXemPtsB8fOrA0cBdiZTXJsKaD595265djV%2Fra8Z6gtp%2F%2F%2FvkcEYo8K4ymXTM26FEPv7Ycgzt07akNluWQXN1bfHgeUJr24Wje4jL9sHeSBlM7a2vurvsyt7VyIlGbhdRCDtnhWM4w9PPt0wY6pgEhlRWRZ0WuwKauM9P4WC3Fr6%2FT8slYcM%2F3WYQGsb1kf5SkVAtS9bMXYc4KTIPruBl6m3tZ6cYrEPHMndQrDfVAmdMaJa4Ev%2BfUFWFQd8hGfIfW7P8ousyDttXfSM6og%2BJShfCxec89M9pj1zcxZ1i7KLJQhC62GhV2LZqsQYfpcdvUkTOBGwihHax5uHXz4%2FHahVyOR8PIyWGPO9a0msrv734mJHSm&X-Amz-Signature=551d38e97d990b461e48304442c1afd8bfa081f69f768bfc742ca7b994996503&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
