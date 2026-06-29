---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663H5PPCO4%2F20260629%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260629T211653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB9CLBVU7y4rShxd1pZ5G7uNIjDbCWXSBXbdlutUwRIzAiAYE7HhG2xRJr1u0XCKhoHfRBSTKzw7hiYCzML88CEi9iqIBAi2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMb50HgSh9amW%2BxbOWKtwDKf9AXdjdcfILUUaHZ8fYHWrfANi%2FcN8pUK9ZwnKzEGxKLzjjBS26SbEwzD9IggCqd2qp%2FTuMEZAOyYDm4aQs5YNeNPgjFFSMJq9LbgkoPo51VN%2FI6Sd%2FL07EO6rrFVyFPkY5HVtm9dc6QA5p5bqqobZPSrSywlyFRJI%2BIzOK6YAgO0rII98KyHgF6ILEmnKpa%2BehdBNxPgnsJpfXicYXOP2LJhpYgh1ZlKoZ8zFOtBaV16WFk2%2FxOkNzpdDVUK68RXU1L1smUr1n5ljVtltcjjyb6i0NSWAkq4KemWdV%2BDPu3tT99P%2BiSrux0pN%2BWM86I03fmVKMvG5IDFbdHSIrMdJldIjTzxW111gl6vtkrUwTVWiBrUPwPn7rQQWTCTLqPcpRQnouVfOfoRrAQuYe6pYsVeREWQuDYgpe2FZ756KMDdMDqItzYN5UniFzCKA6CwnL1v0SQiuff4i0U%2FIkBtGU2%2BHQ%2FDo64iEgvI5WuTHR04sb15Yqqsf5a1nT9evycU34dWOXUK0jFutI454I0a0QqDgCTO%2F%2FFZ8a8f3E9HZfNPctxx%2FOHSiUW2dhRJ9eHzmMe1MqRJmJ4OxnvHCiDgHgoRavyppbYw6LlhnFStimwXu5KbmSkPKoIXkw072L0gY6pgFIyCxLQYDsdZjRansBFoSCiTFIYw%2FtzwzkSPrhj3utIr2OVdvMCIj9eKZI8AHY%2Fsv%2B0Il%2Fx4bG1s5xkCidEZOet4s1s9E6i%2BU5MHViO2D6cdgVov8mXVKTJu46eW2zUubRXKRkeyciUIt1sB%2FBUzNlXi9zwWwUMGtTSLqMgbj9tEFUrpIflpnoOmD7MIdMD9wY0tAXbxdzlPmDdnfSHiiuNpAGYL3w&X-Amz-Signature=7bcec7748d390e1bd6e9a177a26a3430053fd46e908ea31e7efe742f11678d50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
