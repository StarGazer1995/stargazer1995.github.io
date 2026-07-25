---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ6UZEL5%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T145510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIBk1lY66UWC4ZagMnf1iUDN9HNtMeBq94YLGurT5p83fAiEAjAKjx3TSacen9qrUVpSmTPHTdAjs%2BBlEBUCQEd5Sh3cq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDKyLdlpMgL4MB3t%2BVCrcA7Ig0oLrJ2Prm%2F4yDA36r9QsIbstBEM5qvFGVKGS6gOuwqXDl%2FB6et54NnkpZNU1yPqg5m3uY%2BgUjbET0gm0IzKgLwL25ogONqFQ7EDZ2A2Qn%2BPG4iqDter3LjnLtTpCE7TLkWw2NfkMJR3%2FSK2rJ6ZcNrVMMw6O1lhFckV%2BL9IeNGs%2B6aKy490kRuKhVai4z8yIzYMJ6QTWPevwL7Y0l3ox0E5El%2BflJeqeqpqr2uk4D9w27x9yRMrSvnI2wyjCukZsvGOxZdlO8TQTWt1oyx3basOX%2FZVfq5BZ8ZtX0%2FUAwWnwch61hKcy%2FrOoD%2BO1QyBnPAuqJIKAYeJ0YulxSLd3%2FQO4NVx9nIb6jFDth48lDhCqhRRMz5UtWviN2uGTgsV7YYTD1tjZ06D9VAppkFiBKVW1kxdFBJjiORjzt56DyE5v9raYTktEaDKqBIU1c%2Fo%2FGs3WmEnuQYUT6hXIfejJoISK1Nnsvgr2tg8nw1FNFlofPA5wQRcXmHiX%2BYMorOoCddWujH%2FTWnMlfAxNZaimAyyC0dN6NMpFRkev6Biyc2wfClvqkhQBAMm2kRKV92Y%2F7zQ9bCyK75%2BvXKAN4MFK46VqHNXF%2BZkXY%2BT4htzc69FN0k6nJxYtvIrNMLmHk9MGOqUBuuFrOun4WEMpOj%2Bwp8NLcYYWGEFgb2wLCXBF1K4Yn8rIQNf0DHFJAaLBgSe8Q%2BIv4h4X4sULkDIRNjn196uonjP8KnUIssSc0rw3tZ7qdJNJSwq%2BDQChEGHHRSM7TO4YQCkwoCYWQMiiyxOvgQqL3ywPWtvStToArxG1nbuuJHE4AjWv0Ab37FXAr8tMYOTHcmmHPpwKu5A024ATnimzVCjGuv%2B1&X-Amz-Signature=0c1c576bc1d5263fdd305dd8fc2554100d979e6b72cc199328c5bf6998736a42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
