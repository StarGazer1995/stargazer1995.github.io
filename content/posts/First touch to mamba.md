---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCUFLNMF%2F20260527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260527T112812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDCHd5XzMqR1cAlOlKTOiP3EBOZJsoD30QtBNkunx8n3AIgavAQBxOW%2ByxuKiH0e2Y3xhAN4R1GuGHaz1QQghykyKIqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBFNuDKxF%2F2AAe064ircA5nqhxQJ2wqUikn1YJcoPu6KQ0MnNDLnhL7ISQ6BNLerTZTfvYXWbSV1qFezMRtOfSC499BH%2BL5O6uQqFmucBDEkrwTjlQkz4t4ZzslHrPSeEuvcyPsBUaaT%2BoZ2VLhFGM0m1JSV3GHV5gjaHlnM4%2Bqt2leRWKH5K%2BEVO6MS%2FR5DTmW%2FBKqwJgq5BeN23Tnv7tPj5nG9WNV0h3n%2B0YgkUDbKB2iVFHsR9Uaga6g9k3X6O2lDsjayvU7ZdiNLh1A1bOSbq6bACZBPnXt9pK%2BcHsKZ0iptz1vhBJ9GV%2FDKI3N6a18KQAu54H%2BzOe4Js%2BmsFsxbqCddv4Fs5kVs%2FfDGddhwSMd11OXgyrrFmZFHYtTXoyeblhYhezFndXBSmvte65eeFSqqpIioG%2B63z2zYNIf5m6uo0WtEfz4qtz7bi5QyVyplGuPbNwFPNshzrENCPgcCXztndLCu2OFE%2BnZJQgUhcMeu%2FEzSkypXdJe5lLayCVz0HI8xCn%2FKPsGPIKzgWyFC484u6LXkDAoyqKJ0hPjHXJGsQ%2BBwF5hOHjUqulUtLBL20SxIlcF%2FI7V4pupWNgeaixqShqiNkx74AzJbfTnufNq5Uvl1DQnw7a7SSQoi0WKCaK3%2FOx95SmkQMLml29AGOqUBjH7Po7K7ztirAo6ektFPe438fwykKr6Bu0cyghID8XzXx9EhyxXHRjASu4VGvigHOyK9vw6dXqluB9NZhOA%2BVrIGQ8AVv7D3sGe8cWEKzx%2BKTHNi%2Bhqw%2F06PePvy3weX6%2FDqbWULcF%2FE8aOr3W%2FYw5DxnsvnIWOgRXtfuGyPdemfqvkCld%2BZBa6Nk1m2o7OgWxwCwVkIf4UECDpvjhYzbnPbgDNn&X-Amz-Signature=9a435577685b4fb5ae614bcb7968319ccec58f89785ad11ffe9eecfa3e9379a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
