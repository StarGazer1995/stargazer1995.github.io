---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KR456XL%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T121454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJHMEUCIQCzwspU13emNRRgb%2FanpR6NbYm8UcsHY05uZH55SzvVfAIgb2W7e9LWb2ZbRsI8NM%2BImDj6NO2gaOzvQSwusTs9Jysq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDB9XhiHcigNUXvTznircA3MB2xg6XLEfW8ecSHAIP7q23%2BeuRg22S9fYK0izy15BiQQhbVXMMj6TCUbB4U89TxVo%2BTTQwQcQqA30EtlpwwTUe0WoflfFQHujyco3cVHl6KPqg4mqcYsD1kHi5KsOviTk33I1clk33dIrdY6kAX8QnQvTWLsVBmpvgJnxrNH0vzLw7OX7YWQtF9sVzDTd3Bd5q8mgkc81pjW0TjHj%2B5kX9Oab1lrxjgpfnchoDENI8S8GtQJiAUv8hRU5VEg6sXXfIOuhOeMJ3aDHmVtnFzibpEL1EtcFplloL35uAMeB2Otq4ytM2ixdFurFVzdoEOBnwNnKIoz%2BQPxfAIACLamaAkMOvQ5QoS3yls48cd3ZViVcc9y2UxfooxAxs5Nvr%2BVMZXnmmX8cjOhsdyM%2FDIznpdPd1uaoXLUwB2UBh6bhvKhIptExudDdvmGDEegH6m0omhEWVtVLzs4KuQk29e1SimnhFLYRXue7Ix5xVTKlrNqhmJPXPiLMM8esHRljXOu66bKgbQ7FNwcBdl1749Cki7l3rq%2BH3nrwgCaJEqrhdGeLbsHoBkWDBduHbePpEGzfwo2Eh0kKUos31Lhx%2FUislhvNcvqeuX132KCxiiY1790pgGkvVfguVLGTMKOagdQGOqUBzy%2FpRb1UVgUHXjWjLHY%2BCljsFOnqA8ztCn98gbpBL6gg%2BTXTK3uYl4IyJIBc1ftfahIznOf2KCp7t%2BYdRwcs1MEQZ2T6XrBj238PUFPnYLRI7WE%2BWuSo4au3DLNaqHphXoeW3a5nPCgld5YsmYQKLbvxtGAgh%2FjOnJeJ5UiuCI1BtDQFI0r4%2BiBTxhjG87FboBnyD15%2BE6ncTAUK%2FI1hQGHdwKLY&X-Amz-Signature=d121539fdeff35daf1c870d2aa3a75c01e97d3ab5157fcf528aaf317282b9110&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
