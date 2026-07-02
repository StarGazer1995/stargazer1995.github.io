---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBOTFW7U%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T225554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIHMtPdj7GS4zkLkQoGo455Z%2FBHMVylWSAVvDqu2lEmHlAiAdb3OAH6NI8Hl9pU%2Fa9YyqWlgYR0mrnOixGNETRzgWtSr%2FAwgAEAAaDDYzNzQyMzE4MzgwNSIMdjxQOO%2BKb9Tjq3vjKtwDlbLGSpkRXUQ1SL0KSHp4WR20voV0LX5hCWhnj%2Bv%2Fa8hxdK10wnd5qDcvlZedoe4sWZVPoMNsYL9uq74XLkY%2F6MVNRQJX5CBw9BVt6%2FaOb6fA1WbfaO3OlGsQJql0Kf97fOyRitG9rWrgEnN8R1mhX9kd%2BIdGJVg25oWKV3IjR60ghd7SyfMKmEfrz7NjEsTliXA%2F5AKZJkhA8NdraXeF%2F2x04fptJEoVCx6PBdDAQpPLhTZmKZcD7zXA8F%2FyBJsq40EcJ5b78wad1IB42dUO6%2FPSEhhwMjjMAXFzqKW4nG0q%2F2wcRFFq2EcYfXm1l9cAFOsqpluxrJOLYRKtCulfsTcOT0PDHFqw9gVIOxsmIVWxdhvgrGr7Ub57yfzeGvZ7gzCQ8OK11R2Aluke0mNIq3YVcMpkEE6YIsrs%2FY26qUWN8CyOJ4sVkWRM1u7TensFdtCEFJw602udt%2Bie%2Fgd7XIBFJQsbzZceRapYOb4uvo6AVO%2FQEkiM2H%2BQNIrzrQCVAaaGH6fzE994q67lMpoM5%2BUblDGXjTjCQwYJOaTwo5JDJv28l%2B84e9%2B3ZI086BPnN4wHgKi1kT4uncLa1V2qgDxKbfrJtqz1rCAx7ttQmhnsb0vjmYrT73qRdycwztSb0gY6pgEMARL0ov0YWpHmhJgscn%2BrpNxh0A28v6S%2BzbjO495l52Ns8LuwW8oNrT9%2F47bBkuBwi42l5YoARpCAp7r8QKUbpLAyYQePQTNxM0XHdUpVgbWfwTs7m61YnW%2F2xmSloreky7bwQ3byahCS4p%2BtDxbAQNORcDP0lK%2BvZZyTOwdsOiCJ8t4JxKxMytnI7DIiAqV47QKLRAowpfLV5r15shbIWXHsjohy&X-Amz-Signature=b00dca09b2ddce98831678e173e11e84960dc458b06401fc3c8ea40910ce72c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
