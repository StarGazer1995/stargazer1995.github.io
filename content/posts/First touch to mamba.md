---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466545LP27I%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T174304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCRApM%2BBQPxepaL3opHmBUlLlPL5n%2FVv%2B5V7BGvcVyzNgIhAJ3tuZBlMML3J9AXsQZ47q9R9YVi1ziZNr4uGLYsp1XMKogECPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igznsl78uzaQcfWlzBsq3AN6fAiTZnTWVjPa7TmLDfZuluWqfHJ0IWaqpV6iMQBgAFrMP11qBHZL33yJOk0j5FQeme5Ts5S0qIiXLlVMFln%2B3sTnkr%2BEMUYuA3jgURHZCIh6tqXVtyrumNg6yd0DowPJmhn1%2Bk1bcnfjKccvq1nIjH0U2BdljxBkKEPL0%2FSOyoJ0iR7Qvb6pM9whg6%2FtJJyWtB8Ik%2BTdaUOnQ6fFyErdx38pxBQ2BxWmjUPNLUih2UGgC%2Fz1zND6KJl3v7b63bBG%2FcRgkp86zlTqnLtDgJlA7L%2BCZYgquzJmBCGpmX4kpgwwj4n7%2BpaSwD9t7Eg2DTh%2BK1%2FddHhKlIX7e%2FE%2FKoeemOZUqnL2hHTqjYw4vqdGkvPf3NbtdyIgTnopcU8YdaN0D2ZIE583ITQRgBSpjqGIM%2FooCiGiyuUhJQzUai7iqQa%2F%2BA7BdbKlR%2FcKplj7tH%2FIaBJKkee77L4UUAKw9dR%2BFvnM2EKpMGoibH9znA%2FeHl%2FOkdDudDaHrL9ecrbF3gYL4N2uNk0F1JPKevSjHXv4YFMkPqbiqvL958D1oBwCzUmQ3aAzLfVm5RHW7zsKOp8NjOO%2BOmEPi8TDuf26ycfBSmw0aeKXUyCKxbrMBdor7jI6tFXgH98w8kix6TDEm5rSBjqkAaxtl2PzMDv0ZzGCU33NBgG%2F7AhHWlgbxHOa7Jgocp4jqTWx55al6R%2BQ1YvRGgwa%2F5RMmvNDy0AG%2BWANH9MPujHCId9%2FtBFmcK12ljNXDjuuno7cSuS2stefK6HUsyoh3UEVHYE5%2Fq%2Bic5l0aPoYmywI%2FjC%2F9ZWlibI%2BjW2bzPtAwfh%2F58N1w9K6SbiHqNkjFMqHF31dXyqcPY5MmLCtKkQ71u8G&X-Amz-Signature=5943eb058c30e9782dc7d4490b6e88be29ec0fb617971e968c9e1f375f351483&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
