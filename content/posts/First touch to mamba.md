---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WINTTNXE%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T025159Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIB5J8omgTfvPpcePu9419Zf4A0TqxHloM18%2BwFPuWXpWAiAOHggvFBJlgkdYX3b6x5j2HINoUeIFm3%2FLdINATjTACir%2FAwg7EAAaDDYzNzQyMzE4MzgwNSIMFLVulcrlXjUnxW%2BmKtwDwCHj9xRUh7IE0%2Blvq3njkiVdiioJy1zg%2BEsLl4kSfM2os4HSLxCLPga5kzSy2loI5zg5j8WNZc0U9HHdwK4Qm6CuO9py6LyHa%2Fxzx79h8fei7v43VBYi%2FHCmxQ775kMOLIiOocZHkfT7xDUzsTyY%2BJz4jRA%2FZ7oCDOF0FB1O8AJdnHpy1mRIbgN7tNFdwEGL8exAVMm3KBiz6h6PSs%2BHm6%2B0%2BhV548Haor2Z%2FpT0sl67msIiHh4ebjRNKvNJiO8Ht2Araze1zjehtp6BfvRsoU4rxzJ631EYvjBWliC%2FhOPDMFpqXP3N6KQpsDvNu1TmPaNIP4LxsUunJ%2BsUnvNLIqEc4PCl15nMwwzkP5rWM9XAz4xzrx44Anx%2BfsyDyvPQZ%2B78t9GsLxpFEdlPMijKFAQWGUA2YOVhpbnPnYkgGX1IR6y6xnT64ZotG1gXEF26o%2Fq%2BK%2BLTfc8rbyCZCYeNcNUAvxOd06n7WKY3%2FlsF4N79gn%2BfksejU%2BorIvsX6utrNitDrkkG9CTLetXZaN3Tk%2FN30M%2F1QyOS1U%2FIAbY5PSgHRQ3UGmf6H3iiKbiKGcQD9jhunno8hwv2ksdujyUnT6F3E9OGCzg1pjz3cqunIvN29jEebNFW9cr7PfMw0t%2BJ1AY6pgHHLpGlqLpowd0ABIja8VsJNUAqq6ZMgaFIqfQxEGGOjMnursc%2F3D4w1JwbnwyrxygkMLYusO97L5Iz5OODT3alQw8ls%2BmNnHt%2BnecJbO9owFfxosgiZ3pI9SH9iQs4O9pllBrsbrrMNAgDOnRIa7H4tfEE4WqbdRqizOD18osT%2BKtcCXmJ75i3UOgI643BNu0H5gYJ6vqCy4Zd2f%2FeTmmX6w%2BsFlOQ&X-Amz-Signature=8b770a75874cc8ef7312d33704c0c029b29e3754370594ffdb24cbe2aeb66398&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
