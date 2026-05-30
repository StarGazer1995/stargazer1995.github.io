---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y25A2RAW%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T165130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIF8RtFHodcm%2FB0MMzPsEJvwEbdTwVENSdFfezszl5PYFAiAk4rJNJEXkY5gkD6gbBWFCWBRTQd0i4TL7jRrB%2Fs4%2BniqIBAjg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9g3knoVE%2FAcZLBvzKtwDV2Rhg99bHQM0QzBKFXZcvfdTo2DZyV2F2Nawu0QceA9jPgZHvsJWaorv8YkfwQHFvWzQV%2FXajfM1XAUY9Y%2FP3pLUwI0vJXx2npPXZ%2BR5AD1xOebF%2FLzSGo67ZUI%2Fl0CWmvxo4SoRVptdfGc%2BnY51E1G4jElDJ4Qn864aAsWw9Xy64RvGU1807rA7T0oUPiS81MpoJDeu%2BL93Ck3%2BpgWhr1ZTM7yDrHA1j6hZTbgMpcbdMzTj9n0ovZ%2Bz%2BlyY2iyymsh8icIEhRva%2FiAM5xj6p2pQ3DjdpJ169qc3d2EgRt9Jn71hPeEDnkp1EKn5ofsdqxL18GcL%2BFa703WBz9MYRg%2BwZuQZULPceTIdazhk%2BqWMxSJwdH5HFv1MZCQIcb8AabIq%2FzmbmITqWGVFBaAU%2BrpZN7L9bdr2DET9APyIXvTiz9ihSU9MWm8ULjqCZ0NE6B8SJcVYXdD29M3ORFI6j02yaEP7Qo2yB%2Bdv42YB5cdPXUNY7jWFvHFOb3QyhduQZ0ivpxRI496Di1bBMuJMy05xf2Sa61i0iMID6ScP35IleeaxPTyxmiqSgH3ZG6YN1J9QSRxnkeJjfijyPb8Bbn9WbGofwDo%2B3HqQE4XJhBLrFQA6rVfAEaQHchMwo4Ls0AY6pgE5VGKxu5nexA2QsyEClYjdXmiNL%2BlnhlUOIiAgBexkMAfAOwUmR6h%2Brepc3FVgVocfSAhV5mgBkE2KOEmNf%2BGOCMA4pl3bOmA14H6ZWmq07F0bWNvRFy7kR2n3X5CJF2T7i10jt56r8hjp3TSZxvPkB136PE9hijOLeH%2B9PmxSwWF90eykDLo7ev6IjJrnuTUOM3yp0gHoAHlU3Si5p72i30HtLkPm&X-Amz-Signature=6e9a53381af9e9e92f436ec3f658341dc5fdecf4ef329ed6d749ee9ffdf8f145&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
