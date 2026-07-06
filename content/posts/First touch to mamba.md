---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDJVQTS3%2F20260706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260706T061805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAlaz4WJHVdHk%2FU5NEk8Q5y%2FYR%2FZLY8yDNWo7exz7DMwIgIjamHHVP27q6qREtOnRNVlMU0Oji1VQRmiF28QdZPiMq%2FwMIThAAGgw2Mzc0MjMxODM4MDUiDL8qTAXmCiJtwGyHcCrcA7mE3DiGv%2B1kPdmGpT9x%2F0cOMxfFykVqVzcLvi6Wfvgp%2BmR6A0elDx0%2FOz3pvPv8GReSyfjX4KP2g7qY7rssgADa%2FwQQmDxpeylVQLecDh%2BrtWofITBarpxYhRDK7tJN1T6iDKC3nrNkectjJOx8nbReGQ91PuuzHfZhtaJnLVIe6bbg0CcI92kNz3UqeSmyOYGbq%2BT6N7dvgoBYabGj6K47PuKiiAvza7gGamcYcxUempwLptdiFY4ElK3mv8nl13C1iHcbKYwVEVJlaCqNw6%2BVZG2p99nJjrXVxtUb5QFAEw3CvnLleuid3Tl9s%2BVAwiRGnJ1O0JnQDgAU98Y4AAAldjXmh4JWDn73FDdy%2BuAw4p%2BACkDuEggaKIo5tFXWkZTr4Wm95%2Bgkz%2BWNZHiCy7cOBAlmTzqKa4AUCjyvMJ0WOJ8Vs6AABmC0rBxGw5SJG%2BvRdwDF1eASmzFZYsmoGvIyDN3kvWVAVr03tENCvZSKrF%2FrWsXLCVFXRPdTuA33Dc9yYJFIUjDP7TlZTs%2FEfI7jukI2GDjlsQgqBXZbOWazv4jU1Kt%2BHaoPJRLdHY3ilbM%2F%2BvqU3IBlZYrAfK7X1oBrRTHN7ofgkjB4JtLvt8ZVUopMwt5kBDPd%2BMiIMIDtrNIGOqUBpoP3i0LjflQXbXo0WiYqk3bstTLdtcYiIDuqDQtak%2FZT%2FUl0HmUX0lnGMZqgwZMzlnsnSrsmVyWBcvKxm4xyTj8ZhEjke284qALckejxglKZ7SJQm%2FAtQxab%2B9tUEUEODdQjt%2FYC39tKe%2F1wAM4PbkqkVCeXUyWQk7X8Hp8Mr3tlqYNw4ojWxKd%2BJPQBJbnoYUaPV5pNDBKOldNoWYRgyZvDIp2N&X-Amz-Signature=a3f34a5b178362b6dcbc31691ff128f059920b59834bbd53b1df7959396f95b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
