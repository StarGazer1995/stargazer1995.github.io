---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665G2MQ4NN%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T170750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQDrsvRAFeUOoCZl6%2BWTqYSOldjqps2cQVK9ZfHJNexkUQIhAIFyjh6rWYsgN5N4Npne7o7RR7VnHYda6FcNmNgEPH27Kv8DCEcQABoMNjM3NDIzMTgzODA1Igwn63WqAwufZPLyis4q3AOkH56olv1OetNDSkvs55kkxi5ugWrFkp1Bqonzn23%2B4O4zlrJRarfMiC4XYtA3xLW4PapqgLSas6GLXslNd85TjvmnkUN00qQOsvQ1xCOb6JcPB7ffkwl4Jqgh0wCY0VfmP%2FL4WCSklnVjDlHi0ymQsgr4AA1E2fM%2F82ASmzW4Eu865bFfqslaH2Y0SNYC%2FutQk49ipGPeaJKa3ox6BaBaJ9JeWGUCjABWBnthiI36Eo30hFWdMTmmuHP3ZT0B06ywpLlwpxBF7z%2BJwWUSwYz7vBXRTAAn6jVvP5ed9gsF7MjvI%2FzF9nD8Lb507qq%2BCEJEDlOnFhckvmwMF2hLJNOhHC5gmXcc82F2n2Lwfy0vz5C9W55odPUkmn0LjNnFB2HDee0BO%2FE6ao6Emo7gnuynYpA4oseyflY%2Bri%2BLhDDaaggxono0DFO9F9bmMZuSm6NAVhuZUK8shJdyJYGn4K10TvQ4nFlgN3InxRw3E3RjM%2B2HEA2JsZDurkSQDqxv%2FYa2dps5727%2BexhwkiePpVCIgAK9hHfOTfATXeIohI7sKhYZ6MUD1HJqd8SidOoq1Nz2zMalFjpcfvrcQUUKqF0th9%2B9Mk9AFV9RLshLJeT5To%2Bu1Z97tAyFCFs6DTDq47rRBjqkASwFwpXJm1VVQi80llBBqvvwxg4YZN1UvKlkpb22Qs8h49ejvyeu%2Bg90qHoya8hmfwJb%2F8s14pP7vc5md0lQy6GHhqMymiX4aDR%2BuSNHXaFTrHCLoL1WS9XcyMI9YVOAeFXKUFcsXorLoaIILraPa8POUV5bDdxPmssHp6bs2ktnTL5wuZr24zbAJbvdcqnSNp1%2BhnuEbcbXniaYv2%2FoCGb22eo2&X-Amz-Signature=400684f05f4cb91e986b168163a42de6cfd12f0e08f338a45e2bcb9bea336553&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
