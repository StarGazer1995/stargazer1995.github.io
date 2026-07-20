---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TS6YK3FC%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T120850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHZHPhIMXCz9kh99vMDJ00zwNcURTicX%2BsPSwamCgshLAiB75g5dO5H3Nr8Fu1NLgui7cU5fxqt%2BB1F0E%2FdyPYPoryqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdr1rE%2FFa%2BhszF8J7KtwD4U%2FVgfKCxLhWoiZxyZY98OEK6und4twSYeC5UrUIhNOFIMmtH5Hnt9YDzfox5PtyxkqRbTxU25jBd9H80%2F2jGPZYqARstq4DS96FEuNCcHxZDCdLFt8A%2BZm9vIRjPd5fRoxCU2ZEUOmgkpAE2wwgC51XULFlI4gaafOR1AY7U20jDDG3lhrSgkTLfhVMWbcYfh6x4V45MSpintkLk7PNwuS1WjHDP2rD0kCQj4znZ3LODYZL8iVzZQPtWkqh7VhKZbywDeBmNJJM6hsx%2BXMhTK0YFm3KuoekwkLqNovD7XdLUw9CXuFhFAIGll9Kc1p7JSk%2BkgqgSZL2JK9GZqpBwfqrH0DKH82UNlnpqf2nbZLUuLW6%2FlWR1IVAIeyeaOim%2FKzfb1ATvMerki1iZZW9UokClYxB8%2FfXEn1usrs1GpKJ7DM7s1dPGBCW426HIZQGhABdP%2FojLEg7aioxBblNTj1b32%2B9ECD2Hq22EZvOpiGdFRzI1gmQD34NcThGPkMQSP0mRFzWmquCmRslomO%2FR6gab0tVOy2JVY%2BdMbBMuFr%2F0lbpZHJ6IXpCmAhvSd8DfYx4bgke5%2FTqLZr8UcmGxgINf2QrOHbalwtP77X8IqElrnnPhJg%2Fqv6Bh5Yw3Pv30gY6pgGbf4CXd9zLfWkfklsOJwoaLA853y1Ib8vEz8Mu8l%2BJCbzjdsIL5iRqUT5JMVwtCVak3GeXY2VwV%2BaKjfvQmjXhtkUFpQzn2bdQoYCwl3d%2FD9pbeV8KcM9DGlluhwPkdUg71GUKpRa2WcW5m5LL5HeY2YTqe14TuRBjTCyO9jhf46KcDf7TBceAai1OcCEjg65lr2zIS%2FRsPpXsKXZivQVcj4GKNP2b&X-Amz-Signature=6a0c4aef884abb535ffd6f465d0a6914ab9a6b0528cc31db5088a8ea7c337a69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
