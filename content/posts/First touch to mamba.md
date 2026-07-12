---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666BVFKPN%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T094215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIETohUXXEYs2m5lDwqSa%2BOzkSOfAxoYM%2FeKByfHqhcsBAiBHCz5coKlXeMHUe%2BVDr6IICQk5pJMTZ62vgkMts3Cz4CqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMowGJZNzwpX3OU6oPKtwDzC82RfXAXDuSN0ZlT18EHIIM9hHL4Z1Wpo0jTJpL2bhqyGGsmuGQoGcdwOD27UugzgBQ1VUw7chpV%2FmWjhuDpZwlEpBt07%2BXNZKv7c6xHIwAqWsnU03twEARAOEyh6WFoDxmdJnrBhbX4BT9CmbJdbjE%2BhbB32irAiGl3lLXMx6djM0aLq3vNU45tqpWaVXiSbuc6s6i0oJBJGGeHWn6Kdw3baunkKz61%2FhQES9Bgt4gdEV7%2FXKKNWU%2FtIdoSnKAM5w41EO%2BpZyBFAh7PZOZuY%2FvObMP%2FF81SStE3FFw6Hnr6A2H5gQBmGANx15OlbWFopbBqvPsWoKXgrhFHHCATihqUYT8Kuhu05SkEQCv60%2BiCa9yDVw91cFXcR6AbCpEarMi0RyV6VC4rzYZzZXaQpVclXsy0%2BIm0YRkXwCVCLlPyiUpbbjsC7W6K7dxJIERA54Vhh9Xj%2BMCEuRStw%2FhEVK0MjilB2xnNRWTs3uftIGoZQkYOy1D9gdVJySPtbefLbHy4p3aPgpHGv%2FalLPvsCYxNMnkKs1%2F0JG0TIgTYLjDlK9SN07Thrax1Ahb%2F7qAYi4LsuYTLvfuJlY%2FBos5c3RYynkSSbUe3bXBGZiDu3kfK%2Bx5rqwR%2F6yU0cIwjp%2FN0gY6pgGKN3AKnXYXMAbuYJgWoMfBR%2BmOtss5%2FTWjnDsOHTo0YStv%2FfJWBGVM4zOx4wL1nVwsd7HEaXG1Lkt%2FvaupChaga%2BSNCDlZK1nPHi5OKaKgnl1WXCfviNoR7Qntw4NOeOwPwUe%2F1Iv5pM8FVhXFOj2ir29DZFKAbExArZ7H%2FYYX%2BXzGqwOK%2Fz58XHfD4HonGR8FuhIXxPawbljuENhSQf8lmPq5t7nv&X-Amz-Signature=a6012388115ecc4a0c54a96af1c0a3d96e2808f81b0a9299dbde229fd5c555d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
