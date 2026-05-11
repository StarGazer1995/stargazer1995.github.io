---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SFYCUO6%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T085558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQDidrCucEK85SKL5VIIyLSshCOuPaDmJs5bCZjb6H%2BXKQIgB1XCxxbAwJEu2df39RoGu49yDJGiIQ1yID7yeWRz2Mcq%2FwMIEhAAGgw2Mzc0MjMxODM4MDUiDCoRbfY7vMz4OYkyiCrcA8dgPK6yVau3VT4NVDN6oOJfivdqhP6GCf7BzJaaJXkS0UFIgEkavApmkKYmomRC%2BLufLXl3b5b%2For13JrkCmULh4OlLiJbkkYElSUPE6NrPtJT%2FXRtmzPMkxCrArIJ2%2Ffo8sOnm4TNXz8nfa3CETBb%2BF6is86RFsd20zyGBSQnZm2q6C4oqtqW%2BWGFmzDmCbCEOZtzYypxCsWI20hB0oxoPGm%2F%2B6PVTgvszMPbqY149G7lcA8HQCiZ63qghpq4JUi75AcLgPE5cjjBH40bO5ewDX7OeIQgn7tBcKPJkQZQLPAJil0mmN1pHiq%2BmDvrlj%2B45y97s5GI4wb0V%2B6bgblv%2BbvmslffrIxnuyKIYz3e0ZXt2mruGcV1sDHFj7mevhV8AUS5xkn5%2BeWW1wIAi1%2B2fP%2BVY9U1VZ0uxiAvtAql10NoR7RZOMcRoWSUjQxwfrHwGOFGB4cttyfN4GTn5%2FePNZD%2FYPcH0iTjacFKY4cG%2FrYwcOIoXCwIcHT1vaEYizQKnoDG3ow%2FDYQNdMkb2Ut5knAMCu8myy7i%2B3tx19yl9VdrMkYi2Vys9OANpAqoXoR03XC%2FKozxJ944zbY%2BUNsSwRuhOJocuPZhJtUfgGg4QBr%2BLw5Q2bEFlqV14MJ6ohtAGOqUBWuiQJCVZvUVGNVg%2B9HBTp2EEG2%2B0hfmooHypIIrmXyZspGc82jSPSdUeYHX4Xtzjx51t3h4MmRsDrCPpCYozRtSOQSDly9VaYGIpHk0U5lFQk%2FlSZ9PyjACw5H09xFel54fUUWo7FG2Ib3PPURv4uQzij8yMF0bgAbYi28WKhLqHeMViCFCQpApwaF5dM18OcDXQnEiA7Z6tufPE05vskj%2B4%2BWCi&X-Amz-Signature=acb4eecf2875476cabeff2e36b8d266b93386e8ca669777656fd1befa908e5a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
