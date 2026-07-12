---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QLWYWVK%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T223738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQCawIi%2FYvh61WhLH%2BZ4Zvp%2F62p0PLOkp7%2B1xYLAO0DRdgIgNwUNQUt9uTuU3GfMeao7B74L1WvnszF619c78cXEF4gqiAQI7v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNGp6LOHEop1v9lPByrcA88sNlx%2Bwai3F1sc3ij7FDt5F1UCimtv7fYAcxgnqeI2p497P6dir6ldgg6J%2Fj2Zt2Wfje4XJahUSeLFyLG%2BWyE%2FgGVPjk0RFk4BkIXgx%2BFBQ1q5pcILqmt1rOkyZoVqRpR8k32SGgiuSNo2kG3z%2BeDeG6dFd5J5d61%2FKWe4i%2FP2R8HMZELe0szIzh1%2BDwnaIQFgY6rG17bxCO2GVRJ%2B%2FzdO90P7YzkfluO4KWLZTO46iAF%2FXbxoVkd5vf%2BFEGOim6N4xwfHJLiGLJzT2siJEdbGcb8wUYT01C9nLF3%2FS1mXv5stxA9cNcL4VwGcm8bmu4R9dQuRLYKfsc1QpszazHu21EL70jp8vQBC7dbpV2eCb3z9Us5Wmh%2B6HZTTOCRoPeDwU4ahS%2FX2eZVp1IN70lSKbKKzURBkfoDZzLYEJ0K5J1PI8Hlvi%2F6tMIszqyjiu7d6h99KVaeN8aZgE67t7j%2BvZHV24S%2FthQgL%2BAB3S179j2OEUzTAjxwKR3yEEahY%2FiU0aG7il5OJCattJZUqwRbb0ETwBj0bxIBiefg445v0uuHH2QBTbmRMTjeiWq%2BwyiOdNicsafAQD3Gf1m970lL9fSueVzwCZ%2Feff4IuUr%2BFlgfoFhavSG2YUe7QMJXzz9IGOqUBTMV7B23GwH67deS%2B50YJLfN3ZzA3hR5InfygA71oBEFCGb177Wm17Q4%2BxzqytZ2B%2BpTF0IV60jXLvdmrE3gvnJNTLfHGLA7XvtSOhNN09vxqz3FUapPkzE6HVqNy9f05zNFkj8psLJZjJoa5pn7YXyOzdu2aAYozhqG%2B7IwFeaLYwZ1k4%2F3LRdFSHs96ZlJOg9OTPFfb1QiRIJI2F79BFmUjo4I4&X-Amz-Signature=196287338f5751aed7f3fddbd4bb64b6dcffe78453d0e96d6bb4ec1d28b6e89a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
